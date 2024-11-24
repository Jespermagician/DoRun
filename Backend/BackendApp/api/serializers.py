
from django.contrib.auth.models import User
from rest_framework import serializers

# Serializer für das User-Modell
class UserSerializer(serializers.ModelSerializer):
    # Metadaten für den Serializer
    class Meta:
        model = User  # Verknüpft den Serializer mit dem User-Modell
        fields = ["id", "username", "password"]  # Definiert die zu serialisierenden Felder
        extra_kwargs = {"password": {"write_only": True}}  # Passwortfeld ist nur schreibbar, wird nicht zurückgegeben

    # Überschreibt die Methode zum Erstellen eines Benutzers
    def create(self, validated_data):
        print(validated_data)  #
        # Erstellt einen neuen Benutzer mit der create_user-Methode (inkl. Passwort-Hashing)
        user = User.objects.create_user(**validated_data)
        return user