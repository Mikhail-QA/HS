import allure
import pytest

from POM.users import Admin
from POM.school_page import FormSignIn
from POM.setup import StartSchoolClassMethod
from POM.admin_delete_users import AdminDeleteUser


@pytest.mark.flaky(reruns=1, reruns_delay=1)
@allure.feature("Админка")
@allure.story("Удалить пользователей в админке")
class RemovingUsersInAdminPanel(StartSchoolClassMethod):
    def test_000_login_admin(self):
        driver = self.driver
        steps_delete = AdminDeleteUser(driver)
        step_user = Admin(driver)
        step_enter = FormSignIn(driver)

        with allure.step("В поле email и password ввести school.interneturok@yandex.ru/34t3hEOfbTT2k"):
            step_user.enter_email(user_name="school.interneturok@yandex.ru")
            step_user.enter_password(password="34t3hEOfbTT2k")
        with allure.step("Нажать на кнопку Авторизоваться"):
            step_enter.click_button_login_admin()
        with allure.step("Перейти в раздел пользователи"):
            steps_delete.go_to_admin()

    def test_delete_HS1(self):
        driver = self.driver
        steps_delete = AdminDeleteUser(driver)

        with allure.step("Удаляю пользователя hs01@yopmail.com"):
            steps_delete.user_1(pupil_1="hs01@yopmail.com")

    def test_delete_HS2(self):
        driver = self.driver
        steps_delete = AdminDeleteUser(driver)

        with allure.step("Удаляю пользователя hs02@yopmail.com"):
            steps_delete.user_2(pupil_2="hs02@yopmail.com")

    def test_delete_HS3(self):
        driver = self.driver
        steps_delete = AdminDeleteUser(driver)

        with allure.step("Удаляю пользователя hs03@yopmail.com"):
            steps_delete.user_3(pupil_3="hs03@yopmail.com")

    def test_delete_HS4(self):
        driver = self.driver
        steps_delete = AdminDeleteUser(driver)

        with allure.step("Удаляю пользователя hs04@yopmail.com"):
            steps_delete.user_4(pupil_4="hs04@yopmail.com")

    def test_delete_HS5(self):
        driver = self.driver
        steps_delete = AdminDeleteUser(driver)

        with allure.step("Удаляю пользователя hs05@yopmail.com"):
            steps_delete.user_5(pupil_5="hs05@yopmail.com")

    def test_delete_social_user(self):
        driver = self.driver
        steps_delete = AdminDeleteUser(driver)

        with allure.step("Удаляю пользователя gruzd-vikto@rambler.ru"):
            steps_delete.user_6(pupil_6="gruzd-vikto@rambler.ru")
