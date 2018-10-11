import allure
from POM.url import UrlHomeSchool
from POM.setup import StartSchoolClassMethod
from POM.school_page import SchoolPage
from POM.school_page import FormRegistration
from POM.users import Hs03
from POM.delete_popup import DeleteModalPopup
from POM.my_profile import MyProfile
from POM.subscribe_page import PageSubscribe
from POM.asserts import AssertForTest003
from POM.refresh import Refresh


@allure.feature("Регистрация и покупка курса")
@allure.story("Регистрация, покупка 11 класс тариф Сзачислением, период 9 месяцев с вкл АП + ПН с АП")
class CreateAccountAndBuyLearningNineMonth(StartSchoolClassMethod):
    def test_buy_learning_per_nine_month(self):
        driver = self.driver
        step_school = SchoolPage(driver)
        step_reg = FormRegistration(driver)
        step_user = Hs03(driver)
        step_delete = DeleteModalPopup(driver)
        step_go_to_profile = UrlHomeSchool(driver)
        step_profile = MyProfile(driver)
        step_buy = PageSubscribe(driver)
        step_assert = AssertForTest003(driver)
        step_refresh = Refresh(driver)

        with allure.step("На странице /school в форме нажать на кнопку Зарегистрироваться"):
            step_school.go_to_popup_registration()
        with allure.step("В поле email и password ввести hs03@yopmail.com/123456"):
            step_user.enter_email(user_name="hs03@yopmail.com")
            step_user.enter_password(password="123456")
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
        with allure.step("Выбрать 11 класс"):
            step_buy.select_eleven_class()
        with allure.step("Выбрать период 9 месяцев"):
            step_buy.choose_period_nine_month()
        with allure.step("Выбрать тарифа с Зачислением"):
            step_buy.choose_tariff_with_enrollment()
        with allure.step("Включить ПН"):
            step_buy.selected_service_personal_mentor()
        with allure.step("Включить АП в ПН"):
            step_buy.enable_button_auto_payments_in_personal_mentor()
        with allure.step(
                "В блоке № 5 отображается текст Класс: 11, Формат обучения: «С Зачислением», «Персональный наставник»: включена, Сумма к оплате: 57 600 руб."):
            step_assert.check_text_in_tab_5()
        with allure.step("Нажать на кнопку Оплатить обучение"):
            step_buy.click_button_pay_school()
        with allure.step("На странице ЯК сумма оплаты соответствует выбранному тарифу 57 600 руб"):
            step_assert.check_text_in_demo_kassa()
        with allure.step("На странице ЯК ввести данные карты"):
            step_buy.enter_data_card()
        with allure.step("Вернуться в Мой профиль по пряммой ссылке"):
            step_go_to_profile.go_to_my_profile()
        with allure.step("Обновить страницу"):
            step_refresh.refresh()

            # element = driver.find_element_by_css_selector("#subjects-page-wrapper > div > div.col-sm-3.col-md-3 > div > div.profile-courses > div > div.profile-courses_item_list > div > div.profile-course_body > div.profile-course_curator.ng-scope")
            # print(element.text)
        with allure.step("В ЛК проверить соответствия купленному курсу"):
            step_assert.check_text_in_widget_my_school()
