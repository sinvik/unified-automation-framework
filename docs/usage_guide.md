### Guidelines:

#### Run tests on local machine
- If API tests need to be executed:
  ```bash
    # Navigate to the project directory (modify this path as needed)
    cd  "D:\projects\unified-automation-framework"

    # Run behave tests with Allure formatter
    behave features/api --format allure_behave.formatter:AllureFormatter --outfile=target/allure-results/

    #Generate Allure report
    allure generate target/allure-results -o target/allure-report --clean

    #Open the generated Allure report
    allure open target/allure-report    
  ```
- Alternate option [Run.bat] [click here](https://gitlab.com/pythonsolutions/unified-automation-framework/-/blob/master/run.bat?ref_type=heads)

#### Run tests via GitLab Pipeline:
- Goto Run Piepline Page - [Click here](https://gitlab.com/pythonsolutions/unified-automation-framework/-/pipelines/new)
- Pass below listed Variables _(Set all true if needs to be executed in parallel)_:
  - API_TEST=true 
  - WEB_TEST=false 
  - DB_TEST=false 