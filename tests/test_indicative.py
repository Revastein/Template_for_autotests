import pytest
from pom.StartPage import StartPageLocators


@pytest.mark.usefixtures('setup')
class TestsMainSteps:

    def test_page_header(self):
        start_page = StartPageLocators(self.driver)
        start_page.get_page_header()

    def test_redirection_link(self):
        start_page = StartPageLocators(self.driver)
        start_page.get_redirection_link()
