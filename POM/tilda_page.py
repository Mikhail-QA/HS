import time
import allure


class TildaPage(object):
    def __init__(self, driver):
        self.driver = driver

    @allure.step
    def open_tilda_page(self):
        self.driver.get("https://iu:123456@test-school01.interneturok.ru/")

    @allure.step
    def click_login_button(self):
        self.driver.find_element_by_link_text("Войти").click()

    @allure.step
    def click_button_registration(self):
        self.driver.find_element_by_link_text("Регистрация").click()
        time.sleep(1)
