def listas():
    cpf = ["50774811803"]
    cell = ["13974256075"]
    nome = ["Pedro Henrique Silva Quixabeira"]
    id_curso = [2]
    matricula = ["00001"]
    nome_curso = ["Análise e Desenvolvimento de Sistemas"]
    d_nascimento = ["13/03/2006"]

    return cpf,cell,nome,id_curso,matricula,nome_curso,d_nascimento

def imprimir(dados):

    cpf = dados[0]
    cell = dados[1]
    nome = dados[2]
    id_curso = dados[3]
    matricula = dados[4]
    nome_curso = dados[5]
    d_nascimento = dados[6]

    i = 0

    for indice in matricula:
            print(f"//Matricula: {matricula[i]}//\n\nCPF: {cpf[i]}\nNome: {nome[i]}\nId_curso: {id_curso[i]}\nNome_curso: {nome_curso[i]}\nCelular: {cell[i]}\nD_nascimento: {d_nascimento[i]}")
            print("---------------------------------------------------------")
            i = i + 1

    input("Pressione Enter para continuar...")

def start():
    dados = listas()
    imprimir(dados)

start()
