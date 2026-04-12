import allure
from pages.base_page import BasePage
from utils.assertion import AssertValues
from webstore_config.locators import OrderOverviewLocators as locators
from webstore_config.links import Links


class OrderOverviewPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url =Links.ORDER_OVERVIEW_PAGE_URL

    def get_products_title(self):
        return [product.text for product in self.find_elements(locators.PRODUCTS)]

    def get_product_count(self, product_name):
        return (self
        .find_visible_element(locators.PRODUCT_DATA(product_name))
        .text
        .split(' ')[0])

    def get_product_price(self, product_name):
        return (self
        .find_visible_element(locators.PRODUCT_DATA(product_name))
        .text
        .split('по ')[1])

    @allure.step("Запрос списка продуктов в заказе")
    def get_products_in_order(self):
        products_dict = list()

        for product in self.find_elements(locators.PRODUCTS_IN_ORDER):
            product_values = product.text.split('\n')
            product_parameters = product_values[2].split(' ')
            products_dict.append(
                {
                    'name': product_values[0],
                    'description': product_values[1],
                    'count': product_parameters[0],
                    'price': product_parameters[-2]
                }
            )

        return products_dict

    @allure.step("Запрос данных пользователя в заказе")
    def get_user_data(self):
        return self.find_visible_element(locators.USER_DATA).text

    def get_first_name(self):
        return self.find_visible_element(locators.FIRST_NAME).text

    def get_second_name(self):
        return self.find_visible_element(locators.SECOND_NAME).text

    def get_middle_name(self):
        return self.find_visible_element(locators.MIDDLE_NAME).text

    @allure.step("Запрос данных о доставке заказа")
    def get_delivery_address(self):
        return self.find_visible_element(locators.DELIVERY_ADDRESS).text.split(': ')[1]

    @allure.step("Запрос данных об оплате заказа")
    def get_cart_number(self):
        return self.find_visible_element(locators.CART_NUMBER).text.split(': ')[1]

    @allure.step("Запрос итоговой стоимости заказа")
    def get_total_cost(self):
        return self.find_visible_element(locators.TOTAL_COST).text.split(': ')[1]

    def get_total_count(self):
        return int(self.find_visible_element(locators.TOTAL_COUNT).text.split(': ')[1])

    def click_complete_order_button(self):
        self.find_clickable_element(locators.COMPLETE_ORDER_BUTTON).click()

    def click_back_to_catalog_button(self):
        self.find_clickable_element(locators.BACK_TO_CATALOG_BUTTON)

    def check_first_name(self, expected_value):
        with allure.step(f'Проверка поля "Имя". Ожидаемое значение: '
                         f'f"{expected_value}"'):
            AssertValues.compare_values(
                "OVERVIEW: FIRST NAME",
                self.get_first_name(),
                f'Имя: {expected_value}'
            )

    def check_second_name(self, expected_value):
        with allure.step(f'Проверка поля "Фамилия". Ожидаемое значение: '
                         f'f"{expected_value}"'):
            AssertValues.compare_values(
                "OVERVIEW: SECOND NAME",
                self.get_second_name(),
                f'Фамилия: {expected_value}'
            )

    def check_middle_name(self, expected_value):
        with allure.step(f'Проверка поля "Отчество". Ожидаемое значение: '
                         f'f"{expected_value}"'):
            AssertValues.compare_values(
                "OVERVIEW: MIDDLE NAME",
                self.get_middle_name(),
                f'Отчество: {expected_value}'
            )

    def check_products_list(self, expected_value):
        with allure.step(f'Проверка списка товаров. Ожидаемое значение: '
                         f'f"{expected_value}"'):
            AssertValues.compare_values(
                "OVERVIEW: PRODUCTS LIST",
                set(self.get_products_title()),
                set(expected_value)
            )

    def check_products_count(self, product_name, expected_value):
        with allure.step(f'Проверка количества товаров. Ожидаемое значение:'
                         f' "{expected_value}"'):
            AssertValues.compare_values(
                f"OVERVIEW: PRODUCT({product_name}) COUNT",
                self.get_product_count(product_name),
                expected_value
            )
            # products = self.get_products_in_order()
            # for i, (product, expected_count) in enumerate(zip(products, expected_value), start=0):
            #     AssertValues.compare_values(
            #         f"PRODUCT '{product[i].get('name')}' COUNT",
            #         product[i].get('count'),
            #         expected_count
            #     )

    def check_products_price(self, product_name, expected_value):
        with allure.step(f'Проверка цены товаров. Ожидаемое значение:'
                         f' "{expected_value}"'):
            AssertValues.compare_values(
                f"OVERVIEW: PRODUCT({product_name}) PRICE",
                self.get_product_price(product_name),
                expected_value
            )

    def check_delivery_address(self, expected_value):
        with allure.step(f'Проверка адреса доставки. Ожидаемое значение:'
                         f' "{expected_value}"'):
            AssertValues.compare_values(
                "OVERVIEW: DELIVERY ADDRESS",
                self.get_delivery_address(),
                expected_value
            )

    def check_cart_number(self, expected_value):
        with allure.step(f'Проверка номера карты. Ожидаемое значение:'
                         f' "{expected_value}"'):
            AssertValues.compare_values(
                "OVERVIEW: CART NUMBER",
                self.get_cart_number(),
                expected_value
            )

    def check_total_count(self, expected_value):
        with allure.step(f'Проверка общего количества товаров. Ожидаемое '
                         f'значение: "{expected_value}"'):
            AssertValues.compare_values(
                "OVERVIEW: TOTAL COUNT",
                self.get_total_count(),
                expected_value
            )

    def check_total_cost(self, expected_value):
        with allure.step(f'Проверка общей стоимости товаров. Ожидаемое'
                         f' значение: "{expected_value}"'):
            AssertValues.compare_values(
                "OVERVIEW: TOTAL COST",
                self.get_total_cost(),
                expected_value
            )