import allure
from allure_commons.types import AttachmentType


class SaveScreen(object):
    def __init__(self, driver):
        self.driver = driver

    def screen(self):
        with allure.step('save a screen'):
            allure.attach(self.driver.get_screenshot_as_png(), name='Scr',
                          attachment_type=AttachmentType.PNG)
