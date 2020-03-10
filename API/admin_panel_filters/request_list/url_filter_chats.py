from API.setting_tests import TokenSave

# Dev01 Staging
staging_dev01 = 'https://api-test-ege.interneturok.ru/api/v1/lesson_dialogs'

# FilterSchools
school_not = '&schools%5B%5D=5'
school_stolichniy_kit = '&schools%5B%5D=15'
# FilterGrades
klass_all = '&subject_ids=all'
klass_one = '&grades%5B%5D=1'
klass_two = '&grades%5B%5D=2'
klass_three = '&grades%5B%5D=3'
klass_four = '&grades%5B%5D=4'
klass_five = '&grades%5B%5D=5'
klass_six = '&grades%5B%5D=6'
klass_seven = '&grades%5B%5D=7'
klass_eight = '&grades%5B%5D=8'
klass_nine = '&grades%5B%5D=9'
klass_ten = '&grades%5B%5D=10'
klass_eleven = '&grades%5B%5D=11'
# FilterSubjects
subjects_all = '&subject_ids=all'
subject_russian_language = '&subjects[]=Русский язык'
subject_literatura = '&subjects[]=Литература'
subject_english_language = '&subjects[]=Английский язык'
subject_matematika = '&subjects[]=Математика'
subject_history = '&subjects[]=История'
subject_prirodavedenie = '&subjects[]=Природоведение'
subject_objestvoznanie = '&subjects[]=Обществознание'
subject_geografia = '&subjects[]=География'
subject_biologia = '&subjects[]=Биология'
subject_algebra_standart = '&subjects[]=Алгебра. Стандартный курс'
subject_geometria_standart = '&subjects[]=Геометрия. Стандартный курс'
subject_fizika_standart = '&subjects[]=Физика. Стандартный курс'
subject_informatika = '&subjects[]=Информатика'
subject_himiya = '&subjects[]=Химия'
subject_algebra = '&subjects[]=Алгебра'
subject_geometria = '&subjects[]=Геометрия'
subject_fizika = '&subjects[]=Физика'
subject_literaturnoe_chtenie = '&subjects[]=Литературное чтение'
subject_okruzauchi_mir = '&subjects[]=Окружающий мир'
subject_matematika_profi = '&subjects[]=Математика Профильный'
subject_matematika_bazovyai = '&subjects[]=Математика Базовый'
subject_vvodni_yrok = '&subjects[]=Вводный урок'
subject_podgotovka_k_OGE_matematika = '&subjects[]=Подготовка к ОГЭ по математике'
subject_podgotovka_k_OGE_russian_language = '&subjects[]=Подготовка к ОГЭ по русскому языку'
subject_algebra_effective = '&subjects[]=Алгебра. Эффективный курс'
subject_fizika_effective = '&subjects[]=Физика. Эффективный курс'
subject_geometria_effective = '&subjects[]=Геометрия. Эффективный курс'
subject_fizra = '&subjects[]=Физкультура'
subject_tehnologiya = '&subjects[]=Технология'
subject_izo = '&subjects[]=ИЗО'
subject_music = '&subjects[]=Музыка'
subject_osnovi_sovetskoi_itiki = '&subjects[]=Основы светской этики'
subject_obz = '&subjects[]=ОБЖ'
subject_astronomia = '&subjects[]=Астрономия'
subject_superJob = '&subjects[]=Профориентация от SuperJob'
subject_german_language = '&subjects[]=Немецкий язык'
subject_osnovy_sovet_itiki = '&subjects[]=Основы светской этики'
subject_tendo_studio = '&subjects[]=Профориентация - игры от tendo.studio'
# FilterFormatAccess
access_all = '?access_type=all'
trial_access = '?access_type=trial'
full_access = '?access_type=full'
# FilterLabels
label_all = '&label_ids='
only_with_labels = '&labels%5B%5D=2&labels%5B%5D=3&labels%5B%5D=4'
label_metodist = '&labels%5B%5D=2'
label_med_spravka = '&labels%5B%5D=3'
label_spisivaet = '&labels%5B%5D=4'
# Search by student
search_name_all = '&search_name='
search_user_hexcal = '&name=hexcal@mail.ru'
# Academic Year
year_2019 = '&year_id=2019'
# Other
token_admin = '&token='
name = '&name='
page = '&page=1'
# The token received after login admin
received_token = TokenSave.get_token_user_admin()


class FilterSchools:
    school_all = staging_dev01 + access_all + name + page + token_admin + received_token + year_2019
    Not_school = staging_dev01 + access_all + name + page + school_not + token_admin + received_token + year_2019
    school_stolichniy_kit = staging_dev01 + access_all + name + page + school_stolichniy_kit + token_admin + received_token + year_2019


class FilterGrades:
    klass_all = staging_dev01 + access_all + name + page + token_admin + received_token + year_2019
    klass_one = staging_dev01 + access_all + klass_one + name + page + token_admin + received_token + year_2019
    klass_two = staging_dev01 + access_all + klass_two + name + page + token_admin + received_token + year_2019
    klass_three = staging_dev01 + access_all + klass_three + name + page + token_admin + received_token + year_2019
    klass_four = staging_dev01 + access_all + klass_four + name + page + token_admin + received_token + year_2019
    klass_five = staging_dev01 + access_all + klass_five + name + page + token_admin + received_token + year_2019
    klass_six = staging_dev01 + access_all + klass_six + name + page + token_admin + received_token + year_2019
    klass_seven = staging_dev01 + access_all + klass_seven + name + page + token_admin + received_token + year_2019
    klass_eight = staging_dev01 + access_all + klass_eight + name + page + token_admin + received_token + year_2019
    klass_nine = staging_dev01 + access_all + klass_nine + name + page + token_admin + received_token + year_2019
    klass_ten = staging_dev01 + access_all + klass_ten + name + page + token_admin + received_token + year_2019
    klass_eleven = staging_dev01 + access_all + klass_eleven + name + page + token_admin + received_token + year_2019


class FilterSubjects:
    subject_russian_language = staging_dev01 + access_all + name + page + subject_russian_language + token_admin + received_token + year_2019
    subject_literatura = staging_dev01 + access_all + name + page + subject_literatura + token_admin + received_token + year_2019
    subject_english_language = staging_dev01 + access_all + name + page + subject_english_language + token_admin + received_token + year_2019
    subject_matematika = staging_dev01 + access_all + name + page + subject_matematika + token_admin + received_token + year_2019
    subject_history = staging_dev01 + access_all + name + page + subject_history + token_admin + received_token + year_2019
    subject_prirodavedenie = staging_dev01 + access_all + name + page + subject_prirodavedenie + token_admin + received_token + year_2019
    subject_objestvoznanie = staging_dev01 + access_all + name + page + subject_objestvoznanie + token_admin + received_token + year_2019
    subject_geografia = staging_dev01 + access_all + name + page + subject_geografia + token_admin + received_token + year_2019
    subject_biologia = staging_dev01 + access_all + name + page + subject_biologia + token_admin + received_token + year_2019
    subject_algebra_standart = staging_dev01 + access_all + name + page + subject_algebra_standart + token_admin + received_token + year_2019
    subject_geometria_standart = staging_dev01 + access_all + name + page + subject_geometria_standart + token_admin + received_token + year_2019
    subject_fizika_standart = staging_dev01 + access_all + name + page + subject_fizika_standart + token_admin + received_token + year_2019
    subject_informatika = staging_dev01 + access_all + name + page + subject_informatika + token_admin + received_token + year_2019
    subject_himiya = staging_dev01 + access_all + name + page + subject_himiya + token_admin + received_token + year_2019
    subject_algebra = staging_dev01 + access_all + name + page + subject_algebra + token_admin + received_token + year_2019
    subject_geometria = staging_dev01 + access_all + name + page + subject_geometria + token_admin + received_token + year_2019
    subject_fizika = staging_dev01 + access_all + name + page + subject_fizika + token_admin + received_token + year_2019
    subject_literaturnoe_chtenie = staging_dev01 + access_all + name + page + subject_literaturnoe_chtenie + token_admin + received_token + year_2019
    subject_okruzauchi_mir = staging_dev01 + access_all + name + page + subject_okruzauchi_mir + token_admin + received_token + year_2019
    subject_matematika_profi = staging_dev01 + access_all + name + page + subject_matematika_profi + token_admin + received_token + year_2019
    subject_matematika_bazovyai = staging_dev01 + access_all + name + page + subject_matematika_bazovyai + token_admin + received_token + year_2019
    subject_vvodni_yrok = staging_dev01 + access_all + name + page + subject_vvodni_yrok + token_admin + received_token + year_2019
    subject_podgotovka_k_OGE_matematika = staging_dev01 + access_all + name + page + subject_podgotovka_k_OGE_matematika + token_admin + received_token + year_2019
    subject_podgotovka_k_OGE_russian_language = staging_dev01 + access_all + name + page + subject_podgotovka_k_OGE_russian_language + token_admin + received_token + year_2019
    subject_algebra_effective = staging_dev01 + access_all + name + page + subject_algebra_effective + token_admin + received_token + year_2019
    subject_fizika_effective = staging_dev01 + access_all + name + page + subject_fizika_effective + token_admin + received_token + year_2019
    subject_geometria_effective = staging_dev01 + access_all + name + page + subject_geometria_effective + token_admin + received_token + year_2019
    subject_fizra = staging_dev01 + access_all + name + page + subject_fizra + token_admin + received_token + year_2019
    subject_tehnologiya = staging_dev01 + access_all + name + page + subject_tehnologiya + token_admin + received_token + year_2019
    subject_izo = staging_dev01 + access_all + name + page + subject_izo + token_admin + received_token + year_2019
    subject_music = staging_dev01 + access_all + name + page + subject_music + token_admin + received_token + year_2019
    subject_osnovi_sovetskoi_itiki = staging_dev01 + access_all + name + page + subject_osnovi_sovetskoi_itiki + token_admin + received_token + year_2019
    subject_obz = staging_dev01 + access_all + name + page + subject_obz + token_admin + received_token + year_2019
    subject_astronomia = staging_dev01 + access_all + name + page + subject_astronomia + token_admin + received_token + year_2019
    subject_superJob = staging_dev01 + access_all + name + page + subject_superJob + token_admin + received_token + year_2019
    subject_german_language = staging_dev01 + access_all + name + page + subject_german_language + token_admin + received_token + year_2019
    subject_osnovy_sovet_itiki = staging_dev01 + access_all + name + page + subject_osnovy_sovet_itiki + token_admin + received_token + year_2019
    subject_tendo_studio = staging_dev01 + access_all + name + page + subject_tendo_studio + token_admin + received_token + year_2019


class FilterFormatAccess:
    access_trial = staging_dev01 + trial_access + name + page + token_admin + received_token + year_2019
    access_full = staging_dev01 + full_access + name + page + token_admin + received_token + year_2019


class FilterMark:
    only_with_labels = staging_dev01 + access_all + only_with_labels + name + page + token_admin + received_token + year_2019
    label_metodist = staging_dev01 + access_all + label_metodist + name + page + token_admin + received_token + year_2019
    label_med_spravka = staging_dev01 + access_all + label_med_spravka + name + page + token_admin + received_token + year_2019
    label_spisivaet = staging_dev01 + access_all + label_spisivaet + name + page + token_admin + received_token + year_2019


class FilterUser:
    search_user_hexcal = staging_dev01 + access_all + search_user_hexcal + name + page + token_admin + received_token + year_2019
