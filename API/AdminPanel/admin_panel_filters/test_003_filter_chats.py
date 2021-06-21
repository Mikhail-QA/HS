import requests
import allure
from API.AdminPanel.admin_panel_filters.request_list.url_filter_chats import FilterGrades
from API.AdminPanel.admin_panel_filters.request_list.url_filter_chats import FilterSchools
from API.AdminPanel.admin_panel_filters.request_list.url_filter_chats import FilterSubjects
from API.AdminPanel.admin_panel_filters.request_list.url_filter_chats import FilterFormatAccess
from API.AdminPanel.admin_panel_filters.request_list.url_filter_chats import FilterMark
from API.AdminPanel.admin_panel_filters.request_list.url_filter_chats import FilterUser

from API.setting_tests import LogInfoApi

parameter_array = ['dialogs', 'total', 'page', 'per_page']
success_total = 25

total_standard = 21  # это стандартное значение кол-ва изначально отображающихся на странице ДЗ.


@allure.feature("Админка Чаты. Проверка фильтра Школы")
@allure.story("Проверяю ответ статус кода в Школах. Во всех остальных фильтрах выбран параметр (Все)")
class TestFilterSchoolsChats:
    def test_not_school(self):
        with allure.step("Проверка параметра (Школа не указан)"):
            url = FilterSchools.Not_school
            not_school = requests.get(url, allow_redirects=False)
            try:
                not_school.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=not_school)
            assert not_school.status_code == 200
            assert list(not_school.json().keys()) == parameter_array
            assert dict(not_school.json()).get('per_page') == success_total

    def test_school_stolichniy_kit(self):
        with allure.step("Проверка параметра (Школа Столичный-КИТ)"):
            url = FilterSchools.school_stolichniy_kit
            school_stolichniy_kit = requests.get(url, allow_redirects=False)
            try:
                school_stolichniy_kit.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=school_stolichniy_kit)
            assert school_stolichniy_kit.status_code == 200
            assert list(school_stolichniy_kit.json().keys()) == parameter_array
            assert dict(school_stolichniy_kit.json()).get('per_page') == success_total


@allure.feature("Админка Чаты. Фильтр Предметы")
@allure.story("Проверяю ответ статус кода с первого предмета по последний. Во всех остальных фильтрах (Все)")
class TestFilterSubjectsChats:
    def test_subjects_russian_language(self):
        with allure.step("Проверка параметра (Русский язык) в предметах"):
            url = FilterSubjects.subject_russian_language
            russian_language = requests.get(url, allow_redirects=False)
            try:
                russian_language.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=russian_language)
            assert russian_language.status_code == 200
            assert list(russian_language.json().keys()) == parameter_array
            assert dict(russian_language.json()).get('per_page') == success_total

    def test_subjects_literatura(self):
        with allure.step("Проверка параметра (Литература) в предметах"):
            url = FilterSubjects.subject_literatura
            literatura = requests.get(url, allow_redirects=False)
            try:
                literatura.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=literatura)
            assert literatura.status_code == 200
            assert list(literatura.json().keys()) == parameter_array
            assert dict(literatura.json()).get('per_page') == success_total

    def test_subjects_english_language(self):
        with allure.step("Проверка параметра (Английский язык) в предметах"):
            url = FilterSubjects.subject_english_language
            english_language = requests.get(url, allow_redirects=False)
            try:
                english_language.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=english_language)
            assert english_language.status_code == 200
            assert list(english_language.json().keys()) == parameter_array
            assert dict(english_language.json()).get('per_page') == success_total

    def test_subjects_matematika(self):
        with allure.step("Проверка параметра (Математика) в предметах"):
            url = FilterSubjects.subject_matematika
            matematika = requests.get(url, allow_redirects=False)
            try:
                matematika.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=matematika)
            assert matematika.status_code == 200
            assert list(matematika.json().keys()) == parameter_array
            assert dict(matematika.json()).get('per_page') == success_total

    def test_subjects_history(self):
        with allure.step("Проверка параметра (История) в предметах"):
            url = FilterSubjects.subject_history
            history = requests.get(url, allow_redirects=False)
            try:
                history.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=history)
            assert history.status_code == 200
            assert list(history.json().keys()) == parameter_array
            assert dict(history.json()).get('per_page') == success_total

    def test_subject_prirodavedenie(self):
        with allure.step("Проверка параметра (Природоведние) в предметах"):
            url = FilterSubjects.subject_prirodavedenie
            prirodavedenie = requests.get(url, allow_redirects=False)
            try:
                prirodavedenie.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=prirodavedenie)
            assert prirodavedenie.status_code == 200
            assert list(prirodavedenie.json().keys()) == parameter_array
            assert dict(prirodavedenie.json()).get('per_page') <= success_total

    def test_subject_objestvoznanie(self):
        with allure.step("Проверка параметра (Обществознание) в предметах"):
            url = FilterSubjects.subject_objestvoznanie
            objestvoznanie = requests.get(url, allow_redirects=False)
            try:
                objestvoznanie.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=objestvoznanie)
            assert objestvoznanie.status_code == 200
            assert list(objestvoznanie.json().keys()) == parameter_array
            assert dict(objestvoznanie.json()).get('per_page') == success_total

    def test_subject_geografia(self):
        with allure.step("Проверка параметра (География) в предметах"):
            url = FilterSubjects.subject_geografia
            geografia = requests.get(url, allow_redirects=False)
            try:
                geografia.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=geografia)
            assert geografia.status_code == 200
            assert list(geografia.json().keys()) == parameter_array
            assert dict(geografia.json()).get('per_page') == success_total

    def test_subject_biologia(self):
        with allure.step("Проверка параметра (Биология) в предметах"):
            url = FilterSubjects.subject_biologia
            biologia = requests.get(url, allow_redirects=False)
            try:
                biologia.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=biologia)
            assert biologia.status_code == 200
            assert list(biologia.json().keys()) == parameter_array
            assert dict(biologia.json()).get('per_page') == success_total

    def test_subject_algebra_standart(self):
        with allure.step("Проверка параметра (Алгебра.Стандартный курс) в предметах"):
            url = FilterSubjects.subject_algebra_standart
            algebra_standart = requests.get(url, allow_redirects=False)
            try:
                algebra_standart.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=algebra_standart)
            assert algebra_standart.status_code == 200
            assert list(algebra_standart.json().keys()) == parameter_array
            assert dict(algebra_standart.json()).get('per_page') == success_total

    def test_subject_geometria_standart(self):
        with allure.step("Проверка параметра (Геометрия.Стандартный курс) в предметах"):
            url = FilterSubjects.subject_geometria_standart
            geometria_standart = requests.get(url, allow_redirects=False)
            try:
                geometria_standart.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=geometria_standart)
            assert geometria_standart.status_code == 200
            assert list(geometria_standart.json().keys()) == parameter_array
            assert dict(geometria_standart.json()).get('per_page') == success_total

    def test_subject_fizika_standart(self):
        with allure.step("Проверка параметра (Физика.Стандартный курс) в предметах"):
            url = FilterSubjects.subject_fizika_standart
            fizika_standart = requests.get(url, allow_redirects=False)
            try:
                fizika_standart.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=fizika_standart)
            assert fizika_standart.status_code == 200
            assert list(fizika_standart.json().keys()) == parameter_array
            assert dict(fizika_standart.json()).get('per_page') == success_total

    def test_subject_informatika(self):
        with allure.step("Проверка параметра (Информатика) в предметах"):
            url = FilterSubjects.subject_informatika
            informatika = requests.get(url, allow_redirects=False)
            try:
                informatika.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=informatika)
            assert informatika.status_code == 200
            assert list(informatika.json().keys()) == parameter_array
            assert dict(informatika.json()).get('per_page') == success_total

    def test_subject_himiya(self):
        with allure.step("Проверка параметра (Химия) в предметах"):
            url = FilterSubjects.subject_himiya
            himiya = requests.get(url, allow_redirects=False)
            try:
                himiya.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=himiya)
            assert himiya.status_code == 200
            assert list(himiya.json().keys()) == parameter_array
            assert dict(himiya.json()).get('per_page') == success_total

    def test_subject_algebra(self):
        with allure.step("Проверка параметра (Алгебра) в предметах"):
            url = FilterSubjects.subject_algebra
            algebra = requests.get(url, allow_redirects=False)
            try:
                algebra.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=algebra)
            assert algebra.status_code == 200
            assert list(algebra.json().keys()) == parameter_array
            assert dict(algebra.json()).get('per_page') == success_total

    def test_subject_geometria(self):
        with allure.step("Проверка параметра (Геометрия) в предметах"):
            url = FilterSubjects.subject_geometria
            geometria = requests.get(url, allow_redirects=False)
            try:
                geometria.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=geometria)
            assert geometria.status_code == 200
            assert list(geometria.json().keys()) == parameter_array
            assert dict(geometria.json()).get('per_page') == success_total

    def test_subject_fizika(self):
        with allure.step("Проверка параметра (Физика) в предметах"):
            url = FilterSubjects.subject_fizika
            fizika = requests.get(url, allow_redirects=False)
            try:
                fizika.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=fizika)
            assert fizika.status_code == 200
            assert list(fizika.json().keys()) == parameter_array
            assert dict(fizika.json()).get('per_page') == success_total

    def test_subject_literaturnoe_chtenie(self):
        with allure.step("Проверка параметра (Литературное чтение) в предметах"):
            url = FilterSubjects.subject_literaturnoe_chtenie
            literaturnoe_chtenie = requests.get(url, allow_redirects=False)
            try:
                literaturnoe_chtenie.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=literaturnoe_chtenie)
            assert literaturnoe_chtenie.status_code == 200
            assert list(literaturnoe_chtenie.json().keys()) == parameter_array
            assert dict(literaturnoe_chtenie.json()).get('per_page') == success_total

    def test_subject_okruzauchi_mir(self):
        with allure.step("Проверка параметра (Окружающий мир) в предметах"):
            url = FilterSubjects.subject_okruzauchi_mir
            okruzauchi_mir = requests.get(url, allow_redirects=False)
            try:
                okruzauchi_mir.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=okruzauchi_mir)
            assert okruzauchi_mir.status_code == 200
            assert list(okruzauchi_mir.json().keys()) == parameter_array
            assert dict(okruzauchi_mir.json()).get('per_page') == success_total

    def test_subject_matematika_profi(self):
        with allure.step("Проверка параметра (Математика Профильный) в предметах"):
            url = FilterSubjects.subject_matematika_profi
            matematika_profi = requests.get(url, allow_redirects=False)
            try:
                matematika_profi.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=matematika_profi)
            assert matematika_profi.status_code == 200
            assert list(matematika_profi.json().keys()) == parameter_array
            assert dict(matematika_profi.json()).get('per_page') == success_total

    def test_subject_matematika_bazovyai(self):
        with allure.step("Проверка параметра (Математика Базовый) в предметах"):
            url = FilterSubjects.subject_matematika_bazovyai
            matematika_bazovyai = requests.get(url, allow_redirects=False)
            try:
                matematika_bazovyai.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=matematika_bazovyai)
            assert matematika_bazovyai.status_code == 200
            assert list(matematika_bazovyai.json().keys()) == parameter_array
            assert dict(matematika_bazovyai.json()).get('per_page') == success_total

    def test_subject_vvodni_yrok(self):
        with allure.step("Проверка параметра (Вводный урок) в предметах"):
            url = FilterSubjects.subject_vvodni_yrok
            vvodni_yrok = requests.get(url, allow_redirects=False)
            try:
                vvodni_yrok.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=vvodni_yrok)
            assert vvodni_yrok.status_code == 200
            assert list(vvodni_yrok.json().keys()) == parameter_array
            assert dict(vvodni_yrok.json()).get('per_page') <= success_total

    def test_subject_podgotovka_k_OGE_matematika(self):
        with allure.step("Проверка параметра (Подготовка к ОГЭ по математике) в предметах"):
            url = FilterSubjects.subject_podgotovka_k_OGE_matematika
            podgotovka_k_OGE_matematika = requests.get(url, allow_redirects=False)
            try:
                podgotovka_k_OGE_matematika.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=podgotovka_k_OGE_matematika)
            assert podgotovka_k_OGE_matematika.status_code == 200
            assert list(podgotovka_k_OGE_matematika.json().keys()) == parameter_array
            assert dict(podgotovka_k_OGE_matematika.json()).get('per_page') <= success_total

    def test_subject_podgotovka_k_OGE_russian_language(self):
        with allure.step("Проверка параметра (Подготовка к ОГЭ по русскому языку) в предметах"):
            url = FilterSubjects.subject_podgotovka_k_OGE_russian_language
            podgotovka_k_OGE_russian_language = requests.get(url, allow_redirects=False)
            try:
                podgotovka_k_OGE_russian_language.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=podgotovka_k_OGE_russian_language)
            assert podgotovka_k_OGE_russian_language.status_code == 200
            assert list(podgotovka_k_OGE_russian_language.json().keys()) == parameter_array
            assert dict(podgotovka_k_OGE_russian_language.json()).get('per_page') <= success_total

    def test_subject_algebra_effective(self):
        with allure.step("Проверка параметра (Алгебра эффективный курс) в предметах"):
            url = FilterSubjects.subject_algebra_effective
            algebra_effective = requests.get(url, allow_redirects=False)
            try:
                algebra_effective.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=algebra_effective)
            assert algebra_effective.status_code == 200
            assert list(algebra_effective.json().keys()) == parameter_array
            assert dict(algebra_effective.json()).get('per_page') == success_total

    def test_subject_fizika_effective(self):
        with allure.step("Проверка параметра (Физика эффективный курс) в предметах"):
            url = FilterSubjects.subject_fizika_effective
            fizika_effective = requests.get(url, allow_redirects=False)
            try:
                fizika_effective.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=fizika_effective)
            assert fizika_effective.status_code == 200
            assert list(fizika_effective.json().keys()) == parameter_array
            assert dict(fizika_effective.json()).get('per_page') == success_total

    def test_subject_fizra(self):
        with allure.step("Проверка параметра (Физра) в предметах"):
            url = FilterSubjects.subject_fizra
            fizra = requests.get(url, allow_redirects=False)
            try:
                fizra.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=fizra)
            assert fizra.status_code == 200
            assert list(fizra.json().keys()) == parameter_array
            assert dict(fizra.json()).get('per_page') == success_total

    def test_subject_tehnologiya(self):
        with allure.step("Проверка параметра (Технология) в предметах"):
            url = FilterSubjects.subject_tehnologiya
            tehnologiya = requests.get(url, allow_redirects=False)
            try:
                tehnologiya.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=tehnologiya)
            assert tehnologiya.status_code == 200
            assert list(tehnologiya.json().keys()) == parameter_array
            assert dict(tehnologiya.json()).get('per_page') == success_total

    def test_subject_izo(self):
        with allure.step("Проверка параметра (ИЗО) в предметах"):
            url = FilterSubjects.subject_izo
            izo = requests.get(url, allow_redirects=False)
            try:
                izo.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=izo)
            assert izo.status_code == 200
            assert list(izo.json().keys()) == parameter_array
            assert dict(izo.json()).get('per_page') == success_total

    def test_subject_music(self):
        with allure.step("Проверка параметра (Музыка) в предметах"):
            url = FilterSubjects.subject_music
            music = requests.get(url, allow_redirects=False)
            try:
                music.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=music)
            assert music.status_code == 200
            assert list(music.json().keys()) == parameter_array
            assert dict(music.json()).get('per_page') == success_total

    def test_subject_osnovi_sovetskoi_itiki(self):
        with allure.step("Проверка параметра (Основы советской этики) в предметах"):
            url = FilterSubjects.subject_osnovi_sovetskoi_itiki
            osnovi_sovetskoi_itiki = requests.get(url, allow_redirects=False)
            try:
                osnovi_sovetskoi_itiki.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=osnovi_sovetskoi_itiki)
            assert osnovi_sovetskoi_itiki.status_code == 200
            assert list(osnovi_sovetskoi_itiki.json().keys()) == parameter_array
            assert dict(osnovi_sovetskoi_itiki.json()).get('per_page') == success_total

    def test_subject_obz(self):
        with allure.step("Проверка параметра (ОБЖ) в предметах"):
            url = FilterSubjects.subject_obz
            obz = requests.get(url, allow_redirects=False)
            try:
                obz.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=obz)
            assert obz.status_code == 200
            assert list(obz.json().keys()) == parameter_array
            assert dict(obz.json()).get('per_page') == success_total

    def test_subject_astronomia(self):
        with allure.step("Проверка параметра (Астрономия) в предметах"):
            url = FilterSubjects.subject_astronomia
            astronomia = requests.get(url, allow_redirects=False)
            try:
                astronomia.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=astronomia)
            assert astronomia.status_code == 200
            assert list(astronomia.json().keys()) == parameter_array
            assert dict(astronomia.json()).get('per_page') == success_total

    def test_subject_geometria_effective(self):
        with allure.step("Проверка параметра (Геометрия эффективный курс) в предметах"):
            url = FilterSubjects.subject_geometria_effective
            geometria_effective = requests.get(url, allow_redirects=False)
            try:
                geometria_effective.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=geometria_effective)
            assert geometria_effective.status_code == 200
            assert list(geometria_effective.json().keys()) == parameter_array
            assert dict(geometria_effective.json()).get('per_page') == success_total

    def test_subject_superjob(self):
        with allure.step("Проверка параметра (Профореинтация от SuperJob) в предметах"):
            url = FilterSubjects.subject_superJob
            superjob = requests.get(url, allow_redirects=False)
            try:
                superjob.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=superjob)
            assert superjob.status_code == 200
            assert list(superjob.json().keys()) == parameter_array
            assert dict(superjob.json()).get('per_page') == success_total

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
            assert dict(german_language.json()).get('per_page') == success_total

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
            assert dict(osnovy_sovet_itiki.json()).get('per_page') == success_total

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
            assert dict(subject_tendo_studio.json()).get('per_page') == success_total


@allure.feature("Админка Чаты. Проверка фильтра Классы")
@allure.story("Проверяю ответ статус кода с 1 по 11 класс. Во всех остальных фильтрах (Все)")
class TestFilterGradesInChats:
    def test_all_subjects(self):
        url = FilterGrades.klass_all
        all_subjects = requests.get(url, allow_redirects=False)
        try:
            all_subjects.raise_for_status()
        except requests.exceptions.HTTPError as e:
            print('ERROR: %s' % e)
        LogInfoApi.log_info(log=all_subjects)
        assert all_subjects.status_code == 200
        assert list(all_subjects.json().keys()) == parameter_array
        assert dict(all_subjects.json()).get('per_page') == success_total

    def test_one_subjects(self):
        with allure.step("Проверка параметра (1) в классах"):
            url = FilterGrades.klass_one
            one_subjects = requests.get(url, allow_redirects=False)
            try:
                one_subjects.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=one_subjects)
            assert one_subjects.status_code == 200
            assert list(one_subjects.json().keys()) == parameter_array
            assert dict(one_subjects.json()).get('per_page') == success_total

    def test_two_subjects(self):
        with allure.step("Проверка параметра (2) в классах"):
            url = FilterGrades.klass_two
            two_subjects = requests.get(url, allow_redirects=False)
            try:
                two_subjects.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=two_subjects)
            assert two_subjects.status_code == 200
            assert list(two_subjects.json().keys()) == parameter_array
            assert dict(two_subjects.json()).get('per_page') == success_total

    def test_three_subjects(self):
        with allure.step("Проверка параметра (3) в классах"):
            url = FilterGrades.klass_three
            three_subjects = requests.get(url, allow_redirects=False)
            try:
                three_subjects.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=three_subjects)
            assert three_subjects.status_code == 200
            assert list(three_subjects.json().keys()) == parameter_array
            assert dict(three_subjects.json()).get('per_page') == success_total

    def test_four_subjects(self):
        with allure.step("Проверка параметра (4) в классах"):
            url = FilterGrades.klass_four
            four_subjects = requests.get(url, allow_redirects=False)
            try:
                four_subjects.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=four_subjects)
            assert four_subjects.status_code == 200
            assert list(four_subjects.json().keys()) == parameter_array
            assert dict(four_subjects.json()).get('per_page') == success_total

    def test_five_subjects(self):
        with allure.step("Проверка параметра (5) в классах"):
            url = FilterGrades.klass_five
            five_subjects = requests.get(url, allow_redirects=False)
            try:
                five_subjects.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=five_subjects)
            assert five_subjects.status_code == 200
            assert list(five_subjects.json().keys()) == parameter_array
            assert dict(five_subjects.json()).get('per_page') == success_total

    def test_six_subjects(self):
        with allure.step("Проверка параметра (6) в классах"):
            url = FilterGrades.klass_six
            six_subjects = requests.get(url, allow_redirects=False)
            try:
                six_subjects.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=six_subjects)
            assert six_subjects.status_code == 200
            assert list(six_subjects.json().keys()) == parameter_array
            assert dict(six_subjects.json()).get('per_page') == success_total

    def test_seven_subjects(self):
        with allure.step("Проверка параметра (7) в классах"):
            url = FilterGrades.klass_seven
            seven_subjects = requests.get(url, allow_redirects=False)
            try:
                seven_subjects.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=seven_subjects)
            assert seven_subjects.status_code == 200
            assert list(seven_subjects.json().keys()) == parameter_array
            assert dict(seven_subjects.json()).get('per_page') == success_total

    def test_eight_subjects(self):
        with allure.step("Проверка параметра (8) в классах"):
            url = FilterGrades.klass_eight
            eight_subjects = requests.get(url, allow_redirects=False)
            try:
                eight_subjects.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=eight_subjects)
            assert eight_subjects.status_code == 200
            assert list(eight_subjects.json().keys()) == parameter_array
            assert dict(eight_subjects.json()).get('per_page') == success_total

    def test_nine_subjects(self):
        with allure.step("Проверка параметра (9) в классах"):
            url = FilterGrades.klass_nine
            nine_subjects = requests.get(url, allow_redirects=False)
            try:
                nine_subjects.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=nine_subjects)
            assert nine_subjects.status_code == 200
            assert list(nine_subjects.json().keys()) == parameter_array
            assert dict(nine_subjects.json()).get('per_page') == success_total

    def test_ten_subjects(self):
        with allure.step("Проверка параметра (10) в классах"):
            url = FilterGrades.klass_ten
            ten_subjects = requests.get(url, allow_redirects=False)
            try:
                ten_subjects.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=ten_subjects)
            assert ten_subjects.status_code == 200
            assert list(ten_subjects.json().keys()) == parameter_array
            assert dict(ten_subjects.json()).get('per_page') == success_total

    def test_eleven_subjects(self):
        with allure.step("Проверка параметра (11) в классах"):
            url = FilterGrades.klass_eleven
            eleven_subjects = requests.get(url, allow_redirects=False)
            try:
                eleven_subjects.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=eleven_subjects)
            assert eleven_subjects.status_code == 200
            assert list(eleven_subjects.json().keys()) == parameter_array
            assert dict(eleven_subjects.json()).get('per_page') == success_total


@allure.feature("Админка Чаты. Проверка Тип доступа ученика:")
@allure.story("Проверяю ответ статус кода во всех доступа ученика. Во всех остальных фильтрах выбран параметр (Все)")
class TestFilterAccessChats:
    def test_access_trial(self):
        with allure.step("Проверка параметра (Пробный доступ) в Тип доступа ученика"):
            url = FilterFormatAccess.access_trial
            access_trial = requests.get(url, allow_redirects=False)
            try:
                access_trial.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=access_trial)
            assert access_trial.status_code == 200
            assert list(access_trial.json().keys()) == parameter_array
            assert dict(access_trial.json()).get('per_page') == success_total

    def test_access_full(self):
        with allure.step("Проверка параметра (Полный доступ) в Тип доступа ученика"):
            url = FilterFormatAccess.access_full
            access_full = requests.get(url, allow_redirects=False)
            try:
                access_full.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=access_full)
            assert access_full.status_code == 200
            assert list(access_full.json().keys()) == parameter_array
            assert dict(access_full.json()).get('per_page') == success_total


@allure.feature("Админка Чаты. Фильтр Метки:")
@allure.story("Проверяю ответ статус кода во всех Метках. Во всех остальных фильтрах выбран параметр (Все)")
class TestFilterLabelsChats:
    def test_only_with_labels(self):
        with allure.step("Проверка параметра (С метками) в Метках"):
            url = FilterMark.only_with_labels
            only_with_labels = requests.get(url, allow_redirects=False)
            try:
                only_with_labels.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=only_with_labels)
            assert only_with_labels.status_code == 200
            assert list(only_with_labels.json().keys()) == parameter_array
            assert dict(only_with_labels.json()).get('per_page') == success_total

    def test_label_metodist(self):
        with allure.step("Проверка параметра (Методист) в Метках"):
            url = FilterMark.label_metodist
            label_metodist = requests.get(url, allow_redirects=False)
            try:
                label_metodist.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=label_metodist)
            assert label_metodist.status_code == 200
            assert list(label_metodist.json().keys()) == parameter_array
            assert dict(label_metodist.json()).get('per_page') == success_total

    def test_label_med_spravka(self):
        with allure.step("Проверка параметра (Мед.справка) в Метках"):
            url = FilterMark.label_med_spravka
            label_med_spravka = requests.get(url, allow_redirects=False)
            try:
                label_med_spravka.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=label_med_spravka)
            assert label_med_spravka.status_code == 200
            assert list(label_med_spravka.json().keys()) == parameter_array
            assert dict(label_med_spravka.json()).get('per_page') == success_total

    def test_label_spisivaet(self):
        with allure.step("Проверка параметра (Списывальщик) в Метках"):
            url = FilterMark.label_spisivaet
            label_spisivaet = requests.get(url, allow_redirects=False)
            try:
                label_spisivaet.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=label_spisivaet)
            assert label_spisivaet.status_code == 200
            assert list(label_spisivaet.json().keys()) == parameter_array
            assert dict(label_spisivaet.json()).get('per_page') == success_total


@allure.feature("Админка Чат. Фильтр Ученик")
@allure.story("Проверка ответ статус кода при поиске E-mail все остальные фильтры Все")
class TestFilterUserChats:
    def test_search_user_hexcal(self):
        with allure.step("В поле ученик пусто (нет e-mail) во всех остальных фильтра Все"):
            url = FilterUser.search_user_hexcal
            search_user_hexcal = requests.get(url, allow_redirects=False)
            try:
                search_user_hexcal.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print('ERROR: %s' % e)
            LogInfoApi.log_info(log=search_user_hexcal)
            assert search_user_hexcal.status_code == 200
            assert list(search_user_hexcal.json().keys()) == parameter_array
            assert dict(search_user_hexcal.json()).get('per_page') == success_total
