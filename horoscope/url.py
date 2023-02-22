from django.contrib import admin
from django.urls import path
from horoscope import views as horoscope_views

urlpatterns = [
    path('<int:current_zodiac_int>', horoscope_views.horoscope_info_digit),
    path('<str:current_zodiac_str>', horoscope_views.horoscope_info, name="url_current_zodiac"),
]
