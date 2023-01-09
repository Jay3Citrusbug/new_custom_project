from django.contrib import admin
from django.urls import path
from .import views



urlpatterns = [
    path("", views.Campaign.as_view(), name='campaign'),
    path("campaign/", views.Campaign.as_view(), name='campaign'),
    path("campaign-creation/", views.CampaignCreate.as_view(),
         name='campaign-creation'),
    path("add_campaign/", views.AddCampaign.as_view(), name='add_campaign'),
    
]