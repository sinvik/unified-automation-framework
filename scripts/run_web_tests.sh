#!/bin/bash
# Run web tests
source /app/.venv/bin/activate
behave features/web/ --tags=web --format allure_behave.formatter:AllureFormatter --outfile=target/allure-results/
