from helpers.action import Action
class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username_input = page.locator("//input[@name='username']")
        self.password_input = page.locator("//input[@name='password']")
        self.login_button = page.locator("//button[@type='submit']")
        self.action = Action(page)

    def login(self,username,password):
        self.action.input_data(self.username_input, username)
        self.action.input_data(self.password_input, password)
        self.action.click_action(self.login_button)
