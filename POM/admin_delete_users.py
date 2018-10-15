import time


class AdminDeleteUser(object):
    def __init__(self, driver):
        self.driver = driver

    def go_to_admin(self):
        self.driver.get("https://web-dev01.interneturok.ru/school/admin/users")
        assert (
            self.driver.find_element_by_css_selector("div.row:nth-child(1) > div:nth-child(1) > button:nth-child(1)"))

    def user_1(self, pupil_1):
        self.driver.find_element_by_css_selector("input.form-control.ng-pristine.ng-untouched.ng-valid").clear()
        self.driver.find_element_by_css_selector("input.form-control.ng-pristine.ng-untouched.ng-valid").send_keys(
            pupil_1)
        self.driver.find_element_by_css_selector(".input-group-btn > button:nth-child(1)").click()
        assert (self.driver.find_element_by_css_selector("i.glyphicon.glyphicon-pencil"))
        time.sleep(1)
        self.driver.find_element_by_css_selector("i.glyphicon.glyphicon-remove").click()
        time.sleep(1)
        self.driver.find_element_by_css_selector(".modal-footer > button:nth-child(1)").click()
        time.sleep(1)
        self.driver.find_element_by_css_selector("button.btn-success:nth-child(1)").click()
        time.sleep(2)
        self.driver.refresh()
        assert (self.driver.find_element_by_css_selector("button.btn:nth-child(3)"))
        time.sleep(2)

    def user_2(self, pupil_2):
        self.driver.find_element_by_css_selector("input.form-control.ng-pristine.ng-untouched.ng-valid").clear()
        self.driver.find_element_by_css_selector("input.form-control").send_keys(
            pupil_2)
        assert (self.driver.find_element_by_css_selector("button.btn:nth-child(3)"))
        self.driver.find_element_by_css_selector(".input-group-btn > button:nth-child(1)").click()
        assert (self.driver.find_element_by_css_selector("i.glyphicon.glyphicon-pencil"))
        time.sleep(3)
        self.driver.find_element_by_css_selector("i.glyphicon.glyphicon-remove").click()
        time.sleep(1)
        self.driver.find_element_by_css_selector(".modal-footer > button:nth-child(1)").click()
        time.sleep(1)
        self.driver.find_element_by_css_selector("button.btn-success:nth-child(1)").click()
        time.sleep(2)
        self.driver.refresh()
        assert (self.driver.find_element_by_css_selector("button.btn:nth-child(3)"))
        time.sleep(2)

    def user_3(self, pupil_3):
        self.driver.find_element_by_css_selector("input.form-control.ng-pristine.ng-untouched.ng-valid").clear()
        self.driver.find_element_by_css_selector("input.form-control").send_keys(
            pupil_3)
        assert (self.driver.find_element_by_css_selector("button.btn:nth-child(3)"))
        self.driver.find_element_by_css_selector(".input-group-btn > button:nth-child(1)").click()
        assert (self.driver.find_element_by_css_selector("i.glyphicon.glyphicon-pencil"))
        time.sleep(3)
        self.driver.find_element_by_css_selector("i.glyphicon.glyphicon-remove").click()
        time.sleep(1)
        self.driver.find_element_by_css_selector(".modal-footer > button:nth-child(1)").click()
        time.sleep(1)
        self.driver.find_element_by_css_selector("button.btn-success:nth-child(1)").click()
        time.sleep(2)
        self.driver.refresh()
        assert (self.driver.find_element_by_css_selector("button.btn:nth-child(3)"))
        time.sleep(2)

    def user_4(self, pupil_4):
        self.driver.find_element_by_css_selector("input.form-control.ng-pristine.ng-untouched.ng-valid").clear()
        self.driver.find_element_by_css_selector("input.form-control").send_keys(
            pupil_4)
        assert (self.driver.find_element_by_css_selector("button.btn:nth-child(3)"))
        self.driver.find_element_by_css_selector(".input-group-btn > button:nth-child(1)").click()
        assert (self.driver.find_element_by_css_selector("i.glyphicon.glyphicon-pencil"))
        time.sleep(3)
        self.driver.find_element_by_css_selector("i.glyphicon.glyphicon-remove").click()
        time.sleep(1)
        self.driver.find_element_by_css_selector(".modal-footer > button:nth-child(1)").click()
        time.sleep(1)
        self.driver.find_element_by_css_selector("button.btn-success:nth-child(1)").click()
        time.sleep(2)
        self.driver.refresh()
        assert (self.driver.find_element_by_css_selector("button.btn:nth-child(3)"))
        time.sleep(2)

    def user_5(self, pupil_5):
        self.driver.find_element_by_css_selector("input.form-control.ng-pristine.ng-untouched.ng-valid").clear()
        self.driver.find_element_by_css_selector("input.form-control").send_keys(
            pupil_5)
        assert (self.driver.find_element_by_css_selector("button.btn:nth-child(3)"))
        self.driver.find_element_by_css_selector(".input-group-btn > button:nth-child(1)").click()
        assert (self.driver.find_element_by_css_selector("i.glyphicon.glyphicon-pencil"))
        time.sleep(3)
        self.driver.find_element_by_css_selector("i.glyphicon.glyphicon-remove").click()
        time.sleep(1)
        self.driver.find_element_by_css_selector(".modal-footer > button:nth-child(1)").click()
        time.sleep(1)
        self.driver.find_element_by_css_selector("button.btn-success:nth-child(1)").click()
        time.sleep(2)
        self.driver.refresh()
        assert (self.driver.find_element_by_css_selector("button.btn:nth-child(3)"))
        time.sleep(2)

    def user_6(self, pupil_6):
        self.driver.find_element_by_css_selector("input.form-control.ng-pristine.ng-untouched.ng-valid").clear()
        self.driver.find_element_by_css_selector("input.form-control").send_keys(
            pupil_6)
        assert (self.driver.find_element_by_css_selector("button.btn:nth-child(3)"))
        self.driver.find_element_by_css_selector(".input-group-btn > button:nth-child(1)").click()
        assert (self.driver.find_element_by_css_selector("i.glyphicon.glyphicon-pencil"))
        time.sleep(3)
        self.driver.find_element_by_css_selector("i.glyphicon.glyphicon-remove").click()
        time.sleep(1)
        self.driver.find_element_by_css_selector(".modal-footer > button:nth-child(1)").click()
        time.sleep(1)
        self.driver.find_element_by_css_selector("button.btn-success:nth-child(1)").click()
        time.sleep(2)
        self.driver.refresh()
        assert (self.driver.find_element_by_css_selector("button.btn:nth-child(3)"))
        time.sleep(2)
