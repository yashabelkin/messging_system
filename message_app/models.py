from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    subject = models.CharField(max_length=200)
    message_content = models.CharField(max_length=5000)
    creation_date = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    sender = models.ForeignKey(User, related_name="sender", on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name="receiver", on_delete=models.CASCADE)


