import json
#Criação de variaveis
caminho_Json = r"H:\H\PYTHON\ghRepository\Python_AutoMoveis-\dados.json"

#FUNÇÃO QUE LÊ O QUE ESTA NO BANCO(JSON --> Python)
def lerJson():
    #open(arquivo que vai ser lido, modo(escrever (w), ler (r) ou etc), encoding="utf=8" -> permitir caracteres especiais)
    with open(caminho_Json, "r", encoding="utf=8") as json_saida:
        #json.load = pega os dados do arquivo json
        #json.loads = transforma o json em string no python
        data_transform = json_saida.read()
    return json.loads(data_transform)

#FUNÇÃO QUE GUARDA AS INFORMAÇÕES DE CADASTRO(Python --> JSON)
#Sera usada logo após as informações do cadastro serem colocadas
#Função que mandara as infos para json
def salvarJson(dados_python:dict, caminho:str = caminho_Json) ->None:
    with open(caminho_Json,"w",encoding="utf=8") as json_entrada:
        #json.dump -> dicionário python para 
        #json.dump(o_que_vou_salvar,arquivo_onde_vai_ser_salvo)
        json.dump(dados_python, json_entrada, ensure_ascii=False, indent=2)
        #indent=2 formato a json com recuo de 2 espaços
        #ensure_ascii=false -> preserva acentos e caracteres especiais
