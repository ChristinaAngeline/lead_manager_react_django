from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('frontend.urls')), #has to be above leads.url
    path('', include('leads.urls')),
]
