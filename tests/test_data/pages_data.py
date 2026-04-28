from dataclasses import dataclass


@dataclass
class TechnicalData:
    HTTPS_URL = 'https://91.197.96.80'
    MAX_TIME_OF_LOAD_WEBSITE = 3.0


@dataclass
class AuthData:
    HEADER = 'Авторизация'


@dataclass
class NavigationData:
    HEADER = 'Меню'


@dataclass
class CatalogData:
    HEADER = 'Продукты'
    MIN_PRODUCT_COUNT =  0
    MAX_PRODUCT_COUNT = 100


@dataclass
class CartData:
    HEADER = 'Корзинка'
    EMPTY_TEXT = "в корзине пока пусто"
    MAX_TOTAL_COST = "Итого: 100000 ₽"


@dataclass
class CheckoutData:
    HEADER = 'Оформление заказа: Данные пользователя'
    ALL_EMPTY_FIELDS_MESSAGE = ("Введите имя, фамилию, отчество, "
                                "адрес доставки, номер карты")


@dataclass
class OrderOverviewData:
    HEADER = 'Оформление заказа: Подтверждение заказа'


@dataclass
class CompleteData:
    HEADER = 'Оформление заказа: Заказ успешно создан'
    SUCCESS_MESSAGE = 'Ваш заказ успешно создан'


@dataclass
class EditProductsData:
    HEADER = 'Редактирование: Товары'


@dataclass
class CreateProductData:
    HEADER = 'Редактирование: Товар'


@dataclass
class UpdateProductData(CreateProductData):
    pass