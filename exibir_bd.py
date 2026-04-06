import funcoes_gerais
import leitura_banco
#FUNÇÕES PARA EXIBIR BANCO DE DADOS (nº1)

def exibir_bd_funcao(banco_pecas, inicio, fim):
    funcoes_gerais.clear_console()
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
            print(f"---ID: {id} | PEÇA: {peca} | VEÍCULOS: {veiculos}\n   TIPO: {tipo} | PARTE: {parte} | FABRICANTE: {fabricante}\n   DATA DA FABRICAÇÃO: {data_fabricacao}")
    input("Pressione Enter para retornar ")

def definir_inicio_e_fim_funcao(escopo_atual, tamanho_banco):
    while True:
        funcoes_gerais.clear_console()
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
        funcoes_gerais.clear_console()
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
            funcoes_gerais.clear_console()
            if inicio == primeiro_registro["id"] and fim == ultimo_registro["id"]:
                escopo_atual = f"Todos [{len(banco_pecas)}]"
            elif inicio == fim:
                escopo_atual = inicio
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
                        funcoes_gerais.saindo(acao)
                        break
                    case 1:
                        exibir_bd_funcao(banco_pecas, inicio, fim)
                    case 2:
                        inicio, fim = definir_inicio_e_fim_funcao(escopo_atual, len(banco_pecas))
                    case _:
                        print("\nERRO: Valor fora das opções.")
                        input()
                        funcoes_gerais.clear_console()
            except ValueError:
                print("\nERRO: Digite um valor númerico inteiro.")
                input()
            except Exception as e:
                print(f"\nERRO: {e}")
                input()