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

# Eu comentei esse blocão de código porque não sei como ele será usado...
# Vocês podem usar ele se precisarem
"""
def cadastro_pecas() -> None: 



    dados = leitura_banco.leitura_banco()



    
    print("-- cadastro Aqui --")
    peca = input("nome peça: ")
    tipo = input("tipo: ")
    parte = input("parte: ")
    fabricante = input("fabricante: ")
    data = input("data de produção ")
    veiculo = input("veiculos compátiveis (separar por virgula) ")
    
    lista_veiculos = []

    novaPeca = {
    
        # "id": novo_id, 
        "peca": peca,   
        "tipo": tipo,
        "parte": parte,
        # "veiculos": lista_veiculos,
        
        "id": novo_id, # criar um id ba que adiciona +1 por cada nova peca para o banco
        "peca": peca,
        "tipo": tipo,
        "parte": parte,
        "veiculo": lista_veiculos, #  veiculos listados compativeis com a novaPeca
        
        "fabricante": fabricante,
        "data_fabricacao": data
        
    dados["peca"] = peca

    print(f"\na {peca} foi cadastrada || id referente: {}")

    leitura_banco.salvar_banco(dados)

    cadastro_pecas()
    }

    peca.append(novaPeca)


cadastro_pecas()
"""

clearConsole()
"""
# Essa pode ser a função principal que será rodada no main.py
def automoveis():
    while True:
        print("-----BD AUTOMOVEIS----")
        print("Por favor, digite:")
        print("0 - Sair;")
        print("1 - Pesquisar peças por modelo de automóvel;")
        try:
            opcao = int(input("Opção desejada: "))
            match opcao:
                case 0:
                    # Não assusta com esse trem não!! Eu só quis fazer um efeitozinho
                    # de "Saindo..." pra quando o usuário digitar "0". Eu pesquisei e
                    # esse código me ajudou a fazer isso. yay!
                    print("\n\rSaindo", end="", flush=True)
                    time.sleep(0.35)
                    print("\rSaindo.", end="", flush=True)
                    time.sleep(0.35)
                    print("\rSaindo..", end="", flush=True)
                    time.sleep(0.35)
                    print("\rSaindo...", end="", flush=True)
                    time.sleep(0.35)
                    break
                case 1:
                    clearConsole()
                    print("-----BD AUTOMOVEIS----")
                    print("--Pesquisar peças por modelo de automóvel--")
                    input()
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
            print(f"\nErro: {e}")
            input()
            break
#boa noite 👋👋
"""
# automoveis()

dados = leitura_banco.leitura_banco()
print(dados)
for item in dados["pecas"]:
    print(item["id"])