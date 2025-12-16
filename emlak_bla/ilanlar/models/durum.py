from django.contrib.auth.models import User
from django.db import models

DURUM_SECENEKLERI = [
    ('Aktif', 'Aktif'), 
    ('Pasif', 'Pasif')
]

class Durum (models.Model):
    durum = models.CharField(
        max_length=20, 
        choices=DURUM_SECENEKLERI, 
        default='Aktif', 
        verbose_name='Durum'
    )
def __str__(self):
        return self.durum