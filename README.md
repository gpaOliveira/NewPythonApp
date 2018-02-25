![Build Status](https://circleci.com/gh/gpaOliveira/NewPythonApp.svg?style=shield&circle-token=:circle-token)

# New App

A simple new application template for python based projects, powered by Flask and SQLAlchemy and tested by Unittest library with some enhancements (like groups of tests).

**Requirements:**

* Python 3.6.x (download & install: https://www.python.org/downloads/)
* Vagrant (**optional** download & install: https://www.vagrantup.com/downloads.html)

# Setup:

Regular setup.py install. 

Details can be found on **bootstrap.sh**, as the same file is also used for building up vagrant machines.

The server is started with **run_server.sh**.

<!-- 

# API Behavior

TBD

-->

# Routes

/v1/alive - To make sure the app is up and running, GET /v1/alive 

# Tests

To run all our tests, execute **run_all_tests.sh** or **python setup.py test**.

<!--
* A Junit output will be generated, named nose2-junit.xml
* A coverage report will be generated on the htmlcov folder

We have three types of tests:
* **Unit tests:** the ones that tests the application trough the controller directly. Run with **run_unit_tests.sh**.
* **Integration tests:** the ones that tests the application mainly trough the endpoints. Run with **run_integration_tests.sh**.
* **End-to-End tests:** the ones that handles the tests the application only by the endpoints
-->

<!---

# Docs

TBD
-->