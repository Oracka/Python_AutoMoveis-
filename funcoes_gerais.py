import leitura_banco
# Importei o "time" porque usei a função "time.sleep" pra fazer o programa esperar segundos.
# Eu imagino que ele também é usado para o tal do datetime né.
import time
# Importei esse "os" pra podermos limpar o terminal quando desejarmos.
# Eu simplesmente copiei um código que encontrei pra limpar tela:
# os.system('cls' if os.name == 'nt' else 'clear')
import os
import exibir_bd
import exibir_pecas_por_veiculo
import remover_peca

def clear_console(): 
    os.system('cls' if os.name == 'nt' else 'clear')

def saindo(acao: str):
    # Não assusta com esse trem não!! Eu só quis fazer um efeitozinho
    # de "Saindo..." pra quando o usuário digitar "0". Eu pesquisei e
    # esse código me ajudou a fazer isso. yay!

    # O parâmetro "acao" permite que você escolha que verbo você vai mostrar na tela com a animação
    # Exemplo: Saindo...; Voltando...;
    segundos = 0.3
    
    print(f"\n\r{acao}", end="", flush=True)
    time.sleep(segundos)
    print(f"\r{acao}.", end="", flush=True)
    time.sleep(segundos)
    print(f"\r{acao}..", end="", flush=True)
    time.sleep(segundos)
    print(f"\r{acao}...", end="", flush=True)
    time.sleep(segundos)

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
                    exibir_bd.exibir_bd(banco_pecas, inicio, fim)
                    clear_console()
                case 2:
                    exibir_pecas_por_veiculo.exibir_peca_por_modelo()
                    clear_console()
                case 3:
                    remover_peca.remover_peca()
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