from django.contrib.auth.models import User
from django.db import models
from django.db.models import Model


class Notification(Model):
    INFORMATION = "IN"
    WARNING = "WA"
    ERROR = "ER"

    TYPE_CHOICES = [
        (INFORMATION, "Information"),
        (WARNING, "Warning"),
        (ERROR, "Error"),
    ]

    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    type = models.CharField(max_length=2, choices=TYPE_CHOICES, default=INFORMATION)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'notifications'
        verbose_name = 'Notification'
