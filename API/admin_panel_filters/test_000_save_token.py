import requests
import json
import time

user = {
    "user[email]": "school.interneturok@yandex.ru",
    "user[password]": "34t3hEOfbTT2k",
    "remember_me": "true"
}
headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
    "Connection": "keep-alive",
    "Content-Length": "97",
    "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
    "Host": "api-test-ege.interneturok.ru",
    "Origin": "https://web-dev01.interneturok.ru",
    "Referer": "https://web-dev01.interneturok.ru/school/login?from=logout&auth=true",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0"
}

# class SaveToken:
#
#     def test_000_create_variable(self):
#         file = open('token.py', 'w')
#         file.write('token = ')
#
#     def test_save_token(self):
#         url_login = "https://api-test-ege.interneturok.ru/auth/"
#
#         r = requests.post(url_login, data=user, headers=headers)
#         r.cookies.get_dict()
#         # print(r.json()["token"])
#         data = r.json()['token']
#         with open('token.py', 'a', encoding='utf-8') as file:
#             json.dump(data, file, indent=2, ensure_ascii=False)
#         file.close()
#
#         time.sleep(5)
#
#
# testInstance = SaveToken()
# testInstance.test_000_create_variable()
# testInstance.test_save_token()

directory_file = r"C:\Users\Михаил\HS\ApiToken.py"


class SaveToken:
    @staticmethod
    def test_000_create_variable():
        file = open(directory_file, 'w')
        file.write('class Gettoken: \n')
        file.write('    token = ')

    @staticmethod
    def test_save_token():
        url_login = "https://api-test-ege.interneturok.ru/auth/"

        r = requests.post(url_login, data=user, headers=headers)
        r.cookies.get_dict()
        # print(r.json()["token"])
        data = r.json()['token']
        with open(directory_file, 'a', encoding='utf-8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)
        file.close()

        time.sleep(5)


testInstance = SaveToken()
testInstance.test_000_create_variable()
testInstance.test_save_token()
