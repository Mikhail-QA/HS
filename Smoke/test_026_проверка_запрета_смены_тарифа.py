import allure
from POM.setup import OpenTilda
from POM.url import UrlHomeSchool
from POM.tilda_page import TildaPage
from POM.popup_auth_and_reg import PopupSignIn
from POM.users import Hs04
from POM.asserts import AssertForTest026
from POM.subscribe_page import PageSubscribe


@allure.feature("Убедиться в запрете самостоятельной смены тарифа")
@allure.story("Авторизация, на странице оплаты выбрать другой тариф курса")
class LoginAndChangeRateCourse(OpenTilda):
    def test_buy_trial_access(self):
        driver = self.driver
        step_tilda = TildaPage(driver)
        step_enter = PopupSignIn(driver)
        step_user = Hs04(driver)
        step_go_to_profile = UrlHomeSchool(driver)
        step_assert = AssertForTest026(driver)
        step_subscribe = PageSubscribe(driver)

        with allure.step("На TILDA нажать на кнопку Войти"):
            step_tilda.click_login_button()
        with allure.step("В поле email и password ввести hs04@yopmail.com/123456"):
            step_user.enter_email(user_name="hs04@yopmail.com")
            step_user.enter_password(password="123456")
        with allure.step("Нажать на кнопку Авторизоваться"):
            step_enter.click_button_login()
        with allure.step("Перейти на страницу оплаты"):
            step_go_to_profile.go_to_page_subjects_subscribe()
        with allure.step("Выбрать тариф С зачислением"):
            step_subscribe.choose_tariff_with_enrollment()
        with allure.step("В блоке №5 появился текст Чтобы оплатить другой формат обучения...."):
            step_assert.check_text_block_tariff_change()
        with allure.step("В блоке №5 отсутствует кнопка Продлить обучение"):
            step_assert.check_button_pay_abonement()
