import allure
import pytest

from POM.popup_auth_and_reg import PopupSignIn
from POM.setup import OpenTilda
from POM.tilda_page import TildaPage
from POM.users import Hs02
from POM.url import UrlHomeSchool
from POM.lesson_page import LessonPage
from POM.TT import Test
from POM.asserts import AssertForTest021


@pytest.mark.flaky(reruns=1, reruns_delay=1)
@allure.feature("Тест")
@allure.story("Авторизоваться, Пройти Тест")
class PassTest(OpenTilda):
    def test_passed(self):
        driver = self.driver
        step_tilda = TildaPage(driver)
        step_enter = PopupSignIn(driver)
        step_user = Hs02(driver)
        url_go = UrlHomeSchool(driver)
        steps_test = LessonPage(driver)
        ask_test = Test(driver)
        assert_step = AssertForTest021(driver)

        step_tilda.click_login_button()
        step_user.enter_email(user_name="hs02@yopmail.com")
        step_user.enter_password(password="123456")
        step_enter.click_button_login()
        url_go.go_to_lesson_tab_test_iu()
        steps_test.go_test()
        ask_test.start_test()
        ask_test.click_button_finish()
        assert_step.check_button_finish_test()
