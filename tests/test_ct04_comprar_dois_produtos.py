import time
import pytest
from pages.checkout_complete_page import CheckoutComplete
from pages.checkout_overview_page import CheckoutOverview
from pages.checkout_your_information_page import CheckoutYourInformation
from pages.carrinho_page import CarrinhoPage
from pages.home_page import HomePage
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup_teardowm")
@pytest.mark.ComprarProduto2
@pytest.mark.carrinho
class TestCT03:
    def test_ct03_comprar_um_produto(self):
        login_page = LoginPage()
        home_page = HomePage()
        carrinho_page = CarrinhoPage()
        checkout_information = CheckoutYourInformation()
        checkout_overview = CheckoutOverview()
        checkout_complete = CheckoutComplete()

        # Variaveis
        page_your_information = "Checkout: Your Information"
        page_overview = "Checkout: Overview"
        page_complete = "Checkout: Complete!"
        produto1 = "Sauce Labs Backpack"
        produto2 = "Sauce Labs Bike Light"
        first_name = "Leonardo"
        last_name = "Magalhães"
        postal_code = "13058699"

        # Faz login
        login_page.fazer_login("standard_user", "secret_sauce")
        time.sleep(1)

        # Verifica se login foi realizado
        home_page.verificar_login_sucesso()
        time.sleep(1)

        # Adicionando primeiro produto
        home_page.adicionar_ao_carrinho(produto1)
        time.sleep(1)

        # Clicando no carrinho
        home_page.acessar_carrinho()
        time.sleep(1)

        # Verificando se o produto esta no carrinho
        carrinho_page.verificar_produto_carrinho_existe(produto1)
        time.sleep(1)

        # Clicando no botão para voltar as compras
        carrinho_page.clicar_continuar_comprando()
        time.sleep(1)

        # Adicionando segundo produto
        home_page.adicionar_ao_carrinho(produto2)
        time.sleep(1)

        # Verificando se os dois produtos estão no carrinho
        home_page.acessar_carrinho()
        carrinho_page.verificar_produto_carrinho_existe(produto1)
        carrinho_page.verificar_produto_carrinho_existe(produto2)
        time.sleep(1)

        # Clicando em checkout
        carrinho_page.click_checkout()
        time.sleep(1)

        # Verificando se foi para a tela "Checkout: Your Information"
        checkout_information.check_page(page_your_information)
        time.sleep(1)

        # Preenchendo "firstName", "lastName" e "postalCode"
        checkout_information.infos(first_name, last_name, postal_code)
        time.sleep(1)

        # Clicando em continue
        checkout_information.clicking_continue()
        time.sleep(1)

        # Verificando se foi para a tela "Checkout: Overview"
        checkout_overview.check_page_overview(page_overview)
        time.sleep(1)

        # Clicando em finish
        checkout_overview.clicking_finish()
        time.sleep(1)

        # Verificando se foi para a tela "Checkout: Complete!"
        checkout_overview.check_page_overview(page_complete)
        time.sleep(1)

        # Clicando em "Back Home"
        checkout_complete.clicking_back_home()
        time.sleep(1)

        # Verificando se foi para a home page
        home_page.verificar_login_sucesso()
        time.sleep(1)
