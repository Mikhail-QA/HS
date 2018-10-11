import time


class TildaPage(object):
    def __init__(self, driver):
        self.driver = driver

    def click_button_enter(self):
        self.driver.find_element_by_link_text("Войти").click()

    def click_button_registration(self):
        self.driver.find_element_by_link_text("Регистрация").click()
        time.sleep(1)
