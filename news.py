from selenium.webdriver.support.expected_conditions import title_contains


class News:

    def __init__(self, title, url, data):
        self.title = title
        self.url = url
        self.data = data

    def get_title(self):
        return self.title

    def get_url(self):
        return self.url

    def get_data(self):
        return self.data