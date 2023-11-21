# Test Automation Repository

This repository contains automated tests for the Oscar Sandbox(a site for training autotests), utilizing Selenium, pytest and allure.

## Allure report

[View the Allure report here.](https://irinafrutiz.github.io/stepik_auto_tests_course_final_block/)

## Running automated tests on GitHub

1. On the [Actions tab](https://github.com/IrinaFrutiz/stepik_auto_tests_course_final_block/actions/workflows/run_tests.yml), click "Run workflow."
2. Choose the target (default is English and Chrome).
3. Wait for all tests to complete.
4. Open or refresh the page with the Allure report to view the new test results.

## Running Tests Locally

1. Clone or download the project to your local machine.
2. Before running the tests, make sure you have the required Python packages installed. Use the following command to install them:

   - **Python packages:**
     ```bash
     pip install -r requirements.txt
     ```

   - **Web Browsers:** Depending on your test configuration, ensure you have the necessary web browsers installed. For example:
     - For Chrome: Ensure you have Google Chrome installed.
     - For Firefox: Ensure you have Mozilla Firefox installed.
     - For Microsoft Edge: Ensure you have Microsoft Edge installed.

3. Use the following commands to run the tests::

   - pytest -v --tb=line --language=en -m need_review
   - pytest -v --tb=line --language=fr
   - pytest -v
   - pytest -v --browser_name=firefox 

By default, the tests will be executed using the Chrome browser and the `en-gb` language.

Please note that there might be instances when the site being tested is down or experiencing maintenance. In such cases, the tests may fail or produce unexpected results. If you encounter any issues, please verify the availability of the site and try again later.

Feel free to modify the test parameters.
