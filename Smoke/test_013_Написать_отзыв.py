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

        with allure.step("На TILDA нажать на кнопку Войти"):
            step_tilda.click_login_button()
        with allure.step("В поле email и password ввести hs02@yopmail.com/123456"):
            step_user.enter_email(user_name="hs02@yopmail.com")
            step_user.enter_password(password="123456")
        with allure.step("Нажать на кнопку Авторизоваться"):
            step_enter.click_button_login()
        with allure.step("Нажать на кнопку Оставить отзыв"):
            step_schedule.click_button_review_block()
        with allure.step("В поп-апе написать сообщение 北京位於華北平原的西北边缘"):
            step_schedule.written_text_in_review_block()
        with allure.step("В поп-апе нажать на кнопку Отправить"):
            step_schedule.click_button_send_text_review()
        with allure.step(
                "После отправки отзыва появляется попап Спасибо за отзыв"):
            step_assert.check_popup_thanks_for_the_feedback()
        with allure.step("В поп-апе нажать на кнопку Закрыть"):
            step_schedule.click_button_close_popup_feedback()
        with allure.step("Попап Спасибо за отзыв не отображается на странице"):
            step_assert.popup_thanks_for_the_feedback_not_display()

