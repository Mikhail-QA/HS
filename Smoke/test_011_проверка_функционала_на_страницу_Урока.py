import allure
import time

from POM.setup import OpenTilda
from POM.tilda_page import TildaPage
from POM.popup_auth_and_reg import PopupSignIn
from POM.users import Hs02
from POM.schedule_page import SchedulePage
from POM.lesson_page import LessonPage
from POM.asserts import AssertForTest014
from POM.url import UrlHomeSchool


# Поменять ссылки в:
# test_002_check_tour_in_lesson_page
# test_006_click_button_next_step
# test_027

@allure.issue("EDU-4327, EDU-4571")
@allure.feature("Страница урока/Страница расписания")
@allure.story("Проверить тур на странице расписания, перейти на страницу урока, проверить фкнуционал страницы урока")
class LoginAndGoToLessonPageTestAllFunction(OpenTilda):
    def test_000_go_lesson_page(self):
        driver = self.driver
        step_tilda = TildaPage(driver)
        step_enter = PopupSignIn(driver)
        step_user = Hs02(driver)

        step_tilda.click_login_button()
        step_user.enter_email(user_name="hs02@yopmail.com")
        step_user.enter_password(password="123456")
        step_enter.click_button_login()

    def test_001_check_tour_in_schedule_page(self):
        driver = self.driver
        step_tour = SchedulePage(driver)
        time.sleep(15)
        step_tour.click_button_next_in_tour()
        step_tour.click_button_prew_in_tour()
        step_tour.click_button_close_in_tour()

    def test_002_check_tour_in_lesson_page(self):
        driver = self.driver
        go_lesson_page = UrlHomeSchool(driver)
        step_lesson_page = LessonPage(driver)
        step_assert = AssertForTest014(driver)
        # Перейти на страницу видеоурока История, 7 класс , неделя 23 (3 февраля - 8 февраля)
        go_lesson_page.go_to_lesson_page_test()
        # Пройти весь тур кликнув Далее 5 раз
        step_lesson_page.click_button_next_in_tour()
        step_lesson_page.click_button_prew_in_tour()
        step_lesson_page.click_button_close_in_tour()
        step_assert.check_text_show_summary()
        step_assert.check_button_display_show_next_step()
        step_assert.check_display_show_block_ask_question()

    def test_003_check_button_show_summary(self):
        driver = self.driver
        step_lesson_page = LessonPage(driver)
        step_assert = AssertForTest014(driver)

        step_lesson_page.click_button_show_summary()
        step_assert.check_button_hide_summary()

    def test_004_ask_a_question_teacher(self):
        driver = self.driver
        step_lesson_page = LessonPage(driver)
        step_assert = AssertForTest014(driver)
        step_lesson_page.send_text_in_input_ask_question()
        step_lesson_page.click_button_send()
        ## шаг необходим из-за выкл faye на дев01
        self.driver.refresh()
        step_assert.check_message_for_ask_questions()

    def test_005_in_tab_ask_a_question_teacher_download_file(self):
        driver = self.driver
        step_lesson_page = LessonPage(driver)
        step_assert = AssertForTest014(driver)
        step_lesson_page.attach_img_in_ask_question()
        step_lesson_page.click_button_send()
        ## шаг необходим из-за выкл faye на дев01
        self.driver.refresh()
        step_assert.check_file_for_ask_question()

    def test_006_click_button_next_step(self):
        driver = self.driver
        step_lesson_page = LessonPage(driver)
        step_go_dz = UrlHomeSchool(driver)
        step_assert = AssertForTest014(driver)

        step_lesson_page.click_button_next_step()
        step_assert.check_redirect_url()
        step_go_dz.go_to_lesson_page_tab_homework()
        step_assert.check_button_go_to_schedule()

    def test_007_to_download_dz(self):
        driver = self.driver
        step_lesson_page = LessonPage(driver)
        step_assert = AssertForTest014(driver)
        step_lesson_page.click_download_dz()
        step_lesson_page.attach_img_in_upload_homework()
        step_lesson_page.click_submit_a_job()
        step_lesson_page.click_yes_in_popup()
        step_assert.check_uploader_progress()
        self.driver.refresh()
        step_assert.check_text_successfully_download_az()

    def test_008_click_button_go_to_schedule(self):
        driver = self.driver
        step_lesson_page = LessonPage(driver)
        step_assert = AssertForTest014(driver)
        step_lesson_page.click_button_go_to_schedule()
        step_assert.check_redirect_user_to_schedule_page()
