from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser ):
    CREATOR = 'CREATOR'
    SUBSCRIBER = 'SUBSCRIBER'

    ROLE_CHOICES = (
        (CREATOR, 'Créateur'),
        (SUBSCRIBER, 'Abonné'),
    )

    profile_photo = models.ImageField(verbose_name="Photo de profil")
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=SUBSCRIBER)
    follow = models.ManyToManyField(
        'self',
        limit_choices_to={'role': CREATOR},
        symmetrical=False
    )