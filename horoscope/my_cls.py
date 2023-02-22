class ZodiacSign:
    def __init__(self, sign: str, description: str, element: str):
        self.__sign = sign
        self.__description = description
        self.__element = element

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
        return f"Знак зодиака {self.sign} стихия {self.__element}, {self.__description}"
