class Action:

    def __init__(self, page):
        self.page = page

    def input_data(self, element, data):
        element.fill(data)

    def click_action(self, element):
        element.click()

    def clear_input(self, element):
        element.fill('')

    def get_text(self, element):
        return element.inner_text()

    def is_visible(self, element):
        return element.is_visible()

    def is_enabled(self, element):
        return element.is_enabled()

    def hover_over(self, element):
        element.hover()

    def wait_for_element(self, selector, timeout=5000):
        return self.page.wait_for_selector(selector, timeout=timeout)

    def press_enter(self, element):
        element.press("Enter")

    def select_dropdown_by_value(self, element, value):
        element.select_option(value=value)
