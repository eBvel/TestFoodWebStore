from utils.http_methods import CustomRequests


class WebstoreAPI:
    def __init__(self, session):
        self.request = CustomRequests(session)
        self.base_url = "http://91.197.96.80:5267/api/v1/"

        self.admin_token = None
        self.user_token = None

        self.auth_end_point = f"{self.base_url}authorization/login"
        self.products_list = f"{self.base_url}storage/products"
        self.create_product_end_point = f"{self.base_url}storage/product"
        self.delete_product_end_point = f"{self.base_url}storage/product?id="
        self.cart_products_end_point = f"{self.base_url}cart/products"
        self.cart_product_end_point = f"{self.base_url}cart/product"

    def auth(self, login, password):
        response = self.request.post(
            url=self.auth_end_point,
            body={
                "username": login,
                "password": password
            }
        )
        is_auth = response.status_code == 200

        if is_auth and login is 'admin':
            self.admin_token = response.json().get('data').get('token')
        elif is_auth:
            self.user_token = response.json().get('data').get('token')

        return is_auth

    def by_admin(self):
        if self.admin_token is not None:
            self.request.set_auth_token(self.admin_token)
        return self

    def by_user(self):
        if self.user_token is not None:
            self.request.set_auth_token(self.user_token)
        return self

    def get_products_list(self):
        response = self.request.get(self.products_list)
        return response.json().get('data')

    def create_product(self, body_json):
        response = self.request.post(
            url=self.create_product_end_point,
            body=body_json
        )
        return response.json().get('data').get('id')

    def delete_product(self, product_id):
        response = self.request.delete(
            url=self.delete_product_end_point+f"{product_id}"
        )
        return response.status_code == 200

    def get_product_id_list(self):
        response = self.request.get(self.cart_products_end_point)
        return response.json().get('data')

    def add_to_cart(self, product_id, count):
        response = self.request.post(
            url=self.cart_product_end_point,
            body={
                "productId": product_id,
                "quantity": count
            }
        )
        return response.status_code == 200

    def remove_from_cart(self, product_id, count):
        response = self.request.delete(
            url=self.cart_product_end_point,
            body={
                "productId": product_id,
                "quantity": count
            }
        )
        return response.status_code == 200