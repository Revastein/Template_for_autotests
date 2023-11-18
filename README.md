# Selenium Web Testing Framework

## Introduction

This project provides a robust Selenium-based web testing framework with reusable components for common web testing scenarios. It includes utility classes for interacting with web elements and emulating various network conditions for testing purposes.

## Files and Structure

- **`baseclass.py`**: This module defines the `SeleniumBase` class, which encapsulates common Selenium interactions. It provides methods for checking element visibility, presence, clickability, and more.

- **`network_settings.py`**: This module contains the `NetworkSettings` class, offering methods for emulating different network conditions using Selenium WebDriver.

- **`StartPage.py`**: This module defines the `StartPageLocators` class, which extends `SeleniumBase`. It encapsulates specific locators and interactions for a sample start page.

- **`test_indicative.py`**: This test module uses PyTest and leverages the Page Object Model (POM) pattern. It includes tests for the start page, checking the correctness of the page header and the behavior of the redirection link.

## How to Use

1. **Clone the Repository:**
   ```
   git clone https://github.com/Revastein/Template_for_autotests.git
   cd Template_for_autotests
   ```
2. **Install Dependencies:**
  ```
  pip install -r requirements.txt
  ```
3. **Run the Tests:**
   ```
   pytest tests/test_indicative.py
   ```
# Contributors
  [Yan Kovzel'](https://github.com/Revastein)
