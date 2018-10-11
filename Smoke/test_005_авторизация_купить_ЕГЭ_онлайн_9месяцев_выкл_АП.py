import allure
from POM.setup import StartTildaClassMethod
from POM.url import UrlHomeSchool
from POM.tilda_page import TildaPage
from POM.popup_auth_and_reg import PopupSignIn
from POM.users import Hs02
from POM.my_profile import MyProfile
from POM.subscribe_page import PageSubscribe
from POM.asserts import AssertForTest002
from POM.refresh import Refresh


@allure.feature("Авторизация и покупка ЕГЭ")
@allure.story("Авторизация, покупка ЕГЭ тариф Онлайн 9 месяцев выкл АП")
class LoginBuyEgeCourseNineMonth(StartTildaClassMethod):
    def test_buy_ege_course(self):
        driver = self.driver
        step_tilda = TildaPage(driver)
        step_enter = PopupSignIn(driver)
        step_user = Hs02(driver)
        step_go_to_profile = UrlHomeSchool(driver)
        step_profile = MyProfile(driver)
        step_buy = PageSubscribe(driver)
        step_assert = AssertForTest002(driver)
        step_refresh = Refresh(driver)

        with allure.step("На TILDA нажать на кнопку Войти"):
            step_tilda.click_button_enter()
        with allure.step("В поле email и password ввести hs02@yopmail.com/123456"):
            step_user.enter_email(user_name="hs02@yopmail.com")
            step_user.enter_password(password="123456")
        with allure.step("Нажать на кнопку Авторизоваться"):
            step_enter.click_button_login()
        with allure.step("Перейти в Личный кабинет"):
            step_go_to_profile.go_to_my_profile()
        with allure.step("Нажать на кнопку Оплатить другие классы"):
            step_profile.click_button_pay_other_classes()
        with allure.step("Нажать на кнопку Профильный курс подготовки к ЕГЭ по математике"):
            step_buy.click_button_see_tab_one_ege_curse()
        with allure.step("Выбрать период 9 месяцев"):
            step_buy.choose_period_nine_month_in_ege()
        with allure.step("Выключить АП"):
            step_buy.click_off_button_auto_payments_in_ege()
        with allure.step("Нажать на кнопку Оплатить"):
            step_buy.click_button_pay_ege_online()
        with allure.step("На странице ЯК сумма оплаты соответствует выбранному тарифу 6300 руб"):
            step_assert.check_text_in_demo_kassa_ege_hs02()
        with allure.step("На странице ЯК ввести данные карты"):
            step_buy.enter_data_card()
        with allure.step("Вернуться в Мой профиль по пряммой ссылке"):
            step_go_to_profile.go_to_my_profile()
        with allure.step("Обновить страницу"):
            step_refresh.refresh()
        with allure.step("В ЛК проверить соответствия купленному курсу"):
            step_assert.check_text_in_widget_my_ege()
