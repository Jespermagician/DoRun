from django.urls import path
from . import mail_handle, views

urlpatterns = [
    # Mail send to specific user to verify the user
    # mostly used as test
    path("sendmail/<int:UserID>/<str:frontendDomain>", mail_handle.sendUserVerifyMail, name="sendmail"),

    # Mail send to specific user to verify the donator
    path("sendmail/don/<int:UserID>/<int:DonationId>/<str:frontendDomain>", mail_handle.sendDonationVerifyMail, name="sendmailDon"),


    # Just an obsolet test
    path("", views.indexMail, name="indexMail"),

    # The user accecc this page to verify himself
    path("auth/<int:UserID>/<str:token>/<str:TimeStamp>", views.verify_user, name="verify_user"),


    # The user accecc this page to verify his donation
    path("auth/don/<int:UserID>/<int:DonRecID>/<str:token>/", views.verify_donRec, name="verify_don"),         

    # Sending the Info Mails to (almost) every user
    path("sponinfo", views.SendInfoMailsSponsors, name="send_Sponsor_info"),
    path("runinfo", views.SendInfoMailsRunners, name="send_Runner_info"),
]