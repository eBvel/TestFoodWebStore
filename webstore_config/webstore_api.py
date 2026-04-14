from utils.http_methods import CustomRequests


class WebstoreAPI:
    def __init__(self, session):
        self.request = CustomRequests(session)
        self.base_url = "http://91.197.96.80:5267/api/v1/"
        self.auth_end_point = f"{self.base_url}authorization/login"
        self.create_product_end_point = f"{self.base_url}storage/product"
        self.delete_product_end_point = f"{self.base_url}storage/product?id="
        self.cart_end_point = f"{self.base_url}cart/product"

    def auth_by_admin(self, login, password):
        response = self.request.post(
            url=self.auth_end_point,
            body={
                "username": login,
                "password": password
            }
        )
        self.request.set_auth_token(response.json().get('data').get('token'))
        return response.status_code == 200


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

    def add_to_cart(self, product_id, count):
        response = self.request.post(
            url=self.cart_end_point,
            body={
                "productId": product_id,
                "quantity": count
            }
        )
        return response.status_code == 200

    def remove_from_cart(self, product_id, count):
        response = self.request.delete(
            url=self.cart_end_point,
            body={
                "productId": product_id,
                "quantity": count
            }
        )
        return response.status_code == 200