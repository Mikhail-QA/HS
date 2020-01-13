import allure
import pytest

from POM.url import UrlHomeSchool
from POM.lesson_page import LessonPage
from POM.setup import OpenTilda
from POM.tilda_page import TildaPage
from POM.users import Hs02
from POM.popup_auth_and_reg import PopupSignIn
from POM.asserts import AssertForTest023


@pytest.mark.flaky(reruns=1, reruns_delay=1)
@allure.feature("Плеер ИУ")
@allure.story("Проверить воспроизведения видео в плеере ИУ")
class PlayVideoIu(OpenTilda):
    def test_check_player_iu(self):
        driver = self.driver
        get_lesson = UrlHomeSchool(driver)
        steps_video = LessonPage(driver)
        step_tilda = TildaPage(driver)
        step_user = Hs02(driver)
        step_enter = PopupSignIn(driver)
        step_assert = AssertForTest023(driver)

        step_tilda.click_login_button()
        step_user.enter_email(user_name="hs02@yopmail.com")
        step_user.enter_password(password="123456")
        step_enter.click_button_login()
        get_lesson.go_to_lesson_tab_video()
        steps_video.click_play_video_iu()
        step_assert.check_button_play_video()
