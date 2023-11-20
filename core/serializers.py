from rest_framework import serializers
from django.contrib.auth import get_user_model

User=get_user_model()


class UserLoginSerializer(serializers.ModelSerializer):
    username=serializers.CharField(max_length=255)
    class Meta:
        model = User
        fields = ('id', 'username', 'password')

    