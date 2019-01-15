import allure
from POM.setup import StartTildaClassMethod
from POM.tilda_page import TildaPage
from POM.popup_auth_and_reg import PopupSignIn
from POM.users import Hs02
from POM.schedule_page import SchedulePage
from POM.asserts import AssertForTest011


@allure.feature("Страница расписания")
@allure.story("Авторизоваться, проверить переход в Список всех занятий")
class LoginAndGoListAllActivities(StartTildaClassMethod):
    def test_go_list_activities(self):
        driver = self.driver
        step_tilda = TildaPage(driver)
        step_enter = PopupSignIn(driver)
        step_user = Hs02(driver)
        step_assert = AssertForTest011(driver)
        step_list = SchedulePage(driver)

        with allure.step("На TILDA нажать на кнопку Войти"):
            step_tilda.click_button_enter()
        with allure.step("В поле email и password ввести hs02@yopmail.com/123456"):
            step_user.enter_email(user_name="hs02@yopmail.com")
            step_user.enter_password(password="123456")
        with allure.step("Нажать на кнопку Авторизоваться"):
            step_enter.click_button_login()
        with allure.step("Нажать на кнопку Список всех занятий"):
            step_list.click_button_list_all_activities()
        with allure.step(
                "Проверить отображение текста Выбрать предметы Список всех занятий Подробное расписание на неделю"):
            step_assert.check_text_in_page_list_all_activities()
