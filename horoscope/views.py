from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse
from horoscope.my_cls import *


# Create your views here.


def menu(requst):
    result = "<ol>"
    for sign in zodiac_dict:
        link = reverse("url_current_zodiac", args=(sign,))
        result += f"<li><a href = '{link}'>{sign.title()}</a></li>"
    result += "<ol>"
    return HttpResponse(f"{result}")


def horoscope_info(request, current_zodiac_str):
    if zodiac_dict.get(current_zodiac_str):
        current_symbol = zodiac_dict[current_zodiac_str]
        return HttpResponse(f" {current_symbol}")
    else:
        return HttpResponseNotFound(
            f"Нам жаль , но мы не знам такой знак зодиака , вы точно имели в виду - {current_zodiac_str}?")


def horoscope_info_digit(requese, current_zodiac_int):
    if len(zodiac_list) >= current_zodiac_int > 0:
        link = reverse("url_current_zodiac", args=(zodiac_list[current_zodiac_int - 1],))
        return HttpResponseRedirect(link)
    else:
        return HttpResponseNotFound(
            f"Нам жаль , но мы не знам  знак зодиака под цифрой - {current_zodiac_int}")


def sign_type(request):
    result = "<ul>"
    for sign_en, sign_ru in zodiac_elements.items():
        link = f"{reverse('type_name')}/{sign_en}"
        result += f"<li> <a href = '{link}'>{sign_ru}</a></li>"
    result += "</ul>"
    return HttpResponse(f"<H3>4 cтихии знаков:</H3>  <br>{result}")


def meme(request):
    return HttpResponse(f"лол , это реально работает ?! )№ !) №) xD")
