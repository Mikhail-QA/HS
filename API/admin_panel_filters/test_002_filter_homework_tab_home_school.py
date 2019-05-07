import requests
import allure
from API.admin_panel_filters.request_list.url_filter_homework import FilterGrades
from API.admin_panel_filters.request_list.url_filter_homework import FilterSubjects
from API.admin_panel_filters.request_list.url_filter_homework import FilterStatusDz
from API.admin_panel_filters.request_list.url_filter_homework import FilterWeek
from API.admin_panel_filters.request_list.url_filter_homework import FilterTypeDz
from API.admin_panel_filters.request_list.url_filter_homework import FilterFormatAccess
from ApiToken import Gettoken


token = Gettoken.token
staging = 'https://api-test-ege.interneturok.ru'
parameter_array = ['homeworks', 'total', 'page', 'per_page']
week_one = '&weeks[]=1'
week_twenty_five = '&weeks[]=25'
week_fifty_three = '&weeks[]=53'
year = '&year_id=2018'


# total_standard = 21  # это стандартное значение кол-ва изначально отображающихся на странице ДЗ.
# per_page_standard = 20  # это стандартное значение количества ДЗ на след. странице.


@allure.feature("Админка Домашние задания вкладка Домашняя школа фильтр Классы")
@allure.story("Проверяю ответ статус кода с 1 по 11 класс. Во всех остальных фильтрах (Все)")
class TestFilterGradesInHomework:
    def test_all_subjects(self):
        # ssesion = requests.Session()
        # ssesion.trust_env = False
        with allure.step("Проверка параметра (Все) в классах"):
            url = FilterGrades.klass_all
            r1 = requests.get(staging + url + token + year, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array
        # with allure.step("Проверяю наличие значения в параметре total:21"):
        #     assert dict(r1.json()).get('total') == total_standard
        # with allure.step("Проверяю наличие значения в параметре per_page:20"):
        #     assert dict(r1.json()).get('per_page') == per_page_standard

        # print("\n 1)", type(r1.json().keys()), "\n")
        # print("\n 2)", list(r1.json().keys()), "\n")
        # print("\n 3)", list(r1.json().keys()) == ['homeworks', 'total', 'page', 'per_page'], "\n")
        # print("\n 4)", r1.json().keys(), "\n")
        # print("\n 5)", dict(r1.json()).get('total') == total_standard, "\n")
        # print("\n 6)", dict(r1.json()).get('per_page') == per_page_standard, "\n")

    def test_one_subjects(self):
        with allure.step("Проверка параметра (1) в классах"):
            url = FilterGrades.klass_one
            r1 = requests.get(staging + url + token + year, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_two_subjects(self):
        with allure.step("Проверка параметра (2) в классах"):
            url = FilterGrades.klass_two
            r1 = requests.get(staging + url + token + year, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_three_subjects(self):
        with allure.step("Проверка параметра (3) в классах"):
            url = FilterGrades.klass_three
            r1 = requests.get(staging + url + token + year, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_foure_subjects(self):
        with allure.step("Проверка параметра (4) в классах"):
            url = FilterGrades.klass_four
            r1 = requests.get(staging + url + token + year, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_five_subjects(self):
        with allure.step("Проверка параметра (5) в классах"):
            url = FilterGrades.klass_five
            r1 = requests.get(staging + url + token + year, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_six_subjects(self):
        with allure.step("Проверка параметра (6) в классах"):
            url = FilterGrades.klass_six
            r1 = requests.get(staging + url + token + year, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_seven_subjects(self):
        with allure.step("Проверка параметра (7) в классах"):
            url = FilterGrades.klass_seven
            r1 = requests.get(staging + url + token + year, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_eight_subjects(self):
        with allure.step("Проверка параметра (8) в классах"):
            url = FilterGrades.klass_eight
            r1 = requests.get(staging + url + token + year, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_nine_subjects(self):
        with allure.step("Проверка параметра (9) в классах"):
            url = FilterGrades.klass_nine
            r1 = requests.get(staging + url + token + year, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_ten_subjects(self):
        with allure.step("Проверка параметра (10) в классах"):
            url = FilterGrades.klass_ten
            r1 = requests.get(staging + url + token + year, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_eleven_subjects(self):
        with allure.step("Проверка параметра (11) в классах"):
            url = FilterGrades.klass_eleven
            r1 = requests.get(staging + url + token + year, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array


@allure.feature("Админка Домашние задания вкладка Домашняя школа Фильтр Предметы")
@allure.story(
    "Проверяю ответ статус кода с первого предмета по последний. Во всех остальных фильтрах (Все)")
class TestFilterSubjectsInHomework:
    def test_subjects_russian_language(self):
        with allure.step("Проверка параметра (Русский язык) в предметах"):
            url = FilterSubjects.subject_russian_language
            r1 = requests.get(staging + url + token + year, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_subjects_literatura(self):
        with allure.step("Проверка параметра (Литература) в предметах"):
            url = FilterSubjects.subject_literatura
            r1 = requests.get(staging + url + token + year, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_subjects_english_language(self):
        with allure.step("Проверка параметра (Английский язык) в предметах"):
            url = FilterSubjects.subject_english_language
            r1 = requests.get(staging + url + token + year, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_subjects_matematika(self):
        with allure.step("Проверка параметра (Математика) в предметах"):
            url = FilterSubjects.subject_matematika
            r1 = requests.get(staging + url + token + year, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_subjects_history(self):
        with allure.step("Проверка параметра (История) в предметах"):
            url = FilterSubjects.subject_history
            r1 = requests.get(staging + url + token + year, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_subject_prirodavedenie(self):
        with allure.step("Проверка параметра (Природоведние) в предметах"):
            url = FilterSubjects.subject_prirodavedenie
            r1 = requests.get(staging + url + token + year, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_subject_objestvoznanie(self):
        with allure.step("Проверка параметра (Обществознание) в предметах"):
            url = FilterSubjects.subject_objestvoznanie
            r1 = requests.get(staging + url + token + year, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_subject_geografia(self):
        with allure.step("Проверка параметра (География) в предметах"):
            url = FilterSubjects.subject_geografia
            r1 = requests.get(staging + url + token + year, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_subject_biologia(self):
        with allure.step("Проверка параметра (Биология) в предметах"):
            url = FilterSubjects.subject_biologia
            r1 = requests.get(staging + url + token + year, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_subject_algebra_standart(self):
        with allure.step("Проверка параметра (Алгебра.Стандартный курс) в предметах"):
            url = FilterSubjects.subject_algebra_standart
            r1 = requests.get(staging + url + token + year, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_subject_geometria_standart(self):
        with allure.step("Проверка параметра (Геометрия.Стандартный курс) в предметах"):
            url = FilterSubjects.subject_geometria_standart
            r1 = requests.get(staging + url + token + year, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_subject_fizika_standart(self):
        with allure.step("Проверка параметра (Физика.Стандартный курс) в предметах"):
            url = FilterSubjects.subject_fizika_standart
            r1 = requests.get(staging + url + token + year, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_subject_informatika(self):
        with allure.step("Проверка параметра (Информатика) в предметах"):
            url = FilterSubjects.subject_informatika
            r1 = requests.get(staging + url + token + year, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_subject_himiya(self):
        with allure.step("Проверка параметра (Химия) в предметах"):
            url = FilterSubjects.subject_himiya
            r1 = requests.get(staging + url + token + year, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_subject_algebra(self):
        with allure.step("Проверка параметра (Алгебра) в предметах"):
            url = FilterSubjects.subject_algebra
            r1 = requests.get(staging + url + token + year, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_subject_geometria(self):
        with allure.step("Проверка параметра (Геометрия) в предметах"):
            url = FilterSubjects.subject_geometria
            r1 = requests.get(staging + url + token + year, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_subject_fizika(self):
        with allure.step("Проверка параметра (Физика) в предметах"):
            url = FilterSubjects.subject_fizika
            r1 = requests.get(staging + url + token + year, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_subject_literaturnoe_chtenie(self):
        with allure.step("Проверка параметра (Литературное чтение) в предметах"):
            url = FilterSubjects.subject_literaturnoe_chtenie
            r1 = requests.get(staging + url + token + year, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_subject_okruzauchi_mir(self):
        with allure.step("Проверка параметра (Окружающий мир) в предметах"):
            url = FilterSubjects.subject_okruzauchi_mir
            r1 = requests.get(staging + url + token + year, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_subject_matematika_profi(self):
        with allure.step("Проверка параметра (Математика Профильный) в предметах"):
            url = FilterSubjects.subject_matematika_profi
            r1 = requests.get(staging + url + token + year, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_subject_matematika_bazovyai(self):
        with allure.step("Проверка параметра (Математика Базовый) в предметах"):
            url = FilterSubjects.subject_matematika_bazovyai
            r1 = requests.get(staging + url + token + year, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_subject_vvodni_yrok(self):
        with allure.step("Проверка параметра (Вводный урок) в предметах"):
            url = FilterSubjects.subject_vvodni_yrok
            r1 = requests.get(staging + url + token + year, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_subject_podgotovka_k_OGE_matematika(self):
        with allure.step("Проверка параметра (Подготовка к ОГЭ по математике) в предметах"):
            url = FilterSubjects.subject_podgotovka_k_OGE_matematika
            r1 = requests.get(staging + url + token + year, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_subject_podgotovka_k_OGE_russian_language(self):
        with allure.step("Проверка параметра (Подготовка к ОГЭ по русскому языку) в предметах"):
            url = FilterSubjects.subject_podgotovka_k_OGE_russian_language
            r1 = requests.get(staging + url + token + year, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_subject_algebra_effective(self):
        with allure.step("Проверка параметра (Алгебра эффективный курс) в предметах"):
            url = FilterSubjects.subject_algebra_effective
            r1 = requests.get(staging + url + token + year, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_subject_fizika_effective(self):
        with allure.step("Проверка параметра (Физика эффективный курс) в предметах"):
            url = FilterSubjects.subject_fizika_effective
            r1 = requests.get(staging + url + token + year, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_subject_fizra(self):
        with allure.step("Проверка параметра (Физра) в предметах"):
            url = FilterSubjects.subject_fizra
            r1 = requests.get(staging + url + token + year, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_subject_tehnologiya(self):
        with allure.step("Проверка параметра (Технология) в предметах"):
            url = FilterSubjects.subject_tehnologiya
            r1 = requests.get(staging + url + token + year, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_subject_izo(self):
        with allure.step("Проверка параметра (ИЗО) в предметах"):
            url = FilterSubjects.subject_izo
            r1 = requests.get(staging + url + token + year, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_subject_music(self):
        with allure.step("Проверка параметра (Музыка) в предметах"):
            url = FilterSubjects.subject_music
            r1 = requests.get(staging + url + token + year, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_subject_osnovi_sovetskoi_itiki(self):
        with allure.step("Проверка параметра (Основы советской этики) в предметах"):
            url = FilterSubjects.subject_osnovi_sovetskoi_itiki
            r1 = requests.get(staging + url + token + year, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_subject_obz(self):
        with allure.step("Проверка параметра (ОБЖ) в предметах"):
            url = FilterSubjects.subject_obz
            r1 = requests.get(staging + url + token + year, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_subject_astronomia(self):
        with allure.step("Проверка параметра (Астрономия) в предметах"):
            url = FilterSubjects.subject_astronomia
            r1 = requests.get(staging + url + token + year, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_subject_geometria_effective(self):
        with allure.step("Проверка параметра (Геометрия эффективный курс) в предметах"):
            url = FilterSubjects.subject_geometria_effective
            r1 = requests.get(staging + url + token + year, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_subject_superjob(self):
        with allure.step("Проверка параметра (Профореинтация от SuperJob) в предметах"):
            url = FilterSubjects.subject_superJob
            r1 = requests.get(staging + url + token + year, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array


@allure.feature("Админка Домашние задания вкладка Домашняя школа Фильтр Неделя:")
@allure.story(
    "Проверяю ответ статус кода в 1, 25, 53, Статус ДЗ Непроверенные. Во всех остальных фильтрах (Все)")
class TestFilterWeeks:
    def test_week_one(self):
        with allure.step("Проверка 1 недели"):
            url = FilterWeek.week_one
            r1 = requests.get(staging + url + token + week_one + year, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_week_twenty_five(self):
        with allure.step("Проверка 25 недели"):
            url = FilterWeek.week_twenty_five
            r1 = requests.get(staging + url + token + week_twenty_five + year, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_week_fifty_three(self):
        with allure.step("Проверка 53 недели"):
            url = FilterWeek.week_fifty_three
            r1 = requests.get(staging + url + token + week_fifty_three + year, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array


@allure.feature("Админка Домашние задания вкладка Домашняя школа Фильтр Статус ДЗ:")
@allure.story(
    "Проверяю ответ статус кода во всех Статусах ДЗ. Во всех остальных фильтрах (Все)")
class TestFilterStatusDz:
    def test_status_unchecked(self):
        with allure.step("Проверка параметра (Непроверенные) в Статус ДЗ"):
            url = FilterStatusDz.status_unchecked
            r1 = requests.get(staging + url + token + year, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_status_checked(self):
        with allure.step("Проверка параметра (Проверенные) в Статус ДЗ"):
            url = FilterStatusDz.status_checked
            r1 = requests.get(staging + url + token + year, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_status_on_repeat(self):
        with allure.step("Проверка параметра (На повторе) в Статус ДЗ"):
            url = FilterStatusDz.status_on_repeat
            r1 = requests.get(staging + url + token + year, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_status_missed(self):
        with allure.step("Проверка параметра (Пропущенные (были на повторе)) в Статус ДЗ"):
            url = FilterStatusDz.status_missed
            r1 = requests.get(staging + url + token + year, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_status_new_missed(self):
        with allure.step("Проверка параметра (Пропущенные (не были на повторе)) в Статус ДЗ"):
            url = FilterStatusDz.status_new_missed
            r1 = requests.get(staging + url + token + year, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array


@allure.feature("Админка Домашние задания вкладка Домашняя школа Фильтр Тип ДЗ:")
@allure.story(
    "Проверяю ответ статус кода во всех Типах ДЗ. Во всех остальных фильтрах выбран параметр (Все)")
class TestFilterTypeDz:
    def test_type_dz_monthly(self):
        with allure.step("Проверка параметра (Месячное ДЗ) в Тип ДЗ"):
            url = FilterTypeDz.type_dz_monthly
            r1 = requests.get(staging + url + token + year, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_type_dz_weekly(self):
        with allure.step("Проверка параметра (Недельное ДЗ) в Тип ДЗ"):
            url = FilterTypeDz.type_dz_weekly
            r1 = requests.get(staging + url + token + year, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array


@allure.feature("Админка Домашние задания вкладка Домашняя школа Фильтр Формат доступа:")
@allure.story(
    "Проверяю ответ статус кода во всех Форматах ДЗ. Во всех остальных фильтрах выбран параметр (Все)")
class TestFilterFormatAccess:
    def test_format_trial_access(self):
        with allure.step("Проверка параметра (Пробный доступ) в Формат доступа"):
            url = FilterFormatAccess.trial_access
            r1 = requests.get(staging + url + token + year, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_format_full_access(self):
        with allure.step("Проверка параметра (Полный доступ) в Формат доступа"):
            url = FilterFormatAccess.full_access
            r1 = requests.get(staging + url + token + year, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array
