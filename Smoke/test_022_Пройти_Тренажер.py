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

        step_tilda.click_login_button()
        step_user.enter_email(user_name="hs02@yopmail.com")
        step_user.enter_password(password="123456")
        step_enter.click_button_login()
        url_go.go_to_lesson_tab_trainer_iu()
        steps_test.go_trainer()
        ask_trainer.test()
        ask_trainer.click_button_finish()
        assert_step.check_button_finish_trainer()
