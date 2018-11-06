import allure
from POM.asserts import AssertForTest024
from POM.popup_auth_and_reg import PopupSignIn
from POM.setup import StartSchoolClassMethod
from POM.school_page import FormSignIn
from POM.tilda_page import TildaPage
from POM.users import Teacher, Hs05
from POM.teacher import StepTeacher
from POM.url import UrlHomeSchool


@allure.feature("Проверка ДЗ учителем")
@allure.story("Авторизаваться учителем, поставить оценку 4 за ДЗ")
class LoginTeacherAndCheckHomeWorks(StartSchoolClassMethod):
    def test_buy_ege_course(self):
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
            driver.delete_all_cookies()

    def test_check_ball_for_student(self):
        driver = self.driver
        step_tilda = TildaPage(driver)
        step_enter = PopupSignIn(driver)
        step_user = Hs05(driver)
        step_url = UrlHomeSchool(driver)
        step_assert = AssertForTest024(driver)

        with allure.step("Перейти на Tilda"):
            step_url.go_to_tilda_landing()
        with allure.step("На TILDA нажать на кнопку Войти"):
            step_tilda.click_button_enter()
        with allure.step("В поле email и password ввести hs02@yopmail.com/123456"):
            step_user.enter_email(user_name="hs02@yopmail.com")
            step_user.enter_password(password="123456")
        with allure.step("Нажать на кнопку Авторизоваться"):
            step_enter.click_button_login()
        with allure.step("Перейти на страницу урока"):
            step_url.go_to_lesson_page_tab_homework()
        with allure.step("Проверить на странице урока во вкладке ДЗ отображение оценки Итоговая оценка: 4 / Хорошо "):
            step_assert.check_bal_in_homweork_for_lesson_page()
