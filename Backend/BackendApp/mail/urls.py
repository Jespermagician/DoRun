from django.urls import path
from . import interface, views


urlpatterns = [
    path("sendmail/", interface.do, name="sendmail"),
    path("", views.indexMail, name="indexMail")
]