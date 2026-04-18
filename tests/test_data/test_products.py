from faker import Faker
from dataclasses import dataclass
fake = Faker("ru_RU")


@dataclass
class Product:
    name: str
    description: str
    category: str
    price: float
    image_url: str

    def get_price_str(self):
        return f'{self.price} ₽'

    def to_json(self) -> dict[str, str | float]:
        return {
            "name": f"{self.name}",
            "price": self.price,
            "category": f"{self.category}",
            "actualCategory": f"{self.category}",
            "imageSource": f"{self.image_url}",
            "description": f"{self.description}"
        }


class ProductBuilder:
    def __init__(self):
        self.__name = None
        self.__description = None
        self.__category = None
        self.__price = None
        self.__image_url = None

    def with_name(self, name):
        self.__name = name
        return self

    def with_description(self, description):
        self.__description = description
        return self

    def with_category(self, category):
        self.__category = category
        return self

    def with_price(self, price):
        self.__price = price
        return self

    def with_image_url(self, url):
        self.__image_url = url
        return self

    def build(self):
        return Product(
            self.__name,
            self.__description,
            self.__category,
            self.__price,
            self.__image_url
        )


class ProductFactory:
    @staticmethod
    def create_product_by_type(product_type) -> Product:
        try:
            products = ProductFactory.get_product_types()
            return products[product_type]()
        except KeyError:
            return ProductFactory.create_product(
                product_name=fake.word(
                    ext_word_list=['Сырники', 'Бовы', 'Драники', 'Шашлык']
                ),
                description=fake.text(max_nb_chars=40),
                category=fake.word(
                    ext_word_list=['Десерт', 'Выпечка', 'Свинина']
                ),
                price=fake.pyfloat(
                    right_digits=0,
                    min_value=1.0,
                    max_value=10000.0
                ),
                image_url=fake.image_url(width=800, height=800)
            )

    @staticmethod
    def create_product(product_name, description, category, price, image_url):
        return (
            ProductBuilder()
            .with_name(product_name)
            .with_description(description)
            .with_category(category)
            .with_price(price)
            .with_image_url(image_url)
            .build()
        )

    @staticmethod
    def sandwich():
        return (
            ProductBuilder()
            .with_name('Сэндвич с ветчиной и сыром')
            .with_description(fake.text(max_nb_chars=40))
            .with_category('Сэндвич')
            .with_price(fake.pyfloat(
                right_digits=0,
                min_value=1.0,
                max_value=999.0
                )
            )
            .with_image_url('https://clck.ru/3RxCex')
            .build()
        )

    @staticmethod
    def caviar():
        return (
            ProductBuilder()
            .with_name('Черная икра Белуги')
            .with_description('Натуральная черная икра Вес: 500 г.')
            .with_category('Икра')
            .with_price(100000.00)
            .with_image_url('https://clck.ru/3RxEqM')
            .build()
        )

    @staticmethod
    def nuggets():
        return (
            ProductBuilder()
            .with_name('Наггетсы')
            .with_description(fake.text(max_nb_chars=40))
            .with_category(fake.word())
            .with_price(fake.pyfloat(
                right_digits=0,
                min_value=200.0,
                max_value=550.0
                )
            )
            .with_image_url('https://clck.ru/3Ryi2U')
            .build()
        )

    @staticmethod
    def pepperoni():
        return (
            ProductBuilder()
            .with_name('Пицца Пепперони')
            .with_description(fake.text(max_nb_chars=40))
            .with_category(fake.word())
            .with_price(fake.pyfloat(
                right_digits=0,
                min_value=550.0,
                max_value=1200.0
                )
            )
            .with_image_url('https://clck.ru/3Ryn8j')
            .build()
        )

    @staticmethod
    def margarita():
        return (
            ProductBuilder()
            .with_name('Пицца Маргарита')
            .with_description(fake.text(max_nb_chars=40))
            .with_category(fake.word())
            .with_price(fake.pyfloat(
                right_digits=0,
                min_value=550.0,
                max_value=1200.0
                )
            )
            .with_image_url('https://clck.ru/3Rystj')
            .build()
        )

    @staticmethod
    def get_product_types():
        return {
            'sandwich': ProductFactory.sandwich,
            'caviar': ProductFactory.caviar,
            'nuggets': ProductFactory.nuggets,
            'pepperoni': ProductFactory.pepperoni,
            'margarita': ProductFactory.margarita
        }


if __name__ == '__main__':
    pass