import allure
import pytest

from POM.url import UrlHomeSchool
from POM.setup import StartLandingClassMethod
from POM.school_page import LandingPage
from POM.users import Hs05
from POM.asserts import AssertForTest017


@pytest.mark.flaky(reruns=1, reruns_delay=1)
@allure.feature("Проверка в ЛК E-mail")
@allure.story("Зарегистрироваться П и проверить указанную почтовы в ЛК")
class CreateAccountAndCheckEmail(StartLandingClassMethod):
    def test_check_email_user(self):
        driver = self.driver
        step_school = LandingPage(driver)
        step_user = Hs05(driver)
        step_go_to_profile = UrlHomeSchool(driver)
        step_assert = AssertForTest017(driver)

        step_school.click_button_to_start()
        step_user.reg_email(user_name="hs05@yopmail.com")
        step_user.reg_password(password="123456")
        step_user.reg_mobile(number="+71234567890")
        step_school.click_sign_up()

        step_go_to_profile.go_to_my_profile()
        step_assert.check_email_in_user()
