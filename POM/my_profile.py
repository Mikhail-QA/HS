import time


class MyProfile(object):
    def __init__(self, driver):
        self.driver = driver

    def input_number_mobile(self):
        self.driver.find_element_by_xpath(
            "//*[@id='subjects-page-wrapper']/div/div[2]/form/div[1]/div/div[1]/user-personal-info/div[6]/div/input").send_keys(
            "+73123213")

    def click_button_save_changes(self):
        self.driver.find_element_by_xpath(
            "//*[@id='subjects-page-wrapper']/div/div[2]/form/div[2]/button").click()

    def click_button_extend_access(self):
        self.driver.find_element_by_css_selector("button.btn.btn-primary.ng-scope").click()
        assert (u"Домашняя школа", self.driver.find_element_by_css_selector("h2.courses-prepare__payment-title").text)
        time.sleep(1)

    def click_button_pay_for_access(self):
        self.driver.find_element_by_css_selector(
            "#subjects-page-wrapper > div > div.col-sm-3.col-md-3 > div > div:nth-child(3) > div > a").click()
        assert (u"Домашняя школа", self.driver.find_element_by_css_selector("h2.courses-prepare__payment-title").text)
        time.sleep(2)

    def click_button_pay_other_classes(self):
        self.driver.find_element_by_css_selector(
            "#subjects-page-wrapper > div > div.col-sm-3.col-md-3 > div > div.profile-courses > div > a").click()
        assert (u"Домашняя школа", self.driver.find_element_by_css_selector("h2.courses-prepare__payment-title").text)

    def click_button_pay_school_in_pd(self):
        self.driver.find_element_by_css_selector("button.btn.btn-success.ng-scope").click()
        assert (u"Домашняя школа", self.driver.find_element_by_css_selector("h2.courses-prepare__payment-title").text)


class OffAutoPayInSchool(object):
    def __init__(self, driver):
        self.driver = driver

    def click_off_auto_pay_in_widget(self):
        self.driver.find_element_by_xpath(
            "//*[@id='subjects-page-wrapper']/div/div[1]/div/div[1]/div/div[2]/div/div[2]/div[5]/label/span[1]").click()

    def click_off_auto_pay_in_tooltip(self):
        self.driver.find_element_by_css_selector("button.btn-autopay").click()

    def click_off_auto_pay_in_popup(self):
        self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[3]/button[2]").click()


class OffAutoPayInPersonalMentor(object):
    def __init__(self, driver):
        self.driver = driver

    def click_off_auto_pay_in_widget(self):
        self.driver.find_element_by_xpath(
            "//*[@id='subjects-page-wrapper']/div/div[1]/div/div[1]/div/div[2]/div/div[2]/div[6]/div[3]/label/span[1]").click()

    def click_off_auto_pay_in_tooltip(self):
        self.driver.find_element_by_xpath(
            "//*[@id='subjects-page-wrapper']/div/div[1]/div/div[1]/div/div[2]/div/div[2]/div[6]/div[3]/label/div/button").click()

    def click_off_auto_pay_in_popup(self):
        self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[3]/button[2]").click()
