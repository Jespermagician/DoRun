# import smtplib
from django.shortcuts import get_object_or_404
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# import pandas as pd
from . import views
from BackendApp import settings as set
from django.http import HttpResponse
from api.models import Users, donationrecord
from django.db.models import Sum
from BackendApp.settings import logger
from .mailSender import MailSender

from django.views.decorators.csrf import csrf_exempt, csrf_protect


# Implement interface for mail here

# Then implement class implemented by the interface
@csrf_protect
def sendUserVerifyMail(request, UserID, frontendDomain):
    user = get_object_or_404(Users, iduser=UserID)  # Get single user by ID

    mail = MailSender()  # Connect to mail server and initialize class

    mailtext_html, mailtext_plain = views.UserAuth(
        request=request,
        UserID=UserID,
        user=user,
        frontendDomain=frontendDomain
    )  # Load HTML and plain text

    # Initiate sending the mail
    mail.SendMail(
        pReceiver=user.email,
        pSubject="Runner Registration - Charity Run",  # Later insert configurable variables here
        pMailText=mailtext_html,
        pPlainText=mailtext_plain,
    )

    mail.CloseConnection()  # Disconnect server connection

    return HttpResponse(f"Mail sent to {user.lastname}, {user.firstname}")  # Send HTTP response


@csrf_protect
def sendDonationVerifyMail(request, UserID, DonationId, frontendDomain):
    user = get_object_or_404(Users, iduser=UserID)  # Get single user by ID
    donRec = get_object_or_404(donationrecord, donationrecid=DonationId)  # Get single donation record by ID

    mail = MailSender()  # Connect to mail server

    mailtext_html, mailtext_plain = views.DonRecAuth(
        request=request,
        UserID=UserID,
        user=user,
        DonRecID=DonationId,
        DonRec=donRec,
        frontendDomain=frontendDomain
    )

    # Initiate sending the mail
    mail.SendMail(
        pReceiver=donRec.email,
        pSubject=f"Charity Run 2025 | Sponsor Registration: {user.firstname}",
        pMailText=mailtext_html,
        pPlainText=mailtext_plain,
    )

    mail.CloseConnection()  # Disconnect server connection

    return HttpResponse(f"Mail sent to {user.lastname}, {user.firstname}")  # Send HTTP response


# Template for a list object to store sponsor data
class SponsData:
    firstname: str
    lastname: str
    kilometer: int
    FixedDonation: bool
    Donation: float
    DonationTotal: float

    def __init__(self, pFirstname, pLastname, pKm, pFixedDon, pDon):
        self.firstname = pFirstname
        self.lastname = pLastname
        self.kilometer = pKm
        self.FixedDonation = pFixedDon
        self.Donation = pDon

        # Check if it's a fixed donation
        if pFixedDon:
            # If it's fixed, the runner must run at least 1 km to receive the donation
            self.DonationTotal = 0
            if pKm > 0:
                self.DonationTotal = pDon
        else:
            self.DonationTotal = pDon * pKm


# Binary search for user object
# can be deleted in future, bc the orm has a method for this
def BinarySearchUsers(users, id):
    min = 0
    max = len(users)
    while min + 1 < max:
        index = min + (max - min) // 2
        val = users[index].iduser
        if val == id:
            return index
        if val < id:
            min = index
        else:
            max = index
    return -1


# Load sponsor information
def loadSponsorInfo(request, DonRecEmail, users):
    donRec = donationrecord.objects.filter(email=DonRecEmail)  # Get all donation records with the email

    set.logger.print(donRec)

    # Initialize variables
    mail = None
    TotalDonation: float = 0
    TotalKilometers = 0
    data = []

    # Iterate over donation entries to gather runner data
    for val in donRec:
        # Binary search user list to find user
        usersIndex = BinarySearchUsers(users, val.iduser)
        if usersIndex < 0:
            logger.print(f"Warning: User ID {val.iduser} doesn't exist")
            continue

        Kilometers = users[usersIndex].kilometers

        # Create data entry
        dataRec = SponsData(
            pFirstname=users[usersIndex].firstname,
            pLastname=users[usersIndex].lastname,
            pKm=Kilometers,
            pFixedDon=val.fixedamount,
            pDon=val.donation
        )

        # Calculate total donations and total kilometers of all sponsored runners
        TotalDonation += dataRec.DonationTotal
        TotalKilometers += Kilometers
        data.append(dataRec)

    # Prepare JSON-like data for rendering
    context = {
        'name': f"{donRec[0].firstname} {donRec[0].lastname}",
        'Amount': len(donRec),
        'data': data,
        'Total': TotalDonation,
        'TotalKilometers': TotalKilometers,
    }

    set.logger.print(context)

    # Pass data, request, and template to generate the email content
    return views.RenderMailText(context=context, request=request, template_name="SponsorInfo.html")


# Send sponsor info emails to all sponsors
def sendSponsorInfo(request):
    users = Users.objects.order_by("iduser")  # Get all users sorted by ID (for binary search)

    # Get distinct email addresses
    eMailArr = donationrecord.objects.values_list('email', flat=True).distinct()

    set.logger.print(users)

    mail = MailSender()  # Connect to mail server

    # Iterate over email addresses
    for eMail in eMailArr:
        mail.SendMail(
            pReceiver=eMail,
            pSubject="Charity Run 2025 | Sponsor Donation Overview",
            pMailText=loadSponsorInfo(request=request, DonRecEmail=eMail, users=users),
            pPlainText=""
        )

    mail.CloseConnection()  # Disconnect from mail server

    return HttpResponse("Mails sent!")  # Send HTTP response


# Load runner information emails
def loadRunnerInfo(request, donRecs, user, RunnerAmount, EventKilometers, EventTotal):
    mail = None
    Kilometers = user.kilometers
    SponsorAmount = donRecs.filter(iduser=user.iduser).count()
    data = []
    RunnerTotal: float = 0

    # Iterate over donation records with user ID
    for val in donRecs.filter(iduser=user.iduser):
        # Create sponsor data entry
        dataRec = SponsData(
            pFirstname=val.firstname,
            pLastname=val.lastname,
            pKm=Kilometers,
            pFixedDon=val.fixedamount,
            pDon=val.donation
        )

        RunnerTotal += dataRec.DonationTotal  # Add runner’s donation income
        data.append(dataRec)  # Add donation record to list

    # Prepare context data for template
    context = {
        'name': f"{user.firstname} {user.lastname}",
        'RunnerKilometers': Kilometers,
        'RunnerAmount': RunnerAmount,
        'SponsorAmount': SponsorAmount,
        'EventKilometers': EventKilometers,
        'EventTotal': EventTotal,
        'RunnerTotal': RunnerTotal,
        'data': data,
    }

    set.logger.print(context)

    # Pass context to generate HTML mail body
    return views.RenderMailText(context=context, request=request, template_name="RunnerInfo.html")


def sendRunnerInfo(request):
    users = Users.objects.filter(verified=True, roleid=3)  # Get verified runners (roleid == 3)
    donRecs = donationrecord.objects.all()

    RunnerAmount = users.count()  # Total number of runners
    EventKilometers = users.aggregate(total_km=Sum('kilometers'))['total_km'] or 0  # Total km of all runners
    EventTotal = 0

    set.logger.print("test")

    # Calculate total donation amount
    for donRec in donRecs.filter(verified=True):
        if donRec.fixedamount:
            EventTotal += donRec.donation
        else:
            set.logger.print(donRec.iduser)
            km = 0
            try:
                km = users.get(iduser=donRec.iduser).kilometers
            except Exception as es:
                set.logger.print("error ", es)

            EventTotal += donRec.donation * km

    mail = MailSender()
    for usr in users:
        mail.SendMail(
            pReceiver=usr.email,
            pSubject="Charity Run Donation Overview",
            pMailText=loadRunnerInfo(
                request=request,
                user=usr,
                donRecs=donRecs,
                EventTotal=EventTotal,
                RunnerAmount=RunnerAmount,
                EventKilometers=EventKilometers
            ),
            pPlainText=""
        )

    mail.CloseConnection()

    return HttpResponse("Mails sent!")


def sendForgotPwd(request, email, frontendDomain):
    mail = MailSender()  # Connect to mail server and initialize class

    # Convert email to lowercase for case-insensitive matching
    user = get_object_or_404(Users, email__iexact=email)

    # Initiate sending the mail
    mail.SendMail(
        pReceiver=email,
        pSubject="Charity Run 2025 | User Login",
        pMailText=views.ForgotPwd_MailBody(request=request, user=user, frontendDomain=frontendDomain, email=email),
        pPlainText=""
    )

    mail.CloseConnection()  # Disconnect server connection

    return HttpResponse(f"Mail sent to email: {email} to change password")
