import pytest
import conftest
import time
from pages.home_page import HomePage
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup_teardowm")
@pytest.mark.loginValido
class TestCT02:
    def test_ct02_login_valido(self):
        # Instancia os objetos a serem usados no teste
        login_page = LoginPage()
        home_page = HomePage()

        username = "standard_user"
        password = "secret_sauce"

        # Faz login
        login_page.fazer_login(username, password)
        time.sleep(1)

        # Verifica se login foi realizado
        home_page.verificar_login_sucesso()
        time.sleep(1)

