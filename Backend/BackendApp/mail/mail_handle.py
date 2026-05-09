"""
Mail handling module for the DoRun charity run application.

Provides functions for sending verification emails to users and donors,
sponsor notification emails, runner summary emails, and password reset emails.
Uses the MailSender class for SMTP communication.
"""
from django.shortcuts import get_object_or_404
from . import views
from BackendApp import settings as set
from django.http import HttpResponse
from api.models import Users, donationrecord
from django.db.models import Sum
from BackendApp.settings import logger
from .mailSender import MailSender

from django.views.decorators.csrf import csrf_exempt, csrf_protect


@csrf_protect
def sendUserVerifyMail(request, UserID, frontendDomain):
    """
    Send a verification email to a newly registered user.

    Generates an HTML email with a verification link containing a token
    that the user must click to confirm their email address.

    Args:
        request: Django HTTP request object
        UserID: ID of the user to verify
        frontendDomain: Base URL of the frontend (used in verification link)
    """
    user = get_object_or_404(Users, iduser=UserID)

    # Initialize mail server connection
    mail = MailSender()

    # Generate HTML and plain-text email content with verification link
    mailtext_html, mailtext_plain = views.UserAuth(
        request=request,
        UserID=UserID,
        user=user,
        frontendDomain=frontendDomain
    )

    # Send the verification email
    mail.SendMail(
        pReceiver=user.email,
        pSubject="Runner Registration - Charity Run",
        pMailText=mailtext_html,
        pPlainText=mailtext_plain,
    )

    # Close the SMTP connection
    mail.CloseConnection()

    return HttpResponse(f"Mail sent to {user.lastname}, {user.firstname}")


@csrf_protect
def sendDonationVerifyMail(request, UserID, DonationId, frontendDomain):
    """
    Send a verification email for a donation/sponsorship record.

    Similar to user verification, but for donation confirmations.
    Contains a link the sponsor must click to verify their pledge.

    Args:
        request: Django HTTP request object
        UserID: ID of the sponsored runner
        DonationId: ID of the donation record
        frontendDomain: Base URL of the frontend
    """
    user = get_object_or_404(Users, iduser=UserID)
    donRec = get_object_or_404(donationrecord, donationrecid=DonationId)

    mail = MailSender()

    mailtext_html, mailtext_plain = views.DonRecAuth(
        request=request,
        UserID=UserID,
        user=user,
        DonRecID=DonationId,
        DonRec=donRec,
        frontendDomain=frontendDomain
    )

    mail.SendMail(
        pReceiver=donRec.email,
        pSubject=f"Charity Run 2025 | Sponsor Registration: {user.firstname}",
        pMailText=mailtext_html,
        pPlainText=mailtext_plain,
    )

    mail.CloseConnection()

    return HttpResponse(f"Mail sent to {user.lastname}, {user.firstname}")


class SponsData:
    """
    Data container for sponsor information used in email templates.

    Calculates the total donation amount based on whether the donation
    is fixed or per-kilometer.

    Attributes:
        firstname: Sponsor's first name
        lastname: Sponsor's last name
        kilometer: Kilometers run by the sponsored runner
        FixedDonation: Whether this is a fixed-amount donation
        Donation: The pledged donation amount
        DonationTotal: Computed total (0 for fixed if 0 km, else amount;
                       for per-km: amount * kilometers)
    """
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

        # Calculate total donation: fixed donations require at least 1 km
        if pFixedDon:
            self.DonationTotal = 0
            if pKm > 0:
                self.DonationTotal = pDon
        else:
            # Per-km donation: amount * kilometers
            self.DonationTotal = pDon * pKm


def BinarySearchUsers(users, id):
    """
    Binary search for a user object by ID in a sorted list.

    Note: This can be replaced by Django ORM's built-in lookup in the future.

    Args:
        users: List of Users objects sorted by iduser
        id: User ID to find

    Returns:
        Index of the user in the list, or -1 if not found
    """
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


def loadSponsorInfo(request, DonRecEmail, users):
    """
    Build email content for a sponsor showing all their sponsored runners.

    For a given sponsor email, finds all donation records, looks up each
    sponsored runner's progress, and prepares HTML email data.

    Args:
        request: Django HTTP request object
        DonRecEmail: Sponsor's email address
        users: Pre-fetched list of all Users (sorted by ID for binary search)

    Returns:
        HTML email body as string
    """
    # Get all donation records for this sponsor email
    donRec = donationrecord.objects.filter(email=DonRecEmail)

    set.logger.print(donRec)

    TotalDonation: float = 0
    TotalKilometers = 0
    data = []

    # Iterate over each sponsored runner
    for donation in donRec:
        # Find the runner using binary search on the sorted user list
        usersIndex = BinarySearchUsers(users, donation.iduser)
        if usersIndex < 0:
            logger.print(f"Warning: User ID {donation.iduser} doesn't exist")
            continue

        Kilometers = users[usersIndex].kilometers

        # Build sponsor data entry for the runner
        dataRec = SponsData(
            pFirstname=users[usersIndex].firstname,
            pLastname=users[usersIndex].lastname,
            pKm=Kilometers,
            pFixedDon=donation.fixedamount,
            pDon=donation.donation
        )

        # Accumulate totals across all sponsored runners
        TotalDonation += dataRec.DonationTotal
        TotalKilometers += Kilometers
        data.append(dataRec)

    # Prepare template context
    context = {
        'name': f"{donRec[0].firstname} {donRec[0].lastname}",
        'Amount': len(donRec),
        'data': data,
        'Total': TotalDonation,
        'TotalKilometers': TotalKilometers,
    }

    set.logger.print(context)

    # Render the HTML email from template
    return views.RenderMailText(
        context=context, request=request, template_name="SponsorInfo.html"
    )


def sendSponsorInfo(request):
    """
    Send donation overview emails to all unique sponsors.

    Iterates over distinct sponsor email addresses, generates personalized
    summaries of all runners they sponsor, and sends them via email.
    """
    # Get all users sorted by ID (required for binary search in loadSponsorInfo)
    users = Users.objects.order_by("iduser")

    # Get distinct sponsor email addresses
    eMailArr = donationrecord.objects.values_list('email', flat=True).distinct()

    set.logger.print(users)

    mail = MailSender()

    for eMail in eMailArr:
        mail.SendMail(
            pReceiver=eMail,
            pSubject="Charity Run 2025 | Sponsor Donation Overview",
            pMailText=loadSponsorInfo(request=request, DonRecEmail=eMail, users=users),
            pPlainText=""
        )

    mail.CloseConnection()

    return HttpResponse("Mails sent!")


def loadRunnerInfo(request, donRecs, user, RunnerAmount, EventKilometers, EventTotal):
    """
    Build email content for a runner showing their sponsorship summary.

    Args:
        request: Django HTTP request object
        donRecs: Queryset of all donation records
        user: The runner's Users object
        RunnerAmount: Total number of runners in the event
        EventKilometers: Total kilometers across all runners
        EventTotal: Total donation amount across the event

    Returns:
        HTML email body as string
    """
    Kilometers = user.kilometers
    SponsorAmount = donRecs.filter(iduser=user.iduser).count()
    data = []
    RunnerTotal: float = 0

    # Iterate over this runner's specific donations
    for donation in donRecs.filter(iduser=user.iduser):
        dataRec = SponsData(
            pFirstname=donation.firstname,
            pLastname=donation.lastname,
            pKm=Kilometers,
            pFixedDon=donation.fixedamount,
            pDon=donation.donation
        )

        RunnerTotal += dataRec.DonationTotal
        data.append(dataRec)

    # Prepare template context
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

    return views.RenderMailText(
        context=context, request=request, template_name="RunnerInfo.html"
    )


def sendRunnerInfo(request):
    """
    Send summary emails to all verified runners.

    Each runner receives an overview of their sponsors, total donations,
    and event-wide statistics.
    """
    # Get verified runners only (roleid == 3)
    users = Users.objects.filter(verified=True, roleid=3)
    donRecs = donationrecord.objects.all()

    RunnerAmount = users.count()
    EventKilometers = users.aggregate(total_km=Sum('kilometers'))['total_km'] or 0
    EventTotal = 0

    # Calculate total event donation amount
    for donRec in donRecs.filter(verified=True):
        if donRec.fixedamount:
            EventTotal += donRec.donation
        else:
            set.logger.print(donRec.iduser)
            km = 0
            try:
                km = users.get(iduser=donRec.iduser).kilometers
            except Exception as es:
                set.logger.print("error", es)

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
    """
    Send a password reset email to a user.

    Looks up the user by email (case-insensitive), generates a password
    reset link, and sends it via email.

    Args:
        request: Django HTTP request object
        email: User's email address
        frontendDomain: Base URL of the frontend (used in reset link)
    """
    mail = MailSender()

    # Case-insensitive email lookup
    user = get_object_or_404(Users, email__iexact=email)

    mail.SendMail(
        pReceiver=email,
        pSubject="Charity Run 2025 | User Login",
        pMailText=views.ForgotPwd_MailBody(
            request=request, user=user, frontendDomain=frontendDomain, email=email
        ),
        pPlainText=""
    )

    mail.CloseConnection()

    return HttpResponse(f"Mail sent to email: {email} to change password")
