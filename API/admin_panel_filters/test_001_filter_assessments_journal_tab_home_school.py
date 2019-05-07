import requests
import allure
from API.admin_panel_filters.request_list.url_filter_assessments_journal import *
from ApiToken import Gettoken
token = Gettoken.token
staging = "https://api-test-ege.interneturok.ru"
parameter_array = ['per_page', 'page', 'total', 'users']


@allure.feature("Админка Журнал оценок вкладка Домашняя школа Фильтр Выбор четверти/год")
@allure.story("Проверяю ответ статус кода с 2 по 4 четверть и Год")
class TestFilterQuarter:
    def test_two_quarter(self):
        with allure.step("2 четверть"):
            url = FilterQuarter.quarter_two
            r1 = requests.get(staging + url + token, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_three_quarter(self):
        with allure.step("3 четверть"):
            url = FilterQuarter.quarter_three
            r1 = requests.get(staging + url + token, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_four_quarter(self):
        with allure.step("4 четверть"):
            url = FilterQuarter.quarter_four
            r1 = requests.get(staging + url + token, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_year_quarter(self):
        with allure.step("Год"):
            url = FilterQuarter.year
            r1 = requests.get(staging + url + token, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array


@allure.feature("Админка Журнал оценок вкладка Домашняя школа Фильтр Год обучения")
@allure.story("Проверяю ответ статус кода в 2018-2019 и 2017-2018 УГ")
class TestFilterYears:
    def test_2018_2019_years(self):
        with allure.step("Фильтр 2018-2019 учебный год"):
            url = FilterYears.year_2018_2019
            r1 = requests.get(staging + url + token, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_2017_2018_years(self):
        with allure.step("Фильтр 2017-2018 учебный год"):
            url = FilterYears.year_2017_2018
            r1 = requests.get(staging + url + token, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array


@allure.feature("Админка Журнал оценок вкладка Домашняя школа Фильтр Формат обучения")
@allure.story("Проверка ответ статус кода во всех форматах обучения")
class TestTrainingFormat:
    def test_format_all(self):
        with allure.step("Фильтр Все"):
            url = FilterTrainingFormat.format_all
            r1 = requests.get(staging + url + token, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_format_basic_education(self):
        with allure.step("Фильтр Основное образование"):
            url = FilterTrainingFormat.format_basic_education
            r1 = requests.get(staging + url + token, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_format_additional_education(self):
        with allure.step("Фильтр Дополнительное образование"):
            url = FilterTrainingFormat.format_additional_education
            r1 = requests.get(staging + url + token, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array


@allure.feature("Админка Журнал оценок вкладка Домашняя школа Фильтр Школы")
@allure.story("Проверка ответ статус кода во всех Школах")
class TestFilterSchool:
    def test_school_all(self):
        with allure.step("Фильтр Все"):
            url = FilterSchool.school_all
            r1 = requests.get(staging + url + token, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_school_no_listed(self):
        with allure.step("Фильтр Школа не укзана"):
            url = FilterSchool.school_no_listed
            r1 = requests.get(staging + url + token, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_school_danko(self):
        with allure.step("Фильтр Данко"):
            url = FilterSchool.school_danko
            r1 = requests.get(staging + url + token, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_school_logos(self):
        with allure.step("Фильтр Логос М"):
            url = FilterSchool.school_logos
            r1 = requests.get(staging + url + token, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_school_alyma_mater(self):
        with allure.step("Фильтр Альм Матер"):
            url = FilterSchool.school_alyma_mater
            r1 = requests.get(staging + url + token, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_school_ypigrof(self):
        with allure.step("Фильтр Эпигров"):
            url = FilterSchool.school_ypigrof
            r1 = requests.get(staging + url + token, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_school_lobachevskogo(self):
        with allure.step("Фильтр Лобачевского"):
            url = FilterSchool.school_lobachevskogo
            r1 = requests.get(staging + url + token, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_school_48(self):
        with allure.step("Фильтр Школа № 48"):
            url = FilterSchool.school_48
            r1 = requests.get(staging + url + token, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_school_vidergeburt(self):
        with allure.step("Фильтр Видергебург"):
            url = FilterSchool.school_vidergeburt
            r1 = requests.get(staging + url + token, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_school_pervay_school(self):
        with allure.step("Фильтр Первая школа"):
            url = FilterSchool.school_pervay_school
            r1 = requests.get(staging + url + token, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_school_nashi_penaty(self):
        with allure.step("Фильтр Наши Пенаты"):
            url = FilterSchool.school_nashi_penaty
            r1 = requests.get(staging + url + token, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_school_stolishnya_kit(self):
        with allure.step("Фильтр Стольчный-КИТ"):
            url = FilterSchool.school_stolishnya_kit
            r1 = requests.get(staging + url + token, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_school_rosinka(self):
        with allure.step("Фильтр Росинка"):
            url = FilterSchool.school_rosinka
            r1 = requests.get(staging + url + token, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array


@allure.feature("Админка Журнал оценок вкладка Домашняя школа Фильтр Классы")
@allure.story("Проверка ответ статус кода во всех Классах")
class TestFilterGradesInAssessmentsJournal:
    def test_all_subjects(self):
        with allure.step("Фильтр Все"):
            url = FilterGrades.klass_all
            r1 = requests.get(staging + url + token, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_one_subjects(self):
        with allure.step("Фильтр 1"):
            url = FilterGrades.klass_one
            r1 = requests.get(staging + url + token, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_two_subjects(self):
        with allure.step("Фильтр 2"):
            url = FilterGrades.klass_two
            r1 = requests.get(staging + url + token, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_three_subjects(self):
        with allure.step("Фильтр 3"):
            url = FilterGrades.klass_three
            r1 = requests.get(staging + url + token, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_four_subjects(self):
        with allure.step("Фильтр 4"):
            url = FilterGrades.klass_four
            r1 = requests.get(staging + url + token, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_five_subjects(self):
        with allure.step("Фильтр 5"):
            url = FilterGrades.klass_five
            r1 = requests.get(staging + url + token, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_six_subjects(self):
        with allure.step("Фильтр 6"):
            url = FilterGrades.klass_six
            r1 = requests.get(staging + url + token, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_seven_subjects(self):
        with allure.step("Фильтр 7"):
            url = FilterGrades.klass_seven
            r1 = requests.get(staging + url + token, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_eight_subjects(self):
        with allure.step("Фильтр 8"):
            url = FilterGrades.klass_eight
            r1 = requests.get(staging + url + token, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_nine_subjects(self):
        with allure.step("Фильтр 9"):
            url = FilterGrades.klass_nine
            r1 = requests.get(staging + url + token, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_ten_subjects(self):
        with allure.step("Фильтр 10"):
            url = FilterGrades.klass_ten
            r1 = requests.get(staging + url + token, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_eleven_subjects(self):
        with allure.step("Фильтр 11"):
            url = FilterGrades.klass_eleven
            r1 = requests.get(staging + url + token, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array


@allure.feature("Админка Журнал оценок вкладка Домашняя школа Фильтр Предметы")
@allure.story("Проверка ответ статус кода во всех Предметах")
class TestFilterSubjectsInAssessmentsJournal:
    def test_subjects_all(self):
        with allure.step("Фильтр Все"):
            url = FilterSubjects.subject_all
            r1 = requests.get(staging + url + token, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_subjects_russian_language(self):
        with allure.step("Фильтр Русский язык"):
            url = FilterSubjects.subject_russian_language
            r1 = requests.get(staging + url + token, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_subjects_literatura(self):
        with allure.step("Фильтр Литература"):
            url = FilterSubjects.subject_literatura
            r1 = requests.get(staging + url + token, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_subjects_english_language(self):
        with allure.step("Фильтр Английский язык"):
            url = FilterSubjects.subject_english_language
            r1 = requests.get(staging + url + token, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_subjects_matematika(self):
        with allure.step("Фильтр Математика"):
            url = FilterSubjects.subject_matematika
            r1 = requests.get(staging + url + token, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_subjects_history(self):
        with allure.step("Фильтр История"):
            url = FilterSubjects.subject_history
            r1 = requests.get(staging + url + token, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_subject_prirodavedenie(self):
        with allure.step("Фильтр Природоведние"):
            url = FilterSubjects.subject_prirodavedenie
            r1 = requests.get(staging + url + token, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_subject_objestvoznanie(self):
        with allure.step("Фильтр Обществознание"):
            url = FilterSubjects.subject_objestvoznanie
            r1 = requests.get(staging + url + token, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_subject_geografia(self):
        with allure.step("Фильтр География"):
            url = FilterSubjects.subject_geografia
            r1 = requests.get(staging + url + token, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_subject_biologia(self):
        with allure.step("Фильтр Биология"):
            url = FilterSubjects.subject_biologia
            r1 = requests.get(staging + url + token, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_subject_algebra_standart(self):
        with allure.step("Фильтр Алгебра.Стандартный курс"):
            url = FilterSubjects.subject_algebra_standart
            r1 = requests.get(staging + url + token, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_subject_geometria_standart(self):
        with allure.step("Фильтр Геометрия.Стандартный курс"):
            url = FilterSubjects.subject_geometria_standart
            r1 = requests.get(staging + url + token, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_subject_fizika_standart(self):
        with allure.step("Фильтр Физика.Стандартный курс"):
            url = FilterSubjects.subject_fizika_standart
            r1 = requests.get(staging + url + token, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_subject_informatika(self):
        with allure.step("Фильтр Информатика"):
            url = FilterSubjects.subject_informatika
            r1 = requests.get(staging + url + token, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_subject_himiya(self):
        with allure.step("Фильтр Химия"):
            url = FilterSubjects.subject_himiya
            r1 = requests.get(staging + url + token, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_subject_algebra(self):
        with allure.step("Фильтр Алгебра"):
            url = FilterSubjects.subject_algebra
            r1 = requests.get(staging + url + token, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_subject_geometria(self):
        with allure.step("Фильтр Геометрия"):
            url = FilterSubjects.subject_geometria
            r1 = requests.get(staging + url + token, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_subject_fizika(self):
        with allure.step("Фильтр Физика"):
            url = FilterSubjects.subject_fizika
            r1 = requests.get(staging + url + token, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_subject_literaturnoe_chtenie(self):
        with allure.step("Фильтр Литературное чтение"):
            url = FilterSubjects.subject_literaturnoe_chtenie
            r1 = requests.get(staging + url + token, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_subject_okruzauchi_mir(self):
        with allure.step("Фильтр Окружающий мир"):
            url = FilterSubjects.subject_okruzauchi_mir
            r1 = requests.get(staging + url + token, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_subject_vvodni_yrok(self):
        with allure.step("Фильтр Вводный урок"):
            url = FilterSubjects.subject_vvodni_yrok
            r1 = requests.get(staging + url + token, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_subject_podgotovka_k_OGE_matematika(self):
        with allure.step("Фильтр Подготовка к ОГЭ по математике"):
            url = FilterSubjects.subject_podgotovka_k_OGE_matematika
            r1 = requests.get(staging + url + token, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_subject_podgotovka_k_OGE_russian_language(self):
        with allure.step("Фильтр Подготовка к ОГЭ по русскому языку"):
            url = FilterSubjects.subject_podgotovka_k_OGE_russian_language
            r1 = requests.get(staging + url + token, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_subject_algebra_effective(self):
        with allure.step("Фильтр Алгебра эффективный курс"):
            url = FilterSubjects.subject_algebra_effective
            r1 = requests.get(staging + url + token, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_subject_fizika_effective(self):
        with allure.step("Фильтр Физика эффективный курс"):
            url = FilterSubjects.subject_fizika_effective
            r1 = requests.get(staging + url + token, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_subject_fizra(self):
        with allure.step("Фильтр Физра"):
            url = FilterSubjects.subject_fizra
            r1 = requests.get(staging + url + token, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_subject_tehnologiya(self):
        with allure.step("Фильтр Технология"):
            url = FilterSubjects.subject_tehnologiya
            r1 = requests.get(staging + url + token, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_subject_izo(self):
        with allure.step("Фильтр ИЗО"):
            url = FilterSubjects.subject_izo
            r1 = requests.get(staging + url + token, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_subject_music(self):
        with allure.step("Фильтр Музыка"):
            url = FilterSubjects.subject_music
            r1 = requests.get(staging + url + token, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_subject_osnovi_sovetskoi_itiki(self):
        with allure.step("Фильтр Основы советской этики"):
            url = FilterSubjects.subject_osnovi_sovetskoi_itiki
            r1 = requests.get(staging + url + token, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_subject_obz(self):
        with allure.step("Фильтр ОБЖ"):
            url = FilterSubjects.subject_obz
            r1 = requests.get(staging + url + token, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_subject_astronomia(self):
        with allure.step("Фильтр Астрономия"):
            url = FilterSubjects.subject_astronomia
            r1 = requests.get(staging + url + token, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_subject_geometria_effective(self):
        with allure.step("Фильтр Геометрия эффективный курс"):
            url = FilterSubjects.subject_geometria_effective
            r1 = requests.get(staging + url + token, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array

    def test_subject_superjob(self):
        with allure.step("Фильтр Профореинтация от SuperJob"):
            url = FilterSubjects.subject_superJob
            r1 = requests.get(staging + url + token, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array


@allure.feature("Админка Журнал оценок вкладка Домашняя школа Фильтр Ученик")
@allure.story("Проверка ответ статус кода при поиске без E-mail все остальные фильтры Все")
class TestFilterUser:
    def test_search_all_users(self):
        with allure.step("В поле ученик пусто (нет e-mail) во всех остальных фильтра Все"):
            url = FilterUser.search_all_users
            r1 = requests.get(staging + url + token, allow_redirects=False)
            try:
                r1.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
        with allure.step("Проверяю статус код == 200"):
            assert r1.status_code == 200
        with allure.step("В ответе запроса проверяю наличие параметров в массиве из переменной (parameter_array"):
            assert list(r1.json().keys()) == parameter_array
