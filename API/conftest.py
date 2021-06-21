import pytest
import requests
from API.setting_tests import Parser


def pytest_addoption(parser):
    parser.addoption(
        '--url',
        action='store',
        default=Parser.config.get('PATH', 'url'),
        help="Base url",
    )


@pytest.fixture(scope='session')
def url(request):
    return request.config.getoption('--url')


@pytest.fixture(scope='function', autouse=False)
def admin():
    user_admin = {
        "user[email]": "ponomarev@interneturok.ru",
        "user[password]": "12qw34er5tfbTT2k",
        "remember_me": "true"
    }

    url1 = 'https://api-test-ege.interneturok.ru/auth/'

    session_admin = requests.Session()
    req1 = session_admin.post(url1, data=user_admin)
    result_tokentype = req1.json()['token']
    return result_tokentype
