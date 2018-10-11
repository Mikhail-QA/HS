import allure
from POM.setup import StartTildaClassMethod
from POM.url import UrlHomeSchool
from POM.tilda_page import TildaPage
from POM.popup_auth_and_reg import PopupSignIn
from POM.users import Hs06
from POM.asserts import AssertForTest017


@allure.feature("Проверка в ЛК E-mail")
@allure.story("Авторизоваться П и проверить соответствие почты в ЛК")
class LoginAndCheckEmailForUser(StartTildaClassMethod):
    def test_check_email_user(self):
        driver = self.driver
        step_tilda = TildaPage(driver)
        step_enter = PopupSignIn(driver)
        step_user = Hs06(driver)
        step_go_to_profile = UrlHomeSchool(driver)
        step_assert = AssertForTest017(driver)

        with allure.step("На TILDA нажать на кнопку Войти"):
            step_tilda.click_button_enter()
        with allure.step("В поле email и password ввести hs05@yopmail.com/123456"):
            step_user.enter_email(user_name="hs05@yopmail.com")
            step_user.enter_password(password="123456")
        with allure.step("Нажать на кнопку Авторизоваться"):
            step_enter.click_button_login()
        with allure.step("Перейти в Личный кабинет"):
            step_go_to_profile.go_to_my_profile()
        with allure.step("В ЛК отображается почта указанная при авторизации"):
            step_assert.check_email_for_user()
