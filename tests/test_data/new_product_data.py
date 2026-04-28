from dataclasses import dataclass


@dataclass
class NewProductData:
    NAME = "Маргарита Пицца"
    DESCRIPTION = "Это Маргарита Пицца"
    CATEGORY = "Пицца"
    PRICE_INT = 1000
    PRICE_STR = "1000.00 ₽"
    IMAGE_URL = "https://clck.ru/3RytXr"