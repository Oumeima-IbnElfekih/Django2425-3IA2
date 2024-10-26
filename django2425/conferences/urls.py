from django.urls import path
from .views import *

urlpatterns = [
    path('list/',conferenceList,name="listeconf"),
    path('listViewConference/',ConferenceListView.as_view(),  name="listeViewconf"),
    path('details/<int:pk>/',DetailsViewConference.as_view(),name="detailConf"),
    path('create/',CreateViewConference.as_view(),name="conference_create"),
    path('update/<int:pk>/',UpdateViewConference.as_view(),name="conference_update"),
    path('delete/<int:pk>/',DeleteViewConference.as_view(),name="conference_delete"),
    path('reservation/<int:conference_id>/',reserve_conf,name="reserve")
] 