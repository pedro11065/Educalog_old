import os

def limpar_terminal(): #limpa o terminal
    os.system('cls' if os.name == 'nt' else 'clear')

def exit(p=None):
    
    if p in ["X","x"]:     
        return True
    else:
        return False

while True:
    cpf_in = input("Digite seu CPF:")   

    if exit(cpf_in) == True:
        break

    limpar_terminal()

    print(f"Seu CPF é: {cpf_in}")

print("Você saiu do sistema pela função exit().") 