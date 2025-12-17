from django.contrib.auth.models import User
from django.db import models
from .durum import DURUM_SECENEKLERI, PASIF_NEDENLERI

class Ilan(models.Model):
    baslik = models.CharField(max_length=150, verbose_name='İlan Başlığı')
    durum = models.CharField(
        max_length=20, 
        choices=DURUM_SECENEKLERI, 
        default='Aktif', 
        verbose_name='İlan Durumu'
    )
    pasif_nedeni = models.CharField(
           max_length=20,
           choices=PASIF_NEDENLERI,
           default='Diger',
           verbose_name='Pasif Nedeni'
    )
    class Meta:
            # Yönetici panelinde tekil isim (Örn: "Ilan ekle")
            verbose_name = "İlan" 
            # Yönetici panelinde çoğul isim (Örn: "İlanlar")
            verbose_name_plural = "İlanlar"
    def __str__(self):
            return self.baslik