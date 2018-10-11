import time


class StepTeacher(object):
    def __init__(self, driver):
        self.driver = driver

    def search_user(self):
        self.driver.find_element_by_css_selector("input.form-control:nth-child(2)").send_keys(
            "hs02@yopmail.com")

    def click_button_show(self):
        self.driver.find_element_by_css_selector(
            "div.row:nth-child(7) > div:nth-child(1) > div:nth-child(2) > button").click()
        assert (self.driver.find_element_by_css_selector("a.btn.btn-sm.btn-primary"))

    def click_button_check(self):
        self.driver.find_element_by_css_selector("a.btn.btn-sm.btn-primary").click()

    def open_select(self):
        self.driver.find_element_by_css_selector(
            "body > div.page-wrapper.ng-isolate-scope > div > div.container > div.row.ng-scope > div > div > div > div > div.tab-pane.ng-scope.active > div > div > div > div:nth-child(9) > ul > li.list-group-item.row.cf.ng-scope > form > div.row.homeworks-row > div:nth-child(7) > select").click()

    def enter_bal_5(self):
        self.driver.find_element_by_css_selector("select.pull-right > option:nth-child(5)").click()

    def click_button_save(self):
        self.driver.find_element_by_css_selector("button.btn.btn-primary.btn-xs").click()
        assert (self.driver.find_element_by_css_selector(".ng-submitted > div:nth-child(1) > div:nth-child(7) > a"))
        time.sleep(3)
