import allure
import pytest
from POM.asserts import AssertForTest028
from POM.setup import StartSchoolClassMethod
from POM.school_page import FormSignIn
from POM.users import Teacher
from POM.teacher import StepTeacher


@pytest.mark.flaky(reruns=1, reruns_delay=1)
@allure.feature("Проверка открытия картинки")
@allure.story("Авторизаваться учителем, в ДЗ напроверку открыть картинку")
class LoginTeacherAndCheckImg(StartSchoolClassMethod):
    def test_checking_img(self):
        driver = self.driver
        step_enter = FormSignIn(driver)
        step_user = Teacher(driver)
        step_teacher = StepTeacher(driver)
        step_assert = AssertForTest028(driver)

        step_user.enter_email(user_name="teacher-test")
        step_user.enter_password(password="teacher-test")
        step_enter.click_button_login_teacher()
        step_teacher.search_user(user_name="hs02@yopmail.com")
        step_teacher.click_button_filter_all()
        step_teacher.click_button_show()
        step_assert.check_one_homework_in_list()
        step_teacher.click_button_ball()
        step_teacher.open_img()
        step_assert.displayed_modal_window()
        step_assert.visible_img_in_modal_window()
