import funcoes_gerais
import leitura_banco

#FUNÇÕES PARA EXIBIR PEÇAS DE ACORDO COM O MODELO DE VEÍCULO DESEJADO

# FUNÇÃO PARA CRIAR LISTA APENAS COM AS PEÇAS DO MODELO DE VEÍCULO DESEJADO
def exibir_peca_por_modelo_funcao(dados, modelo_desejado):
    # Esse código demandou uma pesquisa pra aprender... Vou tentar explicar:

    """
    Eu crio uma lista vazia (lista_pecas_filtradas = []) que depois vai receber
    todas as peças compatíveis com o veículo desejado.
    """
    lista_pecas_filtradas = []
    """
    Esse bloco "for" cria uma lista (lista_pecas) para receber todos os dicionários dentro
    de dados["pecas"]* (dados foi passado como parâmetro na função).
        *: lembrando que a estrutura de nosso arquivo json é:
        um dicionário com UMA chave (pecas), que tem uma LISTA como valor. Essa LISTA
        contém dicionários. Dessa maneira (exemplo):
        {
            "pecas": [
                {"id": 1, "peca": "Primeira peça", "veiculos": ["Porsche","Mustang"]}
                {"id": 2, "peca": "Segunda peça", "veiculos": ["Fusca","Kombi","Voyage"]}
                {"id": 3, "peca": "Terceira peça", "veiculos": ["Fusca","Kombi"]}
                {"id": 4, "peca": "Quarta peça", "veiculos": ["Mustang, Voyage"]}
                {"id": 5, "peca": "Quinta peça", "veiculos": ["Fusca"]}
            ]
        }
        eu espero que não tenha deixado sua cabeça ainda mais confusa...
    """
    for lista_pecas in dados["pecas"]:
        """
        Esse "if" verifica se o "modelo_desejado" (que foi passado como parâmetro para a função)
        está dentro da lista de "veiculos" ("veiculos" é uma chave dentro dos dicionário de
        "lista_pecas" que possue como valor uma lista de veículos).
        Em seguida, ele adiciona o dicionário que atende à condição à "lista_pecas_filtradas"

        pqp eu sinto que expliquei de maneira muito confusa... mas foi o que eu consegui
        """
        if modelo_desejado in lista_pecas["veiculos"]:
            lista_pecas_filtradas.append(lista_pecas)

    print(f"--PEÇAS COMPATÍVEIS COM {modelo_desejado.upper()}--")

    """
    Por último, um "for" passa por cada dicionário da lista "listaPecaFiltradas" e obtém o "id", "peca"
    e "fabricante" do item para printar ele na tela!
    CABOU
    """
    for items in lista_pecas_filtradas:
        id = items["id"]
        peca = items["peca"]
        fabricante = items["fabricante"]
        print(f"-{peca} - {fabricante} (ID: {id});")
    input("Pressione Enter para retornar ")

# FUNÇÃO PARA FUNCIONALIDADE DE PESQUISAR PEÇA POR MODELO DE VEÍCULO
def exibir_peca_por_modelo():
    while True:
        funcoes_gerais.clear_console()
        dados = leitura_banco.ler_banco()
        print("-----BD AUTOMOVEIS----")
        print("--Pesquisar peças por modelo de automóvel--")
        print("0 - Voltar")
        print("Modelos dísponíveis atualmente:")
        print("-Fusca;")
        print("-Kombi;")
        print("-Mustang;")
        print("-Porsche;")
        print("-Voyage.")
        try:
            modelo_desejado = input("Digite o modelo desejado: ").lower()
            match modelo_desejado:
                case "0":
                    acao = "Voltando"
                    funcoes_gerais.saindo(acao)
                    break
                case "fusca":
                    funcoes_gerais.clear_console()
                    modelo_desejado = (modelo_desejado.capitalize()) # TESTE ESSE CÓDIGO NO SEU COMPUTER THEO
                    exibir_peca_por_modelo_funcao(dados, modelo_desejado)
                case "kombi":
                    funcoes_gerais.clear_console()
                    modelo_desejado = "Kombi"
                    exibir_peca_por_modelo_funcao(dados, modelo_desejado)
                case "mustang":
                    funcoes_gerais.clear_console()
                    modelo_desejado = "Mustang"
                    exibir_peca_por_modelo_funcao(dados, modelo_desejado)
                case "porsche":
                    funcoes_gerais.clear_console()
                    modelo_desejado = "Porsche"
                    exibir_peca_por_modelo_funcao(dados, modelo_desejado)
                case "voyage":
                    funcoes_gerais.clear_console()
                    modelo_desejado = "Voyage"
                    exibir_peca_por_modelo_funcao(dados, modelo_desejado)
                case _:
                    print("\nModelo não identificado, pressione Enter para tentar novamente.")
                    input()
        except Exception as e:
            print(f"\nERRO: {e}")
