class DeleteModalPopup(object):
    def __init__(self, driver):
        self.driver = driver

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
