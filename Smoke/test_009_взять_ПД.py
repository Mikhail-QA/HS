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
        step_school.click_button_to_start()
        step_user.reg_email(user_name="hs04@yopmail.com")
        step_user.reg_password(password="123456")
        step_user.reg_mobile(number="+7123456")
        step_school.click_sign_up()
        step_take_pd.select_class_10()
        step_take_pd.click_button_see_schedule_page()
        step_go_to_profile.go_to_my_profile()
        step_assert.check_text_in_widget_my_school()
