#!/bin/bash
# Run DB tests
source /app/.venv/bin/activate
export sql_user=$sql_user
export sql_pwd=$sql_pwd
echo "Database logging as $sql_user"
behave features/db/ --tags=db --format allure_behave.formatter:AllureFormatter --outfile=target/allure-results/