from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .models import Message, User
from .serializer import MessageSerializer
from rest_framework import status
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'admin/': 'admin', 
        'messages/':'GET' '/' 'POST',
        'messages/<int:pk>/':'GET' '/' 'DELETE',
        'messages/unread/' : 'GET',
        'login/' : 'POST',
    }
    return Response(api_urls, status= status.HTTP_200_OK)


@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def messages_handler(request):
    user = request.user
    if request.method == 'GET':
        messages = Message.objects.filter(Q(sender=user) | Q(receiver=user))
        serializer = MessageSerializer(messages, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    elif request.method == 'POST':
        Message.objects.create(
            message_content = request.data['message_content'],
            subject = request.data['subject'],
            sender = User.objects.get(id = user.id),
            receiver = User.objects.get(id = request.data['receiver']))
        return Response(request.data, status=status.HTTP_201_CREATED)

    
@api_view(['GET', 'DELETE'])
@permission_classes([IsAuthenticated])
def message_handler(request, pk):
    user = request.user
    try:
        message = Message.objects.get(id = pk)
        if (message.receiver != user) and (message.sender != user):
            return Response ('Could not fonud this message in your messages', status=status.HTTP_403_FORBIDDEN)

    except Message.DoesNotExist:
        return Response("message does not exists", status=status.HTTP_404_NOT_FOUND)    

    if request.method == 'GET':
        message.is_read = True
        message.save()
        serializer = MessageSerializer(message)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        message.delete()    
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def unread_messages(request):
    user = request.user
    if request.method == 'GET':
        messages = Message.objects.filter(receiver=user, is_read=False)
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
