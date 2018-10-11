import allure
from POM.setup import StartTildaClassMethod
from POM.tilda_page import TildaPage
from POM.popup_auth_and_reg import PopupSignIn
from POM.users import Hs05
from POM.schedule_page import SchedulePage
from POM.asserts import AssertForTest012


@allure.feature("Страница расписания")
@allure.story("Авторизоваться, открыть Выбрать предметы")
class LoginAndOpenChosenSubject(StartTildaClassMethod):
    def test_open_chosen_subject(self):
        driver = self.driver
        step_tilda = TildaPage(driver)
        step_enter = PopupSignIn(driver)
        step_user = Hs05(driver)
        step_assert = AssertForTest012(driver)
        step_schedule = SchedulePage(driver)

        with allure.step("На TILDA нажать на кнопку Войти"):
            step_tilda.click_button_enter()
        with allure.step("В поле email и password ввести hs02@yopmail.com/123456"):
            step_user.enter_email(user_name="hs02@yopmail.com")
            step_user.enter_password(password="123456")
        with allure.step("Нажать на кнопку Авторизоваться"):
            step_enter.click_button_login()
        with allure.step("Нажать на кнопку Выбрать предметы"):
            step_schedule.click_button_chosen_subject()
        with allure.step(
                "Проверить отображение списка предметов в открытом списке Выбрать Предметы"):
            step_assert.check_text_in_page_chosen_subject()
