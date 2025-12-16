from django.apps import AppConfig
  
class IlanlarConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ilanlar'
    # Admin panelinde görünen Türkçe isim
    verbose_name = 'İlan Yönetimi'