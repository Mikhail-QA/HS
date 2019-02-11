import time


class UrlHomeSchool(object):
    def __init__(self, driver):
        self.driver = driver

    def go_to_my_profile(self):
        self.driver.get("https://web-dev01.interneturok.ru/school/profile/my_profile")
        time.sleep(2)
        assert (u"E-mail:", self.driver.find_element_by_xpath(
            "//*[@id='subjects-page-wrapper']/div/div[2]/form/div[1]/div/div[1]/user-personal-info/div[7]/label").text)

    def go_to_tilda_landing(self):
        self.driver.get("http://iu:123456@project752209.tilda.ws/")
        assert (self.driver.find_element_by_css_selector("div.t396__elem.tn-elem.tn-elem__596361131472555385669"))

    def exit_profile(self):
        self.driver.get("https://web-dev01.interneturok.ru/school/logout")

    def go_to_lesson_page_test(self):
        self.driver.get("https://web-dev01.interneturok.ru/school/lesson/21860/video/95238")
        assert (self.driver.find_element_by_css_selector("#step9"))

    def go_to_lesson_page_1_klass(self):
        self.driver.get("https://web-dev01.interneturok.ru/school/lesson/21493/homework/91341")

    def go_to_lesson_page_tab_homework(self):
        self.driver.get("https://web-dev01.interneturok.ru/school/lesson/21860/homework/95239")
        assert (self.driver.find_element_by_css_selector(
            ".next-item-btn"))
        time.sleep(2)

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

    def go_to_page_subjects_subscribe(self):
        self.driver.get("https://web-dev01.interneturok.ru/school/subjects-subscribe")
        assert (u"Домашняя школа", self.driver.find_element_by_css_selector("h2.courses-prepare__payment-title").text)
