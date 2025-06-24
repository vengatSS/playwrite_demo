import allure
from playwright.sync_api import sync_playwright
from helpers.data_provider import DataProvider
from helpers.waiters import Waiter
from behave.model_core import Status
from allure_commons.types import AttachmentType

def before_all(context):
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=False,args=["--start-maximized"])
    context.context = context.browser.new_context(viewport=None)
    context.page = context.context.new_page()
    login_url = DataProvider.load_json("utils/test_data.json")["urls"]["login"]
    context.page.goto(login_url)

def after_all(context):
    context.browser.close()
    context.playwright.stop()



def after_step(context, step):
    if step.status == Status.failed and hasattr(context, "page"):
        waiter = Waiter(context.page, timeout=5000)
        waiter.wait_for_page_load()
        screenshot_bytes = context.page.screenshot()
        allure.attach(screenshot_bytes, name="screenshot", attachment_type=AttachmentType.PNG)
    else:
        if step.status == Status.passed and hasattr(context, "page"):
            waiter = Waiter(context.page, timeout=5000)
            waiter.wait_for_page_load()
            screenshot_bytes = context.page.screenshot()
            allure.attach(screenshot_bytes, name="screenshot", attachment_type=AttachmentType.PNG)    
 
 
