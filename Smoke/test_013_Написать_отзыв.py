import allure
from POM.setup import OpenTilda
from POM.tilda_page import TildaPage
from POM.popup_auth_and_reg import PopupSignIn
from POM.users import Hs02
from POM.schedule_page import SchedulePage
from POM.asserts import AssertForTest013


@allure.feature("Страница расписания")
@allure.story("Авторизоваться, Отправить отзыв")
class LoginAndWrittenReview(OpenTilda):
    def test_written_review(self):
        driver = self.driver
        step_tilda = TildaPage(driver)
        step_enter = PopupSignIn(driver)
        step_user = Hs02(driver)
        step_assert = AssertForTest013(driver)
        step_schedule = SchedulePage(driver)

        step_tilda.click_login_button()
        step_user.enter_email(user_name="hs02@yopmail.com")
        step_user.enter_password(password="123456")
        step_enter.click_button_login()
        step_schedule.click_button_review_block()
        step_schedule.written_text_in_review_block()
        step_schedule.click_button_send_text_review()
        step_assert.check_popup_thanks_for_the_feedback()
        step_schedule.click_button_close_popup_feedback()
        step_assert.popup_thanks_for_the_feedback_not_display()
