import leitura_banco

def adicionar_pecas() -> None: # adicionar "pecas" ao bamco "dados", ele vai adicionando e aceita copias
    
    dados = leitura_banco.ler_banco()

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