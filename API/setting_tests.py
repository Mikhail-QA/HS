import logging
import requests


class LogInfoApi:
    @staticmethod
    def log_info(log):
        logging.info(f"\nRequest url: {log.request.url} \nbody: {log.request.body}")
        logging.info(f"\nRequest status: {log.status_code} \nbody: {log.text}\n    ")


class TokenSave:
    @staticmethod
    def get_token_user_admin():
        user_admin = {
            "user[email]": "school.interneturok@yandex.ru",
            "user[password]": "34t3hEOfbTT2k",
            "remember_me": "true"
        }

        url1 = 'https://api-test-ege.interneturok.ru/auth/'

        session_admin = requests.Session()
        req1 = session_admin.post(url1, data=user_admin)
        result_tokentype = req1.json()['token']
        return result_tokentype
