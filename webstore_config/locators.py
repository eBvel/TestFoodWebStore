from selenium.webdriver.common.by import By


class BaseLocators:
    NAVIGATION_BAR = (By.XPATH, "//button[@aria-label='Toggle navigation']")
    HEADER_BUTTON = (By.XPATH, "//a[@class='router-link-active router-link-exact-active navbar-brand']")
    CART_BUTTON = (By.XPATH, "//button[@class='btn btn-light btn-sm d-flex position-relative']")


class AuthLocators:
    HEADER = (By.XPATH, "//div[@class='fs-2 mb-5 text-light']")
    LOGIN = (By.XPATH, "//input[@placeholder='Логин']")
    PASSWORD = (By.XPATH, "//input[@placeholder='Пароль']")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")


class CatalogLocators:
    HEADER = (By.XPATH, "//div[@class='navbar-brand']")
    PRODUCT_TITLES = (By.XPATH, "//div[@class='card-title fs-4 text-success']")
    COUNT_OF_PRODUCT = lambda product_name: \
        (By.XPATH, f"//div[contains(text(), '{product_name}')]/../../div[@class='m-auto']/div/input")
    PRODUCT = lambda product_name: \
        (By.XPATH, f"//div[contains(text(), '{product_name}')]/../..")
    PRODUCT_IMG = lambda product_name: \
        (By.XPATH, f"//div[contains(text(), '{product_name}')]/../..//img")
    ADD_BUTTON = lambda product_name: \
        (By.XPATH, f"//div[text()='{product_name}']/../../div[@class='m-auto']/div/button/span[text()='add']")
    REMOVE_BUTTON = lambda product_name: \
        (By.XPATH, f"//div[text()='{product_name}']/../../div[@class='m-auto']/div/button/span[text()='remove']")
    CART_COUNTER = (By.XPATH, "//a[@href='/cart']/button/span[2]")
    PRODUCT_PRICES = (By.XPATH, "//div[@class='fs-5 align-content-center m-3']")
    PRODUCT_PRICE = lambda product_name: \
        (By.XPATH, f"//div[text()='{product_name}']/../../div[@class='fs-5 align-content-center m-3']")
    PRODUCT_DESCRIPTION = lambda product_name: \
        (By.XPATH, f"//div[text()='{product_name}']/../p")


class NavigationBarLocators:
    HEADER = (By.XPATH, "//h5[@class='offcanvas-title']")
    EDIT_PRODUCTS_BUTTON = (By.XPATH, "//a[@href='/manageProductsPage']")
    NAVIGATION_BAR = (By.XPATH, "//button[@aria-label='Toggle navigation']")
    CATALOG_BUTTON = (By.XPATH, "//ul[@class='nav-item']/a[@href='/']")
    CART_BUTTON = (By.XPATH, "//ul[@class='nav-item']/a[@href='/cart']")
    LOGOUT_BUTTON = (By.XPATH, "//li[@class='nav-item']")


class CartLocators:
    HEADER = (By.XPATH, "//div[@class='navbar-brand']")
    CART_IS_EMPTY_TEXT = (By.XPATH, "//div[@class='mx-auto my-2 fs-5 text-center']")
    TOTAL_PRICE = (By.XPATH, "//div[@class='mx-2 my-4 fs-5 text-end']")
    PLACE_AN_ORDER_BUTTON = (By.XPATH, "//button[@class='btn btn-success text-light text-end px-5']")
    REMOVE_BUTTON = lambda product_name: \
        (By.XPATH, f"//div[text()='{product_name}']/../../div/div/button[1]")
    ADD_BUTTON = lambda product_name: \
        (By.XPATH, f"//div[text()='{product_name}']/../../div/div/button[2]")
    COUNT_OF_PRODUCT = lambda product_name: \
        (By.XPATH, f"//div[text()='{product_name}']/../../div/div/input")
    PRODUCTS_TITLE = (By.XPATH, "//div[@class='card-title fs-4 text-success']")
    PRODUCT_PRICE = lambda product_name: \
        (By.XPATH, f"//div[text()='{product_name}']/../../div[2]/div[2]")
    TOTAL_COST = (By.XPATH, "//div[@class='mx-2 my-4 fs-5 text-end']")


class UserDataLocators:
    HEADER = (By.XPATH, "//div[@class='navbar-brand']")
    FIRST_NAME_FIELD = (By.XPATH, "//input[@placeholder='Имя']")
    SECOND_NAME_FIELD = (By.XPATH, "//input[@placeholder='Фамилия']")
    MIDDLE_NAME_FIELD = (By.XPATH, "//input[@placeholder='Отчество']")
    DELIVERY_ADDRESS_FIELD = (By.XPATH, "//input[@placeholder='Адрес доставки']")
    CART_NUMBER_FIELD = (By.XPATH, "//input[@placeholder='Номер карты']")
    PLACE_AN_ORDER_BUTTON = (By.XPATH, "//button[@class='btn btn-success text-light text-end px-5']")
    BACK_TO_CATALOG_BUTTON = (By.XPATH, "//button[@class='btn btn-dark text-light text-end px-5']")
    EMPTY_FIELDS_ALERT = (By.XPATH, "//div[@class='alert alert-danger']")


class OrderOverviewLocators:
    HEADER = (By.XPATH, "//div[@class='navbar-brand']")
    PRODUCTS_IN_ORDER = (By.XPATH, "//div[@class='card-body mx-2 d-flex flex-column justify-content-between']")
    USER_DATA = (By.XPATH, "//div[@class='fs-6 ms-3'][1]")
    DELIVERY_ADDRESS = (By.XPATH, "//div[@class='fs-6 ms-3'][2]/div[1]")
    CART_NUMBER = (By.XPATH, "//div[@class='fs-6 ms-3'][3]/div[2]")
    TOTAL_COST = (By.XPATH, "//div[@class='fs-6 ms-3'][4]/div[2]")
    TOTAL_COUNT = (By.XPATH, "//div[@class='fs-6 ms-3'][4]/div[1]")
    COMPLETE_ORDER_BUTTON = (By.XPATH, "//button[@class='btn btn-success text-light text-end px-5']")
    FIRST_NAME = (By.XPATH, "//div[@class='fs-6 ms-3'][1]/div[1]")
    SECOND_NAME = (By.XPATH, "//div[@class='fs-6 ms-3'][1]/div[2]")
    MIDDLE_NAME = (By.XPATH, "//div[@class='fs-6 ms-3'][1]/div[3]")
    PRODUCTS = (By.XPATH, "//div[@class='card-title fs-6 text-success']")
    BACK_TO_CATALOG_BUTTON = (By.XPATH, "//button[@class='btn btn-dark text-light text-end px-5']")
    PRODUCT_DATA = lambda product_name: \
        (By.XPATH, f"//div[contains(text(), '{product_name}')]/../../div[2]")


class CompleteLocators:
    HEADER = (By.XPATH, "//div[@class='navbar-brand']")
    COMPLETE_MESSAGE = (By.XPATH, "//div[@class='mx-auto mt-1 fs-4 fw-bold text-center']")
    BACK_TO_CATALOG_BUTTON = (By.XPATH, "//button[@class='btn btn-success text-light text-end px-5 mx-auto mt-5']")


class EditProductsLocators:
    HEADER = (By.XPATH, "//div[@class='navbar-brand']")
    CREATE_PRODUCT_BUTTON = (By.XPATH, "//button[@class='btn btn-success text-light text-end px-5']")
    EDIT_PRODUCT_BUTTON = lambda product_name: \
        (By.XPATH, f"//div[contains(text(), '{product_name}')]/../../../div[3]/a/button")
    DELETE_PRODUCT_BUTTON = lambda product_name: \
        (By.XPATH, f"//div[contains(text(), '{product_name}')]/../../../div[4]/button")
    PRODUCT_IS_EXISTS = lambda product_name: \
        (By.XPATH, f"//div[contains(text(), '{product_name}')]")


class CreateProductLocators:
    HEADER = (By.XPATH, "//div[@class='navbar-brand']")
    ID_FIELD = (By.XPATH, "//input[@placeholder='id']")
    NAME_FIELD = (By.XPATH, "//input[@placeholder='Наименование']")
    DESCRIPTION_FIELD = (By.XPATH, "//input[@placeholder='Описание']")
    EXPECTED_CATEGORY_FIELD = (By.XPATH, "//input[@placeholder='Ожидаемая категория']")
    CATEGORY_IN_LIST_FIELD = (By.XPATH, "//input[@class='form-control shadow-none rounded-1']")
    PRICE_FIELD = (By.XPATH, "//input[@placeholder='Цена']")
    IMAGE_SOURCE_FIELD = (By.XPATH, "//input[@placeholder='Image Source']")
    CREATE_PRODUCT_BUTTON = (By.XPATH, "//button[@class='btn btn-success text-light text-end px-5']")
    BACK_TO_EDIT_PRODUCTS_PAGE_BUTTON = (By.XPATH, "//button[@class='btn btn-dark text-light text-end px-5']")
    IMAGE = (By.XPATH, "//img[@class='object-fit-contain w-100 h-100']")