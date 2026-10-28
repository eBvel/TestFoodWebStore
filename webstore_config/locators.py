from selenium.webdriver.common.by import By
from typing import Literal, Callable

ByType = Literal["id", "xpath", "link text", "partial link text", "name", "tag name", "class name", "css selector"]
LocatorType = tuple[ByType, str]
LambdaType = Callable[[str], LocatorType]


class BaseLocators:
    NAVIGATION_BAR: LocatorType = (
        By.XPATH, 
        "//button[@aria-label='Toggle navigation']"
    )
    HEADER_BUTTON: LocatorType = (
        By.XPATH,
        "//a[@class='router-link-active "
        "router-link-exact-active navbar-brand']"
    )
    CART_BUTTON: LocatorType = (
        By.XPATH,
        "//button[@class='btn btn-light btn-sm d-flex position-relative']"
    )
    HEADER: LocatorType = (By.XPATH, "//div[@class='navbar-brand']")


class AuthLocators:
    HEADER: LocatorType = (By.XPATH, "//div[@class='fs-2 mb-5 text-light']")
    LOGIN: LocatorType = (By.XPATH, "//input[@placeholder='Логин']")
    PASSWORD: LocatorType = (By.XPATH, "//input[@placeholder='Пароль']")
    LOGIN_BUTTON: LocatorType = (
        By.XPATH,
        "//button[contains(text(), 'Войти')]"
    )


class CatalogLocators:
    PRODUCT_TITLES: LocatorType = (
        By.XPATH,
        "//div[@class='card-title fs-4 text-success']"
    )
    COUNT_OF_PRODUCT: LambdaType = lambda product_name: (
        By.XPATH,
        f"//div[contains(text(), "
        f"'{product_name}')]/../../div[@class='m-auto']/div/input"
    )
    PRODUCT_IMG: LambdaType = lambda product_name: (
        By.XPATH,
        f"//div[contains(text(), '{product_name}')]/../..//img"
    )
    ADD_BUTTON: LambdaType = lambda product_name: (
        By.XPATH,
        f"//div[text()='{product_name}']"
        f"/../../div[@class='m-auto']/div/button/span[text()='add']"
    )
    REMOVE_BUTTON: LambdaType = lambda product_name: (
        By.XPATH,
        f"//div[text()='{product_name}']"
        f"/../../div[@class='m-auto']/div/button/span[text()='remove']"
    )
    CART_COUNTER: LocatorType = (By.XPATH, "//a[@href='/cart']/button/span[2]")
    PRODUCT_PRICE: LambdaType = lambda product_name: (
        By.XPATH,
        f"//div[text()='{product_name}']"
        f"/../../div[@class='fs-5 align-content-center m-3']"
    )
    PRODUCT_DESCRIPTION: LambdaType = lambda product_name: (
        By.XPATH,
        f"//div[text()='{product_name}']/../p"
    )


class NavigationBarLocators:
    HEADER: LocatorType = (By.XPATH, "//h5[@class='offcanvas-title']")
    EDIT_PRODUCTS_BUTTON: LocatorType = (
        By.XPATH,
        "//a[@href='/manageProductsPage']"
    )
    MENU: LocatorType = (By.XPATH, "//div[@id='offcanvasNavbar']")
    CATALOG_BUTTON: LocatorType = (
        By.XPATH,
        "//ul[@class='nav-item']/a[@href='/']"
    )
    CART_BUTTON: LocatorType = (
        By.XPATH,
        "//ul[@class='nav-item']/a[@href='/cart']"
    )
    LOGOUT_BUTTON: LocatorType = (By.XPATH, "//li[@class='nav-item']")


class CartLocators:
    CART_IS_EMPTY_TEXT: LocatorType = (
        By.XPATH,
        "//div[@class='mx-auto my-2 fs-5 text-center']"
    )
    PLACE_AN_ORDER_BUTTON: LocatorType = (
        By.XPATH,
        "//button[@class='btn btn-success text-light text-end px-5']"
    )
    REMOVE_BUTTON: LambdaType = lambda product_name: (
        By.XPATH,
        f"//div[text()='{product_name}']/../../div/div/button[1]"
    )
    ADD_BUTTON: LambdaType = lambda product_name: (
        By.XPATH,
        f"//div[text()='{product_name}']/../../div/div/button[2]"
    )
    COUNT_OF_PRODUCT: LambdaType = lambda product_name: (
        By.XPATH,
        f"//div[text()='{product_name}']/../../div/div/input"
    )
    PRODUCT_PRICE: LambdaType = lambda product_name: (
        By.XPATH,
        f"//div[text()='{product_name}']/../../div[2]/div[2]"
    )
    TOTAL_COST: LocatorType = (
        By.XPATH,
        "//div[@class='mx-2 my-4 fs-5 text-end']"
    )


class UserDataLocators:
    FIRST_NAME_FIELD: LocatorType = (By.XPATH, "//input[@placeholder='Имя']")
    SECOND_NAME_FIELD: LocatorType = (
        By.XPATH,
        "//input[@placeholder='Фамилия']"
    )
    MIDDLE_NAME_FIELD: LocatorType = (
        By.XPATH,
        "//input[@placeholder='Отчество']"
    )
    DELIVERY_ADDRESS_FIELD: LocatorType = (
        By.XPATH,
        "//input[@placeholder='Адрес доставки']"
    )
    CART_NUMBER_FIELD: LocatorType = (
        By.XPATH,
        "//input[@placeholder='Номер карты']"
    )
    PLACE_AN_ORDER_BUTTON: LocatorType = (
        By.XPATH,
        "//button[@class='btn btn-success text-light text-end px-5']"
    )
    BACK_TO_CATALOG_BUTTON: LocatorType = (
        By.XPATH,
        "//button[@class='btn btn-dark text-light text-end px-5']"
    )
    EMPTY_FIELDS_ALERT: LocatorType = (
        By.XPATH,
        "//div[@class='alert alert-danger']"
    )


class OrderOverviewLocators:
    DELIVERY_ADDRESS: LocatorType = (
        By.XPATH,
        "//div[@class='fs-6 ms-3'][2]/div[1]"
    )
    CART_NUMBER: LocatorType = (
        By.XPATH,
        "//div[@class='fs-6 ms-3'][3]/div[2]"
    )
    TOTAL_COST: LocatorType = (By.XPATH, "//div[@class='fs-6 ms-3'][4]/div[2]")
    TOTAL_COUNT: LocatorType = (
        By.XPATH,
        "//div[@class='fs-6 ms-3'][4]/div[1]"
    )
    COMPLETE_ORDER_BUTTON: LocatorType = (
        By.XPATH,
        "//button[@class='btn btn-success text-light text-end px-5']"
    )
    FIRST_NAME: LocatorType = (By.XPATH, "//div[@class='fs-6 ms-3'][1]/div[1]")
    SECOND_NAME: LocatorType = (
        By.XPATH,
        "//div[@class='fs-6 ms-3'][1]/div[2]"
    )
    MIDDLE_NAME: LocatorType = (
        By.XPATH,
        "//div[@class='fs-6 ms-3'][1]/div[3]"
    )
    PRODUCTS: LocatorType = (
        By.XPATH,
        "//div[@class='card-title fs-6 text-success']"
    )
    BACK_TO_CATALOG_BUTTON: LocatorType = (
        By.XPATH,
        "//button[@class='btn btn-dark text-light text-end px-5']"
    )
    PRODUCT_DATA: LambdaType = lambda product_name: (
        By.XPATH,
        f"//div[contains(text(), '{product_name}')]/../../div[2]"
    )


class CompleteLocators:
    COMPLETE_MESSAGE: LocatorType = (
        By.XPATH,
        "//div[@class='mx-auto mt-1 fs-4 fw-bold text-center']"
    )
    BACK_TO_CATALOG_BUTTON: LocatorType = (
        By.XPATH,
        "//button[@class='btn btn-success "
        "text-light text-end px-5 mx-auto mt-5']"
    )


class EditProductsLocators:
    CREATE_PRODUCT_BUTTON: LocatorType = (
        By.XPATH,
        "//button[@class='btn btn-success text-light text-end px-5']"
    )
    EDIT_PRODUCT_BUTTON: LambdaType = lambda product_name: (
        By.XPATH,
        f"//div[contains(text(), '{product_name}')]/../../../div[3]/a/button"
    )
    DELETE_PRODUCT_BUTTON: LambdaType = lambda product_name: (
        By.XPATH,
        f"//div[contains(text(), '{product_name}')]/../../../div[4]/button"
    )
    PRODUCT_IS_EXISTS: LambdaType = lambda product_name: (
        By.XPATH,
        f"//div[contains(text(), '{product_name}')]"
    )
    PRODUCT_DESCRIPTION: LambdaType = lambda product_name: (
        By.XPATH,
        f"//div[contains(text(), '{product_name}')]/../p"
    )
    PRODUCT_PRICE: LambdaType = lambda product_name: (
        By.XPATH,
        f"//div[contains(text(), '{product_name}')]/../../div[3]/div"
    )
    PRODUCT_IMAGE_URL: LambdaType = lambda product_name: (
        By.XPATH,
        f"//div[contains(text(), '{product_name}')]/../../../div[1]/img"
    )


class CreateProductLocators:
    ID_FIELD: LocatorType = (By.XPATH, "//input[@placeholder='id']")
    NAME_FIELD: LocatorType = (
        By.XPATH,
        "//input[@placeholder='Наименование']"
    )
    DESCRIPTION_FIELD: LocatorType = (
        By.XPATH,
        "//input[@placeholder='Описание']"
    )
    EXPECTED_CATEGORY_FIELD: LocatorType = (
        By.XPATH,
        "//input[@placeholder='Ожидаемая категория']"
    )
    PRICE_FIELD: LocatorType = (By.XPATH, "//input[@placeholder='Цена']")
    IMAGE_SOURCE_FIELD: LocatorType = (
        By.XPATH,
        "//input[@placeholder='Image Source']"
    )
    CREATE_PRODUCT_BUTTON: LocatorType = (
        By.XPATH,
        "//button[@class='btn btn-success text-light text-end px-5']"
    )
    BACK_TO_EDIT_PRODUCTS_PAGE_BUTTON: LocatorType = (
        By.XPATH,
        "//button[@class='btn btn-dark text-light text-end px-5']"
    )
    IMAGE: LocatorType = (
        By.XPATH,
        "//img[@class='object-fit-contain w-100 h-100']"
    )