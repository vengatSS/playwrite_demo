# import os
# from behave.__main__ import main as behave_main
# from allure_behave.formatter import AllureFormatter
# from behave.formatter._registry import register_as

# # Register 'allure' formatter
# register_as("allure", AllureFormatter)

# # Make sure output dir exists
# os.makedirs("reports/allure-results", exist_ok=True)
# os.makedirs("reports/allure-report",exist_ok=True)

# # Run Behave with Allure and Pretty formatters
# behave_main([
#      "--format=pretty",
#     "--format=allure",
#     "--outfile=stdout",
#     "--outfile=reports/allure-results",
#     "features"
# ])
