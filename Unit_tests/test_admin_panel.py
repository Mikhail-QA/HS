import requests
import allure
from Unit_tests.url import FilterSubjects

token = "691011ce025c0722b30c1e0cf29e6717d937284d75759cd2d3ed7bc5392de98c"
staging = "https://api-test-ege.interneturok.ru"


@allure.feature("Админка Фильтр Классы")
@allure.story("Проверяю ответ статус кода с 1 по 11 класс. Во всех остальных фильтрах выбран параметр (Все)")
class TestFilterSubjects:

    def test_all_subjects(self):
        with allure.step("Проверка параметра (Все) в классах"):
            url = FilterSubjects.klass_all
            r1 = requests.get(staging + url + token, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            assert r1.status_code == 200
            assert r1.url == staging + url + token

    def test_one_subjects(self):
        with allure.step("Проверка параметра (1) в классах"):
            url = FilterSubjects.klass_one
            r1 = requests.get(staging + url + token, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            assert r1.status_code == 200
            assert r1.url == staging + url + token

    def test_two_subjects(self):
        with allure.step("Проверка параметра (2) в классах"):
            url = FilterSubjects.klass_two
            r1 = requests.get(staging + url + token, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            assert r1.status_code == 200
            assert r1.url == staging + url + token

    def test_three_subjects(self):
        with allure.step("Проверка параметра (3) в классах"):
            url = FilterSubjects.klass_three
            r1 = requests.get(staging + url + token, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            assert r1.status_code == 200
            assert r1.url == staging + url + token

    def test_foure_subjects(self):
        with allure.step("Проверка параметра (4) в классах"):
            url = FilterSubjects.klass_four
            r1 = requests.get(staging + url + token, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            assert r1.status_code == 200
            assert r1.url == staging + url + token

    def test_five_subjects(self):
        with allure.step("Проверка параметра (5) в классах"):
            url = FilterSubjects.klass_five
            r1 = requests.get(staging + url + token, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            assert r1.status_code == 200
            assert r1.url == staging + url + token

    def test_six_subjects(self):
        with allure.step("Проверка параметра (6) в классах"):
            url = FilterSubjects.klass_six
            r1 = requests.get(staging + url + token, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            assert r1.status_code == 200
            assert r1.url == staging + url + token

    def test_seven_subjects(self):
        with allure.step("Проверка параметра (7) в классах"):
            url = FilterSubjects.klass_seven
            r1 = requests.get(staging + url + token, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            assert r1.status_code == 200
            assert r1.url == staging + url + token

    def test_eight_subjects(self):
        with allure.step("Проверка параметра (8) в классах"):
            url = FilterSubjects.klass_eight
            r1 = requests.get(staging + url + token, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            assert r1.status_code == 200
            assert r1.url == staging + url + token

    def test_nine_subjects(self):
        with allure.step("Проверка параметра (9) в классах"):
            url = FilterSubjects.klass_nine
            r1 = requests.get(staging + url + token, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            assert r1.status_code == 200
            assert r1.url == staging + url + token

    def test_ten_subjects(self):
        with allure.step("Проверка параметра (10) в классах"):
            url = FilterSubjects.klass_ten
            r1 = requests.get(staging + url + token, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            assert r1.status_code == 200
            assert r1.url == staging + url + token

    def test_eleven_subjects(self):
        with allure.step("Проверка параметра (11) в классах"):
            url = FilterSubjects.klass_eleven
            r1 = requests.get(staging + url + token, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            assert r1.status_code == 200
            assert r1.url == staging + url + token
