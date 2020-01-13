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

        step_user.enter_email(user_name="teacher-test")
        step_user.enter_password(password="teacher-test")
        step_enter.click_button_login_teacher()
        step_teacher.search_user(user_name="hs02@yopmail.com")
        step_teacher.click_button_show()
        step_assert.check_one_homework_in_list()
        step_teacher.click_button_check()
        step_teacher.open_select()
        step_teacher.enter_bal_5()
        step_teacher.click_button_save()
        step_assert.check_bal_and_teacher()
