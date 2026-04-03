# Olha o grupo pra ver porque eu tirei meus códigos daqui ok!!
# -Theo

import leitura_banco

<<<<<<< HEAD
# Eu comentei esse blocão de código porque não sei como ele será usado...
# Vocês podem usar ele se precisarem

def adicionar_pecas() -> None: # adicionar "pecas" ao bamco "dados", ele vai adicionando e aceita copias
    
    dados = leitura_banco.leitura_banco()

    print("'''Campo de adição de peca \n'''")

    peca_nome = input("Nome da peça: ").strip().title() # Sempre vai acionar uma Maiuscula no inicio de uma palavra(filtrar erros do usuario)

while True:
    tipo = input("tipo da peça: \n [1]-Mecanica | [2]-Eletronica | [3|-Interna | [4]-Externa | [5]-iluminação [ainda nao existente]-Cancelar Registro") # impedir que o usuario coloque algo alem de int no input e aceitar entre as duas opções 
    try:
        if tipo == "1":
            tipo = "Mecanica"
            break
        elif tipo == "2":
            tipo = "Eletronica"
            break
        elif tipo == "3":
            tipo = "Interna"
            break
        elif tipo == "4":
            tipo = "Externa"
            break 
        elif tipo == "5":
            tipo = "Iluminação"
        # ! adicionar depois uma alternativa de saida para o menu principal(main)
        else:
            print("! Coloque uma opção viavel entre as 1 e 4")
    except ValueError:
        print("coloque um valor inteiro para escolher entre as opções | EX( ... : 1 (vai aparecer 'mecanico' na saida))")

print(f"tipo de peça escolhida: {tipo} \n continuando...")

if tipo == "Mecanica":
     







def pesquisa_pecas():


    clearConsole()

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
                # Botei abluble só como placeholder
                print("\nabluble")
                # Coloquei esse input() só pra o código não rodar de uma vez sem o usuário conseguir ler
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
=======
def cadastro_pecas() -> None: 

    dados = leitura_banco.ler_banco()

    
    print("-- cadastro Aqui --")
    novo_id = 0 # Coloquei o valor de "0" só para o resto do código não ter erro de sintaxe
                # ("novo_id" is not defined), mas não tá certo!!
    peca = input("nome peça: ")
    tipo = input("tipo: ")
    parte = input("parte: ")
    fabricante = input("fabricante: ")
    data = input("data de produção ")
    veiculo = input("veiculos compátiveis (separar por virgula) ")
    
    lista_veiculos = []

    novaPeca = {
        "id": novo_id, # criar um id ba que adiciona +1 por cada nova peca para o banco
        "peca": peca,
        "tipo": tipo,
        "parte": parte,
        "veiculo": lista_veiculos, #  veiculos listados compativeis com a novaPeca
        
        "fabricante": fabricante,
        "data_fabricacao": data
        
    }
    dados["peca"] = peca

    print(f"\na {peca} foi cadastrada || id referente: {novo_id}")

    leitura_banco.salvar_banco(dados)

    cadastro_pecas()

    peca.append(novaPeca)

>>>>>>> ce9f1bc5d98af3ada8b815087018946a112ee064
