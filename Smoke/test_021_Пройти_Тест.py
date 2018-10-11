import allure
from POM.popup_auth_and_reg import PopupSignIn
from POM.setup import StartTildaClassMethod
from POM.tilda_page import TildaPage
from POM.users import Hs05
from POM.url import UrlHomeSchool
from POM.lesson_page import LessonPage
from POM.TT import Test
from POM.asserts import AssertForTest021


@allure.feature("Тест")
@allure.story("Авторизоваться, Пройти Тест")
class PassTest(StartTildaClassMethod):
    def test_passed(self):
        driver = self.driver
        step_tilda = TildaPage(driver)
        step_enter = PopupSignIn(driver)
        step_user = Hs05(driver)
        url_go = UrlHomeSchool(driver)
        steps_test = LessonPage(driver)
        ask_test = Test(driver)
        assert_step = AssertForTest021(driver)

        with allure.step("На TILDA нажать на кнопку Войти"):
            step_tilda.click_button_enter()
        with allure.step("В поле email и password ввести hs02@yopmail.com/123456"):
            step_user.enter_email(user_name="hs02@yopmail.com")
            step_user.enter_password(password="123456")
        with allure.step("Нажать на кнопку Авторизоваться"):
            step_enter.click_button_login()
        with allure.step("Перейти на урок"):
            url_go.go_to_lesson_tab_test_iu()
        with allure.step("В Тесте нажать на кнопку Пройти"):
            steps_test.go_test()
        with allure.step("Отвечать на вопросы в тесте"):
            ask_test.start_test()
        with allure.step("В финальном поп-апе нажать на кнопку Завершить"):
            ask_test.click_button_finish()
        with allure.step("После пройденного Теста название кнопки Пройти поменялась на Повторить"):
            assert_step.check_button_finish_test()
