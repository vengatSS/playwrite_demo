# allure_patch.py
from behave.formatter._registry import register_as
from allure_behave.formatter import AllureFormatter

register_as("allure", AllureFormatter)
