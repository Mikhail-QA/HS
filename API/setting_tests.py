import logging
import requests
import os
import configparser


class LogInfoApi:
    @staticmethod
    def log_info(log):
        logging.info(f"\nRequest url: {log.request.url} \nbody: {log.request.body}")
        logging.info(f"\nRequest status: {log.status_code} \nbody: {log.text}\n    ")


class TokenSave:
    @staticmethod
    def get_token_user_admin():
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


class Parser:
    config = configparser.ConfigParser()
    file_local = os.path.join(os.path.dirname(__file__), '.', 'local.ini')
    config.read(file_local)
