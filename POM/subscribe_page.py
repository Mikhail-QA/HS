import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class PageSubscribe(object):
    def __init__(self, driver):
        self.driver = driver
    @allure.step
    def select_one_class(self):
        self.driver.find_element_by_css_selector(".payment-class-item:nth-child(1)").click()

    @allure.step
    def select_seven_class(self):
        self.driver.find_element_by_css_selector(".payment-class-item:nth-child(7)").click()

    @allure.step
    def select_ten_class(self):
        self.driver.find_element_by_css_selector(".payment-class-item:nth-child(10)").click()
        time.sleep(0.5)

    @allure.step
    def choose_tariff_independent(self):
        self.driver.find_element_by_css_selector(".payment-format-item:nth-child(1)").click()

    @allure.step
    def choose_tariff_with_the_teacher(self):
        self.driver.find_element_by_css_selector(".payment-format-item:nth-child(2)").click()

    @allure.step
    def choose_tariff_with_enrollment(self):
        self.driver.find_element_by_css_selector(".payment-format-item:nth-child(3)").click()

    @allure.step
    def choose_period_one_month(self):
        self.driver.find_element_by_css_selector(".payment-period-item:nth-child(1)").click()

    @allure.step
    def choose_period_three_month(self):
        self.driver.find_element_by_css_selector(".payment-period-item:nth-child(2)").click()

    @allure.step
    def choose_period_nine_month(self):
        self.driver.find_element_by_css_selector(".payment-period-item:nth-child(3)").click()

    @allure.step
    def selected_service_personal_mentor(self):
        self.driver.find_element_by_css_selector("label.mentor__checkbox-label").click()
        time.sleep(1)

    @allure.step
    def extend_service_personal_mentor(self):
        self.driver.find_element_by_css_selector(".payment-item:nth-child(5) div.mentor__checkbox").click()
        time.sleep(1)

    @allure.step
    def click_off_button_auto_payments_in_curse(self):
        self.driver.find_element_by_css_selector(
            "div.payment-item_content_autopay label.payment-autopay_checkbox_label").click()

    @allure.step
    def enable_button_auto_payments_in_personal_mentor(self):
        self.driver.find_element_by_css_selector(
            "div:nth-child(5) > div.payment-item_content_autopay.ng-scope > label").click()

    @allure.step
    def click_button_see_tab_one_ege_curse(self):
        # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.find_element_by_css_selector(
            "div:nth-child(2) > tarif-table-ege > div > button").click()
        time.sleep(2)

    @allure.step
    def choose_period_one_month_in_ege(self):
        self.driver.find_element_by_css_selector(
            "div:nth-child(2) > tarif-table-ege > div > div > div > table > tfoot > tr:nth-child(1) > td:nth-child(2) > div:nth-child(1) > label > i").click()
        time.sleep(1)

    @allure.step
    def choose_period_nine_month_in_ege(self):
        self.driver.find_element_by_css_selector(
            "div:nth-child(2) > div > div > div:nth-child(2) > tarif-table-ege > div > div > div > table > tfoot > tr:nth-child(1) > td:nth-child(3) > div:nth-child(2) > div:nth-child(4) > label > i").click()
        time.sleep(1)

    @allure.step
    def click_off_button_auto_payments_in_ege(self):
        self.driver.find_element_by_css_selector(
            "div:nth-child(2) > tarif-table-ege > div > div > div > table > tfoot > tr:nth-child(3) > td:nth-child(2) > div > label").click()
        time.sleep(1)

    @allure.step
    def click_button_pay_school(self):
        self.driver.find_element_by_class_name("button__w100").click()
        assert (self.driver.find_element_by_css_selector("button.button"))

    @allure.step
    def click_button_pay_ege_independent(self):
        self.driver.find_element_by_css_selector("button.btn.btn-primary.ng-binding").click()

    @allure.step
    def click_button_pay_ege_online(self):
        self.driver.find_element_by_css_selector(
            "div:nth-child(2) > div > div > div:nth-child(2) > tarif-table-ege > div > div > div > table > tfoot > tr:nth-child(2) > td:nth-child(3)").click()

    @allure.step
    def enter_data_card(self):
        self.driver.find_element_by_id("cardNumber").send_keys("5555555555554444")
        self.driver.find_element_by_name("skr_month").send_keys("12")
        self.driver.find_element_by_name("skr_year").send_keys("20")
        self.driver.find_element_by_name("skr_cardCvc").send_keys("000")
        time.sleep(1)
        self.driver.find_element_by_css_selector("button.button").click()
        # WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.ID, 'submitcvc')))
        # self.driver.find_element_by_id("submitcvc").click()
        assert (self.driver.find_element_by_css_selector("i.icon_name_checkmark-green"))


class SubscribeLocatorsStepSix:
    # element_school_years = ".payment-summary_list:nth-child(1) div:nth-child(1)"
    element_grade = ".payment-summary_list:nth-child(1) div:nth-child(1)"
    element_format_in_course = ".payment-summary_list:nth-child(1) div:nth-child(2)"
    element_payment_course = ".payment-summary_list:nth-child(1) div:nth-child(3)"
    element_lock_date_course = ".payment-summary_list:nth-child(1) div:nth-child(4)"
    element_mentor_service_included = ".payment-summary_list:nth-child(1) div:nth-child(5)"
    element_period_mentor = ".payment-summary_list:nth-child(1) div:nth-child(6)"
    element_lock_date_mentor = ".payment-summary_list:nth-child(1) div:nth-child(7)"
    element_payment_summary_price = ".payment-summary_price"
