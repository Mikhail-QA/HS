import time


class PageSubscribe(object):
    def __init__(self, driver):
        self.driver = driver

    def select_one_class(self):
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div[2]/div/div[1]/div[2]/div/div[1]").click()

    def select_six_class(self):
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div[2]/div/div[1]/div[2]/div/div[7]").click()

    def select_eleven_class(self):
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div[2]/div/div[1]/div[2]/div/div[10]").click()
        time.sleep(0.5)

    def choose_tariff_independent(self):
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div[2]/div/div[2]/div[2]/div/div[1]/div[1]").click()

    def choose_tariff_with_the_teacher(self):
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div[2]/div/div[2]/div[2]/div/div[2]/div[1]").click()

    def choose_tariff_with_enrollment(self):
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div[2]/div/div[2]/div[2]/div/div[3]/div[1]").click()

    def choose_period_one_month(self):
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div[2]/div/div[3]/div[2]/div/div[1]").click()

    def choose_period_three_month(self):
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div[2]/div/div[3]/div[2]/div/div[2]").click()

    def choose_period_nine_month(self):
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div[2]/div/div[3]/div[2]/div/div[3]").click()

    def selected_service_personal_mentor(self):
        self.driver.find_element_by_css_selector("label.mentor__checkbox-label").click()
        time.sleep(1)

    def extend_service_personal_mentor(self):
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div/div[5]/div[1]/div[1]/label").click()
        time.sleep(1)

    def click_off_button_auto_payments_in_curse(self):
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div[2]/div/div[3]/div[3]/label").click()

    def enable_button_auto_payments_in_personal_mentor(self):
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div[2]/div/div[4]/div[3]/label").click()

    def click_button_see_tab_one_ege_curse(self):
        # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.find_element_by_css_selector(
            "body > div.page-wrapper.ng-isolate-scope > div > div.container > div.row.ng-scope > div > div.home-school.col-sm-12.no-padding.ng-scope > div:nth-child(2) > div > div > div:nth-child(2) > tarif-table-ege > div > button").click()
        time.sleep(2)

    def choose_period_one_month_in_ege(self):
        self.driver.find_element_by_css_selector(
            "body > div.page-wrapper.ng-isolate-scope > div > div.container > div.row.ng-scope > div > div.home-school.col-sm-12.no-padding.ng-scope > div:nth-child(2) > div > div > div:nth-child(2) > tarif-table-ege > div > div > div > table > tfoot > tr:nth-child(1) > td:nth-child(2) > div:nth-child(1) > label > i").click()
        time.sleep(1)

    def choose_period_nine_month_in_ege(self):
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div[2]/div/div/div[1]/tarif-table-ege/div/div/div/table/tfoot/tr[1]/td[3]/div[2]/div[4]").click()
        time.sleep(1)

    def click_off_button_auto_payments_in_ege(self):
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div[2]/div/div/div[1]/tarif-table-ege/div/div/div/table/tfoot/tr[3]/td[2]/div/label").click()
        time.sleep(1)

    def click_button_pay_school(self):
        self.driver.find_element_by_class_name("button__w100").click()
        time.sleep(61)

    def click_button_pay_ege_independent(self):
        self.driver.find_element_by_css_selector("button.btn.btn-primary.ng-binding").click()
        # time.sleep(40)

    def click_button_pay_ege_online(self):
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div[2]/div/div/div[1]/tarif-table-ege/div/div/div/table/tfoot/tr[2]/td[3]/button").click()
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
