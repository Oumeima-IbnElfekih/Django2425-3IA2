from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import Conference
from django.views.generic import ListView,DetailView
# Create your views here.

def conferenceList(req):
    liste=Conference.objects.all().order_by('-start_date')
    print(liste)
    return render(req,'conferences/conferencelist.html',
                  {'conferenceslist':liste})

class ConferenceListView(ListView):
    model=Conference
    template_name ='conferences/conference_liste.html'
    context_object_name='conferences'
    def get_queryset(self):
        return Conference.objects.order_by('start_date')
    
class DetailsViewConference(DetailView):
    model=Conference
    template_name='conferences/conference_detail_view.html'
    context_object_name ='conference'