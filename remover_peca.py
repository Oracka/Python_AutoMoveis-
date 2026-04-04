import funcoes_gerais
import leitura_banco

#FUNÇÕES PARA REMOVER PEÇAS DO BD (nº3)

def remover_peca_funcao(dados):
    pass

def remover_peca():
    while True:
        funcoes_gerais.clear_console()
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
                    funcoes_gerais.saindo(acao)
                    break
                case 1 | 2:
                    print("\nFunção ainda não implementada.")
                    input()
                    funcoes_gerais.clear_console()
                case _:
                    print("\nERRO: Valor fora das opções.")
                    input()
                    funcoes_gerais.clear_console()
        except ValueError:
            print("\nERRO: Digite um valor númerico inteiro.")
            input()
        # E esse bloco vai tratar de todos os outros erros e registrá-los nessa variavel "e"
        except Exception as e:
            print(f"\nERRO: {e}")
            input()