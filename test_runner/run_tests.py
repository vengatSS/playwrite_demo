import os
import argparse
from behave.__main__ import main as behave_main
from allure_behave.formatter import AllureFormatter
from behave.formatter._registry import register_as

# Register Allure formatter
register_as("allure", AllureFormatter)

# Ensure Allure result folders exist
os.makedirs("reports/allure-results", exist_ok=True)
os.makedirs("reports/allure-report", exist_ok=True)

def run_behave(tags=None, feature=None):
    cmd = [
        "--format=pretty",
        "--format=allure",
        "--outfile=stdout",
        "--outfile=reports/allure-results",
    ]

    if tags:
        cmd.append(f"--tags={tags}")
    if feature:
        cmd.append(feature)
    else:
        cmd.append("features")

    behave_main(cmd)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run Behave BDD tests")
    parser.add_argument("--tags", help="Run scenarios with specific tags (e.g. @smoke)")
    parser.add_argument("--feature", help="Run specific feature file (e.g. features/login.feature)")
    args = parser.parse_args()

    run_behave(tags=args.tags, feature=args.feature)
