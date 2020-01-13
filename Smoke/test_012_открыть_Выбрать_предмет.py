import allure
import pytest

from POM.setup import OpenTilda
from POM.tilda_page import TildaPage
from POM.popup_auth_and_reg import PopupSignIn
from POM.users import Hs02
from POM.schedule_page import SchedulePage
from POM.asserts import AssertForTest012


@pytest.mark.flaky(reruns=1, reruns_delay=1)
@allure.feature("Страница расписания")
@allure.story("Авторизоваться, открыть Выбрать предметы")
class LoginAndOpenChosenSubject(OpenTilda):
    def test_open_chosen_subject(self):
        driver = self.driver
        step_tilda = TildaPage(driver)
        step_enter = PopupSignIn(driver)
        step_user = Hs02(driver)
        step_assert = AssertForTest012(driver)
        step_schedule = SchedulePage(driver)

        step_tilda.click_login_button()
        step_user.enter_email(user_name="hs02@yopmail.com")
        step_user.enter_password(password="123456")
        step_enter.click_button_login_and_wait_donwload_main_page()
        step_schedule.click_button_chosen_subject()
        step_assert.check_text_in_page_chosen_subject()
