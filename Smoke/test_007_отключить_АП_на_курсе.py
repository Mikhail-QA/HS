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

        step_tilda.click_login_button()
        step_user.enter_email(user_name="hs02@yopmail.com")
        step_user.enter_password(password="123456")
        step_enter.click_button_login()
        step_go_to_profile.go_to_my_profile()
        step_off.click_off_auto_pay_in_widget()
        step_off.click_off_auto_pay_in_tooltip()
        step_off.click_off_auto_pay_in_popup()
        step_refresh.refresh()
        step_assert.check_text_in_widget_my_school()
