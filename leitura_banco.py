import json

ARQUIVO = r"C:\Users\tpere\Downloads\Python_AutoMoveis-\dados.json"

# Função que lê o banco de dados JSON e retorna um dicionário
# caminho tem valor padrão, então pode ser chamada sem argumentos: ler_banco()
def leitura_banco():
    try:
        # Abre o arquivo no modo leitura com encoding UTF-8 para suportar acentos
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
            return dados
            # Se o arquivo estiver vazio, avisa e retorna dicionário vazio
            if not conteudo:
                print("Arquivo vazio.")
                return {}
            
            # Converte o texto JSON em dicionário Python e retorna
            return json.loads(conteudo)
        
    # Caso o arquivo não exista no caminho informado
    except FileNotFoundError:
        print(f"Arquivo '{ARQUIVO}' não encontrado.")
        return {}

    # Caso o conteúdo do arquivo não seja um JSON válido
    except json.JSONDecodeError as e:
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