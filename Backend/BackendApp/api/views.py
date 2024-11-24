from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny
from django import forms
from django.http import JsonResponse
from .models import Users
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import login, authenticate

# Create ur views here
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    
class RegistrationForm(forms.Form):
    #Input fields for registration
    first_name = forms.CharField(label='Your First Name', max_length=100, required=True)
    last_name = forms.CharField(label='Your Last Name', max_length=100, required=True)
    email = forms.EmailField(label='E-Mail', required=True)
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(),
        required=True
    )
    repeat_password = forms.CharField(
        label='Repeat Password',
        widget=forms.PasswordInput(),
        required=True
    )

    # Optionale Methode zur Validierung von Passwortfeldern
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        repeat_password = cleaned_data.get("repeat_password")

        if password and repeat_password and password != repeat_password:
            raise forms.ValidationError("Passwords do not match!")

#Handels the registration page
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Daten auslesen
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            #Erstelle neuen Benutzer auf der Datenbank
            NewUser = Users.RegisterUser(first_name,last_name,email,password)
            
            #Nur für Ausgabe der UserID später ersetzen!
            NewUser = int(NewUser.iduser)
            
            return JsonResponse(NewUser, safe=False)
            
            #return redirect('success')  # Weiterleitung auf eine Erfolgsseite
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})        

#Login user
def cust_login(request):
    # Wenn das Formular über POST gesendet wurde
    if request.method == 'POST':
        # Benutzerdaten aus dem Formular erhalten
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Versuche den Benutzer anzumelden
        user = Users.LoginUser(username,password)
        
        if user is not None:
            # Erfolgreiche anmeldung
            # Setzt für die session die anmeldung auf true(Verwendung um Seiten nur für Nutzer anzuzeigen) 
            request.session["UserIsAuth"] = True
            request.session["iduser"] = user.iduser
            messages.success(request, 'Erfolgreich eingeloggt!')
            return redirect('home')  # Nach erfolgreichem Login weiterleiten (zu einer Seite namens "home")
        else:
            # Fehlgeschlagene anmeldung
            # Setzt für die session die anmeldung auf false(Verwendung um Seiten für nicht Nutzer zu blockieren)
            request.session["UserIsAuth"] = False
            messages.error(request, 'Benutzername oder Passwort sind falsch.')
            return redirect('login')  # Benutzer zurück zur Login-Seite leiten

    # Wenn es sich um eine GET-Anfrage handelt, das Login-Formular anzeigen
    return render(request, 'login.html')

def home(request):
# Prüft ob ein Benutzer angemeldet ist    
    if (request.session["UserIsAuth"] == True):
        return render(request, 'home.html')