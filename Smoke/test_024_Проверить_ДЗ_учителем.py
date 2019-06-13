import allure
import pytest

from POM.asserts import AssertForTest024
from POM.setup import StartSchoolClassMethod
from POM.school_page import FormSignIn
from POM.users import Teacher
from POM.teacher import StepTeacher


@pytest.mark.flaky(reruns=1, reruns_delay=1)
@allure.feature("Проверка ДЗ учителем")
@allure.story("Авторизаваться учителем, поставить оценку 4 за ДЗ")
class LoginTeacherAndCheckHomeWorks(StartSchoolClassMethod):
    def test_home_works(self):
        driver = self.driver
        step_enter = FormSignIn(driver)
        step_user = Teacher(driver)
        step_teacher = StepTeacher(driver)
        step_assert = AssertForTest024(driver)

        with allure.step("В поле email и password ввести teacher-test/teacher-test"):
            step_user.enter_email(user_name="teacher-test")
            step_user.enter_password(password="teacher-test")
        with allure.step("Нажать на кнопку Авторизоваться"):
            step_enter.click_button_login_teacher()
        with allure.step("Учителем ввести в поле поиска П hs02@yopmail.com"):
            step_teacher.search_user(user_name="hs02@yopmail.com")
        with allure.step("Учителем нажать на кнопку Показать"):
            step_teacher.click_button_show()
        with allure.step("Проверить в списке ДЗ отображения только одного ДЗ"):
            step_assert.check_one_homework_in_list()
        with allure.step("Нажать на кнопку Проверить"):
            step_teacher.click_button_check()
        with allure.step("Нажать на селект выбора оценки"):
            step_teacher.open_select()
        with allure.step("Выбрать оценку 4"):
            step_teacher.enter_bal_5()
        with allure.step("Нажать на кнопку Сохранить"):
            step_teacher.click_button_save()
        with allure.step("После проставления оценки отображается оценка 4 и ФИО учителя"):
            step_assert.check_bal_and_teacher()
