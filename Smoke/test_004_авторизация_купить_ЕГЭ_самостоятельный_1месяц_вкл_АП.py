import allure
import time

from POM.setup import OpenTilda
from POM.url import UrlHomeSchool
from POM.tilda_page import TildaPage
from POM.popup_auth_and_reg import PopupSignIn
from POM.users import Hs01
from POM.my_profile import MyProfile
from POM.subscribe_page import PageSubscribe
from POM.asserts import AssertForTest001
from POM.refresh import Refresh


@allure.feature("Авторизация и покупка ЕГЭ")
@allure.story("Авторизация, покупка ЕГЭ тариф Самостоятельный 1 месяц вкл АП")
class LoginAndBuyEgeCourseOneMonth(OpenTilda):
    def test_buy_ege_course(self):
        driver = self.driver
        step_tilda = TildaPage(driver)
        step_enter = PopupSignIn(driver)
        step_user = Hs01(driver)
        step_go_to_profile = UrlHomeSchool(driver)
        step_profile = MyProfile(driver)
        step_buy = PageSubscribe(driver)
        step_assert = AssertForTest001(driver)
        step_refresh = Refresh(driver)

        step_tilda.click_login_button()
        step_user.enter_email(user_name="hs01@yopmail.com")
        step_user.enter_password(password="123456")
        step_enter.click_button_login()
        step_go_to_profile.go_to_my_profile()
        step_profile.click_button_pay_other_classes()
        step_buy.click_button_see_tab_one_ege_curse()
        step_buy.choose_period_one_month_in_ege()
        step_buy.click_button_pay_ege_independent()
        step_assert.price_amount_displayed_in_demo_kassa_ege_hs01()
        step_assert.not_display_select_payment_types()
        step_buy.enter_data_card()
        step_go_to_profile.go_to_my_profile()
        time.sleep(5)
        step_refresh.refresh()
        step_assert.check_text_in_widget_my_ege()
