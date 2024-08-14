import conftest
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckoutYourInformation(BasePage):

    def __init__(self):
        self.driver = conftest.driver
        self.page_your_information = (By.XPATH, "//span[@class='title' and text()='{}']")
        self.write_first_name = (By.ID, "first-name")
        self.write_last_name = (By.ID, "last-name")
        self.write_postal_code = (By.ID, "postal-code")
        self.button_click_continue = (By.ID, "continue")

    def check_page(self, nome_page):
        page = (self.page_your_information[0], self.page_your_information[1].format(nome_page))
        self.verificar_se_elemento_existe(page)

    def infos(self, first_name, last_name, postal_code):
        self.escrever(self.write_first_name, first_name)
        self.escrever(self.write_last_name, last_name)
        self.escrever(self.write_postal_code, postal_code)

    def clicking_continue(self):
        self.clicar(self.button_click_continue)
