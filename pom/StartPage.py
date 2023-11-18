from base.baseclass import SeleniumBase
from selenium.webdriver.remote.webelement import WebElement


class StartPageLocators(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        self.__page_header = "h1"
        self.__redirection_link = "a"

    def get_page_header(self):
        page_header = self.is_visible('tag_name', self.__page_header)
        assert page_header.text == "Example Domain"
        return page_header.text

    def get_redirection_link(self) -> WebElement:
        redirection_link = self.is_clickable('tag_name', self.__redirection_link)
        expected_url = 'https://www.iana.org/domains/example'
        assert self.driver.current_url == expected_url, 'Page did not redirect to the expected URL'
        return redirection_link
