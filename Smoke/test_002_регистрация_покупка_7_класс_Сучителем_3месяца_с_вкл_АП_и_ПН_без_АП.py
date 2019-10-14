import allure
import time
from POM.url import UrlHomeSchool
from POM.setup import StartLandingClassMethod
from POM.school_page import LandingPage
from POM.school_page import FormRegistration
from POM.users import Hs02
from POM.delete_popup import DeleteModalPopup
from POM.my_profile import MyProfile
from POM.subscribe_page import PageSubscribe
from POM.asserts import AssertForTest002
from POM.refresh import Refresh


@allure.feature("Регистрация и покупка курса")
@allure.story("Регистрация, покупка 7 класс тариф Сучителем, период 3 месяц с вкл АП + ПН без АП")
class CreateAccountAndBuyLearningThreeMonth(StartLandingClassMethod):
    def test_buy_learning_per_three_month(self):
        driver = self.driver
        step_school = LandingPage(driver)
        step_user = Hs02(driver)
        step_go_to_profile = UrlHomeSchool(driver)
        step_profile = MyProfile(driver)
        step_buy = PageSubscribe(driver)
        step_assert = AssertForTest002(driver)
        step_refresh = Refresh(driver)

        with allure.step("На странице /landing в форме нажать на кнопку Начать заниматься"):
            step_school.click_button_to_start()
        with allure.step("В поле email и password ввести hs02@yopmail.com/123456"):
            step_user.reg_email(user_name="hs02@yopmail.com")
            step_user.reg_password(password="123456")
            step_user.reg_mobile(number="+712345678")
        with allure.step("Нажать на кнопку Зарегистрироваться"):
            step_school.click_sign_up()
        with allure.step("Перейти в Личный кабинет"):
            step_go_to_profile.go_to_my_profile()
        with allure.step("Нажать на кнопку Оплатить доступ"):
            step_profile.click_button_pay_for_access()
        with allure.step("Выбрать 7 класс"):
            step_buy.select_seven_class()
        with allure.step("Выбрать период 3 месяц"):
            step_buy.choose_period_three_month()
        with allure.step("Выбрать тарифа с Учителем"):
            step_buy.choose_tariff_with_the_teacher()
        with allure.step("Включить ПН"):
            step_buy.selected_service_personal_mentor()
        with allure.step(
                "В блоке № 6 отображается текст Класс: 7, Формат обучения: «С учителем», Дата Услуга «Персональный наставник»: включена, Сумма к оплате: 13 800 руб."):
            step_assert.check_text_in_tab_6()
        with allure.step("Нажать на кнопку Оплатить обучение"):
            step_buy.click_button_pay_school()
        with allure.step("На странице ЯК сумма оплаты соответствует выбранному тарифу 13 800 руб"):
            step_assert.price_amount_displayed_in_demo_kassa()
        with allure.step("На странице ЯКассы П с вкл АП отсутствует блок выбора способа оплаты"):
            step_assert.not_display_select_payment_types()
        with allure.step("На странице ЯК ввести данные карты и нажать на кнопку Заплатить"):
            step_buy.enter_data_card()
        with allure.step("Вернуться в Мой профиль по пряммой ссылке"):
            step_go_to_profile.go_to_my_profile()
        with allure.step("Обновить страницу"):
            step_refresh.refresh()
        with allure.step("В ЛК проверить соответствия купленному курсу"):
            step_assert.check_text_in_widget_my_school()
        with allure.step("Перейти на главную страницу"):
            driver.get("https://web-dev01.interneturok.ru/school")
