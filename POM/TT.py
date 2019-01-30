import time


class Test(object):
    def __init__(self, driver):
        self.driver = driver

    def start_test(self):
        self.driver.find_element_by_css_selector("div.b-input-radio__name").click()
        self.driver.find_element_by_link_text(u"Ответить").click()
        time.sleep(5)

        self.driver.find_element_by_css_selector("div.b-input-radio__name").click()
        self.driver.find_element_by_link_text(u"Ответить").click()
        time.sleep(5)

        self.driver.find_element_by_css_selector("div.b-input-radio__name").click()
        self.driver.find_element_by_link_text(u"Ответить").click()
        time.sleep(5)

        self.driver.find_element_by_css_selector("div.b-input-radio__name").click()
        self.driver.find_element_by_link_text(u"Ответить").click()
        time.sleep(5)

        self.driver.find_element_by_css_selector("div.b-input-radio__name").click()
        self.driver.find_element_by_link_text(u"Ответить").click()
        time.sleep(5)

    def click_button_finish(self):
        self.driver.find_element_by_link_text("Завершить").click()
        time.sleep(1)


class Exercise(object):
    def __init__(self, driver):
        self.driver = driver

    def test(self):
        step = 1
        answer = 1
        please = False
        for n in range(1, 7):
            time.sleep(7)
            major_text = self.driver.find_element_by_css_selector("small.b-progress-test__desc").text
            cont_list = major_text.split(" ")
            # print(">>> ANSW COUNT", major_text)
            # print(">>> CONT LIST", cont_list)
            if int(cont_list[1]) is 1 and not please:
                step = 2
                answer = 1
                please = True
            elif int(cont_list[1]) is 2:
                return True
            element = self.driver.find_element_by_css_selector(
                "body > div.arcticmodal-container > table > tbody > tr > td > div > div > div.b-popup__content.b-popup__content_border_top > div > div > dl > div:nth-child({0}) > dd > ul > li:nth-child({1}) > div > label > span".format(
                    str(step), str(answer)))
            element.click()
            answer += 1

    def click_button_finish(self):
        self.driver.find_element_by_link_text("Завершить").click()
        time.sleep(2)
