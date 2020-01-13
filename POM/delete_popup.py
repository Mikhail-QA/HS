import allure
import time
from selenium.webdriver.common.keys import Keys


class DeleteModalPopup(object):
    def __init__(self, driver):
        self.driver = driver

    @allure.step
    def delete_popup_mobile(self):
        element = self.driver.find_element_by_css_selector(
            'body > div.modal.fade.ng-isolate-scope.iu-fade.modal-phone.in > div')
        self.driver.execute_script("""
        var element = arguments[0];
        element.parentNode.removeChild(element);
        """, element)

        element = self.driver.find_element_by_css_selector(
            'body > div.modal.fade.ng-isolate-scope.iu-fade.modal-phone.in')
        self.driver.execute_script("""
        var element = arguments[0];
        element.parentNode.removeChild(element);
        """, element)

        element = self.driver.find_element_by_css_selector(
            'body > div.modal-backdrop.fade.in')
        self.driver.execute_script("""
        var element = arguments[0];
        element.parentNode.removeChild(element);
        """, element)

    @allure.step
    def delete_popup_trial(self):
        self.driver.find_element_by_tag_name('body').send_keys(Keys.ESCAPE)
        time.sleep(2)
