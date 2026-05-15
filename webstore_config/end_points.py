

class EndPoints:
    BASE_URL: str = "http://91.197.96.80:5267/api/v1/"
    AUTH: str = f"{BASE_URL}authorization/login"
    PRODUCT_LIST: str = f"{BASE_URL}storage/products"
    CREATE_PRODUCT: str = f"{BASE_URL}storage/product"
    DELETE_PRODUCT: str = f"{BASE_URL}storage/product?id="
    CART_PRODUCTS: str = f"{BASE_URL}cart/products"
    CART_PRODUCT: str = f"{BASE_URL}cart/product"