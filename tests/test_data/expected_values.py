from dataclasses import dataclass


@dataclass
class ExpectedValues:
    CATALOG_COUNT_AFTER_ADD = 1
    CATALOG_COUNT_AFTER_REMOVE = 0

    CART_TOTAL_COST_IS_DISPLAY = True
    CART_TOTAL_COST_TO_STRING = lambda x: f'Итого: {x:.{0}f} ₽'
    CART_AFTER_CLEAR_IS_EMPTY =True
    CART_COUNT_AFTER_ADD = 2
    CART_PLACE_AN_ORDER_BUTTON_IS_NOT_DISPLAY = False
    CART_PLACE_AN_ORDER_BUTTON_IS_DISPLAY = True

    CHECKOUT_EMPTY_FIELD = ''

    OVERVIEW_TOTAL_COST_TO_STRING = lambda x: f'{x:.{0}f} ₽'

    EDIT_PRODUCT_IS_NOT_EXIST = False

    CREATE_PRODUCT_IS_EXIST = True
    CREATE_BUTTON_IS_DISABLED = False
    CREATE_ERROR_BORDER_COLOR = 'rgb(220, 53, 69)'

    UPDATE_PRODUCT_IS_EXIST = True