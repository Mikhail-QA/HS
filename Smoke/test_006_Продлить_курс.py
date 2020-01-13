import allure
import time

from POM.setup import OpenTilda
from POM.url import UrlHomeSchool
from POM.tilda_page import TildaPage
from POM.popup_auth_and_reg import PopupSignIn
from POM.users import Hs02
from POM.my_profile import MyProfile
from POM.subscribe_page import PageSubscribe
from POM.asserts import AssertForTest006
from POM.refresh import Refresh


@allure.feature("Авторизоваться и продлить курс ДШ")
@allure.story("Авторизация, продлить 7 класс, С Учителем, 3 месяца + ПН")
class LoginAndExtendCourseSchool(OpenTilda):
    def test_extend_course_school(self):
        driver = self.driver
        step_tilda = TildaPage(driver)
        step_enter = PopupSignIn(driver)
        step_user = Hs02(driver)
        step_go_to_profile = UrlHomeSchool(driver)
        step_profile = MyProfile(driver)
        step_buy = PageSubscribe(driver)
        step_assert = AssertForTest006(driver)
        step_refresh = Refresh(driver)

        step_tilda.click_login_button()
        step_user.enter_email(user_name="hs02@yopmail.com")
        step_user.enter_password(password="123456")
        step_enter.click_button_login()
        step_go_to_profile.go_to_my_profile()
        step_profile.click_button_extend_access()
        step_buy.extend_service_personal_mentor()
        step_assert.check_text_in_tab_total()
        step_buy.click_button_pay_school()
        step_assert.price_amount_displayed_in_demo_kassa()
        step_buy.enter_data_card()
        step_go_to_profile.go_to_my_profile()
        time.sleep(5)
        step_refresh.refresh()
        step_assert.check_text_in_widget_my_school()
