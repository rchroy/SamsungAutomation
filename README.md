# SamsungPhoneTest
A page object model framework using python and selenium to extract data from the Samsung website.
# Prerequisites for running the project
Must have Python3.9 installed

Must have Pycharm installed

Must have selenium package added

Must have pytest package added

Folder containing Chromedriver and Geckodriver must be in the environment variable


# Code to run complete test suite in CMD

Run In Chrome

py.test tests/test_suite.py --browser chrome

Run In Firefox

py.test tests/test_suite.py --browser firefox

# Code to run all the tests including test suite in CMD

Run In Chrome

py.test -s -v --browser chrome

Run In Firefox

py.test -s -v --browser firefox

The log file is generated in Automation.log file that includes various logs.

It also contains various text that is extracted from the website
