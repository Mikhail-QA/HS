import allure
import pytest
from POM.setup import OpenTilda
from POM.asserts import AssertForTest027
from POM.popup_auth_and_reg import PopupSignIn
from POM.tilda_page import TildaPage
from POM.users import Hs02
from POM.url import UrlHomeSchool


@pytest.mark.flaky(reruns=1, reruns_delay=1)
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

        step_tilda.click_login_button()
        step_user.enter_email(user_name="hs02@yopmail.com")
        step_user.enter_password(password="123456")
        step_enter.click_button_login()
        step_url.go_to_lesson_page_tab_homework()
        step_assert.check_bal_in_homweork_for_lesson_page()
