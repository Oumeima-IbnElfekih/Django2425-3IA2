from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import Conference,Category
from users.models import Reservation
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404,redirect
# Create your views here.

@login_required(login_url="login")
def conferenceList(req):
    liste=Conference.objects.all().order_by('-start_date')
    print(liste)
    return render(req,'conferences/conferencelist.html',
                  {'conferenceslist':liste})

class ConferenceListView(ListView):
    model=Conference
    template_name ='conferences/conference_liste.html'
    context_object_name='conferences'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        user_reservations=Reservation.objects.filter(participant=self.request.user).values_list('conference_id',flat=True)
        context['user_reservations']=user_reservations
        return context
    def get_queryset(self):
        category_id=self.request.GET.get('category')
        query=Conference.objects.order_by('start_date')
        if category_id:
            query=Conference.objects.filter(category=category_id)
        return query
    
class DetailsViewConference(LoginRequiredMixin, DetailView):
    model = Conference
    template_name = 'conferences/conference_detail_view.html'
    context_object_name = 'conference'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        conference = self.get_object()
        # Récupérer les réservations associées à cette conférence
        context['reservations'] = Reservation.objects.filter(conference=conference)
        return context

class CreateViewConference(LoginRequiredMixin,CreateView):
    login_url=reverse_lazy('login')
    model=Conference
    template_name='conferences/conference_form.html'
    form_class=ConferenceForm
    #fields=['title','description','start_date','end_date','location','price','capacity','program','category'] 
    success_url = reverse_lazy('listeViewconf')   


class UpdateViewConference(UpdateView):
    model=Conference
    fields=['title','description','start_date','end_date','location','price','capacity','program','category'] 
    success_url = reverse_lazy('listeViewconf') 


class DeleteViewConference(DeleteView):
    model=Conference
    success_url = reverse_lazy('listeViewconf') 



def reserve_conf(req,conference_id):
    user=req.user
    conference=get_object_or_404(Conference,id=conference_id)
    if Reservation.objects.filter(participant=user,conference=conference).count()==0:
        reservation=Reservation.objects.create(participant=user,conference=conference)
        reservation.save()
        conference.capacity-=1
        conference.save()
        return redirect('listeViewconf')
    
