import time
import allure


class MyProfile(object):
    def __init__(self, driver):
        self.driver = driver

    @allure.step
    def input_number_mobile(self):
        self.driver.find_element_by_xpath(
            "//*[@id='subjects-page-wrapper']/div/div[2]/form/div[1]/div/div[1]/user-personal-info/div[6]/div/input").send_keys(
            "+73123213")

    @allure.step
    def click_button_save_changes(self):
        self.driver.find_element_by_xpath(
            "//*[@id='subjects-page-wrapper']/div/div[2]/form/div[2]/button").click()

    @allure.step
    def click_button_extend_access(self):
        self.driver.find_element_by_css_selector("button.btn.btn-primary.ng-scope").click()
        assert (u"Домашняя школа", self.driver.find_element_by_css_selector("h2.courses-prepare__payment-title").text)
        time.sleep(1)

    @allure.step
    def click_button_pay_for_access(self):
        self.driver.find_element_by_css_selector("a.btn.btn-primary").click()
        assert (u"Домашняя школа", self.driver.find_element_by_css_selector("h2.courses-prepare__payment-title").text)
        time.sleep(2)

    @allure.step
    def click_button_pay_other_classes(self):
        self.driver.find_element_by_css_selector(
            ".col-sm-3.col-md-3 div.profile-courses div a:nth-child(3)").click()
        assert (u"Домашняя школа", self.driver.find_element_by_css_selector("h2.courses-prepare__payment-title").text)

    @allure.step
    def click_button_pay_school_in_pd(self):
        self.driver.find_element_by_css_selector("button.btn.btn-success.ng-scope").click()
        assert (u"Домашняя школа", self.driver.find_element_by_css_selector("h2.courses-prepare__payment-title").text)


class OffAutoPayInSchool(object):
    def __init__(self, driver):
        self.driver = driver

    @allure.step
    def click_off_auto_pay_in_widget(self):
        self.driver.find_element_by_css_selector(
            "div:nth-child(1) > div.profile-course_body > div.profile-course_autopay > label > span.switch-reverse.ng-scope").click()

    @allure.step
    def click_off_auto_pay_in_tooltip(self):
        self.driver.find_element_by_css_selector("button.btn-autopay").click()

    @allure.step
    def click_off_auto_pay_in_popup(self):
        self.driver.find_element_by_css_selector(".autopay-modal-footer.ng-scope > button:nth-child(2)").click()


class OffAutoPayInPersonalMentor(object):
    def __init__(self, driver):
        self.driver = driver

    @allure.step
    def click_off_auto_pay_in_widget(self):
        self.driver.find_element_by_css_selector(
            "div:nth-child(1) > div.profile-course_body > div.profile-course_curator.ng-scope > div.autopay-curator > label > span.switch-label").click()

    @allure.step
    def click_off_auto_pay_in_tooltip(self):
        self.driver.find_element_by_css_selector(
            "div:nth-child(1) > div.profile-course_body > div.profile-course_curator.ng-scope > div.autopay-curator > label > div > button").click()

    @allure.step
    def click_off_auto_pay_in_popup(self):
        self.driver.find_element_by_css_selector(".autopay-modal-footer.ng-scope > button:nth-child(2)").click()
