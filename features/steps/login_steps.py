from behave import given, when, then
from features.pages.login_page import LoginPage
from helpers.data_provider import DataProvider
from helpers.assertion import Assert


@given("the user is on the login page")
def step_impl(context):
    context.login_page = LoginPage(context.page)

@when("the user enters valid credentials")
def step_impl(context):
    creds = DataProvider.load_json("utils/test_data.json")["valid_user"]
    context.login_page.login(creds["username"], creds["password"])

@then("the user should be redirected to the dashboard")
def step_impl(context):
    current_url = context.page.url
    Assert.assert_in("dashboard", current_url, message="User is not on the dashboard page")
