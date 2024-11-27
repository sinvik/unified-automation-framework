#!/bin/bash
# Run API tests
source /app/.venv/bin/activate
behave features/api/ --tags=api --format allure_behave.formatter:AllureFormatter --outfile=target/allure-results/
