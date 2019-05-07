import requests
import allure
from .request_list.url_login import TildaPage

user = {
    "user[email]": "hexcal@mail.ru",
    "user[password]": "123456",
}


@allure.step
def test_forget_your_password():
    r1 = requests.get(TildaPage.forget_your_password, allow_redirects=False)
    try:
        r1.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print('ERROR: %s' % e)
    assert r1.status_code == 200


@allure.step
def test_login_in_tilda():
    r1 = requests.post(TildaPage.login, data=user, allow_redirects=False)
    try:
        r1.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print('ERROR: %s' % e)
    assert r1.status_code == 200
