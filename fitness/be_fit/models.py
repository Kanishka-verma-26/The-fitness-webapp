from django.db import models
from django.utils import timezone


# Create your models here.
class Registered_Users(models.Model):
    user_name = models.CharField(max_length=50,unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50,null=False)
    c_pass = models.CharField(max_length=50,null=False)
    create_date = models.DateTimeField(default=timezone.now)

    class Meta:
        # verbose_name_plural='Registered User'
        verbose_name = 'Registered User'

    def __str__(self):
        return self.user_name




