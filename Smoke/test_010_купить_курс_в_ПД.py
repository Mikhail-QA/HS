import allure
import time

from POM.setup import StartTildaClassMethod
from POM.url import UrlHomeSchool
from POM.tilda_page import TildaPage
from POM.popup_auth_and_reg import PopupSignIn
from POM.users import Hs04
from POM.refresh import Refresh
from POM.asserts import AssertForTest010
from POM.my_profile import MyProfile
from POM.subscribe_page import PageSubscribe


@allure.feature("Купить курс у ПД пользователя")
@allure.story("Авторизация, купить курс через виджет ПД в ЛК")
class LoginAndBuyCourseInTrialAccess(StartTildaClassMethod):
    def test_buy_trial_access(self):
        driver = self.driver
        step_tilda = TildaPage(driver)
        step_enter = PopupSignIn(driver)
        step_user = Hs04(driver)
        step_go_to_profile = UrlHomeSchool(driver)
        step_refresh = Refresh(driver)
        step_assert = AssertForTest010(driver)
        step_profile = MyProfile(driver)
        step_subscribe = PageSubscribe(driver)

        with allure.step("На TILDA нажать на кнопку Войти"):
            step_tilda.click_button_enter()
        with allure.step("В поле email и password ввести hs04@yopmail.com/123456"):
            step_user.enter_email(user_name="hs04@yopmail.com")
            step_user.enter_password(password="123456")
        with allure.step("Нажать на кнопку Авторизоваться"):
            step_enter.click_button_login()
        with allure.step("Перейти в Личный кабинет"):
            step_go_to_profile.go_to_my_profile()
        with allure.step("В 10 классе нажать на кнопку Олпатить обучение"):
            step_profile.click_button_pay_school_in_pd()
        with allure.step(
                "В блоке № 5 отображается текст Класс: 10, Формат обучения: «С учителем», Дата Услуга «Персональный наставник»: выключена, Сумма к оплате: 6 600 руб."):
            step_assert.check_text_in_tab_6()
        with allure.step("На странице оплаты нажать на кнопку Оплатить обучение"):
            step_subscribe.click_button_pay_school()
        with allure.step("На странице ЯК сумма оплаты соответствует выбранному тарифу 6 600 руб"):
            step_assert.price_amount_displayed_in_demo_kassa()
        with allure.step("На странице ЯК ввести данные карты"):
            step_subscribe.enter_data_card()
        with allure.step("Вернуться в Мой профиль по пряммой ссылке"):
            step_go_to_profile.go_to_my_profile()
            time.sleep(5)
        with allure.step("Обновить страницу"):
            step_refresh.refresh()
        with allure.step("В ЛК проверить соответствия купленному курсу"):
            step_assert.check_text_in_widget_my_school()
