from django.shortcuts import render
from django.http import HttpResponse
from horoscope.my_cls import ZodiacSign

# Create your views here.


zodiac_dict = {
    "aries": ZodiacSign("aries", "Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).", "fire"),
    "taurus": ZodiacSign("taurus", "Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).", "fire"),
    "gemini": ZodiacSign("gemini", "Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).", "fire"),
    "cancer": ZodiacSign("cancer", "Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).).", "fire"),
    "leo": ZodiacSign("leo", "Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).", "fire"),
    "virgo": ZodiacSign("virgo", "Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).", "fire"),
    "scorpio": ZodiacSign("scorpio", "Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).",
                          "fire"),
    "sagittarius": ZodiacSign("sagittarius",
                              "Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).",
                              "fire"),
    "capricorn": ZodiacSign("capricorn", "Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).",
                            "fire"),
    "aquarius": ZodiacSign("aquarius",
                           "Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).",
                           "fire"),
    "pisces": ZodiacSign("pisces", "Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).",
                         "fire"),
}


def horoscope_info(request, current_zodiac):
    if zodiac_dict.get(current_zodiac):
        current_symbol = zodiac_dict[current_zodiac]
        return HttpResponse(f" {current_symbol}")
