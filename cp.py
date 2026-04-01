# !!-Esse é o arquivo da Janaína que copiei aqui só caso a gente precise- !!
# (chama cp.py porque cp = cadastro_pecas)


# Importa o módulo de leitura do banco, que contém as funções ler_banco e salvar_banco
import leitura_banco

# Função que exibe as opções já existentes no banco antes do cadastro
# Recebe a lista de peças como parâmetro
def cadastrar_peca():
    estoque = leitura_banco.leitura_banco()
    
    
    print("\n--- Cadastro de Peça ---")
    
    peca = input("Nome da peça: ").lower()
    
    if peca in estoque:
        quantidade = estoque[peca]["quantidade"]
        print(f"Já existem {quantidade} unidades dessa peça no estoque.")
        
        opcao = input("Deseja atualizar/cadastrar mais? (1 = sim / 2 = não): ")
        if opcao != "1":
            return  # sai da função
    
    else:
        print("Peça não encontrada no estoque.")
        opcao = input("Digite 1 para cadastrar nova peça ou qualquer tecla para sair: ")
        if opcao != "1":
            return
    
    # 👇 Só chega aqui se o usuário quiser cadastrar
    print("\n--- Preencha os dados da peça ---")
    
    tipo       = input("Tipo: ")
    parte      = input("Parte: ")
    fabricante = input("Fabricante: ")
    data       = input("Data de fabricação (AAAA-MM-DD): ")
    veiculos   = input("Veículos compatíveis (separados por vírgula): ")
    quantidade = int(input("Quantidade: "))
    
    # salva no dicionário
    estoque[peca] = {
        "tipo": tipo,
        "parte": parte,
        "fabricante": fabricante,
        "data": data,
        "veiculos": [v.strip() for v in veiculos.split(",")],
        "quantidade": quantidade
    }
    
    # salva no banco
    leitura_banco.salvar_banco(estoque)
    
    print("✅ Peça cadastrada com sucesso!")



cadastrar_peca() 