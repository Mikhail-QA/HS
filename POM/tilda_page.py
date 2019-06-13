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
        self.driver.find_element_by_css_selector("a.singin__link").click()
        time.sleep(1.5)

    @allure.step
    def click_button_registration(self):
        self.driver.find_element_by_css_selector("a.pp_.footer__top_button.orange__link").click()
        time.sleep(1)
