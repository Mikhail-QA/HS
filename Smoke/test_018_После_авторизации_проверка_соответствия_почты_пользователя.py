import allure
import pytest

from POM.setup import OpenTilda
from POM.url import UrlHomeSchool
from POM.tilda_page import TildaPage
from POM.popup_auth_and_reg import PopupSignIn
from POM.users import Hs05
from POM.asserts import AssertForTest017


@pytest.mark.end_to_end
@pytest.mark.regression
@allure.feature("Проверка в ЛК E-mail")
@allure.story("Авторизоваться П и проверить соответствие почты в ЛК")
class LoginAndCheckEmailForUser(OpenTilda):
    def test_check_email_user(self):
        self.tilda_page = TildaPage(self.driver)
        self.popup_sigin = PopupSignIn(self.driver)
        self.user = Hs05(self.driver)
        self.go = UrlHomeSchool(self.driver)
        self.assert_step = AssertForTest017(self.driver)

        self.tilda_page.click_login_button()
        self.user.enter_email(user_name="hs05@yopmail.com")
        self.user.enter_password(password="123456")
        self.popup_sigin.click_button_login()
        self.go.go_to_my_profile()
        self.assert_step.check_email_in_user()
