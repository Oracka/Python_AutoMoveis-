import json
#Leo = mexer no leitura banco
ARQUIVO = r"H:\H\PYTHON\ghRepository\Python_AutoMoveis--1\Python_AutoMoveis-\dados.json"

# Função que lê o banco de dados JSON e retorna um dicionário
# caminho tem valor padrão, então pode ser chamada sem argumentos: ler_banco()
def ler_banco():
    try:
        # Abre o arquivo no modo leitura com encoding UTF-8 para suportar acentos
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
            # Se o arquivo estiver vazio, avisa e retorna dicionário vazio
            if not dados:
                print("Arquivo vazio.")
                return {}
        # Converte o texto JSON em dicionário Python e retorna
        
        if isinstance(dados, dict):
            return dados
        else:
            return json.loads(dados)
        
    except FileNotFoundError:
        # Caso o arquivo não exista no caminho informado
        print(f"Arquivo '{ARQUIVO}' não encontrado.")
        return {}

    except json.JSONDecodeError as e:
        # Caso o conteúdo do arquivo não seja um JSON válido
        print(f"Erro ao decodificar JSON: {e}")
        return {}

# Função que salva o dicionário de volta no arquivo JSON
# dados = dicionário completo a ser salvo
# caminho tem valor padrão, então pode ser chamada apenas com: salvar_banco(dados)
def salvar_banco(dados: dict, caminho: str = ARQUIVO) -> None:
    # Abre o arquivo no modo escrita — sobrescreve o conteúdo anterior
    with open(caminho, "w", encoding="utf-8") as arquivo:
        # Converte o dicionário para JSON e salva no arquivo
        # ensure_ascii=False preserva acentos e caracteres especiais
        # indent=2 formata o JSON com recuo de 2 espaços, deixando legível
        json.dump(dados, arquivo, ensure_ascii=False, indent=2)