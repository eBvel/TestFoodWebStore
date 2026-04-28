import dotenv
import os

from dataclasses import dataclass
dotenv.load_dotenv()


@dataclass
class LoginData:
    USER1_LOGIN = os.getenv('USER1_LOGIN')
    USER1_PASSWORD = os.getenv('USER1_PASSWORD')
    USER2_LOGIN = os.getenv('USER2_LOGIN')
    USER2_PASSWORD = os.getenv('USER2_PASSWORD')
    USER3_LOGIN = os.getenv('USER3_LOGIN')
    USER3_PASSWORD = os.getenv('USER3_PASSWORD')
    USER4_LOGIN = os.getenv('USER4_LOGIN')
    USER4_PASSWORD = os.getenv('USER4_PASSWORD')
    ADMIN_LOGIN = os.getenv('ADMIN_LOGIN')
    ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD')

    INCORRECT_USER1_LOGIN = "покупатель"
    INCORRECT_USER1_PASSWORD = "покупатель"
    INCORRECT_ADMIN_LOGIN = "admin1"
    INCORRECT_ADMIN_PASSWORD = "admin1"