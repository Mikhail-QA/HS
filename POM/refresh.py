import unittest

import time


class Refresh(unittest.TestCase):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.counter = 56

    def refresh(self):
        time.sleep(4)
        self.driver.refresh()
        time.sleep(4)



