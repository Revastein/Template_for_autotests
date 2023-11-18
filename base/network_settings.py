import time


class NetworkSettings:
    """
    Предоставляет методы для эмуляции различных сетевых условий в тестах,
    используя инструменты Selenium WebDriver.

    Методы класса позволяют эмулировать отсутствие подключения, медленные и быстрые
    2G, 3G, 4G, и Wi-Fi соединения, а также нестабильное соединение.
    """
    @staticmethod
    def offline(driver):
        """
        Эмулирует отсутствие подключения.

        :param driver: Экземпляр Selenium WebDriver
        :return: Обновленный экземпляр WebDriver
        """
        network_conditions = {
            'offline': True,
            'latency': 0,
            'download_throughput': 0,
            'upload_throughput': 0
        }
        driver.set_network_conditions(**network_conditions)
        return driver

    @staticmethod
    def slow_2g(driver):
        """
        Эмулирует медленное 2G подключение.

        :param driver: Экземпляр Selenium WebDriver
        :return: Обновленный экземпляр WebDriver
        """
        network_conditions = {
            'offline': False,
            'latency': 500,
            'download_throughput': 500 * 1024,
            'upload_throughput': 250 * 1024
        }
        driver.set_network_conditions(**network_conditions)
        return driver

    @staticmethod
    def slow_3g(driver):
        """
        Эмулирует медленное 3G подключение.

        :param driver: Экземпляр Selenium WebDriver
        :return: Обновленный экземпляр WebDriver
        """
        network_conditions = {
            'offline': False,
            'latency': 200,
            'download_throughput': 1.5 * 1024 * 1024,
            'upload_throughput': 750 * 1024
        }
        driver.set_network_conditions(**network_conditions)
        return driver

    @staticmethod
    def fast_4g(driver):
        """
        Эмулирует быстрое 4G подключение.

        :param driver: Экземпляр Selenium WebDriver
        :return: Обновленный экземпляр WebDriver
        """
        network_conditions = {
            'offline': False,
            'latency': 20,
            'download_throughput': 25 * 1024 * 1024,
            'upload_throughput': 10 * 1024 * 1024
        }
        driver.set_network_conditions(**network_conditions)
        return driver

    @staticmethod
    def fast_wifi(driver):
        """
        Эмулирует быстрое Wi-Fi подключение.

        :param driver: Экземпляр Selenium WebDriver
        :return: Обновленный экземпляр WebDriver
        """
        network_conditions = {
            'offline': False,
            'latency': 5,
            'download_throughput': 100 * 1024 * 1024,
            'upload_throughput': 50 * 1024 * 1024
        }
        driver.set_network_conditions(**network_conditions)
        return driver

    @staticmethod
    def intermittent_connection(driver):
        """
        Эмулирует нестабильное соединение.

        :param driver: Экземпляр Selenium WebDriver
        :return: Обновленный экземпляр WebDriver
        """
        network_conditions = {
            'offline': False,
            'latency': 50,
            'download_throughput': 10 * 1024 * 1024,
            'upload_throughput': 5 * 1024 * 1024
        }

        driver.set_network_conditions(**network_conditions)
        time.sleep(2)

        network_conditions['offline'] = True
        driver.set_network_conditions(**network_conditions)
        time.sleep(2)

        return driver
