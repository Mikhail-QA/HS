import time


class PageSubscribe(object):
    def __init__(self, driver):
        self.driver = driver

    def select_one_class(self):
        self.driver.find_element_by_css_selector(".payment-class-item:nth-child(1)").click()

    def select_seven_class(self):
        self.driver.find_element_by_css_selector(".payment-class-item:nth-child(7)").click()

    def select_ten_class(self):
        self.driver.find_element_by_css_selector(".payment-class-item:nth-child(10)").click()
        time.sleep(0.5)

    def choose_tariff_independent(self):
        self.driver.find_element_by_css_selector(".payment-format-item:nth-child(1)").click()

    def choose_tariff_with_the_teacher(self):
        self.driver.find_element_by_css_selector(".payment-format-item:nth-child(2)").click()

    def choose_tariff_with_enrollment(self):
        self.driver.find_element_by_css_selector(".payment-format-item:nth-child(3)").click()

    def choose_period_one_month(self):
        self.driver.find_element_by_css_selector(".payment-period-item:nth-child(1)").click()

    def choose_period_three_month(self):
        self.driver.find_element_by_css_selector(".payment-period-item:nth-child(2)").click()

    def choose_period_nine_month(self):
        self.driver.find_element_by_css_selector(".payment-period-item:nth-child(3)").click()

    def selected_service_personal_mentor(self):
        self.driver.find_element_by_css_selector("label.mentor__checkbox-label").click()
        time.sleep(1)

    def extend_service_personal_mentor(self):
        self.driver.find_element_by_css_selector(".payment-item:nth-child(5) div.mentor__checkbox").click()
        time.sleep(1)

    def click_off_button_auto_payments_in_curse(self):
        self.driver.find_element_by_css_selector(
            "div:nth-child(3) > div.payment-item_content_autopay.ng-scope > label").click()

    def enable_button_auto_payments_in_personal_mentor(self):
        self.driver.find_element_by_css_selector(
            "div:nth-child(4) > div.payment-item_content_autopay.ng-scope > label").click()

    def click_button_see_tab_one_ege_curse(self):
        # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.find_element_by_css_selector(
            "div:nth-child(2) > tarif-table-ege > div > button").click()
        time.sleep(2)

    def choose_period_one_month_in_ege(self):
        self.driver.find_element_by_css_selector(
            "div:nth-child(2) > tarif-table-ege > div > div > div > table > tfoot > tr:nth-child(1) > td:nth-child(2) > div:nth-child(1) > label > i").click()
        time.sleep(1)

    def choose_period_nine_month_in_ege(self):
        self.driver.find_element_by_css_selector(
            "div:nth-child(2) > div > div > div:nth-child(2) > tarif-table-ege > div > div > div > table > tfoot > tr:nth-child(1) > td:nth-child(3) > div:nth-child(2) > div:nth-child(4) > label > i").click()
        time.sleep(1)

    def click_off_button_auto_payments_in_ege(self):
        self.driver.find_element_by_css_selector(
            "div:nth-child(2) > tarif-table-ege > div > div > div > table > tfoot > tr:nth-child(3) > td:nth-child(2) > div > label").click()
        time.sleep(1)

    def click_button_pay_school(self):
        self.driver.find_element_by_class_name("button__w100").click()
        time.sleep(61)

    def click_button_pay_ege_independent(self):
        self.driver.find_element_by_css_selector("button.btn.btn-primary.ng-binding").click()
        # time.sleep(40)

    def click_button_pay_ege_online(self):
        self.driver.find_element_by_css_selector(
            "div:nth-child(2) > div > div > div:nth-child(2) > tarif-table-ege > div > div > div > table > tfoot > tr:nth-child(2) > td:nth-child(3)").click()
        # time.sleep(40)

    def enter_data_card(self):
        self.driver.find_element_by_id("cardNumber").send_keys("4444444444444448")
        self.driver.find_element_by_name("skr_month").send_keys("12")
        self.driver.find_element_by_name("skr_year").send_keys("20")
        self.driver.find_element_by_name("skr_cardCvc").send_keys("000")
        time.sleep(3)
        self.driver.find_element_by_class_name("payment-contract__pay-button").click()
        assert (self.driver.find_element_by_css_selector("h1.title.title_last_yes"))
        time.sleep(3)
