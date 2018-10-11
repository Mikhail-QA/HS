import allure
from POM.setup import StartTildaClassMethod
from POM.url import UrlHomeSchool
from POM.tilda_page import TildaPage
from POM.popup_auth_and_reg import PopupSignIn
from POM.users import Hs03
from POM.refresh import Refresh
from POM.asserts import AssertForTest008
from POM.my_profile import OffAutoPayInPersonalMentor


@allure.feature("Отключить автоплатеж в ПН")
@allure.story("Авторизация, отключить АП в ПН в 11 классе")
class LoginAndOffAutoPaymentInPersonalMentor(StartTildaClassMethod):
    def test_off_auto_payment(self):
        driver = self.driver
        step_tilda = TildaPage(driver)
        step_enter = PopupSignIn(driver)
        step_user = Hs03(driver)
        step_go_to_profile = UrlHomeSchool(driver)
        step_refresh = Refresh(driver)
        step_assert = AssertForTest008(driver)
        step_off = OffAutoPayInPersonalMentor(driver)

        with allure.step("На TILDA нажать на кнопку Войти"):
            step_tilda.click_button_enter()
        with allure.step("В поле email и password ввести hs03@yopmail.com/123456"):
            step_user.enter_email(user_name="hs03@yopmail.com")
            step_user.enter_password(password="123456")
        with allure.step("Нажать на кнопку Авторизоваться"):
            step_enter.click_button_login()
        with allure.step("Перейти в Личный кабинет"):
            step_go_to_profile.go_to_my_profile()
        with allure.step("В виджите Нажать на кнопку Вкл в автоплатеже"):
            step_off.click_off_auto_pay_in_widget()
        with allure.step("В тултипе нажать на кнопку Отключить автоплатеж"):
            step_off.click_off_auto_pay_in_tooltip()
        with allure.step("В попапе нажать на кнопку Отключить автоплатеж"):
            step_off.click_off_auto_pay_in_popup()
        with allure.step("Перезагрузить страницу"):
            step_refresh.refresh()
        with allure.step("В поле АП текст поменялся на Автоплатеж Выкл"):
            step_assert.check_text_in_widget_my_school()
