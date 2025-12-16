from django.contrib import admin

from ilanlar.models.ilan import Ilan


# Register your models here.
class IlanAdmin(admin.ModelAdmin):
    list_display = ('baslik', 'durum')

    fieldsets = [
        ('Temel Bilgiler',
         {
             'fields': (
                 'baslik', 'durum'
             )
         })
    ]
admin.site.register(Ilan, IlanAdmin)