from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    GENDER_CHOICES = (
        ('male', "O'g'il bola"),
        ('female', "Qiz bola"),
    )
    date_of_birth=models.DateField(null=True,blank=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, verbose_name="Jinsi")
    phone = models.CharField(max_length=20, verbose_name="Telefon")
    address = models.CharField(max_length=255, blank=True, null=True, verbose_name="Manzil")
    father_name = models.CharField(max_length=150, blank=True, null=True, verbose_name="Otasining ism-familiyasi")
    father_phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Otasining telefon raqami")
    mother_name = models.CharField(max_length=150, blank=True, null=True, verbose_name="Onasining ism-familiyasi")
    mother_phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Onasining telefon raqami")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Ro'yxatdan o‘tgan vaqt")