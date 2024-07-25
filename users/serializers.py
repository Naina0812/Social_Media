from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'user', 'firstname', 'lastname', 'email', 'bio', 'date_of_birth', 'gender', 'updated', 'created', 'image']
