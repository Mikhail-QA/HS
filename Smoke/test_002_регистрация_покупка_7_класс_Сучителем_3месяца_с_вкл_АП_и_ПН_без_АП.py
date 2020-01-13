import allure
from POM.url import UrlHomeSchool
from POM.setup import StartLandingClassMethod
from POM.school_page import LandingPage
from POM.users import Hs02
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

        step_school.click_button_to_start()
        step_user.reg_email(user_name="hs02@yopmail.com")
        step_user.reg_password(password="123456")
        step_user.reg_mobile(number="+712345678")
        step_school.click_sign_up()
        step_go_to_profile.go_to_my_profile()
        step_profile.click_button_pay_for_access()
        step_buy.select_seven_class()
        step_buy.choose_period_three_month()
        step_buy.choose_tariff_with_the_teacher()
        step_buy.selected_service_personal_mentor()
        step_assert.check_text_in_tab_6()
        step_buy.click_button_pay_school()
        step_assert.price_amount_displayed_in_demo_kassa()
        step_assert.not_display_select_payment_types()
        step_buy.enter_data_card()
        step_go_to_profile.go_to_my_profile()
        step_refresh.refresh()
        step_assert.check_text_in_widget_my_school()
        driver.get("https://web-dev01.interneturok.ru/school")
