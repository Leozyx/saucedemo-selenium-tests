import conftest
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckoutOverview(BasePage):

    def __init__(self):
        self.driver = conftest.driver
        self.page_checkout_overview = (By.XPATH, "//span[@class='title' and text()='{}']")
        self.button_click_finish = (By.ID, "finish")

    def check_page_overview(self, nome_page):
        page = (self.page_checkout_overview[0], self.page_checkout_overview[1].format(nome_page))
        self.verificar_se_elemento_existe(page)

    def clicking_finish(self):
        self.clicar(self.button_click_finish)
