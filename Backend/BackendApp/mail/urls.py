from django.urls import path
from . import interface, views


urlpatterns = [
    path("sendmail/<int:UserID>", interface.sendUserVerifyMail, name="sendmail"),
    path("sendmail/don/<int:UserID>/<int:DonationId>/", interface.sendDonationVerifyMail, name="sendmailDon"),
    path("", views.indexMail, name="indexMail"),
    path("auth/<int:UserID>/<str:token>/", views.verify_user, name="verify_user"),
    path("auth/don/<int:UserID>/<int:DonRecID>/<str:token>/", views.verify_donRec, name="verify_user"),
    path("sponinfo/<str:DonRecEmail>", interface.sendSponsorInfo, name="verify_user"),

]