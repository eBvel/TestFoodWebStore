from requests import Session, Response
from utils.http_methods import CustomRequests
from webstore_config.end_points import EndPoints
from typing_extensions import Self


class WebstoreAPI:
    def __init__(self, session: Session):
        self.request: CustomRequests = CustomRequests(session)
        self.admin_token: str = ''
        self.user_token: str = ''

    def auth(self, login: str, password: str) -> bool:
        response: Response = self.request.post(
            url=EndPoints.AUTH,
            body={
                "username": login,
                "password": password
            }
        )
        is_auth: bool = response.status_code == 200

        if is_auth and login == 'admin':
            self.admin_token = response.json().get('data').get('token')
        elif is_auth:
            self.user_token = response.json().get('data').get('token')

        return is_auth

    def by_admin(self) -> Self:
        if self.admin_token is not None:
            self.request.set_auth_token(self.admin_token)
        return self

    def by_user(self) -> Self:
        if self.user_token is not None:
            self.request.set_auth_token(self.user_token)
        return self

    def get_products_list(self) -> dict[str, int | str | float]:
        response: Response = self.request.get(EndPoints.PRODUCT_LIST)
        return response.json().get('data')

    def create_product(self, body_json: dict[str, str | float] | str) -> int:
        response: Response = self.request.post(
            url=EndPoints.CREATE_PRODUCT,
            body=body_json
        )
        return response.json().get('data').get('id')

    def delete_product(self, product_id: int) -> bool:
        response: Response = self.request.delete(
            url=EndPoints.DELETE_PRODUCT+f"{product_id}"
        )
        return response.status_code == 200

    def get_product_id_list(self) -> dict[str, int]:
        response: Response = self.request.get(EndPoints.CART_PRODUCTS)
        return response.json().get('data')

    def add_to_cart(self, product_id: int, quantity: int) -> bool:
        response: Response = self.request.post(
            url=EndPoints.CART_PRODUCT,
            body={
                "productId": product_id,
                "quantity": quantity
            }
        )
        return response.status_code == 200

    def remove_from_cart(self, product_id: int, quantity: int) -> bool:
        response: Response = self.request.delete(
            url=EndPoints.CART_PRODUCT,
            body={
                "productId": product_id,
                "quantity": quantity
            }
        )
        return response.status_code == 200