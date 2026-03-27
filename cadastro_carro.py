import leitura_banco # importando outro doc é possível utilizar suas  funções e classes

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
        "id": novo_id, # criar um id ba que adiciona +1 por cada nova peca para o banco
        "peca": peca,
        "tipo": tipo,
        "parte": parte,
        "veiculo": lista_veiculos, #  veiculos listados compativeis com a novaPeca
        "fabricante": fabricante,
        "data_fabricacao": data
    }

    peca.append(novaPeca)

    dados["peca"] = peca

    print(f"\na {peca} foi cadastrada || id referente: {}")

    leitura_banco.salvar_banco(dados)

    cadastro_pecas()

    
