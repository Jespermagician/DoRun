from django.urls import path
from . import mail_handle, views


urlpatterns = [
    path("sendmail/<int:UserID>", mail_handle.sendUserVerifyMail, name="sendmail"),
    path("sendmail/don/<int:UserID>/<int:DonationId>/", mail_handle.sendDonationVerifyMail, name="sendmailDon"),
    path("", views.indexMail, name="indexMail"),
    path("auth/<int:UserID>/<str:token>/", views.verify_user, name="verify_user"),
    path("auth/don/<int:UserID>/<int:DonRecID>/<str:token>/", views.verify_donRec, name="verify_user"),
    path("sponinfo", views.SendInfoMailsSponsors, name="send_Sponsor_info"),
    path("runinfo", views.SendInfoMailsRunners, name="send_Runner_info"),
]