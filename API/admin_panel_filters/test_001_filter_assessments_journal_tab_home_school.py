import requests
import allure
from API.admin_panel_filters.request_list.url_filter_assessments_journal import *
from API.setting_tests import LogInfoApi

parameter_array = ['per_page', 'page', 'total', 'users']


@allure.feature("Админка Журнал оценок вкладка Домашняя школа Фильтр Выбор четверти/год")
@allure.story("Проверяю ответ статус кода с 2 по 4 четверть и Год")
class TestFilterQuarter:
    def test_two_quarter(self):
        with allure.step("2 четверть"):
            url = FilterQuarter.quarter_two
            two_quarter = requests.get(url, allow_redirects=False)
            try:
                two_quarter.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=two_quarter)
            assert two_quarter.status_code == 200
            assert list(two_quarter.json().keys()) == parameter_array

    def test_three_quarter(self):
        with allure.step("3 четверть"):
            url = FilterQuarter.quarter_three
            three_quarter = requests.get(url, allow_redirects=False)
            try:
                three_quarter.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=three_quarter)
            assert three_quarter.status_code == 200
            assert list(three_quarter.json().keys()) == parameter_array

    def test_four_quarter(self):
        with allure.step("4 четверть"):
            url = FilterQuarter.quarter_four
            four_quarter = requests.get(url, allow_redirects=False)
            try:
                four_quarter.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=four_quarter)
            assert four_quarter.status_code == 200
            assert list(four_quarter.json().keys()) == parameter_array

    def test_year_quarter(self):
        with allure.step("Год"):
            url = FilterQuarter.year
            year_quarter = requests.get(url, allow_redirects=False)
            try:
                year_quarter.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=year_quarter)
            assert year_quarter.status_code == 200
            assert list(year_quarter.json().keys()) == parameter_array


@allure.feature("Админка Журнал оценок вкладка Домашняя школа Фильтр Год обучения")
@allure.story("Проверяю ответ статус кода в 2018-2019 и 2017-2018 УГ")
class TestFilterYears:
    def test_2018_2019_years(self):
        with allure.step("Фильтр 2018-2019 учебный год"):
            url = FilterYears.year_2018_2019
            years_2019 = requests.get(url, allow_redirects=False)
            try:
                years_2019.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=years_2019)
            assert years_2019.status_code == 200
            assert list(years_2019.json().keys()) == parameter_array

    def test_2017_2018_years(self):
        with allure.step("Фильтр 2017-2018 учебный год"):
            url = FilterYears.year_2017_2018
            years_2018 = requests.get(url, allow_redirects=False)
            try:
                years_2018.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=years_2018)
            assert years_2018.status_code == 200
            assert list(years_2018.json().keys()) == parameter_array


@allure.feature("Админка Журнал оценок вкладка Домашняя школа Фильтр Формат обучения")
@allure.story("Проверка ответ статус кода во всех форматах обучения")
class TestTrainingFormat:
    def test_format_all(self):
        with allure.step("Фильтр Все"):
            url = FilterTrainingFormat.format_all
            format_all = requests.get(url, allow_redirects=False)
            try:
                format_all.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=format_all)
            assert format_all.status_code == 200
            assert list(format_all.json().keys()) == parameter_array

    def test_format_basic_education(self):
        with allure.step("Фильтр Основное образование"):
            url = FilterTrainingFormat.format_basic_education
            format_basic_education = requests.get(url, allow_redirects=False)
            try:
                format_basic_education.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=format_basic_education)
            assert format_basic_education.status_code == 200
            assert list(format_basic_education.json().keys()) == parameter_array

    def test_format_additional_education(self):
        with allure.step("Фильтр Дополнительное образование"):
            url = FilterTrainingFormat.format_additional_education
            format_additional_education = requests.get(url, allow_redirects=False)
            try:
                format_additional_education.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=format_additional_education)
            assert format_additional_education.status_code == 200
            assert list(format_additional_education.json().keys()) == parameter_array


@allure.feature("Админка Журнал оценок вкладка Домашняя школа Фильтр Школы")
@allure.story("Проверка ответ статус кода во всех Школах")
class TestFilterSchool:
    def test_school_all(self):
        with allure.step("Фильтр Все"):
            url = FilterSchool.school_all
            school_all = requests.get(url, allow_redirects=False)
            try:
                school_all.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=school_all)
            assert school_all.status_code == 200
            assert list(school_all.json().keys()) == parameter_array

    def test_school_no_listed(self):
        with allure.step("Фильтр Школа не укзана"):
            url = FilterSchool.school_no_listed
            school_no_listed = requests.get(url, allow_redirects=False)
            try:
                school_no_listed.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=school_no_listed)
            assert school_no_listed.status_code == 200
            assert list(school_no_listed.json().keys()) == parameter_array

    def test_school_stolishnya_kit(self):
        with allure.step("Фильтр Стольчный-КИТ"):
            url = FilterSchool.school_stolishnya_kit
            school_stolishnya_kit = requests.get(url, allow_redirects=False)
            try:
                school_stolishnya_kit.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=school_stolishnya_kit)
            assert school_stolishnya_kit.status_code == 200
            assert list(school_stolishnya_kit.json().keys()) == parameter_array


@allure.feature("Админка Журнал оценок вкладка Домашняя школа Фильтр Классы")
@allure.story("Проверка ответ статус кода во всех Классах")
class TestFilterGradesInAssessmentsJournal:
    def test_all_subjects(self):
        with allure.step("Фильтр Все"):
            url = FilterGrades.klass_all
            all_subjects = requests.get(url, allow_redirects=False)
            try:
                all_subjects.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=all_subjects)
            assert all_subjects.status_code == 200
            assert list(all_subjects.json().keys()) == parameter_array

    def test_one_subjects(self):
        with allure.step("Фильтр 1"):
            url = FilterGrades.klass_one
            one_subjects = requests.get(url, allow_redirects=False)
            try:
                one_subjects.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=one_subjects)
            assert one_subjects.status_code == 200
            assert list(one_subjects.json().keys()) == parameter_array

    def test_two_subjects(self):
        with allure.step("Фильтр 2"):
            url = FilterGrades.klass_two
            two_subjects = requests.get(url, allow_redirects=False)
            try:
                two_subjects.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=two_subjects)
            assert two_subjects.status_code == 200
            assert list(two_subjects.json().keys()) == parameter_array

    def test_three_subjects(self):
        with allure.step("Фильтр 3"):
            url = FilterGrades.klass_three
            three_subjects = requests.get(url, allow_redirects=False)
            try:
                three_subjects.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=three_subjects)
            assert three_subjects.status_code == 200
            assert list(three_subjects.json().keys()) == parameter_array

    def test_four_subjects(self):
        with allure.step("Фильтр 4"):
            url = FilterGrades.klass_four
            four_subjects = requests.get(url, allow_redirects=False)
            try:
                four_subjects.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=four_subjects)
            assert four_subjects.status_code == 200
            assert list(four_subjects.json().keys()) == parameter_array

    def test_five_subjects(self):
        with allure.step("Фильтр 5"):
            url = FilterGrades.klass_five
            five_subjects = requests.get(url, allow_redirects=False)
            try:
                five_subjects.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=five_subjects)
            assert five_subjects.status_code == 200
            assert list(five_subjects.json().keys()) == parameter_array

    def test_six_subjects(self):
        with allure.step("Фильтр 6"):
            url = FilterGrades.klass_six
            six_subjects = requests.get(url, allow_redirects=False)
            try:
                six_subjects.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=six_subjects)
            assert six_subjects.status_code == 200
            assert list(six_subjects.json().keys()) == parameter_array

    def test_seven_subjects(self):
        with allure.step("Фильтр 7"):
            url = FilterGrades.klass_seven
            seven_subjects = requests.get(url, allow_redirects=False)
            try:
                seven_subjects.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=seven_subjects)
            assert seven_subjects.status_code == 200
            assert list(seven_subjects.json().keys()) == parameter_array

    def test_eight_subjects(self):
        with allure.step("Фильтр 8"):
            url = FilterGrades.klass_eight
            eight_subjects = requests.get(url, allow_redirects=False)
            try:
                eight_subjects.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=eight_subjects)
            assert eight_subjects.status_code == 200
            assert list(eight_subjects.json().keys()) == parameter_array

    def test_nine_subjects(self):
        with allure.step("Фильтр 9"):
            url = FilterGrades.klass_nine
            nine_subjects = requests.get(url, allow_redirects=False)
            try:
                nine_subjects.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=nine_subjects)
            assert nine_subjects.status_code == 200
            assert list(nine_subjects.json().keys()) == parameter_array

    def test_ten_subjects(self):
        with allure.step("Фильтр 10"):
            url = FilterGrades.klass_ten
            ten_subjects = requests.get(url, allow_redirects=False)
            try:
                ten_subjects.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=ten_subjects)
            assert ten_subjects.status_code == 200
            assert list(ten_subjects.json().keys()) == parameter_array

    def test_eleven_subjects(self):
        with allure.step("Фильтр 11"):
            url = FilterGrades.klass_eleven
            eleven_subjects = requests.get(url, allow_redirects=False)
            try:
                eleven_subjects.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=eleven_subjects)
            assert eleven_subjects.status_code == 200
            assert list(eleven_subjects.json().keys()) == parameter_array


@allure.feature("Админка Журнал оценок вкладка Домашняя школа Фильтр Предметы")
@allure.story("Проверка ответ статус кода во всех Предметах")
class TestFilterSubjectsInAssessmentsJournal:
    def test_subjects_all(self):
        with allure.step("Фильтр Все"):
            url = FilterSubjects.subject_all
            subjects_all = requests.get(url, allow_redirects=False)
            try:
                subjects_all.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=subjects_all)
            assert subjects_all.status_code == 200
            assert list(subjects_all.json().keys()) == parameter_array

    def test_subjects_russian_language(self):
        with allure.step("Фильтр Русский язык"):
            url = FilterSubjects.subject_russian_language
            subjects_russian_language = requests.get(url, allow_redirects=False)
            try:
                subjects_russian_language.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=subjects_russian_language)
            assert subjects_russian_language.status_code == 200
            assert list(subjects_russian_language.json().keys()) == parameter_array

    def test_subjects_literatura(self):
        with allure.step("Фильтр Литература"):
            url = FilterSubjects.subject_literatura
            subjects_literatura = requests.get(url, allow_redirects=False)
            try:
                subjects_literatura.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=subjects_literatura)
            assert subjects_literatura.status_code == 200
            assert list(subjects_literatura.json().keys()) == parameter_array

    def test_subjects_english_language(self):
        with allure.step("Фильтр Английский язык"):
            url = FilterSubjects.subject_english_language
            english_language = requests.get(url, allow_redirects=False)
            try:
                english_language.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=english_language)
            assert english_language.status_code == 200
            assert list(english_language.json().keys()) == parameter_array

    def test_subjects_matematika(self):
        with allure.step("Фильтр Математика"):
            url = FilterSubjects.subject_matematika
            subjects_matematika = requests.get(url, allow_redirects=False)
            try:
                subjects_matematika.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=subjects_matematika)
            assert subjects_matematika.status_code == 200
            assert list(subjects_matematika.json().keys()) == parameter_array

    def test_subjects_history(self):
        with allure.step("Фильтр История"):
            url = FilterSubjects.subject_history
            subjects_history = requests.get(url, allow_redirects=False)
            try:
                subjects_history.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=subjects_history)
            assert subjects_history.status_code == 200
            assert list(subjects_history.json().keys()) == parameter_array

    def test_subject_prirodavedenie(self):
        with allure.step("Фильтр Природоведние"):
            url = FilterSubjects.subject_prirodavedenie
            subject_prirodavedenie = requests.get(url, allow_redirects=False)
            try:
                subject_prirodavedenie.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=subject_prirodavedenie)
            assert subject_prirodavedenie.status_code == 200
            assert list(subject_prirodavedenie.json().keys()) == parameter_array

    def test_subject_objestvoznanie(self):
        with allure.step("Фильтр Обществознание"):
            url = FilterSubjects.subject_objestvoznanie
            subject_objestvoznanie = requests.get(url, allow_redirects=False)
            try:
                subject_objestvoznanie.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=subject_objestvoznanie)
            assert subject_objestvoznanie.status_code == 200
            assert list(subject_objestvoznanie.json().keys()) == parameter_array

    def test_subject_geografia(self):
        with allure.step("Фильтр География"):
            url = FilterSubjects.subject_geografia
            subject_geografia = requests.get(url, allow_redirects=False)
            try:
                subject_geografia.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=subject_geografia)
            assert subject_geografia.status_code == 200
            assert list(subject_geografia.json().keys()) == parameter_array

    def test_subject_biologia(self):
        with allure.step("Фильтр Биология"):
            url = FilterSubjects.subject_biologia
            subject_biologia = requests.get(url, allow_redirects=False)
            try:
                subject_biologia.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=subject_biologia)
            assert subject_biologia.status_code == 200
            assert list(subject_biologia.json().keys()) == parameter_array

    def test_subject_algebra_standart(self):
        with allure.step("Фильтр Алгебра.Стандартный курс"):
            url = FilterSubjects.subject_algebra_standart
            subject_algebra_standart = requests.get(url, allow_redirects=False)
            try:
                subject_algebra_standart.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=subject_algebra_standart)
            assert subject_algebra_standart.status_code == 200
            assert list(subject_algebra_standart.json().keys()) == parameter_array

    def test_subject_geometria_standart(self):
        with allure.step("Фильтр Геометрия.Стандартный курс"):
            url = FilterSubjects.subject_geometria_standart
            subject_geometria_standart = requests.get(url, allow_redirects=False)
            try:
                subject_geometria_standart.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=subject_geometria_standart)
            assert subject_geometria_standart.status_code == 200
            assert list(subject_geometria_standart.json().keys()) == parameter_array

    def test_subject_fizika_standart(self):
        with allure.step("Фильтр Физика.Стандартный курс"):
            url = FilterSubjects.subject_fizika_standart
            subject_fizika_standart = requests.get(url, allow_redirects=False)
            try:
                subject_fizika_standart.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=subject_fizika_standart)
            assert subject_fizika_standart.status_code == 200
            assert list(subject_fizika_standart.json().keys()) == parameter_array

    def test_subject_informatika(self):
        with allure.step("Фильтр Информатика"):
            url = FilterSubjects.subject_informatika
            subject_informatika = requests.get(url, allow_redirects=False)
            try:
                subject_informatika.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=subject_informatika)
            assert subject_informatika.status_code == 200
            assert list(subject_informatika.json().keys()) == parameter_array

    def test_subject_himiya(self):
        with allure.step("Фильтр Химия"):
            url = FilterSubjects.subject_himiya
            subject_himiya = requests.get(url, allow_redirects=False)
            try:
                subject_himiya.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=subject_himiya)
            assert subject_himiya.status_code == 200
            assert list(subject_himiya.json().keys()) == parameter_array

    def test_subject_algebra(self):
        with allure.step("Фильтр Алгебра"):
            url = FilterSubjects.subject_algebra
            subject_algebra = requests.get(url, allow_redirects=False)
            try:
                subject_algebra.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=subject_algebra)
            assert subject_algebra.status_code == 200
            assert list(subject_algebra.json().keys()) == parameter_array

    def test_subject_geometria(self):
        with allure.step("Фильтр Геометрия"):
            url = FilterSubjects.subject_geometria
            subject_geometria = requests.get(url, allow_redirects=False)
            try:
                subject_geometria.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=subject_geometria)
            assert subject_geometria.status_code == 200
            assert list(subject_geometria.json().keys()) == parameter_array

    def test_subject_fizika(self):
        with allure.step("Фильтр Физика"):
            url = FilterSubjects.subject_fizika
            subject_fizika = requests.get(url, allow_redirects=False)
            try:
                subject_fizika.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=subject_fizika)
            assert subject_fizika.status_code == 200
            assert list(subject_fizika.json().keys()) == parameter_array

    def test_subject_literaturnoe_chtenie(self):
        with allure.step("Фильтр Литературное чтение"):
            url = FilterSubjects.subject_literaturnoe_chtenie
            subject_literaturnoe_chtenie = requests.get(url, allow_redirects=False)
            try:
                subject_literaturnoe_chtenie.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=subject_literaturnoe_chtenie)
            assert subject_literaturnoe_chtenie.status_code == 200
            assert list(subject_literaturnoe_chtenie.json().keys()) == parameter_array

    def test_subject_okruzauchi_mir(self):
        with allure.step("Фильтр Окружающий мир"):
            url = FilterSubjects.subject_okruzauchi_mir
            subject_okruzauchi_mir = requests.get(url, allow_redirects=False)
            try:
                subject_okruzauchi_mir.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=subject_okruzauchi_mir)
            assert subject_okruzauchi_mir.status_code == 200
            assert list(subject_okruzauchi_mir.json().keys()) == parameter_array

    def test_subject_vvodni_yrok(self):
        with allure.step("Фильтр Вводный урок"):
            url = FilterSubjects.subject_vvodni_yrok
            subject_vvodni_yrok = requests.get(url, allow_redirects=False)
            try:
                subject_vvodni_yrok.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=subject_vvodni_yrok)
            assert subject_vvodni_yrok.status_code == 200
            assert list(subject_vvodni_yrok.json().keys()) == parameter_array

    def test_subject_podgotovka_k_OGE_matematika(self):
        with allure.step("Фильтр Подготовка к ОГЭ по математике"):
            url = FilterSubjects.subject_podgotovka_k_OGE_matematika
            subject_podgotovka_k_OGE_matematika = requests.get(url, allow_redirects=False)
            try:
                subject_podgotovka_k_OGE_matematika.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=subject_podgotovka_k_OGE_matematika)
            assert subject_podgotovka_k_OGE_matematika.status_code == 200
            assert list(subject_podgotovka_k_OGE_matematika.json().keys()) == parameter_array

    def test_subject_podgotovka_k_OGE_russian_language(self):
        with allure.step("Фильтр Подготовка к ОГЭ по русскому языку"):
            url = FilterSubjects.subject_podgotovka_k_OGE_russian_language
            subject_podgotovka_k_OGE_russian_language = requests.get(url, allow_redirects=False)
            try:
                subject_podgotovka_k_OGE_russian_language.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=subject_podgotovka_k_OGE_russian_language)
            assert subject_podgotovka_k_OGE_russian_language.status_code == 200
            assert list(subject_podgotovka_k_OGE_russian_language.json().keys()) == parameter_array

    def test_subject_algebra_effective(self):
        with allure.step("Фильтр Алгебра эффективный курс"):
            url = FilterSubjects.subject_algebra_effective
            subject_algebra_effective = requests.get(url, allow_redirects=False)
            try:
                subject_algebra_effective.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=subject_algebra_effective)
            assert subject_algebra_effective.status_code == 200
            assert list(subject_algebra_effective.json().keys()) == parameter_array

    def test_subject_fizika_effective(self):
        with allure.step("Фильтр Физика эффективный курс"):
            url = FilterSubjects.subject_fizika_effective
            subject_fizika_effective = requests.get(url, allow_redirects=False)
            try:
                subject_fizika_effective.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=subject_fizika_effective)
            assert subject_fizika_effective.status_code == 200
            assert list(subject_fizika_effective.json().keys()) == parameter_array

    def test_subject_fizra(self):
        with allure.step("Фильтр Физра"):
            url = FilterSubjects.subject_fizra
            subject_fizra = requests.get(url, allow_redirects=False)
            try:
                subject_fizra.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=subject_fizra)
            assert subject_fizra.status_code == 200
            assert list(subject_fizra.json().keys()) == parameter_array

    def test_subject_tehnologiya(self):
        with allure.step("Фильтр Технология"):
            url = FilterSubjects.subject_tehnologiya
            subject_tehnologiya = requests.get(url, allow_redirects=False)
            try:
                subject_tehnologiya.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=subject_tehnologiya)
            assert subject_tehnologiya.status_code == 200
            assert list(subject_tehnologiya.json().keys()) == parameter_array

    def test_subject_izo(self):
        with allure.step("Фильтр ИЗО"):
            url = FilterSubjects.subject_izo
            subject_izo = requests.get(url, allow_redirects=False)
            try:
                subject_izo.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=subject_izo)
            assert subject_izo.status_code == 200
            assert list(subject_izo.json().keys()) == parameter_array

    def test_subject_music(self):
        with allure.step("Фильтр Музыка"):
            url = FilterSubjects.subject_music
            subject_music = requests.get(url, allow_redirects=False)
            try:
                subject_music.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=subject_music)
            assert subject_music.status_code == 200
            assert list(subject_music.json().keys()) == parameter_array

    def test_subject_osnovi_sovetskoi_itiki(self):
        with allure.step("Фильтр Основы советской этики"):
            url = FilterSubjects.subject_osnovi_sovetskoi_itiki
            subject_osnovi_sovetskoi_itiki = requests.get(url, allow_redirects=False)
            try:
                subject_osnovi_sovetskoi_itiki.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=subject_osnovi_sovetskoi_itiki)
            assert subject_osnovi_sovetskoi_itiki.status_code == 200
            assert list(subject_osnovi_sovetskoi_itiki.json().keys()) == parameter_array

    def test_subject_obz(self):
        with allure.step("Фильтр ОБЖ"):
            url = FilterSubjects.subject_obz
            subject_obz = requests.get(url, allow_redirects=False)
            try:
                subject_obz.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=subject_obz)
            assert subject_obz.status_code == 200
            assert list(subject_obz.json().keys()) == parameter_array

    def test_subject_astronomia(self):
        with allure.step("Фильтр Астрономия"):
            url = FilterSubjects.subject_astronomia
            subject_astronomia = requests.get(url, allow_redirects=False)
            try:
                subject_astronomia.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=subject_astronomia)
            assert subject_astronomia.status_code == 200
            assert list(subject_astronomia.json().keys()) == parameter_array

    def test_subject_geometria_effective(self):
        with allure.step("Фильтр Геометрия эффективный курс"):
            url = FilterSubjects.subject_geometria_effective
            subject_geometria_effective = requests.get(url, allow_redirects=False)
            try:
                subject_geometria_effective.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=subject_geometria_effective)
            assert subject_geometria_effective.status_code == 200
            assert list(subject_geometria_effective.json().keys()) == parameter_array

    def test_subject_superjob(self):
        with allure.step("Фильтр Профореинтация от SuperJob"):
            url = FilterSubjects.subject_superJob
            subject_superjob = requests.get(url, allow_redirects=False)
            try:
                subject_superjob.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=subject_superjob)
            assert subject_superjob.status_code == 200
            assert list(subject_superjob.json().keys()) == parameter_array

    def test_subject_german_language(self):
        with allure.step("Проверка параметра (Немецкий язык) в предметах"):
            url = FilterSubjects.subject_german_language
            german_language = requests.get(url, allow_redirects=False)
            try:
                german_language.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=german_language)
            assert german_language.status_code == 200
            assert list(german_language.json().keys()) == parameter_array

    def test_subject_osnovy_sovet_itiki(self):
        with allure.step("Проверка параметра (Основы светской этики) в предметах"):
            url = FilterSubjects.subject_osnovy_sovet_itiki
            osnovy_sovet_itiki = requests.get(url, allow_redirects=False)
            try:
                osnovy_sovet_itiki.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=osnovy_sovet_itiki)
            assert osnovy_sovet_itiki.status_code == 200
            assert list(osnovy_sovet_itiki.json().keys()) == parameter_array

    def test_subject_tendo_studio(self):
        with allure.step("Проверка параметра (Профориентация - игры от tendo.studio) в предметах"):
            url = FilterSubjects.subject_tendo_studio
            subject_tendo_studio = requests.get(url, allow_redirects=False)
            try:
                subject_tendo_studio.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=subject_tendo_studio)
            assert subject_tendo_studio.status_code == 200
            assert list(subject_tendo_studio.json().keys()) == parameter_array


@allure.feature("Админка Журнал оценок вкладка Домашняя школа Фильтр Ученик")
@allure.story("Проверка ответ статус кода при поиске без E-mail все остальные фильтры Все")
class TestFilterUser:
    def test_search_all_users(self):
        with allure.step("В поле ученик пусто (нет e-mail) во всех остальных фильтра Все"):
            url = FilterUser.search_all_users
            search_all_users = requests.get(url, allow_redirects=False)
            try:
                search_all_users.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=search_all_users)
            assert search_all_users.status_code == 200
            assert list(search_all_users.json().keys()) == parameter_array


@allure.feature("Админка Журнал оценок")
@allure.story("Выставление оценки за урок в журнале ученика")
class TestPutMarkUser:
    def test_put_mark_users(self):
        with allure.step("В журанле оценок выставить оценку 4"):
            url = PutMark.put_mark_4
            put_mark_users = requests.put(url, data=PutMark.data, allow_redirects=False)
            try:
                put_mark_users.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=put_mark_users)
            assert put_mark_users.status_code == 200
