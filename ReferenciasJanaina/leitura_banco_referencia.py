# !! -Esse é o arquivo da Janaína que copiei aqui só caso a gente precise- !!
# DETALHE!: o nosso arquivo de leitura_banco também usou o código dela, mas
# eu acabei mudando ele um pouco então ele tá diferentinho desse aqui (que é
# uma cópia do arquivo que ela nos mandou no email)
# (chama lb.py porque lb = leitura_banco)


# Importa o módulo json, responsável por ler e escrever arquivos no formato JSON
import json

# Caminho completo do arquivo banco.json — usado como valor padrão nas funções
ARQUIVO = "C:/Users/janai/OneDrive/Documentos/modulos_funcoes/banco.json"


# Função que lê o banco de dados JSON e retorna um dicionário
# caminho tem valor padrão, então pode ser chamada sem argumentos: ler_banco()
def leitura_banco():
    try:
        # Abre o arquivo no modo leitura com encoding UTF-8 para suportar acentos
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:

            # Lê todo o conteúdo e remove espaços/quebras de linha nas bordas
            conteudo = arquivo.read().strip()

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