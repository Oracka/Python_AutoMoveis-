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

def clear_console(): 
    os.system('cls' if os.name == 'nt' else 'clear')

def saindo(acao: str):
    # Não assusta com esse trem não!! Eu só quis fazer um efeitozinho
    # de "Saindo..." pra quando o usuário digitar "0". Eu pesquisei e
    # esse código me ajudou a fazer isso. yay!

    # O parâmetro "acao" permite que você escolha que verbo você vai mostrar na tela com a animação
    # Exemplo: Saindo...; Voltando...;
    segundos = 0.20
    print(f"\n\r{acao}", end="", flush=True)
    time.sleep(segundos)
    print(f"\r{acao}.", end="", flush=True)
    time.sleep(segundos)
    print(f"\r{acao}..", end="", flush=True)
    time.sleep(segundos)
    print(f"\r{acao}...", end="", flush=True)
    time.sleep(segundos)

# ///////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////

def exibir_bd_funcao(banco_pecas, inicio, fim):
    clear_console()
    dados = leitura_banco.ler_banco()
    # ---TEMPORARIO:
    banco_pecas = []
    for item in dados["pecas"]:
        banco_pecas.append(item)
    # ---
    primeiro_registro = banco_pecas[0]
    ultimo_registro = banco_pecas[-1]

    if inicio == primeiro_registro["id"] and fim == ultimo_registro["id"]:
        print("--BANCO DE PEÇAS (TODOS)--")
    else:
        print(f"--BANCO DE PEÇAS ({inicio} A {fim})--")

    item = 0
    for banco_pecas in banco_pecas:
        id = banco_pecas["id"]
        peca = banco_pecas["peca"]
        tipo = banco_pecas["tipo"]
        parte = banco_pecas["parte"]
        veiculos = banco_pecas["veiculos"]
        fabricante = banco_pecas["fabricante"]
        data_fabricacao = banco_pecas["data_fabricacao"]
        item += 1
        if item >= inicio and item <= fim:
            print(f"---ID: {id} | PEÇA: {peca} | VEÍCULOS: {veiculos}\n   TIPO: {tipo} | PARTE: {parte} | FABRICANTE: {fabricante}\n   DATA DA FABRICAÃO: {data_fabricacao}")
    input("Pressione Enter para retornar ")

def definir_inicio_e_fim_funcao(escopo_atual, tamanho_banco):
    while True:
        clear_console()
        print("-----BD AUTOMOVEIS----")
        print("--Exibir banco de peças--")
        print("0 - Voltar")
        print("1 - Exibir banco")
        print(f"2 - Definir quantidade de registros a serem exibidos (ATUAL: {escopo_atual})")
        print("Opção desejada: 2")
        try:
            inicio = int(input("\nDigite o valor de início: "))
            break
        except ValueError:
            print("\nERRO: Digite um valor númerico inteiro.")
            input()
        except Exception as e:
            print(f"\nERRO: {e}")
            input()
    aviso_tamanho_inicio = ""
    if inicio > tamanho_banco:
        aviso_tamanho_inicio = f"(O valor inserido ({inicio}) excede o número de peças do banco ({tamanho_banco}))"
        inicio = tamanho_banco
    elif inicio < 1:
        aviso_tamanho_inicio = f"(O valor inserido ({inicio}) é menor que 1)"
        inicio = 1
    while True:
        clear_console()
        print("-----BD AUTOMOVEIS----")
        print("--Exibir banco de peças--")
        print("0 - Voltar")
        print("1 - Exibir banco")
        print(f"2 - Definir quantidade de registros a serem exibidos (ATUAL: {escopo_atual})")
        print("Opção desejada: 2")
        print(f"\nDigite o valor de início: {inicio} {aviso_tamanho_inicio}")
        try:
            fim = int(input("Digite o valor final: "))
            break
        except ValueError:
            print("\nERRO: Digite um valor númerico inteiro.")
            input()
        except Exception as e:
            print(f"\nERRO: {e}")
            input()
    if fim < inicio:
        aviso_tamanho_fim = f"(O valor inserido ({fim}) é menor que o valor de início ({inicio}))"
        fim = inicio
    if fim > tamanho_banco:
        aviso_tamanho_inicio = f"(O valor inserido ({inicio}) excede o número de peças do banco ({tamanho_banco}))"
        fim = tamanho_banco
    return inicio, fim

def exibir_bd(banco_pecas, inicio, fim):
        primeiro_registro = banco_pecas[0]
        ultimo_registro = banco_pecas[-1]
        while True:
            clear_console()
            if inicio == primeiro_registro["id"] and fim == ultimo_registro["id"]:
                escopo_atual = f"Todos [{len(banco_pecas)}]"
            else:
                escopo_atual = f"{inicio} a {fim}"
            print("-----BD AUTOMOVEIS----")
            print("--Exibir banco de peças--")
            print("0 - Voltar")
            print("1 - Exibir banco")
            print(f"2 - Definir quantidade de registros a serem exibidos (ATUAL: {escopo_atual})")
            try:
                opcao = int(input("Opção desejada: "))
                match opcao:
                    case 0:
                        acao = "Voltando"
                        saindo(acao)
                        break
                    case 1:
                        exibir_bd_funcao(banco_pecas, inicio, fim)
                    case 2:
                        inicio, fim = definir_inicio_e_fim_funcao(escopo_atual, len(banco_pecas))
            except ValueError:
                print("\nERRO: Digite um valor númerico inteiro.")
                input()
            except Exception as e:
                print(f"\nERRO: {e}")
                input()

# ///////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////

# FUNÇÃO PARA CRIAR LISTA APENAS COM AS PEÇAS DO MODELO DE CARRO DESEJADO
def exibir_peca_por_modelo_funcao(dados, modelo_desejado):
    # Esse código demandou uma pesquisa pra aprender... Vou tentar explicar:

    """
    Eu crio uma lista vazia (lista_pecas_filtradas = []) que depois vai receber
    todas as peças compatíveis com o veículo desejado.
    """
    lista_pecas_filtradas = []
    """
    Esse bloco "for" cria uma lista (lista_pecas) para receber todos os dicionários dentro
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
    for lista_pecas in dados["pecas"]:
        """
        Esse "if" verifica se o "modelo_desejado" (que foi passado como parâmetro para a função)
        está dentro da lista de "veiculos" ("veiculos" é uma chave dentro dos dicionário de
        "lista_pecas" que possue como valor uma lista de veículos).
        Em seguida, ele adiciona o dicionário que atende à condição à "lista_pecas_filtradas"

        pqp eu sinto que expliquei de maneira muito confusa... mas foi o que eu consegui
        """
        if modelo_desejado in lista_pecas["veiculos"]:
            lista_pecas_filtradas.append(lista_pecas)

    print(f"--PEÇAS COMPATÍVEIS COM {modelo_desejado.upper()}--")

    """
    Por último, um "for" passa por cada dicionário da lista "listaPecaFiltradas" e obtém o "id", "peca"
    e "fabricante" do item para printar ele na tela!
    CABOU
    """
    for items in lista_pecas_filtradas:
        id = items["id"]
        peca = items["peca"]
        fabricante = items["fabricante"]
        print(f"-{peca} - {fabricante} (ID: {id});")
    input("Pressione Enter para retornar ")

# FUNÇÃO PARA FUNCIONALIDADE DE PESQUISAR PEÇA POR MODELO DE VEÍCULO
def exibir_peca_por_modelo():
    while True:
        clear_console()
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
            modelo_desejado = input("Digite o modelo desejado: ").lower()
            match modelo_desejado:
                case "0":
                    acao = "Voltando"
                    saindo(acao)
                    break
                case "fusca":
                    clear_console()
                    modelo_desejado = "Fusca"
                    exibir_peca_por_modelo_funcao(dados, modelo_desejado)
                case "kombi":
                    clear_console()
                    modelo_desejado = "Kombi"
                    exibir_peca_por_modelo_funcao(dados, modelo_desejado)
                case "mustang":
                    clear_console()
                    modelo_desejado = "Mustang"
                    exibir_peca_por_modelo_funcao(dados, modelo_desejado)
                case "porsche":
                    clear_console()
                    modelo_desejado = "Porsche"
                    exibir_peca_por_modelo_funcao(dados, modelo_desejado)
                case "voyage":
                    clear_console()
                    modelo_desejado = "Voyage"
                    exibir_peca_por_modelo_funcao(dados, modelo_desejado)
                case _:
                    print("\nModelo não identificado, tente novamente.")
                    input()
        except Exception as e:
            print(f"\nERRO: {e}")

# ///////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////

def remover_peca_funcao(dados):
    for lista_pecas in dados["pecas"]:
        lista_pecas.append[dados]

        print(lista_pecas)

def remover_peca():
    while True:
        clear_console()
        dados = leitura_banco.ler_banco()
        print("-----BD AUTOMOVEIS----")
        print("--Remover peças--")
        print("0 - Voltar;")
        print("1 - Remover peça;")
        print("2 - Exibir banco de dados.")
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
        # E esse bloco vai tratar de todos os outros erros e registrá-los nessa variavel "e"
        except Exception as e:
            print(f"\nERRO: {e}")
            input()

# ///////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////

# FUNÇÃO PRINCIPAL QUE RODARÁ NO MAIN.PY E CONTÉM AS FUNCIONALIDADES
def automoveis():
    while True:
        clear_console()
        print("-----BD AUTOMOVEIS----")
        print("Por favor, digite:")
        print("0 - Sair;")
        print("1 - Exibir banco de dados;")
        print("2 - Pesquisar peças por modelo de automóvel;")
        print("3 - Remover peça.")
        try:
            opcao = int(input("Opção desejada: "))
            match opcao:
                case 0:
                    acao = "Saindo"
                    saindo(acao)
                    break
                case 1:
                    dados = leitura_banco.ler_banco()
                    banco_pecas = []
                    for item in dados["pecas"]:
                        banco_pecas.append(item)
                    inicio = 1
                    fim = len(banco_pecas)
                    exibir_bd(banco_pecas, inicio, fim)
                    clear_console()
                case 2:
                    exibir_peca_por_modelo()
                    clear_console()
                case 3:
                    remover_peca()
                    clear_console()
                # "case _:" funciona como um "default".
                # Ele é tipo o "else" no sentido de que vai rodar se nenhum dos
                # casos anteriores forem atendidos   
                case _:
                    print("\nERRO: Valor fora das opções.")
                    input()
                    clear_console()
        # "ValueError" trata dos erros que ocorrem quando o valor inserido está fora do escopo* 
        # *: eu aacho que se diz escopo...
        # Exemplo: o valor "x" é inserido numa variável int (que só aceita valores inteiros)  
        except ValueError:
            print("\nERRO: Digite um valor númerico inteiro.")
            input()
        # E esse bloco vai tratar de todos os outros erros e registrá-los nessa variavel "e"
        except Exception as e:
            print(f"\nERRO: {e}")
            input()
            break
#boa noite 👋👋

automoveis()