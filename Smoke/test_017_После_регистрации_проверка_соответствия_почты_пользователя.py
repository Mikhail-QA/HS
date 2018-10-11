import allure
from POM.url import UrlHomeSchool
from POM.setup import StartSchoolClassMethod
from POM.school_page import SchoolPage
from POM.school_page import FormRegistration
from POM.users import Hs06
from POM.delete_popup import DeleteModalPopup
from POM.my_profile import MyProfile
from POM.asserts import AssertForTest017


@allure.feature("Проверка в ЛК E-mail")
@allure.story("Зарегистрироваться П и проверить указанную почтовы в ЛК")
class CreateAccountAndCheckEmail(StartSchoolClassMethod):
    def test_check_email_user(self):
        driver = self.driver
        step_school = SchoolPage(driver)
        step_reg = FormRegistration(driver)
        step_user = Hs06(driver)
        step_delete = DeleteModalPopup(driver)
        step_go_to_profile = UrlHomeSchool(driver)
        step_profile = MyProfile(driver)
        step_assert = AssertForTest017(driver)

        with allure.step("На странице /school в форме нажать на кнопку Зарегистрироваться"):
            step_school.go_to_popup_registration()
        with allure.step("В поле email и password ввести hs05@yopmail.com/123456"):
            step_user.reg_email(user_name="hs05@yopmail.com")
            step_user.reg_password(password="123456")
        with allure.step("Нажать на кнопку Зарегистрироваться"):
            step_reg.click_sign_up()
        with allure.step("Перейти в Личный кабинет"):
            step_go_to_profile.go_to_my_profile()
        with allure.step("Удалить попап подтверждения телефона"):
            step_delete.delete_popup_mobile()
        with allure.step("Ввести номер телефона"):
            step_profile.input_number_mobile()
        with allure.step("Нажать на кнопку Сохранить"):
            step_profile.click_button_save_changes()
        with allure.step("В ЛК отображается почта указанная при регистрации"):
            step_assert.check_email_for_user()
