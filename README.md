# Selenium Web Testing Framework
Project Overview:
This project provides a Selenium-based web testing framework with reusable components for common web testing scenarios. It includes utility classes for interacting with web elements and emulating various network conditions for testing purposes.

Files and Structure
baseclass.py
This module defines the SeleniumBase class, which encapsulates common Selenium interactions. It provides methods for checking element visibility, presence, clickability, and more. The class also includes a method for converting user-friendly locator strings to Selenium By constants.

network_settings.py
This module contains the NetworkSettings class, which offers methods for emulating different network conditions using Selenium WebDriver. It includes methods for simulating offline mode, slow 2G/3G, fast 4G/Wi-Fi connections, and intermittent network conditions.

StartPage.py
This module defines the StartPageLocators class, which extends SeleniumBase. It encapsulates specific locators and interactions for a sample start page. The class includes methods to retrieve the page header and a redirection link.

test_indicative.py
This test module uses PyTest and leverages the Page Object Model (POM) pattern. It includes tests for the start page, checking the correctness of the page header and the behavior of the redirection link.

# How to Use
Clone the Repository:
  git clone https://github.com/Revastein/Template_for_autotests.git
  cd Template_for_autotests.git

# Install Dependencies:
  pip install -r requirements.txt

# Run the Tests:
  pytest tests/test_indicative.py

# Contributors
  https://github.com/Revastein (Yan Kovzel')
