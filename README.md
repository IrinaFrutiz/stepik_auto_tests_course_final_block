# Test Automation Repository

This repository contains automated tests for web application using Selenium and pytest.

## Allure report

[You can find allure report here.](https://irinafrutiz.github.io/stepik_auto_tests_course_final_block/)

## Prerequisites

Before running the tests, make sure you have the following:

- Python packages: Install Selenium and pytest by running the following command:

    ```
    pip install -r requirements.txt
    ```
    
## Running the Tests

To run the tests, use the following command:

- pytest -v --tb=line --language=en -m need_review
- pytest -v --tb=line --language=fr
- pytest -v
- pytest -v --browser_name=firefox 

By default, the tests will be executed using the Chrome browser and the `en-gb` language.

Please note that there might be instances when the site being tested is down or experiencing maintenance. In such cases, the tests may fail or produce unexpected results. If you encounter any issues, please verify the availability of the site and try again later.

Feel free to modify the test parameters.

