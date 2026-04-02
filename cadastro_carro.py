# Olha o grupo pra ver porque eu tirei meus códigos daqui ok!!
# -Theo

import leitura_banco

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

