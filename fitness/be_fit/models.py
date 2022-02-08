from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import User


# Create your models here.
class User_otp(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,unique=False)
    otp = models.CharField(max_length=6,editable=True)
    otp_generate_time = models.DateTimeField(default=datetime.datetime.now(tz=timezone.utc))
    otp_expiration_time = models.DateTimeField(default=datetime.datetime.now(tz=timezone.utc) + datetime.timedelta(minutes=2))

    def __str__(self):
        return self.user.username



