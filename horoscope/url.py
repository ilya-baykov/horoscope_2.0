from django.contrib import admin
from django.urls import path
from horoscope import views as horoscope_views

urlpatterns = [
    path('<str:current_zodiac>', horoscope_views.horoscope_info),
]
