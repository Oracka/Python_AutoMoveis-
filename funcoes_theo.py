"""
Eu, Theo, estou tentando lembrar de colocar os comentário sempre ANTES das linhas
de código às quais elas se referem, ok?!? Gostaria de deixar esse aviso aqui porque
alguns comentários são BEM grandes e explicativos. Então, nesses casos, lembre-se de
rolar a página para verificar a linha de código à qual me refiro no comentário.

Ah, e eu to alternando entre comentários com o # e o """ """. Só avisando.

É isso obrigado pela atenção
"""

import leitura_banco
# Importei o "time" porque usei a função "time.sleep" pra fazer o programa esperar segundos.
# Eu imagino que ele também é usado para o tal do datetime né.
import time
# Importei esse "os" pra podermos limpar o terminal quando desejarmos.
# Eu simplesmente copiei um código que encontrei pra limpar tela:
# os.system('cls' if os.name == 'nt' else 'clear')
import os

def clearConsole(): 
    os.system('cls' if os.name == 'nt' else 'clear')

def saindo(acao: str):
    # Não assusta com esse trem não!! Eu só quis fazer um efeitozinho
    # de "Saindo..." pra quando o usuário digitar "0". Eu pesquisei e
    # esse código me ajudou a fazer isso. yay!

    # O parâmetro "acao" permite que você escolha que verbo você vai mostrar na tela com a animação
    # Exemplo: Saindo...; Voltando...;
    print(f"\n\r{acao}", end="", flush=True)
    time.sleep(0.25)
    print(f"\r{acao}.", end="", flush=True)
    time.sleep(0.25)
    print(f"\r{acao}..", end="", flush=True)
    time.sleep(0.25)
    print(f"\r{acao}...", end="", flush=True)
    time.sleep(0.25)

clearConsole()

# FUNÇÃO PARA CRIAR LISTA APENAS COM AS PEÇAS DO MODELO DE CARRO DESEJADO
def filtrarEMostrarPecasFuncao(dados, modeloDesejado):
    # Esse código demandou uma pesquisa pra aprender... Vou tentar explicar:

    """
    Eu crio uma lista vazia (listaPecasFiltradas = []) que depois vai receber
    todas as peças compatíveis com o veículo desejado.
    """
    listaPecasFiltradas = []
    """
    Esse bloco "for" cria uma lista (listaPecas) para receber todos os dicionários dentro
    de dados["pecas"]* (dados foi passado como parâmetro na função).
        *: lembrando que a estrutura de nosso arquivo json é:
        um dicionário com UMA chave (pecas), que tem uma LISTA como valor. Essa LISTA
        contém dicionários. Dessa maneira (exemplo):
        {
            "pecas": [
                {"id": 1, "peca": "Primeira peça", "veiculos": ["Porsche","Mustang"]}
                {"id": 2, "peca": "Segunda peça", "veiculos": ["Fusca","Kombi","Voyage"]}
                {"id": 3, "peca": "Terceira peça", "veiculos": ["Fusca","Kombi"]}
                {"id": 4, "peca": "Quarta peça", "veiculos": ["Mustang, Voyage"]}
                {"id": 5, "peca": "Quinta peça", "veiculos": ["Fusca"]}
            ]
        }
        eu espero que não tenha deixado sua cabeça ainda mais confusa...
    """
    for listaPecas in dados["pecas"]:
        """
        Esse "if" verifica se o "modeloDesejado" (que foi passado como parâmetro para a função)
        está dentro da lista de "veiculos" ("veiculos" é uma chave dentro dos dicionário de
        "listaPecas" que possue como valor uma lista de veículos).
        Em seguida, ele adiciona o dicionário que atende à condição à "listaPecasFiltradas"

        pqp eu sinto que expliquei de maneira muito confusa... mas foi o que eu consegui
        """
        if modeloDesejado in listaPecas["veiculos"]:
            listaPecasFiltradas.append(listaPecas)

    print(f"--PEÇAS COMPATÍVEIS COM {modeloDesejado.upper()}--")

    """
    Por último, um "for" passa por cada dicionário da lista "listaPecaFiltradas" e obtém o "id", "peca"
    e "fabricante" do item para printar ele na tela!
    CABOU
    """
    for items in listaPecasFiltradas:
        id = items["id"]
        peca = items["peca"]
        fabricante = items["fabricante"]
        print(f"-{peca} - {fabricante} (ID: {id});")
    input("Pressione Enter para retornar ")

# FUNÇÃO PARA FUNCIONALIDADE DE PESQUISAR PEÇA POR MODELO DE VEÍCULO
def pesquisarPecaPorModelo():
    while True:
        clearConsole()
        dados = leitura_banco.ler_banco()
        print("-----BD AUTOMOVEIS----")
        print("--Pesquisar peças por modelo de automóvel--")
        print("0 - Voltar")
        print("Modelos dísponíveis atualmente:")
        print("-Fusca;")
        print("-Kombi;")
        print("-Mustang;")
        print("-Porsche;")
        print("-Voyage.")
        try:
            modeloDesejado = input("Digite o modelo desejado: ").lower()
            match modeloDesejado:
                case "0":
                    acao = "Voltando"
                    saindo(acao)
                    break
                case "fusca":
                    clearConsole()
                    modeloDesejado = "Fusca"
                    filtrarEMostrarPecasFuncao(dados, modeloDesejado)
                case "kombi":
                    clearConsole()
                    modeloDesejado = "Kombi"
                    filtrarEMostrarPecasFuncao(dados, modeloDesejado)
                case "mustang":
                    clearConsole()
                    modeloDesejado = "Mustang"
                    filtrarEMostrarPecasFuncao(dados, modeloDesejado)
                case "porsche":
                    clearConsole()
                    modeloDesejado = "Porsche"
                    filtrarEMostrarPecasFuncao(dados, modeloDesejado)
                case "voyage":
                    clearConsole()
                    modeloDesejado = "Voyage"
                    filtrarEMostrarPecasFuncao(dados, modeloDesejado)
                case _:
                    print("\nModelo não identificado, tente novamente.")
                    input()
        except Exception as e:
            print(f"\nERRO: {e}")

"""
-perguntar ao usuário
1. remover peça
2. mostrar banco de dados
    -até que índice mostrar
"""
def removerPecaFuncao():
    

def removerPeca():
    while True:
        clearConsole()
        dados = leitura_banco.ler_banco()
        print("-----BD AUTOMOVEIS----")
        print("--Remover peças--")
        print("0 - Voltar;")
        print("1 - Remover peça;")
        print("2 - Mostrar banco de dados.")
        try:
            opcao = int(input("Opção desejada: "))
            match opcao:
                case 0:
                    acao = "Voltar"
                    saindo(acao)
                    break
        except ValueError:
            print("\nERRO: Digite um valor númerico inteiro.")
            input()
            clearConsole()
        # E esse bloco vai tratar de todos os outros erros e registrá-los nessa variavel "e"
        except Exception as e:
            print(f"\nErro: {e}")
            input()


# FUNÇÃO PRINCIPAL QUE RODARÁ NO MAIN.PY E CONTÉM AS FUNCIONALIDADES
def automoveis():
    while True:
        print("-----BD AUTOMOVEIS----")
        print("Por favor, digite:")
        print("0 - Sair;")
        print("1 - Pesquisar peças por modelo de automóvel;")
        print("2 - Remover peça.")
        try:
            opcao = int(input("Opção desejada: "))
            match opcao:
                case 0:
                    acao = "Saindo"
                    saindo(acao)
                    break
                case 1:
                    pesquisarPecaPorModelo()
                    clearConsole()
                case 2:
                    removerPeca()
                    clearConsole()
                # "case _:" funciona como um "default".
                # Ele é tipo o "else" no sentido de que vai rodar se nenhum dos
                # casos anteriores forem atendidos   
                case _:
                    print("\nERRO: Valor fora das opções.")
                    input()
                    clearConsole()
        # "ValueError" trata dos erros que ocorrem quando o valor inserido está fora do escopo* 
        # *: eu aacho que se diz escopo...
        # Exemplo: o valor "x" é inserido numa variável int (que só aceita valores inteiros)  
        except ValueError:
            print("\nERRO: Digite um valor númerico inteiro.")
            input()
            clearConsole()
        # E esse bloco vai tratar de todos os outros erros e registrá-los nessa variavel "e"
        except Exception as e:
            print(f"\nERRO: {e}")
            input()
            break
#boa noite 👋👋

automoveis()