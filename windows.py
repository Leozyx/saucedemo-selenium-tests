import tkinter as tk
import subprocess


def executar_comando(comando, cenario):
    try:
        result = subprocess.run(comando, check=True, capture_output=True, text=True)
        mensagem = f"Sucesso: {cenario} executado com sucesso.\n\n{result.stdout}"
    except subprocess.CalledProcessError as e:
        mensagem = f"Erro: Falha ao executar {cenario}.\n\n{e.stderr}"

    output_text.insert(tk.END, mensagem + "\n" + "=" * 80 + "\n")
    output_text.see(tk.END)


# Função para executar o comando
def executar_cenario_1():
    #
    comando = ["pytest", "tests/test_ct01_adicionar_produto_carrinho.py"]
    executar_comando(comando, "Adicionar produto ao carrinho")


def executar_cenario_2():
    #
    comando2 = ["pytest", "tests/test_ct02_login_valido.py"]
    executar_comando(comando2, "Login valido")


def executar_cenario_3():
    #
    comando3 = ["pytest", "tests/test_ct03_comprar_um_produto.py"]
    executar_comando(comando3, "Comprar um produto")


def executar_cenario_4():
    #
    comando4 = ["pytest", "tests/test_ct04_comprar_dois_produtos.py"]
    executar_comando(comando4, "Comprar dois produtos")


def executar_cenario_5():
    #
    comando5 = ["pytest"]
    executar_comando(comando5, "Todos os cenários")


# Criar a janela principal
janela = tk.Tk()
janela.title("Cenarios de teste")

# Criar o botão e associá-lo à função
botao_executar_cenario_1 = tk.Button(janela, text="Cenario 1", command=executar_cenario_1)
botao_executar_cenario_1.pack(pady=20)

botao_executar_cenario_2 = tk.Button(janela, text="Cenario 2", command=executar_cenario_2)
botao_executar_cenario_2.pack(pady=20)

botao_executar_cenario_3 = tk.Button(janela, text="Cenario 3", command=executar_cenario_3)
botao_executar_cenario_3.pack(pady=20)

botao_executar_cenario_4 = tk.Button(janela, text="Cenario 4", command=executar_cenario_4)
botao_executar_cenario_4.pack(pady=20)

botao_executar_cenario_5 = tk.Button(janela, text="Todos os cenarios existentes", command=executar_cenario_5)
botao_executar_cenario_5.pack(pady=20)

# Criar um widget de texto para exibir a saída do comando
output_text = tk.Text(janela, height=20, width=80)
output_text.pack(pady=10)

# Iniciar o loop principal da interface gráfica
janela.mainloop()
