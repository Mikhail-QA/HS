import allure
from POM.setup import OpenTilda
from POM.tilda_page import TildaPage
from POM.popup_auth_and_reg import PopupSignIn
from POM.users import Hs02
from POM.schedule_page import SchedulePage
from POM.asserts import AssertForTest016


@allure.feature("Страница расписания")
@allure.story("Авторизоваться, Перейти в Ленту")
class LoginAndGoToFeed(OpenTilda):
    def test_go_feed(self):
        driver = self.driver
        step_tilda = TildaPage(driver)
        step_enter = PopupSignIn(driver)
        step_user = Hs02(driver)
        step_assert = AssertForTest016(driver)
        step_schedule = SchedulePage(driver)

        step_tilda.click_login_button()
        step_user.enter_email(user_name="hs02@yopmail.com")
        step_user.enter_password(password="123456")
        step_enter.click_button_login()
        step_schedule.go_to_feed()
        step_assert.check_text_all_page()
        step_assert.check_url()
