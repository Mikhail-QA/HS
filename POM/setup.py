import time
import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


class StarSchool(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(40)
        self.driver.maximize_window()
        self.driver.get("https://web-dev01.interneturok.ru/school/")
        time.sleep(3)
        self.verificationErrors = []


class StartYandexMail(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(40)
        self.driver.maximize_window()
        self.driver.get("https://mail.yandex.ru/")
        self.verificationErrors = []


class StartInterneturokAdmin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Edge()
        self.driver.implicitly_wait(40)
        self.driver.maximize_window()
        self.driver.get("hhttps://web-dev01.interneturok.ru/school/")
        self.verificationErrors = []


class StartInterneturokAdminClassMethod(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Edge()
        cls.driver.implicitly_wait(40)
        cls.driver.maximize_window()
        cls.driver.get("https://web-dev01.interneturok.ru/school/")
        cls.verificationErrors = []

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()


class StartSchoolClassMethod(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(40)
        cls.driver.maximize_window()
        cls.driver.get("https://web-dev01.interneturok.ru/school/")
        time.sleep(3)
        cls.verificationErrors = []

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException:
            return False
        return True

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()


class StartTildaClassMethod(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(40)
        cls.driver.maximize_window()
        cls.driver.get("http://iu:123456@test-school01.interneturok.ru/")
        time.sleep(3)
        cls.verificationErrors = []

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException:
            return False
        return True

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()


class StartLandingClassMethod(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(40)
        cls.driver.maximize_window()
        cls.driver.get("https://web-dev01.interneturok.ru/school_landing/")
        time.sleep(3)
        cls.verificationErrors = []

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException:
            return False
        return True

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()


class StartAmoClassMethod(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(40)
        cls.driver.maximize_window()
        cls.driver.get("https://www.amocrm.ru/")
        time.sleep(3)
        cls.verificationErrors = []

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException:
            return False
        return True

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
