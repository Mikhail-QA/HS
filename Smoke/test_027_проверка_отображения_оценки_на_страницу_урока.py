import allure
import time

from POM.setup import OpenTilda
from POM.asserts import AssertForTest027
from POM.popup_auth_and_reg import PopupSignIn
from POM.tilda_page import TildaPage
from POM.users import Hs02
from POM.url import UrlHomeSchool


@allure.feature("Проверка отображения оценки в слайде ДЗ на странице урока")
@allure.story("Авторизаваться учеником, перейти в слайд ДЗ, отображается оценка 4")
class LoginStudentAndCheckBallInHomeWorks(OpenTilda):

    def test_check_ball_for_student(self):
        driver = self.driver
        step_tilda = TildaPage(driver)
        step_enter = PopupSignIn(driver)
        step_user = Hs02(driver)
        step_url = UrlHomeSchool(driver)
        step_assert = AssertForTest027(driver)

        with allure.step("На TILDA нажать на кнопку Вход"):
            step_tilda.click_login_button()
        with allure.step("В поле email и password ввести hs02@yopmail.com/123456"):
            step_user.enter_email(user_name="hs02@yopmail.com")
            step_user.enter_password(password="123456")
        with allure.step("Нажать на кнопку Авторизоваться"):
            step_enter.click_button_login()
        with allure.step("Перейти на страницу урока"):
            step_url.go_to_lesson_page_tab_homework()
        with allure.step("Проверить на странице урока во вкладке ДЗ отображение оценки Итоговая оценка: 4 / Хорошо"):
            step_assert.check_bal_in_homweork_for_lesson_page()
