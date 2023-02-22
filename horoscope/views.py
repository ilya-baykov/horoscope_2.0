from django.shortcuts import render
from django.http import HttpResponse
from horoscope.my_cls import ZodiacSign

# Create your views here.


zodiac_dict = {
    "aries": ZodiacSign("aries", "Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).", "Огня"),
    "taurus": ZodiacSign("taurus", "Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).", "Земли"),
    "gemini": ZodiacSign("gemini", "Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).", "Земли"),
    "cancer": ZodiacSign("cancer", "Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).", "Огня"),
    "leo": ZodiacSign("leo", "Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).).", "Огня"),
    "virgo": ZodiacSign("virgo", "Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).", "Огня"),
    "libra": ZodiacSign("libra", "Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).", "Огня"),
    "scorpio": ZodiacSign("scorpio", "Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).",
                          "Огня"),
    "sagittarius": ZodiacSign("sagittarius",
                              "Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).", "Огня"),
    "capricorn": ZodiacSign("capricorn", "Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).",
                            "Огня"),
    "aquarius": ZodiacSign("aquarius",
                           "Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).",
                           "Огня"),
    "pisces": ZodiacSign("pisces", "Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).",
                         "Огня"),
}


def horoscope_info(request, current_zodiac):
    if zodiac_dict.get(current_zodiac):
        current_symbol = zodiac_dict[current_zodiac]
        return HttpResponse(f" {current_symbol}")
