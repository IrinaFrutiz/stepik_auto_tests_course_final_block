# Test Automation Repository

This repository contains automated tests for web applications using Selenium and pytest.

## Prerequisites

Before running the tests, make sure you have the following:

- Chrome WebDriver: Download the latest version from [here](https://chromedriver.storage.googleapis.com/index.html?path=114.0.5735.90/) and place it in the `c:\chromedriver\` folder.
- Firefox WebDriver (geckodriver): Download the latest version from [here](https://github.com/mozilla/geckodriver/releases) and place it in the `c:\geckodriver\` folder.
- Python packages: Install Selenium and pytest by running the following command:

    ```
    pip install -r requirements.txt
    ```

## Running the Tests

To run the tests, use the following command:

- pytest -v --tb=line --language=en -m need_review
- pytest -v

By default, the tests will be executed using the Chrome browser and the `en-gb` language.

Please note that there might be instances when the site being tested is down or experiencing maintenance. In such cases, the tests may fail or produce unexpected results. If you encounter any issues, please verify the availability of the site and try again later.

Feel free to modify the test parameters.

