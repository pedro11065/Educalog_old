import pandas as pd
from openpyxl import Workbook

def listas():

    cpf = ["2222222222","1111111111"]
    cell = ["13974256075","991376136"]
    nome = ["Pedro Henrique Silva Quixabeira","Daniela Maluy Da Silva"]
    id_curso = [2,1]
    matricula = ["00001","00002"]
    nome_curso = ["Analise e Desenvolvimento de Sistemas","Sistemas para Internet"]
    d_nascimento = ["13/03/2006","20/03/1972"]

    return cpf,cell,nome,id_curso,matricula,nome_curso,d_nascimento

def start():

    dados = listas()
    imprimir(dados)

def imprimir(dados):

    cpf = dados[0]
    cell = dados[1]
    nome = dados[2]
    id_curso = dados[3]
    matricula = dados[4]
    nome_curso = dados[5]
    d_nascimento = dados[6]

    df = pd.DataFrame(dados)

    nome_arquivo = "dados.xlsx"

    try:
        with pd.ExcelWriter(nome_arquivo) as writer:
            df.to_excel(writer, index=False)
        print("Dados exportados para", nome_arquivo)
    except Exception as e:
        print("Ocorreu um erro ao exportar para o Excel:", e)

start()