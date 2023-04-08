import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)

    # CHOICES
    USER_TYPE_ROOT = 1
    USER_TYPE_CLIENT = 2
    USER_TYPE_REGULAR = 3
    USER_TYPE_PREMIUN = 4
    USER_TYPE_CHOICES = (
        (USER_TYPE_ROOT, 'root'),
        (USER_TYPE_CLIENT, 'client'),
        (USER_TYPE_REGULAR, 'regular'),
        (USER_TYPE_PREMIUN, 'premiun'),
    )

    type_user = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, null=False)
