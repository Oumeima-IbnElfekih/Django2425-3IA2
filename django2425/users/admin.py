from django.contrib import admin
from .models import Participant,Reservation
# Register your models here.
#à revoir

class ParticipantAdmin(admin.ModelAdmin):
    def save_model(self,request,obj,form,change):
        obj.set_password(form.cleaned_data['password'])
        super().save_model(request,obj,form,change)

#l'erreur qu'on a eu en classe , c'est que j'ai mis ParticipantAdmin comme premier parametre dans la méthode register
admin.site.register(Participant,ParticipantAdmin)
admin.site.register(Reservation)
