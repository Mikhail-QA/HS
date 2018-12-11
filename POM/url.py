import time


class UrlHomeSchool(object):
    def __init__(self, driver):
        self.driver = driver

    def go_to_my_profile(self):
        self.driver.get("https://web-dev01.interneturok.ru/school/profile/my_profile")
        assert (u"E-mail:", self.driver.find_element_by_xpath(
            "//*[@id='subjects-page-wrapper']/div/div[2]/form/div[1]/div/div[1]/user-personal-info/div[7]/label").text)

    def go_to_tilda_landing(self):
        self.driver.get("http://iu:123456@project752209.tilda.ws/")

    def exit_profile(self):
        self.driver.get("https://web-dev01.interneturok.ru/school/logout")

    def go_to_lesson_page_test(self):
        self.driver.get("https://web-dev01.interneturok.ru/school/lesson/21829/video/94974")
        assert (self.driver.find_element_by_css_selector("#step9"))

    def go_to_lesson_page_1_klass(self):
        self.driver.get("https://web-dev01.interneturok.ru/school/lesson/21485/homework/90516")

    def go_to_lesson_page_tab_homework(self):
        self.driver.get("https://web-dev01.interneturok.ru/school/lesson/21829/homework/94973")
        assert (self.driver.find_element_by_css_selector(
            "body > div.page-wrapper.ng-isolate-scope > div > div.container > div.row.ng-scope > div > div > div:nth-child(2) > div"))
        time.sleep(6)

    def go_to_lesson_tab_test_iu(self):
        self.driver.get("https://web-dev01.interneturok.ru/school/lesson/18402/training_iu/91896")
        assert (self.driver.find_element_by_css_selector("#step9 > button"))
        time.sleep(1.5)

    def go_to_lesson_tab_trainer_iu(self):
        self.driver.get("https://web-dev01.interneturok.ru/school/lesson/18325/training_iu/90787")
        assert (self.driver.find_element_by_css_selector("#step9 > button"))
        time.sleep(1.5)

    def go_to_lesson_tab_video(self):
        self.driver.get("https://web-dev01.interneturok.ru/school/lesson/18112/video/72658")
        assert (self.driver.find_element_by_css_selector("#step9 > button"))
        time.sleep(1.5)
