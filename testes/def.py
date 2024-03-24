import os

def funcoes(data):
    
    def def_nome():
        nome_in = input("Digite seu nome:")
        return nome_in
    
    def limpar_terminal():
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def saida(nome):
        nome_out = nome
        print(f"Seu nome é {nome_out}")

    ######################
    def executar_funcoes(data):
        if 1 in data:
            nome = def_nome()

        if 2 in data:
            limpar_terminal()
    
        if 3 in data:
            saida(nome)

    executar_funcoes(data)
    
def start():

    def set_data():
        data = 1,2,3
        return data
    
    data = set_data()

    funcoes(data)

start()