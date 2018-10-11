import unittest

import time


class Refresh(unittest.TestCase):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.counter = 56

    def refresh(self):
        time.sleep(8)
        self.driver.refresh()



