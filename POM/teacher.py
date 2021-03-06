import time
import allure


class StepTeacher(object):
    def __init__(self, driver):
        self.driver = driver

    @allure.step
    def search_user(self, user_name="hs02@yopmail.com"):
        self.driver.find_element_by_css_selector("div.col-md-8 input.ng-untouched.ng-valid.ng-empty").send_keys(
            user_name)

    @allure.step
    def click_button_show(self):
        self.driver.find_element_by_css_selector("div.col-md-4 button.btn.btn-xs.btn-warning").click()
        time.sleep(1)
        assert (self.driver.find_element_by_css_selector("a.btn.btn-sm.btn-primary"))
        time.sleep(1.5)

    @allure.step
    def click_button_check(self):
        self.driver.find_element_by_css_selector("a.btn.btn-sm.btn-primary").click()
        assert (self.driver.find_element_by_css_selector("div.col-sm-2"))

    @allure.step
    def click_button_ball(self):
        self.driver.find_element_by_css_selector("div.text-center:nth-child(7) > a:nth-child(2)").click()

    @allure.step
    def open_select(self):
        self.driver.find_element_by_css_selector(".text-center select").click()

    @allure.step
    def enter_bal_5(self):
        self.driver.find_element_by_css_selector("select.pull-right > option:nth-child(5)").click()

    @allure.step
    def click_button_save(self):
        self.driver.find_element_by_css_selector("button.btn.btn-primary.btn-xs").click()
        assert (self.driver.find_element_by_css_selector(".ng-submitted > div:nth-child(1) > div:nth-child(7) > a"))
        time.sleep(3)

    @allure.step
    def click_button_filter_all(self):
        self.driver.find_element_by_css_selector("div.filter:nth-child(4) span.ng-not-empty:nth-child(2)").click()

    @allure.step
    def open_img(self):
        self.driver.find_element_by_css_selector("span.atach-img").click()
