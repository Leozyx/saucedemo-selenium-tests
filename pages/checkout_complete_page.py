import conftest
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckoutComplete(BasePage):

    def __init__(self):
        self.driver = conftest.driver
        self.page_checkout_complete = (By.XPATH, "//span[@class='title' and text()='{}']")
        self.button_click_back_home = (By.ID, "back-to-products")

    def check_page_complete(self, nome_page):
        page = (self.page_checkout_complete[0], self.page_checkout_complete[1].format(nome_page))
        self.verificar_se_elemento_existe(page)

    def clicking_back_home(self):
        self.clicar(self.button_click_back_home)

