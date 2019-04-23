import allure
import pytest

from POM.popup_auth_and_reg import PopupSignIn
from POM.setup import OpenTilda
from POM.tilda_page import TildaPage
from POM.users import Hs02
from POM.url import UrlHomeSchool
from POM.lesson_page import LessonPage
from POM.TT import Exercise
from POM.asserts import AssertForTest022


@pytest.mark.flaky(reruns=1, reruns_delay=1)
@allure.feature("Тренажер")
@allure.story("Авторизоваться, Пройти Тренажер")
class PassTrainer(OpenTilda):
    def test_trainer_passed(self):
        driver = self.driver
        step_tilda = TildaPage(driver)
        step_enter = PopupSignIn(driver)
        step_user = Hs02(driver)
        url_go = UrlHomeSchool(driver)
        steps_test = LessonPage(driver)
        ask_trainer = Exercise(driver)
        assert_step = AssertForTest022(driver)

        with allure.step("На TILDA нажать на кнопку Войти"):
            step_tilda.click_login_button()
        with allure.step("В поле email и password ввести hs02@yopmail.com/123456"):
            step_user.enter_email(user_name="hs02@yopmail.com")
            step_user.enter_password(password="123456")
        with allure.step("Нажать на кнопку Авторизоваться"):
            step_enter.click_button_login()
        with allure.step("Перейти на урок"):
            url_go.go_to_lesson_tab_trainer_iu()
        with allure.step("В Тренажере нажать на кнопку Пройти"):
            steps_test.go_trainer()
        with allure.step("Отвечать на вопросы в Тренажере"):
            ask_trainer.test()
        with allure.step("В финальном поп-апе нажать на кнопку Завершить"):
            ask_trainer.click_button_finish()
        with allure.step("После пройденного Тренажёра название кнопки Пройти поменялась на Повторить"):
            assert_step.check_button_finish_trainer()
