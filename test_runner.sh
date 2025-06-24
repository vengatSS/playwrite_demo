#!/bin/bash
set -euo pipefail

all() {
    echo "Running all tests..."
    python test_runner/run_tests.py
    allure generate reports/allure-results -o reports/allure-report --clean
}

smoke() {
    echo "Running smoke tests..."
    python test_runner/run_tests.py --tags=@smoke
    allure generate reports/allure-results -o reports/allure-report --clean
    allure open reports/allure-report
}

parallel() {
    echo "Running tests in parallel..."
    python test_runner/run_parallel.py
    allure generate reports/allure-results -o reports/allure-report --clean
    allure open reports/allure-report
}

case "${1:-}" in
    all) all ;;
    smoke) smoke ;;
    parallel) parallel ;;
    *)
        echo "Usage: $0 {all|smoke|parallel}"
        exit 1
        ;;
esac
