from selenium.webdriver.support.expected_conditions import title_contains


class News:

    def __init__(self, title, url):
        self.title = title
        self.url = url

    def get_title(self):
        return self.title

    def get_url(self):
        return self.url