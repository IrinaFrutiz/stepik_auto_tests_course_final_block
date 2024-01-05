# Test Automation Repository

This repository contains automated tests for the Oscar Sandbox(a site for training autotests) and API tests for DummyAPI, utilizing Selenium, pytest, requests and allure.

## Allure report

[View the Allure report here.](https://irinafrutiz.github.io/stepik_auto_tests_course_final_block/)

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

3. Create a file named `.env` in the project directory. Open the [dummyapi.io](https://dummyapi.io/) website and register to obtain your API key. You can find the API key on the [Account](https://dummyapi.io/account) page or click "Generate App ID". In the `.env` file, add the following line, replacing `<YOUR_APP_ID>` with your actual API key:
```bash
APP_ID=<YOUR_APP_ID>
```
This step is necessary to provide the required API key for the tests.

4. Use the following commands to run the tests:

   - pytest -v --tb=line --language=en -m need_review
   - pytest -v --tb=line --language=fr
   - pytest -v
   - pytest -v --browser_name=firefox
   - pytest test_api_requests.py

By default, the tests will be executed using the Chrome browser and the `en-gb` language.

Please note that there might be instances when the site being tested is down or experiencing maintenance. In such cases, the tests may fail or produce unexpected results. If you encounter any issues, please verify the availability of the site and try again later.

Feel free to modify the test parameters.
