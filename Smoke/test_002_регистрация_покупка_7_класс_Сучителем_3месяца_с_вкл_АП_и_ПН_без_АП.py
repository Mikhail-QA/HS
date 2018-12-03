import allure
import time

from POM.url import UrlHomeSchool
from POM.setup import StartSchoolClassMethod
from POM.school_page import SchoolPage
from POM.school_page import FormRegistration
from POM.users import Hs02
from POM.delete_popup import DeleteModalPopup
from POM.my_profile import MyProfile
from POM.subscribe_page import PageSubscribe
from POM.asserts import AssertForTest002
from POM.refresh import Refresh


@allure.feature("Регистрация и покупка курса")
@allure.story("Регистрация, покупка 7 класс тариф Сучителем, период 3 месяц с вкл АП + ПН без АП")
class CreateAccountAndBuyLearningThreeMonth(StartSchoolClassMethod):
    def test_buy_learning_per_three_month(self):
        driver = self.driver
        step_school = SchoolPage(driver)
        step_reg = FormRegistration(driver)
        step_user = Hs02(driver)
        step_delete = DeleteModalPopup(driver)
        step_go_to_profile = UrlHomeSchool(driver)
        step_profile = MyProfile(driver)
        step_buy = PageSubscribe(driver)
        step_assert = AssertForTest002(driver)
        step_refresh = Refresh(driver)

        with allure.step("На странице /school в форме нажать на кнопку Зарегистрироваться"):
            step_school.go_to_popup_registration()
        with allure.step("В поле email и password ввести hs02@yopmail.com/123456"):
            step_user.reg_email(user_name="hs02@yopmail.com")
            step_user.reg_password(password="123456")
        with allure.step("Нажать на кнопку Зарегистрироваться"):
            step_reg.click_sign_up()
        with allure.step("Перейти в Личный кабинет"):
            step_go_to_profile.go_to_my_profile()
        with allure.step("Удалить попап подтверждения телефона"):
            step_delete.delete_popup_mobile()
        with allure.step("Ввести номер телефона"):
            step_profile.input_number_mobile()
        with allure.step("Нажать на кнопку Сохранить"):
            step_profile.click_button_save_changes()
        with allure.step("Нажать на кнопку Оплатить доступ"):
            step_profile.click_button_pay_for_access()
        # with allure.step("Выбрать 7 класс"):
        #     step_buy.select_six_class()
        # with allure.step("Выбрать период 3 месяц"):
        #     step_buy.choose_period_three_month()
        # with allure.step("Выбрать тарифа с Учителем"):
        #     step_buy.choose_tariff_with_the_teacher()
        with allure.step("Включить ПН"):
            step_buy.selected_service_personal_mentor()
        with allure.step(
                "В блоке № 5 отображается текст Класс: 7, Формат обучения: «С учителем», Дата Услуга «Персональный наставник»: включена, Сумма к оплате: 13 800 руб."):
            step_assert.check_text_in_tab_5()
        with allure.step("Нажать на кнопку Оплатить обучение"):
            step_buy.click_button_pay_school()
        with allure.step("На странице ЯК сумма оплаты соответствует выбранному тарифу 13 800 руб"):
            step_assert.check_text_in_demo_kassa()
        with allure.step("На странице ЯК ввести данные карты"):
            step_buy.enter_data_card()
        with allure.step("Вернуться в Мой профиль по пряммой ссылке"):
            step_go_to_profile.go_to_my_profile()
            time.sleep(40)
        with allure.step("Обновить страницу"):
            step_refresh.refresh()
        with allure.step("В ЛК проверить соответствия купленному курсу"):
            step_assert.check_text_in_widget_my_school()
