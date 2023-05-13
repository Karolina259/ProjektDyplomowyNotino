class BasePage:

    def __init__(self, driver):
        self.driver = driver
        # Kazda strona bedzie sie automatycznie sprawdzala
        self._verify_page()

    def _verify_page(self):
        pass
