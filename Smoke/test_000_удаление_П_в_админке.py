import allure
import time

from POM.users import Admin
from POM.school_page import FormSignIn
from POM.setup import StartSchoolClassMethod
from POM.admin_delete_users import AdminDeleteUser


@allure.feature("Админка")
@allure.story("Удалить пользователей в админке")
class RemovingUsersInAdminPanel(StartSchoolClassMethod):
    def test_000_login_admin(self):
        driver = self.driver
        steps_delete = AdminDeleteUser(driver)
        step_user = Admin(driver)
        step_enter = FormSignIn(driver)

        with allure.step("В поле email и password ввести school.interneturok@yandex.ru/34t3hEOfbTT2k"):
            step_user.enter_email(user_name="school.interneturok@yandex.ru")
            step_user.enter_password(password="34t3hEOfbTT2k")
        with allure.step("Нажать на кнопку Авторизоваться"):
            step_enter.click_button_login_admin()
        with allure.step("Перейти в раздел пользователи"):
            steps_delete.go_to_admin()

    def test_delete_HS1(self):
        # driver = self.driver
        # steps_delete = AdminDeleteUser(driver)

        with allure.step("В инпуте удалить текст"):
            self.driver.find_element_by_css_selector("input.form-control.ng-pristine.ng-untouched.ng-valid").clear()
            time.sleep(1)
        with allure.step("В инпуте ввести почту ученика"):
            self.driver.find_element_by_css_selector("input.form-control.ng-pristine.ng-untouched.ng-valid").send_keys(
                "hs01@yopmail.com")
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
        # with allure.step("Обновить страницу"):
        #     self.driver.refresh()
        with allure.step("Дождаться появления кнопки Применить в подвале сайта"):
            assert (self.driver.find_element_by_css_selector("button.btn:nth-child(3)"))
            time.sleep(2)

        # with allure.step("Удаляю пользователя hs01@yopmail.com"):
        #     steps_delete.user_1(pupil_1="hs01@yopmail.com")

    def test_delete_HS2(self):
        with allure.step("В инпуте удалить текст"):
            self.driver.find_element_by_css_selector("input.form-control.ng-valid.ng-dirty.ng-valid-parse.ng-touched").clear()
            time.sleep(1)
        with allure.step("В инпуте ввести почту ученика"):
            self.driver.find_element_by_css_selector(
                "input.form-control.ng-valid.ng-dirty.ng-valid-parse.ng-touched").send_keys(
                "hs02@yopmail.com")
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
        # with allure.step("Обновить страницу"):
        #     self.driver.refresh()
        with allure.step("Дождаться появления кнопки Применить в подвале сайта"):
            assert (self.driver.find_element_by_css_selector("button.btn:nth-child(3)"))
            time.sleep(2)

        # driver = self.driver
        # steps_delete = AdminDeleteUser(driver)
        #
        # with allure.step("Удаляю пользователя hs02@yopmail.com"):
        #     steps_delete.user_2(pupil_2="hs02@yopmail.com")

    def test_delete_HS3(self):
        with allure.step("В инпуте удалить текст"):
            self.driver.find_element_by_css_selector("input.form-control.ng-valid.ng-dirty.ng-valid-parse.ng-touched").clear()
            time.sleep(1)
        with allure.step("В инпуте ввести почту ученика"):
            self.driver.find_element_by_css_selector(
                "input.form-control.ng-valid.ng-dirty.ng-valid-parse.ng-touched").send_keys(
                "hs03@yopmail.com")
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
        # with allure.step("Обновить страницу"):
        #     self.driver.refresh()
        with allure.step("Дождаться появления кнопки Применить в подвале сайта"):
            assert (self.driver.find_element_by_css_selector("button.btn:nth-child(3)"))
            time.sleep(2)

        # driver = self.driver
        # steps_delete = AdminDeleteUser(driver)
        #
        # with allure.step("Удаляю пользователя hs03@yopmail.com"):
        #     steps_delete.user_3(pupil_3="hs03@yopmail.com")

    def test_delete_HS4(self):
        with allure.step("В инпуте удалить текст"):
            self.driver.find_element_by_css_selector("input.form-control.ng-valid.ng-dirty.ng-valid-parse.ng-touched").clear()
            time.sleep(1)
        with allure.step("В инпуте ввести почту ученика"):
            self.driver.find_element_by_css_selector(
                "input.form-control.ng-valid.ng-dirty.ng-valid-parse.ng-touched").send_keys(
                "hs04@yopmail.com")
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
        # with allure.step("Обновить страницу"):
        #     self.driver.refresh()
        with allure.step("Дождаться появления кнопки Применить в подвале сайта"):
            assert (self.driver.find_element_by_css_selector("button.btn:nth-child(3)"))
            time.sleep(2)

        # driver = self.driver
        # steps_delete = AdminDeleteUser(driver)
        #
        # with allure.step("Удаляю пользователя hs04@yopmail.com"):
        #     steps_delete.user_4(pupil_4="hs04@yopmail.com")

    def test_delete_HS5(self):
        with allure.step("В инпуте удалить текст"):
            self.driver.find_element_by_css_selector("input.form-control.ng-valid.ng-dirty.ng-valid-parse.ng-touched").clear()
            time.sleep(1)
        with allure.step("В инпуте ввести почту ученика"):
            self.driver.find_element_by_css_selector(
                "input.form-control.ng-valid.ng-dirty.ng-valid-parse.ng-touched").send_keys(
                "hs05@yopmail.com")
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
        # with allure.step("Обновить страницу"):
        #     self.driver.refresh()
        with allure.step("Дождаться появления кнопки Применить в подвале сайта"):
            assert (self.driver.find_element_by_css_selector("button.btn:nth-child(3)"))
            time.sleep(2)

        # driver = self.driver
        # steps_delete = AdminDeleteUser(driver)
        #
        # with allure.step("Удаляю пользователя hs05@yopmail.com"):
        #     steps_delete.user_5(pupil_5="hs05@yopmail.com")

    def test_delete_social_user(self):
        with allure.step("В инпуте удалить текст"):
            self.driver.find_element_by_css_selector("input.form-control.ng-valid.ng-dirty.ng-valid-parse.ng-touched").clear()
            time.sleep(1)
        with allure.step("В инпуте ввести почту ученика"):
            self.driver.find_element_by_css_selector(
                "input.form-control.ng-valid.ng-dirty.ng-valid-parse.ng-touched").send_keys(
                "gruzd-vikto@rambler.ru")
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

        # driver = self.driver
        # steps_delete = AdminDeleteUser(driver)
        #
        # with allure.step("Удаляю пользователя gruzd-vikto@rambler.ru"):
        #     steps_delete.user_6(pupil_6="gruzd-vikto@rambler.ru")
