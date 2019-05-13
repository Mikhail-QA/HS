import allure
import pytest

from POM.url import UrlHomeSchool
from POM.setup import StartLandingClassMethod
from POM.school_page import LandingPage
# from POM.school_page import FormRegistration
from POM.users import Hs05
# from POM.delete_popup import DeleteModalPopup
# from POM.my_profile import MyProfile
from POM.asserts import AssertForTest017


@pytest.mark.flaky(reruns=1, reruns_delay=1)
@allure.feature("Проверка в ЛК E-mail")
@allure.story("Зарегистрироваться П и проверить указанную почтовы в ЛК")
class CreateAccountAndCheckEmail(StartLandingClassMethod):
    def test_check_email_user(self):
        driver = self.driver
        step_school = LandingPage(driver)
        # step_reg = FormRegistration(driver)
        step_user = Hs05(driver)
        # step_delete = DeleteModalPopup(driver)
        step_go_to_profile = UrlHomeSchool(driver)
        # step_profile = MyProfile(driver)
        step_assert = AssertForTest017(driver)

        with allure.step("На странице /landing в форме нажать на кнопку Начать заниматься"):
            step_school.click_button_to_start()
        with allure.step("В поле email и password ввести hs05@yopmail.com/123456"):
            step_user.reg_email(user_name="hs05@yopmail.com")
            step_user.reg_password(password="123456")
            step_user.reg_mobile(number="+71234567890")
        with allure.step("Нажать на кнопку Зарегистрироваться"):
            step_school.click_sign_up()

        # with allure.step("На странице /school в форме нажать на кнопку Зарегистрироваться"):
        #     step_school.go_to_popup_registration()
        # with allure.step("В поле email и password ввести hs05@yopmail.com/123456"):
        #     step_user.reg_email(user_name="hs05@yopmail.com")
        #     step_user.reg_password(password="123456")
        # with allure.step("Нажать на кнопку Зарегистрироваться"):
        #     step_reg.click_sign_up()
        with allure.step("Перейти в Личный кабинет"):
            step_go_to_profile.go_to_my_profile()
        # with allure.step("Удалить попап подтверждения телефона"):
        #     step_delete.delete_popup_mobile()
        # with allure.step("Ввести номер телефона"):
        #     step_profile.input_number_mobile()
        # with allure.step("Нажать на кнопку Сохранить"):
        #     step_profile.click_button_save_changes()
        with allure.step("В ЛК отображается почта указанная при регистрации"):
            step_assert.check_email_in_user()
