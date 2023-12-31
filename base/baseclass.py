from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ex_con
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from typing import List


class SeleniumBase:
    """Содержит основные методы для POM."""
    def __init__(self, driver):
        self.driver = driver
        self.__wait = WebDriverWait(driver, 20, 0.3)

    @staticmethod
    def __get_selenium_by(find_by: str) -> str:
        """
        Словарь с основными методами Selenium.
        :param find_by: css, xpath, class_name, id, link_text, name, partial_link_text, tag_name.
        :return: Возвращает метод по которому ищет элемент.
        """
        find_by = find_by.lower()
        locating = {'css': By.CSS_SELECTOR,
                    'xpath': By.XPATH,
                    'class_name': By.CLASS_NAME,
                    'id': By.ID,
                    'link_text': By.LINK_TEXT,
                    'name': By.NAME,
                    'partial_link_text': By.PARTIAL_LINK_TEXT,
                    'tag_name': By.TAG_NAME}
        return locating[find_by]

    def is_visible(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        return self.__wait.until(ex_con.visibility_of_element_located((self.__get_selenium_by(find_by), locator)),
                                 locator_name)

    def are_visible(self, find_by: str, locator: str, locator_name: str = None) -> List[WebElement]:
        return self.__wait.until(ex_con.visibility_of_all_elements_located((self.__get_selenium_by(find_by), locator)),
                                 locator_name)

    def is_present(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        return self.__wait.until(ex_con.presence_of_element_located((self.__get_selenium_by(find_by), locator)),
                                 locator_name)

    def is_not_present(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        return self.__wait.until(ex_con.invisibility_of_element_located((self.__get_selenium_by(find_by), locator)),
                                 locator_name)

    def are_present(self, find_by: str, locator: str, locator_name: str = None) -> List[WebElement]:
        return self.__wait.until(ex_con.presence_of_all_elements_located((self.__get_selenium_by(find_by), locator)),
                                 locator_name)

    def is_clickable(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        return self.__wait.until(ex_con.element_to_be_clickable((self.__get_selenium_by(find_by), locator)),
                                 locator_name)

    def is_invisible(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        return self.__wait.until(ex_con.invisibility_of_element_located((self.__get_selenium_by(find_by), locator)),
                                 locator_name)
