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
def index(request):
    return HttpResponse("Hello... ")

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    
#class Register(forms.Form):
#    Name = forms.TextField(label='Your Age',null=False)
#    LastName = forms.TextField(label='Your Lastname',null=False)
#    Email = forms.EmailField(label='E-Mail',unique=False, null=False)
#    Password = forms.BinaryField(label='Passwort',null=False)  # Manuelles Hashing erforderlich
#    Repeat_Password = forms.BinaryField(label='Repeat Passwort',null=False)
    
class RegistrationForm(forms.Form):
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
        
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Daten auslesen
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']  # Hinweis: Passwörter sollten gehasht werden!

            # Hier könntest du den Benutzer in der Datenbank speichern, z. B. mit Django-User-Modell
            # User.objects.create_user(username=email, first_name=first_name, last_name=last_name, password=password)
            NewUser = Users.RegisterUser(first_name,last_name,email,password)
            
            return JsonResponse(NewUser, safe=False)
            
            #return redirect('success')  # Weiterleitung auf eine Erfolgsseite
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})        

def cust_login(request):
    # Wenn das Formular über POST gesendet wurde
    if request.method == 'POST':
        # Benutzerdaten aus dem Formular erhalten
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Versuche den Benutzer zu authentifizieren
        user = Users.LoginUser(username,password)
        
        if user is not None:
            # Erfolgreiche Authentifizierung
            request.session["UserIsAuth"] = True
            messages.success(request, 'Erfolgreich eingeloggt!')
            return redirect('home')  # Nach erfolgreichem Login weiterleiten (zu einer Seite namens "home")
        else:
            # Fehlgeschlagene Authentifizierung
            request.session["UserIsAuth"] = False
            messages.error(request, 'Benutzername oder Passwort sind falsch.')
            return redirect('login')  # Benutzer zurück zur Login-Seite leiten

    # Wenn es sich um eine GET-Anfrage handelt, das Login-Formular anzeigen
    return render(request, 'login.html')

def home(request):
    if (request.session["UserIsAuth"] == True):
        return render(request, 'home.html')