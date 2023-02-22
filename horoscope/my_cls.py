class ZodiacSign:
    all_signs = {}

    def __init__(self, sign: str, description: str, element: str):
        self.__sign = sign
        self.__description = description
        self.__element = element
        ZodiacSign.all_signs.update({sign: self})

    @property
    def sign(self):
        return self.__sign

    @property
    def description(self):
        return self.__description

    @property
    def element(self):
        return self.__element

    def __repr__(self):
        return f"Знак зодиака {self.sign.title()} стихия {self.__element}, {self.__description}"


ZodiacSign("aries", "Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).", "Огня")
ZodiacSign("taurus", "Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).", "Земли")
ZodiacSign("gemini", "Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).",
           "Воздушные")
ZodiacSign("cancer", "Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).", "Водные")
ZodiacSign("leo", "Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).).", "Огня")
ZodiacSign("virgo", "Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).",
           "Земли")
ZodiacSign("libra", "Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).",
           "Воздушные")
ZodiacSign("scorpio", "Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).",
           "Водные")
ZodiacSign("sagittarius",
           "Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).", "Огня")
ZodiacSign("capricorn", "Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).",
           "Земли")
ZodiacSign("aquarius",
           "Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).",
           "Воздушные"),
ZodiacSign("pisces", "Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).",
           "Водные")

