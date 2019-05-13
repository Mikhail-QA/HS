import allure
import pytest

from POM.setup import OpenTilda
from POM.tilda_page import TildaPage
from POM.popup_auth_and_reg import PopupSignIn
from POM.users import Hs02
from POM.schedule_page import SchedulePage
from POM.asserts import AssertForTest015


@pytest.mark.flaky(reruns=1, reruns_delay=1)
@allure.feature("Страница расписания")
@allure.story("Авторизоваться, Перейти на Журнала успеваемости")
class LoginAndGoToAcademicJournal(OpenTilda):
    def test_go_journal(self):
        driver = self.driver
        step_tilda = TildaPage(driver)
        step_enter = PopupSignIn(driver)
        step_user = Hs02(driver)
        step_assert = AssertForTest015(driver)
        step_schedule = SchedulePage(driver)

        with allure.step("На TILDA нажать на кнопку Войти"):
            step_tilda.click_login_button()
        with allure.step("В поле email и password ввести hs02@yopmail.com/123456"):
            step_user.enter_email(user_name="hs02@yopmail.com")
            step_user.enter_password(password="123456")
        with allure.step("Нажать на кнопку Авторизоваться"):
            step_enter.click_button_login()
        with allure.step("Перейти на страницу Журнала успеваемости"):
            step_schedule.go_to_academic_journal()
        with allure.step("На странице Журнала успеваемости отоброжается текст I четверть"):
            step_assert.check_text_all_page()
        with allure.step("Сверить url со ссылкой на которой находится П"):
            step_assert.check_url()
