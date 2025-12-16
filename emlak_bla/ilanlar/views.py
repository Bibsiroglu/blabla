from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import ListView, CreateView

from ilanlar.models.ilan import Ilan 

class IlanListView(ListView):
    model: Ilan
    context_object_name = 'ilanlar'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context
class IlanCreateView(CreateView):
    model: Ilan
    fields = [
        'baslik', 'durum'
    ]

