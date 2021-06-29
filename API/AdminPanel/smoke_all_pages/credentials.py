# Админка раздел редактор курсов
# Энпоинты меню редактора курсов ДШ в тек. уг
path_admin_schedules_grade_1 = '/schedules?grade=1&school=true&'
path_admin_schedules_grade_2 = '/schedules?grade=2&school=true&'
path_admin_schedules_grade_3 = '/schedules?grade=3&school=true&'
path_admin_schedules_grade_4 = '/schedules?grade=4&school=true&'
path_admin_schedules_grade_5 = '/schedules?grade=5&school=true&'
path_admin_schedules_grade_6 = '/schedules?grade=6&school=true&'
path_admin_schedules_grade_7 = '/schedules?grade=7&school=true&'
path_admin_schedules_grade_8 = '/schedules?grade=8&school=true&'
path_admin_schedules_grade_9 = '/schedules?grade=9&school=true&'
path_admin_schedules_grade_10 = '/schedules?grade=10&school=true&'
path_admin_schedules_grade_11 = '/schedules?grade=11&school=true&'
# Прикрепление\удаление предмета
path_admin_add_subject = '/schedules?'
path_admin_delete_subject = '/schedules/5583026?'
# Раздел редактирования предмета
path_admin_item_editor = '/schedule_items.json?schedule_id=3908531&'  # переход в редактор предмета
path_admin_add_topic = '/topics?'  # добавить тему
path_admin_add_lesson = 'lessons.json?'  # Создание нового урока
path_admin_lesson_for_day = '/schedule_items.json?'  # привязка урока к дате
path_admin_remove_lesson = '/lessons/37865.json?'  # удаление урока
path_admin_remove_topic = '/topics/24273?addLessonHide=true&addLessonNameEvent=click&calendarActive=false&editTopicNameHide=true&lessonsHide=false&name=тест&schedule_id=3908531&subject_id=201&'
path_admin_save_date_ege = '/schedules/3908531?'  # сохранение даты ЕГЭ
# редактор МДЗ
path_admin_monthly_homework_editor = '/monthly_homeworks?schedule_id=3908531&'  # открытие редактора МДЗ
path_admin_create_monthly_homework = '/monthly_homeworks?'  # создание МДЗ
path_admin_delete_monthly_homework = '/monthly_homeworks/7229?'  # удаление МДЗ
# Энпоинты редактора курсов ЕГЭ
path_admin_editor_ege = '/schedules?grade=11&school=false&'  # переход в редактор егэ
path_admin_attach_subject_ege = '/schedules?'  # прикрепление предмета  егэ
path_admin_delete_subject_ege = '/schedules/5583707?'  # удаление предмета егэ
path_admin_add_topic = '/topics?'  # добавить тему


def __init__(self, token=None):
    self.token = token


def get_token(self):
    headers_user = {
        "Authorization": self.access_token,
    }
    return headers_user
