# Olha o grupo pra ver porque eu tirei meus códigos daqui ok!!
# -Theo
from datetime import datetime
import leitura_banco

# Eu comentei esse blocão de código porque não sei como ele será usado...
# Vocês podem usar ele se precisarem

def adicionar_pecas() -> None:  # adicionar novas peças aos dados.json(nome, tipo, parte, veiculos compativeis, fabricante e futuramente quant)
    # a função foi orientada a filtrar todos os erros possiveis antes de entrar no banco 
    dados = leitura_banco.leitura_banco()

    print("'''Campo de adição de peca \n'''")  

    peca = input("Nome da peça: ").strip().title()
    print(f"nova peça em criação.. {peca}")

    while True:
        tipo = input("tipo da peça: \n [1]-Mecanica | [2]-Eletronica | [3|-Interna | [4]-Externa | [5]-iluminação [ainda nao existente]-Cancelar Registro").strip()

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
            else:
                print("! Coloque uma opção viavel entre as 1 e 4")
        except ValueError:
            print("coloque um valor inteiro para escolher entre as opções")

    print(f"tipo de peça escolhida: {tipo} \n continuando...")

    if tipo == "Mecanica":
        while True:
            parte = input("qual é a parte referente da peça? | [1]-Suspensao | [2]-Freio | [3]-Escape").strip()
            try:
                if parte == "1":
                    parte = "Suspensao"
                    break
                elif parte == "2":
                    parte = "Freio"
                    break
                elif parte == "3":
                    parte = "Escape"
                    break
                else:
                    print("coloque uma opção viavel entre as opções")
            except ValueError:
                print("coloque um valor inteiro")

    elif tipo == "Eletronica":
        while True:
            parte = input("qual é a parte referente da peça? | [1]-Radio | [2]-painel | [3]-Carroceria(sensor)").strip()
            try:
                if parte == "1":
                    parte = "Radio"
                    break
                elif parte == "2":
                    parte = "Painel"
                    break
                elif parte == "3":
                    parte = "Carroceria"
                    break
                else:
                    print("coloque uma opção viavel entre as opções")
            except ValueError:
                print("coloque um valor inteiro")

    elif tipo == "Interna":   
        while True:
            parte = input("qual é a parte referente da peça? | [1]-Suspensao | [2]-Freio").strip()
            try: 
                if parte == "1":
                    parte = "Suspensao"
                    break
                elif parte == "2":
                    parte = "Freio"
                    break
                else:
                    print("coloque uma opção viavel entre as opções")
            except ValueError:
                print("coloque um valor inteiro")

    elif tipo == "Externa":   
        while True:
            parte = input("qual é a parte referente da peça? | [1]-Carroceria | [2]-Rodas").strip()
            try: 
                if parte == "1":
                    parte = "Carroceria"
                    break
                elif parte == "2":
                    parte = "Rodas"
                    break
                else:
                    print("coloque uma opção viavel entre as opções")
            except ValueError:
                print("coloque um valor inteiro")

    elif tipo == "Iluminação":
        while True:
            parte = input("qual é a parte referente da peça? | [1]-Frontal | [2]-Traseira | [3]-Interior").strip()
            try:
                if parte == "1":
                    parte = "Frontal"
                    break
                elif parte == "2":
                    parte = "Traseira"
                    break
                elif parte == "3":
                    parte = "Interior"
                    break
                else:
                    print("coloque uma opção viavel entre as opções")
            except ValueError:
                print("coloque um valor inteiro")

    print(f"Parte escolhida: {parte} \n  Continuando... ")

    opcoes = { # utilizei uma pesquisa a mais e o suporte da ia para essa soluçao, ja que tem muita abertura para erros 
        1: "Porsche",
        2: "Mustang",
        3: "Fusca",
        4: "Kombi",
        5: "Voyage"
    }

    print("Veículos compativeis com esta nova peça: ...")

    while True:
        try:
            veiculos = input("adicione 1 ou 3 modelo compatíveis para a peça")
            escolhas = [int(modelos.strip()) for modelos in veiculos.split(",")]

            if len(escolhas) == 0 or len(escolhas) > 3:
                print("aplique pelo menos um modelo de veiculo compativel ate no maximo 3..")

            escolhas = list(set(escolhas))

            if not all(modelo in opcoes for modelo in escolhas):
                print("opções invalidas, escolha as que estão disponiveis como 1 a 5")

            veiculos = [opcoes[modelo] for modelo in escolhas]
            break

        except ValueError:
            print("digite apenas NUMEROS separados por virgula") 

    print(f"peca compatível com os veiculos: {veiculos} continuando...")

    print("Fabricante da peça: ...")

    while True:
        try:
            fabricante = input("coloque o numero da fabricante da nova peça: ")
            if fabricante == "1":
                fabricante = "AutoLux Components"
                break
            elif fabricante == "2":
                fabricante = "NovaMotion Parts"
                break
            elif fabricante == "3":
                fabricante = "TitanDrive Industries"
                break
            else:
                print("coloque entre as 3 opções de fabricante")
        except ValueError:
            print("coloque um valor numero para escolher a fabricante")

    print(f"fabricante referente: {fabricante}. Continuando...")

    print("marcação de data...")

    while True:
        try:
            data_atual = datetime.now()
            data = input("escolha sua preferencia: ")

            if data == "1":
                while True:
                    try:
                        data_registrada = input(f"utilize esse modelo (ex: {data_atual})")
                        data = data_registrada
                        break
                    except ValueError:
                        print("coloque valores válidos")

            elif data == "2":
                data = data_atual
                break

        except ValueError:
            print("erro de data")

    peca = { # aqui pode mudar devido a parte do leo, mas aqui o dicionario que precisa ser adicionado ao dados.json ou no dados_completo.json
        # obs: ele segue a mesma estrutura do dados_completos.json
        "peca": peca,
        "tipo": tipo,
        "parte": parte,
        "veiculos": veiculos,
        "fabricante": fabricante,
        "data_fabricacao": str(data)
    }
    # adicionar depois um adicionador de id crescente, seja pelo o leitura ou no cadastro direto.






        



     







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

