import allure
from POM.setup import OpenTilda
from POM.url import UrlHomeSchool
from POM.tilda_page import TildaPage
from POM.popup_auth_and_reg import PopupSignIn
from POM.users import Hs02
from POM.refresh import Refresh
from POM.asserts import AssertForTest007
from POM.my_profile import OffAutoPayInSchool


@allure.feature("Отключить автоплатеж в ДШ классе №7")
@allure.story("Авторизация, отключить АП в 7 класс")
class LoginAndOffAutoPaymentInCourseSchool(OpenTilda):
    def test_off_auto_payment(self):
        driver = self.driver
        step_tilda = TildaPage(driver)
        step_enter = PopupSignIn(driver)
        step_user = Hs02(driver)
        step_go_to_profile = UrlHomeSchool(driver)
        step_refresh = Refresh(driver)
        step_assert = AssertForTest007(driver)
        step_off = OffAutoPayInSchool(driver)

        with allure.step("На TILDA нажать на кнопку Войти"):
            step_tilda.click_login_button()
        with allure.step("В поле email и password ввести hs02@yopmail.com/123456"):
            step_user.enter_email(user_name="hs02@yopmail.com")
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
