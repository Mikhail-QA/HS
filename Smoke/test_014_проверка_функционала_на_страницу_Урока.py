import allure
import time

from POM.setup import StartTildaClassMethod
from POM.tilda_page import TildaPage
from POM.popup_auth_and_reg import PopupSignIn
from POM.users import Hs05
from POM.schedule_page import SchedulePage
from POM.lesson_page import LessonPage
from POM.asserts import AssertForTest014
from POM.url import UrlHomeSchool
from POM.refresh import Refresh


@allure.issue("EDU-4327")
@allure.feature("Страница урока/Страница расписания")
@allure.story(
    "Проверить тур на странице расписания, перейти на страницу урока, проверить фкнуционал страницы урока")
class LoginAndGoToLessonPageTestAllFunction(StartTildaClassMethod):
    def test_000_go_lesson_page(self):
        driver = self.driver
        step_tilda = TildaPage(driver)
        step_enter = PopupSignIn(driver)
        step_user = Hs05(driver)

        with allure.step("На TILDA нажать на кнопку Войти"):
            step_tilda.click_button_enter()
        with allure.step("В поле email и password ввести hs02@yopmail.com/123456"):
            step_user.enter_email(user_name="hs02@yopmail.com")
            step_user.enter_password(password="123456")
        with allure.step("Нажать на кнопку Авторизоваться"):
            step_enter.click_button_login()

    def test_001_check_tour_in_schedule_page(self):
        driver = self.driver
        step_tour = SchedulePage(driver)
        step_refresh = Refresh(driver)

        with allure.step("Обновить страницу"):
            step_refresh.refresh()
            time.sleep(20)
            step_refresh.refresh()
        with allure.step("Пройти весь тур кликнув Далее 7 раз"):
            step_tour.click_button_next_in_tour()
        with allure.step("В туре нажать на кнопку Назад"):
            step_tour.click_button_prew_in_tour()
        with allure.step("В туре нажать на кнопку Закрыть"):
            step_tour.click_button_close_in_tour()

    def test_002_check_tour_in_lesson_page(self):
        driver = self.driver
        step_schedule = SchedulePage(driver)
        step_lesson_page = LessonPage(driver)
        step_assert = AssertForTest014(driver)
        with allure.step("Перейти на страницу урока"):
            step_schedule.go_to_lesson_page()
        with allure.step("Пройти весь тур кликнув Далее 5 раз"):
            step_lesson_page.click_button_next_in_tour()
        with allure.step("В туре нажать на кнопку Назад"):
            step_lesson_page.click_button_prew_in_tour()
        with allure.step("В туре нажать на кнопку Закрыть"):
            step_lesson_page.click_button_close_in_tour()
        with allure.step("На странице урока отображаются Показать конспект, Следующий шаг, Блок Задай вопрос"):
            step_assert.check_text_show_summary()
            step_assert.check_button_display_show_next_step()
            step_assert.check_display_show_block_ask_question()

    def test_003_check_button_show_summary(self):
        driver = self.driver
        go_lesson_page = UrlHomeSchool(driver)
        step_lesson_page = LessonPage(driver)
        step_assert = AssertForTest014(driver)
        with allure.step("Перейти на страницу урока Информатика, 7 класс , неделя 12 (12 ноября - 17 ноября)тест"):
            go_lesson_page.go_to_lesson_page_test()
        with allure.step("Нажать на кнопку Показать конспект"):
            step_lesson_page.click_button_show_summary()
        with allure.step("Кнопка Показать конспект поменяла название на Свернуть конспект"):
            step_assert.check_button_hide_summary()

    def test_004_ask_a_question_teacher(self):
        driver = self.driver
        step_lesson_page = LessonPage(driver)
        step_assert = AssertForTest014(driver)
        with allure.step("Ввести текст в инпут Задать вопрос ومنظومة الظواهر الملحوظة"):
            step_lesson_page.send_text_in_input_ask_question()
        with allure.step("Нажать на кнопку Отправить"):
            step_lesson_page.click_button_send()
        with allure.step("После появляется сообщение от П с текстом ومنظومة الظواهر الملحوظة"):
            step_assert.check_message_for_ask_questions()

    def test_005_in_tab_ask_a_question_teacher_download_file(self):
        driver = self.driver
        step_lesson_page = LessonPage(driver)
        step_assert = AssertForTest014(driver)
        with allure.step("Нажать на кнопку Загрузить файл"):
            step_lesson_page.click_button_download_file_in_ask_question()
        with allure.step("Загрузить картинку"):
            step_lesson_page.attach_img_in_ask_question()
        with allure.step("Нажать на кнопку Отправить"):
            step_lesson_page.click_button_send()
        with allure.step("После появляется сообщение от П с название файла photo_2018-09-18_13-28-24.jpg "):
            step_assert.check_file_for_ask_question()

    def test_006_click_button_next_step(self):
        driver = self.driver
        step_lesson_page = LessonPage(driver)
        step_assert = AssertForTest014(driver)

        with allure.step("Нажать на кнопку Следующий шаг"):
            step_lesson_page.click_button_next_step()
        with allure.step(
                "После нажатия на кнопку Следующий шаг П перешел во вкладку ДЗ"
                "кнопка поменяла название на Перейти к расписанию и поменлся URL"):
            step_assert.check_button_go_to_schedule()

    def test_007_to_download_dz(self):
        driver = self.driver
        step_lesson_page = LessonPage(driver)
        step_assert = AssertForTest014(driver)
        with allure.step("Нажать на кнопку Загрузить решение"):
            step_lesson_page.click_download_dz()
        with allure.step("Загрузить картинку"):
            step_lesson_page.attach_img_in_upload_homework()
        with allure.step("Нажать на кнопку Отправить решение"):
            step_lesson_page.click_submit_a_job()
        with allure.step("В попапе нажать на кнопку Да"):
            step_lesson_page.click_yes_in_popup()
        with allure.step(
                "После отправки ДЗ появилось сообщение Ваше решение успешно отправлено и ожидает проверки учителем."):
            step_assert.check_text_successfully_download_az()

    def test_008_click_button_go_to_schedule(self):
        driver = self.driver
        step_lesson_page = LessonPage(driver)
        step_assert = AssertForTest014(driver)
        with allure.step("Нажать на кнопку Перейти к расписанию"):
            step_lesson_page.click_button_go_to_schedule()
        with allure.step(
                "Пользователя редиректит на страницу расписания /school"):
            step_assert.check_redirect_user_to_schedule_page()
