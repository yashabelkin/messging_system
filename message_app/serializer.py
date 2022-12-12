from rest_framework.serializers import ModelSerializer
from .models import User, Message


class MessageSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = 'username', 'password'
