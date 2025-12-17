from django.contrib import admin

from ilanlar.models.ilan import Ilan


# Register your models here.
class IlanAdmin(admin.ModelAdmin):
    list_display = ('baslik', 'durum', 'pasif_nedeni')

    fieldsets = [
        ('Temel Bilgiler',
         {
             'fields': (
                 'baslik', 'durum', 'pasif_nedeni'
             )
         })
    ]

    class Media:
        js = ('admin/js/ilan_admin.js',)

admin.site.register(Ilan, IlanAdmin)