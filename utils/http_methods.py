from requests import Session, Response


class CustomRequests:
    def __init__(self, session):
        self.session : Session = session
        self.headers: dict = {"Content-type": "application/json"}
        self.cookie: dict = {}

    def get(self, url: str) -> Response:
        return self.session.get(
            url=url,
            headers=self.headers,
            cookies=self.cookie
        )

    def post(self, url: str, body: dict | str) -> Response:
        return self.session.post(
            url,
            json=body,
            headers=self.headers,
            cookies=self.cookie
        )

    def delete(self, url: str, body: dict | str =None) -> Response:
        return self.session.delete(
            url,
            json=body,
            headers=self.headers,
            cookies=self.cookie
        )

    def set_auth_token(self, token: str) -> None:
        self.headers["Authorization"] = f"Bearer {token}"