from API.setting_tests import TokenSave

# Dev01 Staging
staging_dev01 = 'https://api-test-ege.interneturok.ru/api/v2/results/homeworks'

# FilterSchools
school_all = '&school_ids='
school_not = '&school_ids=5'
school_stolichniy_kit = '&school_ids=15'
# FilterGrades
klass_all = '&subject_ids=all'
klass_one = '&subject_ids=127,131,135,139,154,170,171,172,173'
klass_two = '&subject_ids=128,132,136,140,143,155,174,175,176,177'
klass_three = '&subject_ids=129,133,137,141,144,156,178,179,180,181'
klass_four = '&subject_ids=130,134,138,142,145,157,182,183,184,185,186,216'
klass_five = '&subject_ids=52,53,54,55,56,57,146,147,148,158,187,188,189,190'
klass_six = '&subject_ids=58,59,60,61,62,63,64,65,159,191,192,193,194'
klass_seven = '&subject_ids=66,68,69,70,71,72,73,74,75,76,160,167,168,169,195,196,204,211'
klass_eight = '&subject_ids=77,78,79,80,81,82,83,84,85,86,87,88,161,197,205,206,207,212'
klass_nine = '&subject_ids=89,90,91,92,93,94,95,96,97,98,99,100,150,151,162,198,208,209,210,213'
klass_ten = '&subject_ids=101,102,103,104,105,106,107,108,109,110,111,112,163,199,200,214'
klass_eleven = '&subject_ids=113,114,115,116,117,118,119,120,121,122,123,164,201,202,203,215'
# FilterSubjects
subjects_all = '&subject_ids=all'
subject_russian_language = '&subject_ids=52,58,66,77,89,101,113,127,128,129,130,152'
subject_literatura = '&subject_ids=53,59,68,78,90,102,114'
subject_english_language = '&subject_ids=54,60,69,79,91,103,115,143,144,145'
subject_matematika = '&subject_ids=55,61,135,136,137,138'
subject_history = '&subject_ids=56,62,72,83,95,107,119'
subject_prirodavedenie = '&subject_ids=57'
subject_objestvoznanie = '&subject_ids=63,73,84,96,108,120,148'
subject_geografia = '&subject_ids=64,74,85,97,109,147'
subject_biologia = '&subject_ids=65,76,88,100,112,123,146'
subject_algebra_standart = '&subject_ids=70,80,92'
subject_geometria_standart = '&subject_ids=71,81,93'
subject_fizika_standart = '&subject_ids=75,86,98'
subject_informatika = '&subject_ids=82,94,106,118,167'
subject_himiya = '&subject_ids=87,99,111,122'
subject_algebra = '&subject_ids=104,116'
subject_geometria = '&subject_ids=105,117'
subject_fizika = '&subject_ids=46,110,121'
subject_literaturnoe_chtenie = '&subject_ids=131,132,133,134'
subject_okruzauchi_mir = '&subject_ids=139,140,141,142'
subject_matematika_profi = '&subject_ids=28'
subject_matematika_bazovyai = '&subject_ids=153'
subject_vvodni_yrok = '&subject_ids=158,159,160,161,162,163,164,154,155,156,157'
subject_podgotovka_k_OGE_matematika = '&subject_ids=150'
subject_podgotovka_k_OGE_russian_language = '&subject_ids=151'
subject_algebra_effective = '&subject_ids=168'
subject_fizika_effective = '&subject_ids=169'
subject_geometria_effective = '&subject_ids=204,206,209'
subject_fizra = '&subject_ids=170,174,178,187,182,191,198,195,199,201,197'
subject_tehnologiya = '&subject_ids=173,177,181,185,190,194,196'
subject_izo = '&subject_ids=176,172,180,184,189,193'
subject_music = '&subject_ids=179,171,192,183,188,175'
subject_osnovi_sovetskoi_itiki = '&subject_ids=186'
subject_obz = '&subject_ids=200,202'
subject_astronomia = '&subject_ids=203'
subject_superJob = '&subject_ids=211,212,213,214,215'
# FilterWeek
week_one = '&weeks[]=1'
week_twenty_five = '&weeks[]=25'
week_fifty_three = '&weeks[]=53'
# FilterStatusDz
status_dz_all = '&filter=all'
status_dz_almost_all = '&filter=almost_all'
status_dz_unchecked = '&filter=unchecked'
status_dz_checked = '&filter=checked'
status_dz_on_repeat = '&filter=on-repeat'
status_dz_missed = '&filter=missed'
status_dz_new_missed = '&filter=new_missed'
# FilterTypeDz
type_dz_all = '&homework_type=all'
type_dz_monthly = '&homework_type=1'
type_dz_weekly = '&homework_type=0'
# FilterFormatAccess
access_all = '?access_type=all'
trial_access = '?access_type=trial'
full_access = '?access_type=full'
# FilterLabels
label_all = '&label_ids='
only_with_labels = '&label_ids=2,3,4'
label_metodist = '&label_ids=2'
label_med_spravka = '&label_ids=3'
label_spisivaet = '&label_ids=4'
# Academic Year
year_2019 = '&year_id=2019'
# Search by student
search_name_all = '&search_name='
search_user_hexcal = '&search_name=hexcal@mail.ru'
# Other
token_admin = '&token='
order = '&order=false'
page = '&page=1'
# The token received after login admin
received_token = TokenSave.get_token_user_admin()


class FilterGrades:
    klass_all = staging_dev01 + access_all + status_dz_all + type_dz_all + label_all + order + page + school_all + search_name_all + klass_all + token_admin + received_token
    klass_one = staging_dev01 + access_all + status_dz_all + type_dz_all + label_all + order + page + school_all + search_name_all + klass_one + token_admin + received_token
    klass_two = staging_dev01 + access_all + status_dz_all + type_dz_all + label_all + order + page + school_all + search_name_all + klass_two + token_admin + received_token
    klass_three = staging_dev01 + access_all + status_dz_all + type_dz_all + label_all + order + page + school_all + search_name_all + klass_three + token_admin + received_token
    klass_four = staging_dev01 + access_all + status_dz_all + type_dz_all + label_all + order + page + school_all + search_name_all + klass_four + token_admin + received_token
    klass_five = staging_dev01 + access_all + status_dz_all + type_dz_all + label_all + order + page + school_all + search_name_all + klass_five + token_admin + received_token
    klass_six = staging_dev01 + access_all + status_dz_all + type_dz_all + label_all + order + page + school_all + search_name_all + klass_six + token_admin + received_token
    klass_seven = staging_dev01 + access_all + status_dz_all + type_dz_all + label_all + order + page + school_all + search_name_all + klass_seven + token_admin + received_token
    klass_eight = staging_dev01 + access_all + status_dz_all + type_dz_all + label_all + order + page + school_all + search_name_all + klass_eight + token_admin + received_token
    klass_nine = staging_dev01 + access_all + status_dz_all + type_dz_all + label_all + order + page + school_all + search_name_all + klass_nine + token_admin + received_token
    klass_ten = staging_dev01 + access_all + status_dz_all + type_dz_all + label_all + order + page + school_all + search_name_all + klass_ten + token_admin + received_token
    klass_eleven = staging_dev01 + access_all + status_dz_all + type_dz_all + label_all + order + page + school_all + search_name_all + klass_eleven + token_admin + received_token


class FilterSubjects:
    subject_russian_language = staging_dev01 + access_all + status_dz_all + type_dz_all + label_all + order + page + school_all + search_name_all + subject_russian_language + token_admin + received_token
    subject_literatura = staging_dev01 + access_all + status_dz_all + type_dz_all + label_all + order + page + school_all + search_name_all + subject_literatura + token_admin + received_token
    subject_english_language = staging_dev01 + access_all + status_dz_all + type_dz_all + label_all + order + page + school_all + search_name_all + subject_english_language + token_admin + received_token
    subject_matematika = staging_dev01 + access_all + status_dz_all + type_dz_all + label_all + order + page + school_all + search_name_all + subject_matematika + token_admin + received_token
    subject_history = staging_dev01 + access_all + status_dz_all + type_dz_all + label_all + order + page + school_all + search_name_all + subject_history + token_admin + received_token
    subject_prirodavedenie = staging_dev01 + access_all + status_dz_all + type_dz_all + label_all + order + page + school_all + search_name_all + subject_prirodavedenie + token_admin + received_token
    subject_objestvoznanie = staging_dev01 + access_all + status_dz_all + type_dz_all + label_all + order + page + school_all + search_name_all + subject_objestvoznanie + token_admin + received_token
    subject_geografia = staging_dev01 + access_all + status_dz_all + type_dz_all + label_all + order + page + school_all + search_name_all + subject_geografia + token_admin + received_token
    subject_biologia = staging_dev01 + access_all + status_dz_all + type_dz_all + label_all + order + page + school_all + search_name_all + subject_biologia + token_admin + received_token
    subject_algebra_standart = staging_dev01 + access_all + status_dz_all + type_dz_all + label_all + order + page + school_all + search_name_all + subject_algebra_standart + token_admin + received_token
    subject_geometria_standart = staging_dev01 + access_all + status_dz_all + type_dz_all + label_all + order + page + school_all + search_name_all + subject_geometria_standart + token_admin + received_token
    subject_fizika_standart = staging_dev01 + access_all + status_dz_all + type_dz_all + label_all + order + page + school_all + search_name_all + subject_fizika_standart + token_admin + received_token
    subject_informatika = staging_dev01 + access_all + status_dz_all + type_dz_all + label_all + order + page + school_all + search_name_all + subject_informatika + token_admin + received_token
    subject_himiya = staging_dev01 + access_all + status_dz_all + type_dz_all + label_all + order + page + school_all + search_name_all + subject_himiya + token_admin + received_token
    subject_algebra = staging_dev01 + access_all + status_dz_all + type_dz_all + label_all + order + page + school_all + search_name_all + subject_algebra + token_admin + received_token
    subject_geometria = staging_dev01 + access_all + status_dz_all + type_dz_all + label_all + order + page + school_all + search_name_all + subject_geometria + token_admin + received_token
    subject_fizika = staging_dev01 + access_all + status_dz_all + type_dz_all + label_all + order + page + school_all + search_name_all + subject_fizika + token_admin + received_token
    subject_literaturnoe_chtenie = staging_dev01 + access_all + status_dz_all + type_dz_all + label_all + order + page + school_all + search_name_all + subject_literaturnoe_chtenie + token_admin + received_token
    subject_okruzauchi_mir = staging_dev01 + access_all + status_dz_all + type_dz_all + label_all + order + page + school_all + search_name_all + subject_okruzauchi_mir + token_admin + received_token
    subject_matematika_profi = staging_dev01 + access_all + status_dz_all + type_dz_all + label_all + order + page + school_all + search_name_all + subject_matematika_profi + token_admin + received_token
    subject_matematika_bazovyai = staging_dev01 + access_all + status_dz_all + type_dz_all + label_all + order + page + school_all + search_name_all + subject_matematika_bazovyai + token_admin + received_token
    subject_vvodni_yrok = staging_dev01 + access_all + status_dz_all + type_dz_all + label_all + order + page + school_all + search_name_all + subject_vvodni_yrok + token_admin + received_token
    subject_podgotovka_k_OGE_matematika = staging_dev01 + access_all + status_dz_all + type_dz_all + label_all + order + page + school_all + search_name_all + subject_podgotovka_k_OGE_matematika + token_admin + received_token
    subject_podgotovka_k_OGE_russian_language = staging_dev01 + access_all + status_dz_all + type_dz_all + label_all + order + page + school_all + search_name_all + subject_podgotovka_k_OGE_russian_language + token_admin + received_token
    subject_algebra_effective = staging_dev01 + access_all + status_dz_all + type_dz_all + label_all + order + page + school_all + search_name_all + subject_algebra_effective + token_admin + received_token
    subject_fizika_effective = staging_dev01 + access_all + status_dz_all + type_dz_all + label_all + order + page + school_all + search_name_all + subject_fizika_effective + token_admin + received_token
    subject_geometria_effective = staging_dev01 + access_all + status_dz_all + type_dz_all + label_all + order + page + school_all + search_name_all + subject_geometria_effective + token_admin + received_token
    subject_fizra = staging_dev01 + access_all + status_dz_all + type_dz_all + label_all + order + page + school_all + search_name_all + subject_fizra + token_admin + received_token
    subject_tehnologiya = staging_dev01 + access_all + status_dz_all + type_dz_all + label_all + order + page + school_all + search_name_all + subject_tehnologiya + token_admin + received_token
    subject_izo = staging_dev01 + access_all + status_dz_all + type_dz_all + label_all + order + page + school_all + search_name_all + subject_izo + token_admin + received_token
    subject_music = staging_dev01 + access_all + status_dz_all + type_dz_all + label_all + order + page + school_all + search_name_all + subject_music + token_admin + received_token
    subject_osnovi_sovetskoi_itiki = staging_dev01 + access_all + status_dz_all + type_dz_all + label_all + order + page + school_all + search_name_all + subject_osnovi_sovetskoi_itiki + token_admin + received_token
    subject_obz = staging_dev01 + access_all + status_dz_all + type_dz_all + label_all + order + page + school_all + search_name_all + subject_obz + token_admin + received_token
    subject_astronomia = staging_dev01 + access_all + status_dz_all + type_dz_all + label_all + order + page + school_all + search_name_all + subject_astronomia + token_admin + received_token
    subject_superJob = staging_dev01 + access_all + status_dz_all + type_dz_all + label_all + order + page + school_all + search_name_all + subject_superJob + token_admin + received_token


class FilterWeek:
    week_one = staging_dev01 + access_all + status_dz_all + type_dz_all + label_all + order + page + school_all + search_name_all + klass_all + token_admin + received_token + week_one + year_2019
    week_twenty_five = staging_dev01 + access_all + status_dz_all + type_dz_all + label_all + order + page + school_all + search_name_all + klass_all + token_admin + received_token + week_twenty_five + year_2019
    week_fifty_three = staging_dev01 + access_all + status_dz_all + type_dz_all + label_all + order + page + school_all + search_name_all + klass_all + token_admin + received_token + week_fifty_three + year_2019


class FilterStatusDz:
    status_dz_almost_all = staging_dev01 + access_all + status_dz_almost_all + type_dz_all + label_all + order + page + school_all + search_name_all + klass_all + token_admin + received_token
    status_dz_unchecked = staging_dev01 + access_all + status_dz_unchecked + type_dz_all + label_all + order + page + school_all + search_name_all + klass_all + token_admin + received_token
    status_dz_checked = staging_dev01 + access_all + status_dz_checked + type_dz_all + label_all + order + page + school_all + search_name_all + klass_all + token_admin + received_token
    status_dz_on_repeat = staging_dev01 + access_all + status_dz_on_repeat + type_dz_all + label_all + order + page + school_all + search_name_all + klass_all + token_admin + received_token
    status_dz_missed = staging_dev01 + access_all + status_dz_missed + type_dz_all + label_all + order + page + school_all + search_name_all + klass_all + token_admin + received_token
    status_new_missed = staging_dev01 + access_all + status_dz_new_missed + type_dz_all + label_all + order + page + school_all + search_name_all + klass_all + token_admin + received_token


class FilterTypeDz:
    type_dz_monthly = staging_dev01 + access_all + status_dz_all + type_dz_monthly + label_all + order + page + school_all + search_name_all + klass_all + token_admin + received_token
    type_dz_weekly = staging_dev01 + access_all + status_dz_all + type_dz_weekly + label_all + order + page + school_all + search_name_all + klass_all + token_admin + received_token


class FilterFormatAccess:
    trial_access = staging_dev01 + trial_access + status_dz_all + type_dz_all + label_all + order + page + school_all + search_name_all + klass_all + token_admin + received_token
    full_access = staging_dev01 + full_access + status_dz_all + type_dz_all + label_all + order + page + school_all + search_name_all + klass_all + token_admin + received_token


class FilterMark:
    only_with_labels = staging_dev01 + access_all + status_dz_all + type_dz_all + only_with_labels + order + page + school_all + search_name_all + klass_all + token_admin + received_token
    label_metodist = staging_dev01 + access_all + status_dz_all + type_dz_all + label_metodist + page + school_all + search_name_all + klass_all + token_admin + received_token
    label_med_spravka = staging_dev01 + access_all + status_dz_all + type_dz_all + label_med_spravka + order + page + school_all + search_name_all + klass_all + token_admin + received_token
    label_spisivaet = staging_dev01 + access_all + status_dz_all + type_dz_all + label_spisivaet + order + page + school_all + search_name_all + klass_all + token_admin + received_token
