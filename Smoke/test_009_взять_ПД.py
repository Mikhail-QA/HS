import allure
from POM.url import UrlHomeSchool
from POM.setup import StartLandingClassMethod
from POM.school_page import LandingPage
from POM.users import Hs04
from POM.asserts import AssertForTest009
from POM.schedule_page import SchedulePage


@allure.feature("Взять ПД")
@allure.story("Регистрация, взять ПД 10 класс")
class CreateAccountAndSelectTrialAccess(StartLandingClassMethod):
    def test_select_trial_access(self):
        driver = self.driver
        step_school = LandingPage(driver)
        step_user = Hs04(driver)
        step_go_to_profile = UrlHomeSchool(driver)
        step_assert = AssertForTest009(driver)
        step_take_pd = SchedulePage(driver)
        with allure.step("На странице /landing в форме нажать на кнопку Начать заниматься"):
            step_school.click_button_to_start()
        with allure.step("В поле email и password ввести hs04@yopmail.com/123456"):
            step_user.reg_email(user_name="hs04@yopmail.com")
            step_user.reg_password(password="123456")
            step_user.reg_mobile(number="+7123456")
        with allure.step("Нажать на кнопку Зарегистрироваться"):
            step_school.click_sign_up()
        with allure.step("В поп-апе выбора ПД взять 10 класс"):
            step_take_pd.select_class_10()
        with allure.step("В поп-апе выбора ПД нажать на кнопку Показать распискние"):
            step_take_pd.click_button_see_schedule_page()
        with allure.step("Перейти в ЛК"):
            step_go_to_profile.go_to_my_profile()
        with allure.step("В ЛК проверить соответствие взятому ПД"):
            step_assert.check_text_in_widget_my_school()


