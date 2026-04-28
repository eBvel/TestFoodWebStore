from dataclasses import dataclass
from tests.test_data.login_data import LoginData
from tests.test_data.test_products import ProductFactory


@dataclass
class Datasets:
    ALL_USERS_LOGIN_DATA = [
        (LoginData.USER1_LOGIN, LoginData.USER1_PASSWORD),
        (LoginData.USER2_LOGIN, LoginData.USER2_PASSWORD),
        (LoginData.USER3_LOGIN, LoginData.USER3_PASSWORD),
        (LoginData.USER4_LOGIN, LoginData.USER4_PASSWORD),
        (LoginData.ADMIN_LOGIN, LoginData.ADMIN_PASSWORD)
    ]
    ALL_USERS_IDS = [
        "Buyer 1",
        "Buyer 2",
        "Buyer 3",
        "Buyer 4",
        "Admin"
    ]
    INCORRECT_PASSWORDS_LIST =  [
        (
            LoginData.USER1_LOGIN,
            LoginData.INCORRECT_USER1_PASSWORD
        ),
        (
            LoginData.ADMIN_LOGIN,
            LoginData.INCORRECT_ADMIN_PASSWORD
        )
    ]
    INCORRECT_LOGINS_LIST = [
        (
            LoginData.INCORRECT_USER1_LOGIN,
            LoginData.USER1_PASSWORD

        ),
        (
            LoginData.INCORRECT_ADMIN_LOGIN,
            LoginData.ADMIN_PASSWORD
        )
    ]
    USER1_ADMIN_IDS = [
        "Buyer 1",
        "Admin"
    ]

    CATALOG_CART_COUNTER = [1, 2, 3]
    CATALOG_STEP_OF_COUNT = [
        (2, 1),
        (5, 3)
    ]
    CATALOG_UPPER_LIMIT_OF_PRODUCT_COUNTER = [99, 100]

    CART_QUANTITIES_OF_CAVIAR = [1, 2]
    CART_QUANTITY_OF_PRODUCT = [2, 3]

    CHECKOUT_INCORRECT_NAMES = ["12345", "!@#$%^", "     "]
    CHECKOUT_INCORRECT_VALUES_FOR_NUMERIC_FIELD = ["abcde", "!@#$%^", "     "]

    ORDER_OVERVIEW_QUANTITIES_OF_PRODUCTS = [
        [5, 3]
    ]

    CREATE_PRODUCT_CORRECT_PRODUCTS = [
        ProductFactory.pepperoni(),
        ProductFactory.pepperoni(price=0)
    ]
    CREATE_PRODUCT_CORRECT_PRODUCTS_IDS = [
        'custom product',
        'product with zero price'
    ]
    CREATE_PRODUCT_INCORRECT_PRODUCTS = [
            ('name', ProductFactory.pepperoni(name='')),
            ('description', ProductFactory.pepperoni(description='')),
            ('price', ProductFactory.pepperoni(price=None)),
            ('price', ProductFactory.pepperoni(price=-1)),
            ('image_url', ProductFactory.pepperoni(image_url=''))
        ]
    CREATE_PRODUCT_INCORRECT_PRODUCTS_IDS = [
            'empty name',
            'empty description',
            'None price',
            'negative price',
            'empty image_url'
        ]