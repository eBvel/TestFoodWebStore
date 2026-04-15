from requests import Session


class CustomRequests:
    def __init__(self, session):
        self.session : Session = session
        self.headers = {"Content-type": "application/json"}
        self.cookie = {}

    def get(self, url):
        return self.session.get(
            url=url,
            headers=self.headers,
            cookies=self.cookie
        )

    def post(self, url, body):
        return self.session.post(
            url,
            json=body,
            headers=self.headers,
            cookies=self.cookie
        )

    def delete(self, url, body=None):
        return self.session.delete(
            url,
            json=body,
            headers=self.headers,
            cookies=self.cookie
        )

    def set_auth_token(self, token):
        self.headers["Authorization"] = f"Bearer {token}"