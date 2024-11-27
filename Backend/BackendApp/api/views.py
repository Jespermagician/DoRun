from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer , NoteSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Note

# Create ur views here
def index(request):
    return HttpResponse("Hello... ")



class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class NoteListCreate(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated] # U can not call this root, unless your authenticated and 

    def get_queryset(self):
        user = self.request.user 
        return Note.objects.filter(author=user) # get all Notes which are written by the User

    # Ovveritting the create Methode
    def perform_create(self, serializer): 
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)


class NoteDelete(generics.DestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user) # make sure u can only delete notes u have created
