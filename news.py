from selenium.webdriver.support.expected_conditions import title_contains


class News:

    def __init__(self, title, url, date):
        self.title = title
        self.url = url
        self.date = date