import allure
import time

from POM.setup import OpenTilda
from POM.url import UrlHomeSchool
from POM.tilda_page import TildaPage
from POM.popup_auth_and_reg import PopupSignIn
from POM.users import Hs04
from POM.refresh import Refresh
from POM.asserts import AssertForTest010
from POM.my_profile import MyProfile
from POM.subscribe_page import PageSubscribe


@allure.feature("Купить курс у ПД пользователя")
@allure.story("Авторизация, купить курс через виджет ПД в ЛК")
class LoginAndBuyCourseInTrialAccess(OpenTilda):
    def test_buy_trial_access(self):
        driver = self.driver
        step_tilda = TildaPage(driver)
        step_enter = PopupSignIn(driver)
        step_user = Hs04(driver)
        step_go_to_profile = UrlHomeSchool(driver)
        step_refresh = Refresh(driver)
        step_assert = AssertForTest010(driver)
        step_profile = MyProfile(driver)
        step_subscribe = PageSubscribe(driver)

        step_tilda.click_login_button()
        step_user.enter_email(user_name="hs04@yopmail.com")
        step_user.enter_password(password="123456")
        step_enter.click_button_login()
        step_go_to_profile.go_to_my_profile()
        step_profile.click_button_pay_school_in_pd()
        step_assert.check_text_in_tab_6()
        step_subscribe.click_button_pay_school()
        step_assert.price_amount_displayed_in_demo_kassa()
        step_subscribe.enter_data_card()
        step_go_to_profile.go_to_my_profile()
        time.sleep(5)
        step_refresh.refresh()
        step_assert.check_text_in_widget_my_school()
