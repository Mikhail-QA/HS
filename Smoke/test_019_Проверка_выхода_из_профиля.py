import allure
import pytest

from POM.delete_popup import DeleteModalPopup
from POM.setup import OpenTilda
from POM.tilda_page import TildaPage
from POM.popup_auth_and_reg import PopupSignIn
from POM.users import Hs05
from POM.asserts import AssertForTest019
from POM.schedule_page import SchedulePage


@pytest.mark.flaky(reruns=1, reruns_delay=1)
@allure.feature("Выход из профиля")
@allure.story("Авторизоваться П и выйти из аккаунта кнопкой выход")
class LoginAndExitProfile(OpenTilda):
    def test_exit_profile(self):
        driver = self.driver
        step_tilda = TildaPage(driver)
        step_enter = PopupSignIn(driver)
        step_user = Hs05(driver)
        step_schedule = SchedulePage(driver)
        step_assert = AssertForTest019(driver)
        step_delete = DeleteModalPopup(driver)

        with allure.step("На TILDA нажать на кнопку Войти"):
            step_tilda.click_login_button()
        with allure.step("В поле email и password ввести hs05@yopmail.com/123456"):
            step_user.enter_email(user_name="hs05@yopmail.com")
            step_user.enter_password(password="123456")
        with allure.step("Нажать на кнопку Авторизоваться"):
            step_enter.click_button_login()
            # with allure.step("Удалить попап подтверждения телефона"):
            #     step_delete.delete_popup_mobile()
        with allure.step("Удалить попап ПД"):
            step_delete.delete_popup_trial()
        with allure.step("Нажать на кнопку Мой профиль"):
            step_schedule.click_button_my_profile()
        with allure.step("Нажать на кнопку Выход"):
            step_schedule.click_text_exit()
        with allure.step("После выхода отображается кнопка Войти и поменялась ссылка в URL"):
            step_assert.check_button_name_enter()
            step_assert.check_url()
