import leitura_banco

def cadastro_pecas() -> None: 




    print("-- cadastro Aqui --")
    peca = input("nome peça: ")
    tipo = input("tipo: ")
    parte = input("parte: ")
    fabricante = input("fabricante: ")
    data = input("data de produção ")
    veiculo = input("veiculos compátiveis (separar por virgula) ")

    novaPeca = {
        "id": novo_id, 
        "peca": peca,
        "tipo": tipo,
        "parte": parte,
        "veiculos": lista_veiculos,
        "fabricante": fabricante,
        "data_fabricacao": data
    }

    peca.append(novaPeca)

    cadastro_pecas()
