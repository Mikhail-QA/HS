import time
import allure


class AdminDeleteUser(object):
    def __init__(self, driver):
        self.driver = driver

    def go_to_admin(self):
        self.driver.get("https://web-dev01.interneturok.ru/school/admin/users")
        assert (self.driver.find_element_by_css_selector("button.btn:nth-child(3)"))
        time.sleep(5)

    def user_1(self, pupil_1):
        with allure.step("В инпуте удалить текст"):
            self.driver.find_element_by_css_selector("input.form-control.ng-pristine.ng-untouched.ng-valid").clear()
            time.sleep(1)
        with allure.step("В инпуте ввести почту ученика"):
            self.driver.find_element_by_css_selector("input.form-control.ng-pristine.ng-untouched.ng-valid").send_keys(
                pupil_1)
            time.sleep(2)
        with allure.step("Нажать на кнопку Найти"):
            self.driver.find_element_by_css_selector(".input-group-btn > button:nth-child(1)").click()
            assert (self.driver.find_element_by_css_selector("i.glyphicon.glyphicon-pencil"))
            time.sleep(5)
        with allure.step("Нажать на кнопку Крестик Удалить"):
            self.driver.find_element_by_css_selector("i.glyphicon.glyphicon-remove").click()
            time.sleep(5)
        with allure.step("В попапе Удалить пользователя ? нажать на кнопку Да"):
            self.driver.find_element_by_css_selector(
                "html.no-js.ng-scope body.modal-open div.modal.fade.ng-isolate-scope.iu-fade.in div.modal-dialog div.modal-content div.ng-scope div.modal-footer.ng-scope button.btn.btn-primary").click()
            time.sleep(1)
        with allure.step("В попапе Пользователь удалён нажать на кнопку Продолжить"):
            self.driver.find_element_by_css_selector("button.btn-success:nth-child(1)").click()
            time.sleep(2)
        with allure.step("Дождаться появления кнопки Применить в подвале сайта"):
            assert (self.driver.find_element_by_css_selector("button.btn:nth-child(3)"))
            time.sleep(2)

    def user_2(self, pupil_2):
        with allure.step("В инпуте удалить текст"):
            self.driver.find_element_by_css_selector(
                "input.form-control.ng-valid.ng-dirty.ng-valid-parse.ng-touched").clear()
            time.sleep(1)
        with allure.step("В инпуте ввести почту ученика"):
            self.driver.find_element_by_css_selector(
                "input.form-control.ng-valid.ng-dirty.ng-valid-parse.ng-touched").send_keys(
                pupil_2)
            time.sleep(2)
        with allure.step("Нажать на кнопку Найти"):
            self.driver.find_element_by_css_selector(".input-group-btn > button:nth-child(1)").click()
            assert (self.driver.find_element_by_css_selector("i.glyphicon.glyphicon-pencil"))
            time.sleep(5)
        with allure.step("Нажать на кнопку Крестик Удалить"):
            self.driver.find_element_by_css_selector("i.glyphicon.glyphicon-remove").click()
            time.sleep(1)
        with allure.step("В попапе Удалить пользователя ? нажать на кнопку Да"):
            self.driver.find_element_by_css_selector(
                "html.no-js.ng-scope body.modal-open div.modal.fade.ng-isolate-scope.iu-fade.in div.modal-dialog div.modal-content div.ng-scope div.modal-footer.ng-scope button.btn.btn-primary").click()
            time.sleep(1)
        with allure.step("В попапе Пользователь удалён нажать на кнопку Продолжить"):
            self.driver.find_element_by_css_selector("button.btn-success:nth-child(1)").click()
            time.sleep(2)
        with allure.step("Дождаться появления кнопки Применить в подвале сайта"):
            assert (self.driver.find_element_by_css_selector("button.btn:nth-child(3)"))
            time.sleep(2)

    def user_3(self, pupil_3):
        with allure.step("В инпуте удалить текст"):
            self.driver.find_element_by_css_selector(
                "input.form-control.ng-valid.ng-dirty.ng-valid-parse.ng-touched").clear()
            time.sleep(1)
        with allure.step("В инпуте ввести почту ученика"):
            self.driver.find_element_by_css_selector(
                "input.form-control.ng-valid.ng-dirty.ng-valid-parse.ng-touched").send_keys(
                pupil_3)
            time.sleep(2)
        with allure.step("Нажать на кнопку Найти"):
            self.driver.find_element_by_css_selector(".input-group-btn > button:nth-child(1)").click()
            assert (self.driver.find_element_by_css_selector("i.glyphicon.glyphicon-pencil"))
            time.sleep(5)
        with allure.step("Нажать на кнопку Крестик Удалить"):
            self.driver.find_element_by_css_selector("i.glyphicon.glyphicon-remove").click()
            time.sleep(1)
        with allure.step("В попапе Удалить пользователя ? нажать на кнопку Да"):
            self.driver.find_element_by_css_selector(
                "html.no-js.ng-scope body.modal-open div.modal.fade.ng-isolate-scope.iu-fade.in div.modal-dialog div.modal-content div.ng-scope div.modal-footer.ng-scope button.btn.btn-primary").click()
            time.sleep(1)
        with allure.step("В попапе Пользователь удалён нажать на кнопку Продолжить"):
            self.driver.find_element_by_css_selector("button.btn-success:nth-child(1)").click()
            time.sleep(2)
        with allure.step("Дождаться появления кнопки Применить в подвале сайта"):
            assert (self.driver.find_element_by_css_selector("button.btn:nth-child(3)"))
            time.sleep(2)

    def user_4(self, pupil_4):
        with allure.step("В инпуте удалить текст"):
            self.driver.find_element_by_css_selector(
                "input.form-control.ng-valid.ng-dirty.ng-valid-parse.ng-touched").clear()
            time.sleep(1)
        with allure.step("В инпуте ввести почту ученика"):
            self.driver.find_element_by_css_selector(
                "input.form-control.ng-valid.ng-dirty.ng-valid-parse.ng-touched").send_keys(
                pupil_4)
            time.sleep(2)
        with allure.step("Нажать на кнопку Найти"):
            self.driver.find_element_by_css_selector(".input-group-btn > button:nth-child(1)").click()
            assert (self.driver.find_element_by_css_selector("i.glyphicon.glyphicon-pencil"))
            time.sleep(5)
        with allure.step("Нажать на кнопку Крестик Удалить"):
            self.driver.find_element_by_css_selector("i.glyphicon.glyphicon-remove").click()
            time.sleep(1)
        with allure.step("В попапе Удалить пользователя ? нажать на кнопку Да"):
            self.driver.find_element_by_css_selector(
                "html.no-js.ng-scope body.modal-open div.modal.fade.ng-isolate-scope.iu-fade.in div.modal-dialog div.modal-content div.ng-scope div.modal-footer.ng-scope button.btn.btn-primary").click()
            time.sleep(1)
        with allure.step("В попапе Пользователь удалён нажать на кнопку Продолжить"):
            self.driver.find_element_by_css_selector("button.btn-success:nth-child(1)").click()
            time.sleep(2)
        with allure.step("Дождаться появления кнопки Применить в подвале сайта"):
            assert (self.driver.find_element_by_css_selector("button.btn:nth-child(3)"))
            time.sleep(2)

    def user_5(self, pupil_5):
        with allure.step("В инпуте удалить текст"):
            self.driver.find_element_by_css_selector(
                "input.form-control.ng-valid.ng-dirty.ng-valid-parse.ng-touched").clear()
            time.sleep(1)
        with allure.step("В инпуте ввести почту ученика"):
            self.driver.find_element_by_css_selector(
                "input.form-control.ng-valid.ng-dirty.ng-valid-parse.ng-touched").send_keys(
                pupil_5)
            time.sleep(2)
        with allure.step("Нажать на кнопку Найти"):
            self.driver.find_element_by_css_selector(".input-group-btn > button:nth-child(1)").click()
            assert (self.driver.find_element_by_css_selector("i.glyphicon.glyphicon-pencil"))
            time.sleep(5)
        with allure.step("Нажать на кнопку Крестик Удалить"):
            self.driver.find_element_by_css_selector("i.glyphicon.glyphicon-remove").click()
            time.sleep(1)
        with allure.step("В попапе Удалить пользователя ? нажать на кнопку Да"):
            self.driver.find_element_by_css_selector(
                "html.no-js.ng-scope body.modal-open div.modal.fade.ng-isolate-scope.iu-fade.in div.modal-dialog div.modal-content div.ng-scope div.modal-footer.ng-scope button.btn.btn-primary").click()
            time.sleep(1)
        with allure.step("В попапе Пользователь удалён нажать на кнопку Продолжить"):
            self.driver.find_element_by_css_selector("button.btn-success:nth-child(1)").click()
            time.sleep(2)
        with allure.step("Дождаться появления кнопки Применить в подвале сайта"):
            assert (self.driver.find_element_by_css_selector("button.btn:nth-child(3)"))
            time.sleep(2)

    def user_6(self, pupil_6):
        with allure.step("В инпуте удалить текст"):
            self.driver.find_element_by_css_selector(
                "input.form-control.ng-valid.ng-dirty.ng-valid-parse.ng-touched").clear()
            time.sleep(1)
        with allure.step("В инпуте ввести почту ученика"):
            self.driver.find_element_by_css_selector(
                "input.form-control.ng-valid.ng-dirty.ng-valid-parse.ng-touched").send_keys(
                pupil_6)
            time.sleep(2)
        with allure.step("Нажать на кнопку Найти"):
            self.driver.find_element_by_css_selector(".input-group-btn > button:nth-child(1)").click()
            assert (self.driver.find_element_by_css_selector("i.glyphicon.glyphicon-pencil"))
            time.sleep(5)
        with allure.step("Нажать на кнопку Крестик Удалить"):
            self.driver.find_element_by_css_selector("i.glyphicon.glyphicon-remove").click()
            time.sleep(1)
        with allure.step("В попапе Удалить пользователя ? нажать на кнопку Да"):
            self.driver.find_element_by_css_selector(
                "html.no-js.ng-scope body.modal-open div.modal.fade.ng-isolate-scope.iu-fade.in div.modal-dialog div.modal-content div.ng-scope div.modal-footer.ng-scope button.btn.btn-primary").click()
            time.sleep(1)
        with allure.step("В попапе Пользователь удалён нажать на кнопку Продолжить"):
            self.driver.find_element_by_css_selector("button.btn-success:nth-child(1)").click()
