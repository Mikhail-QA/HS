import allure
from POM.setup import StartTildaClassMethod
from POM.url import UrlHomeSchool
from POM.tilda_page import TildaPage
from POM.popup_auth_and_reg import PopupSignIn
from POM.users import Hs02
from POM.my_profile import MyProfile
from POM.subscribe_page import PageSubscribe
from POM.asserts import AssertForTest006
from POM.refresh import Refresh


@allure.feature("Авторизоваться и продлить курс ДШ")
@allure.story("Авторизация, продлить 7 класс, С Учителем, 3 месяца, вкл АП без ПН")
class LoginAndExtendCourseSchool(StartTildaClassMethod):
    def test_extend_course_school(self):
        driver = self.driver
        step_tilda = TildaPage(driver)
        step_enter = PopupSignIn(driver)
        step_user = Hs02(driver)
        step_go_to_profile = UrlHomeSchool(driver)
        step_profile = MyProfile(driver)
        step_buy = PageSubscribe(driver)
        step_assert = AssertForTest006(driver)
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
        with allure.step("Нажать на кнопку Продлить обучение"):
            step_profile.click_button_extend_access()
        with allure.step("Включить ПН"):
            step_buy.selected_service_personal_mentor()
        with allure.step(
                "На странице продления отображается текст: Класс: 7 класс, Формат обучения: С учителем, Продление обучения на: 3 месяца, Сумма к оплате: 13 800 руб."):
            step_assert.check_text_in_tab_total()
        with allure.step("Нажать на кнопку Оплатить"):
            step_buy.click_button_pay_school()
        with allure.step("На странице ЯК сумма оплаты соответствует выбранному тарифу 13 800 руб"):
            step_assert.check_text_in_demo_kassa()
        with allure.step("На странице ЯК ввести данные карты"):
            step_buy.enter_data_card()
        with allure.step("Вернуться в Мой профиль по пряммой ссылке"):
            step_go_to_profile.go_to_my_profile()
        with allure.step("Обновить страницу"):
            step_refresh.refresh()
        with allure.step("В ЛК проверить соответствия купленному курсу"):
            step_assert.check_text_in_widget_my_school()
