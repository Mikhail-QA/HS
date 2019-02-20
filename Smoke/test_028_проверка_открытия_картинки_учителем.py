import allure
from POM.asserts import AssertForTest028
from POM.setup import StartSchoolClassMethod
from POM.school_page import FormSignIn
from POM.users import Teacher
from POM.teacher import StepTeacher


@allure.feature("Проверка открытия картинки")
@allure.story("Авторизаваться учителем, в ДЗ напроверку открыть картинку")
class LoginTeacherAndCheckImg(StartSchoolClassMethod):
    def test_checking_img(self):
        driver = self.driver
        step_enter = FormSignIn(driver)
        step_user = Teacher(driver)
        step_teacher = StepTeacher(driver)
        step_assert = AssertForTest028(driver)

        with allure.step("В поле email и password ввести teacher-test/teacher-test"):
            step_user.enter_email(user_name="teacher-test")
            step_user.enter_password(password="teacher-test")
        with allure.step("Нажать на кнопку Авторизоваться"):
            step_enter.click_button_login_teacher()
        with allure.step("Учителем ввести в поле поиска П hs02@yopmail.com"):
            step_teacher.search_user(user_name="hs02@yopmail.com")
        with allure.step("В фильтре Статус ДЗ выбрать Проверенные"):
            step_teacher.click_button_filter_checked()
        with allure.step("Учителем нажать на кнопку Показать"):
            step_teacher.click_button_show()
        with allure.step("Нажать на оценку"):
            step_teacher.click_button_ball()
        with allure.step("Нажать на прикриплённую учеником картинку"):
            step_teacher.open_img()
        with allure.step("После нажатия на картинку открывается модальное окно"):
            step_assert.displayed_modal_window()
        with allure.step("В модальном окне отображается картинка"):
            step_assert.visible_img_in_modal_window()
