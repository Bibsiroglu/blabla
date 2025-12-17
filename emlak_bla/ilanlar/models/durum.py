from django.contrib.auth.models import User
from django.db import models

DURUM_SECENEKLERI = [
    ('Aktif', 'Aktif'), 
    ('Pasif', 'Pasif')
]

PASIF_NEDENLERI = [
      ('Satildi', 'Satıldı'),
      ('Kiralandi', 'Kiralandı'),
      ('Yayin_Suresi_Bitti', 'Yayın Süresi Bitti'),
      ('Yayindan_Kaldirildi', 'Yayından Kaldırıldı'),
      ('Diger', 'Diğer')
]

class Durum (models.Model):
    durum = models.CharField(
        max_length=20, 
        choices=DURUM_SECENEKLERI, 
        default='Aktif', 
        verbose_name='Durum'
    )

    pasif_nedeni = models.CharField(
          max_length=20,
          choices=PASIF_NEDENLERI,
          default='Diger',
          verbose_name='Pasif Nedeni'
    )

def __str__(self):
        return self.durum