import time
import pytest
from pages.carrinho_page import CarrinhoPage
from pages.home_page import HomePage
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup_teardowm")
@pytest.mark.carrinho
@pytest.mark.smoke
class TestCT01:
    def test_ct01_adicionar_produto_carrinhos(self):
        login_page = LoginPage()
        home_page = HomePage()
        carrinho_page = CarrinhoPage()

        produto1 = "Sauce Labs Backpack"
        produto2 = "Sauce Labs Bike Light"

        # Faz login
        login_page.fazer_login("standard_user", "secret_sauce")
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

