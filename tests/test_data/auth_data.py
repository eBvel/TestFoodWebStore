ALL_USERS_LOGIN_DATA = [
    ('покупатель1', 'покупатель1'),
    ('покупатель2', 'покупатель2'),
    ('покупатель3', 'покупатель3'),
    ('покупатель4', 'покупатель4'),
    ('admin', 'admin')
]
ALL_USERS_IDS = [
    "Buyer 1",
    "Buyer 2",
    "Buyer 3",
    "Buyer 4",
    "Admin"
]

USER1_LOGIN = "покупатель1"
USER1_PASSWORD = USER1_LOGIN
ADMIN_LOGIN = "admin"
ADMIN_PASSWORD = ADMIN_LOGIN
INCORRECT_USER1_LOGIN = "покупатель"
INCORRECT_USER1_PASSWORD = "покупатель"
INCORRECT_ADMIN_LOGIN = "admin1"
INCORRECT_ADMIN_PASSWORD = "admin1"

INCORRECT_PASSWORDS_LIST =  [
    [
        USER1_LOGIN,
        INCORRECT_USER1_PASSWORD
    ],
    [
        ADMIN_LOGIN,
        INCORRECT_ADMIN_PASSWORD
    ]
]

INCORRECT_LOGINS_LIST = [
    [
        INCORRECT_USER1_LOGIN,
        USER1_PASSWORD

    ],
    [
        INCORRECT_ADMIN_LOGIN,
        ADMIN_PASSWORD
    ]
]

USER1_ADMIN_IDS = [
    "Buyer 1",
    "Admin"
]