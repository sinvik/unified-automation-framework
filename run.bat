@echo off

REM Validate input arguments
IF "%1" == "" (
    echo "Usage: run_tests.bat [web|api|db]"
    exit /b 1
)

REM Navigate to the project directory (modify this path as needed)
cd /d "D:\projects\unified-automation-framework"

REM Set the feature directory based on input argument
IF "%1" == "web" (
    set FEATURE_DIR=features/web
) ELSE IF "%1" == "api" (
    set FEATURE_DIR=features/api
) ELSE IF "%1" == "db" (
    set FEATURE_DIR=features/db
) ELSE (
    echo "Invalid argument. Usage: run_tests.bat [web|api|db]"
    exit /b 1
)

REM Delete and recreate the target directory
rmdir /s /q target
mkdir target

REM Run behave tests with Allure formatter
behave %FEATURE_DIR% --format allure_behave.formatter:AllureFormatter --outfile=target/allure-results/

REM Check if the behave tests executed successfully
IF %ERRORLEVEL% NEQ 0 (
    echo "Behave tests failed."
)

REM Generate Allure report
allure generate target/allure-results -o target/allure-report --clean

REM Check if the Allure report generation succeeded
IF %ERRORLEVEL% NEQ 0 (
    echo "Allure report generation failed."
    exit /b %ERRORLEVEL%
)

REM Open the generated Allure report
allure open target/allure-report

REM Check if opening the Allure report succeeded
IF %ERRORLEVEL% NEQ 0 (
    echo "Failed to open Allure report."
    exit /b %ERRORLEVEL%
)

echo "Allure report generated and opened successfully."
exit /b 0
