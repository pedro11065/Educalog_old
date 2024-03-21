import os #os.system('cls' if os.name == 'nt' else 'clear')

cpf = []
cell = []
nome = []
id_curso = []
matricula = []
nome_curso = []
d_nascimento = []

def tarefa():
    executando = True

    while executando:
        data_data = obter_tarefa()

        if data_data is None:
            break
        
        executando = call(data_data)

def obter_tarefa():
    while True:
        tarefa = input("\nO que deseja fazer?\n\n(A)Adicionar aluno \n(B)Buscar aluno \n(X)Excluir aluno \n(E)Editar aluno \n(L)Listar alunos\n:")
       
        if tarefa in ["A", "a"]:
            tarefa = 1
            
            tarefa_nome = "Adicionar"
            
            return tarefa, tarefa_nome
                    
        elif tarefa in ["B", "b"]:  
            tarefa = 2
            tarefa_nome = "Buscar"
            
            return tarefa, tarefa_nome         
            
        elif tarefa in ["X", "x"]:
            tarefa = 3
            tarefa_nome = "Excluir"
            
            return tarefa, tarefa_nome
                    
        elif tarefa in ["E", "e"]:
            tarefa = 4
            tarefa_nome = "Editar"
            
            return tarefa, tarefa_nome 

        elif tarefa in ["L", "l"]:
            tarefa = 5
            tarefa_nome = "Listar"

            return tarefa, tarefa_nome
        
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("#Erro 001#\n\nComando inválido.")
            continue

def call(data_data):
    tarefa = data_data[0]

    if tarefa == 1:
        Adicionar(data_data)
    elif tarefa == 2:
        Buscar(data_data)
    #... Lógica para outras tarefas

    continuar = input("Deseja continuar? (S/N): ")
    return continuar.upper() == 'S'

def Adicionar(data_data):

    cpf_true = 0
    nome_true = []
    lista_cursos = [1,2,3,4,5,6,7,8,9]
    x = 0
    i = 0

    tarefa = data_data[0]

    while x == 0:

        while x == 0: #CPF

            os.system('cls' if os.name == 'nt' else 'clear')
            print("Digite X para voltar para o menu.\n")  
            cpf_in = input("Digite seu CPF:")      

            if cpf_in in ["X","x"]:
                x = 1
                break
            if len(cpf_in) != 11:

                os.system('cls' if os.name == 'nt' else 'clear')#limpar terminal
                print("CPF inválido. #001#")
                continue 

            try:
                int(cpf_in)
                str(cpf_in)
            except:
                print("CPF inválido. #002#")
                continue

            if cpf_in in cpf:

                os.system('cls' if os.name == 'nt' else 'clear')
                print("Aluno já é matriculado. #003#")
                x = 1
                break

            cpf.append(cpf_in)
            break               
                    
        while x == 0: #NOME COMPLETO 

            nome_in = input("\nDigite o nome completo:")
            if nome_in in ["X","x"]:
                x = 1
                break
            try:
                nome_teste = nome_in.split(" ")
            except:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Nome inválido. #004#")
                continue

            if len(nome_in) <= 2:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Nome inválido. #005#")
                continue
            
            nome.append(nome_in)
            break

        while x == 0: #CURSO
 
            curso_in = input("\n\nSI - 1\nADS - 2\nLogística - 3\nGestão de RH - 4\nLogística AMS - 5\nGestão portuária - 6\nCiência de dados - 7\nGestão empresarial - 8\nProcessos gerenciais - 9\n\nCurso: ")
            if curso_in in ["X","x"]:
                x = 1
                break
            try:
                curso_in = int(curso_in)
            except:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Curso inválido. #006#")
                continue
            
            if curso_in in lista_cursos:
                if curso_in == 1:
                    curso_name = "Sistemas para internet"
                
                elif curso_in == 2:
                    curso_name = "Análie de Desenvolvimento de Sistemas"
                
                elif curso_in == 3:
                    curso_name = "Logística"
                
                elif curso_in == 4:
                    curso_name = "Gestão de RH"
                
                elif curso_in == 5:
                    curso_name = "Logística AMS"
                
                elif curso_in == 6:
                    curso_name = "Gestão portuária"
                
                elif curso_in == 7:
                    curso_name = "Ciência de dados"

                elif curso_in == 8:
                    curso_name = "Gestão empresarial"

                elif curso_in == 9:
                    curso_name = "Processos gerenciais"
                
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("#Erro #404#") ; x = 1 ; break
                
                id_curso.append(curso_in)
                nome_curso.append(curso_name)
                break

            else:
                print("Curso Inválido. #007#")
                continue

        while x == 0: #DATA DE NASCIMENTO
            
            nasc_in = input("\n\nData de nascimento(ex:13/03/2006): ")

            if nasc_in in ["X","x"]:
                x = 1
                break

            if len(nasc_in) == 10:
                try:
                    datas = nasc_in.split("/")     
                except:    
                    print("Ano de nascimento inválido. #008#")   
                    continue
                     
                try:
                    nasc_teste = datas[0]+datas[1]+datas[2]
                    nasc_teste = int(nasc_teste) 
                except:
                    print("Data de nascimento inválido. #009#")

                dia = int(datas[0])
                mes = int(datas[1])
                ano = int(datas[2])

                meses_31 = [1,3,5,7,8,10,12]

                ano_bissexto = [1924,1928,1932,1936,1940, 
                1944,1948,1952,1956,1960,1964,1968, 
                1972,1976,1980,1984,1988,1992,1996, 
                2000,2004,2008,2012, 2016,2020,2024]

                if dia > 29 and mes == 2 and ano in ano_bissexto: #fevereiro bissesto
                    print("Dia inválido. #010#")
                    continue
                elif dia > 28 and mes == 2 and ano not in ano_bissexto: #feveireiro não bissesto
                    print("Dia inválido. #011#")
                    continue

                elif dia == 31 and mes not in meses_31: #meses com 31 dias
                    print("Dia inválido. #012#")
                    continue

                elif dia > 31: #resto dos dias
                    print("Dia inválido. #013#")
                    continue

                elif mes > 12:
                    print("Mes inválido. #014#")
                    continue

                elif ano > 2008:
                    print("Ano inválido. #015#")
                    return
                
                d_nascimento.append(nasc_in)
                break

            if i > 4:
                print("Você é uma anta? sem barrinha caralho!")
                continue
            else:
                print("Data de nascimento inválida. #016#")
                i = i + 1
                continue

        while x == 0: #NUM DE TELEFONE

            cell_in = input("\n\nNúmero de telefone: ")
        
            if curso_in in ["X","x"]:
                x = 1
                break

            try:
                cell_in = int(cell_in)
                cell_in = str(cell_in)
            except:
                print("Número de telefone inválido. #017#")
                continue
            
            cell_len = len(cell_in)
            cell_len = str(cell_len)

            if len(cell_len) in  ["10", "11"]:
                print("Número de telefone inválido.#018#")
                continue

            cell.append(cell_in)
            break
            
        while x == 0: #MATRICULA
            
            cpf_matricula = int(cpf_in)
            curso_in = int(curso_in)
            matricula_out = len(matricula)+1
            matricula_out ='{:05d}'.format(matricula_out)

            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"\n\nA matricula do novo aluno é: {matricula_out}\n")

            input("Pressione Enter para continuar...")

            matricula.append(matricula_out)
            x = 1
            break
    return 0

def Buscar(data_data):

    x = 0
    i = 0

    tarefa = data_data[0]

    while x == 0:

        while x == 0:

            if len(matricula) != 0:

                print("Digite X para voltar para o menu.\n") 
                busca_in = input("Digite o nome completo ou a matricula do aluno: \n")

                if busca_in in ["X","x"]:
                    x = 1
                    break

                if busca_in in matricula:


                    indice = matricula.index(busca_in)

                    os.system('cls' if os.name == 'nt' else 'clear')
                    print()

                    print(f"CPF: {cpf[i]}")
                    print(f"Curso: {nome_curso[i]}")
                    print(f"Celular: {cell[i]}")
                    print(f"Nome completo: {nome[i]}")
                    print(f"Data de nascimento: {d_nascimento[i]}")

                    input("\nPressione Enter para continuar...")
                    os.system('cls' if os.name == 'nt' else 'clear')

                    x = 1
                    break
                    

                elif busca_in in nome:

                    indice = nome.index(busca_in)

                    os.system('cls' if os.name == 'nt' else 'clear')

                    print()

                    print(f"CPF: {cpf[i]}")  
                    print(f"Curso: {nome_curso[i]}")
                    print(f"Celular: {cell[i]}")
                    print(f"Matricula: {matricula[i]}")
                    print(f"Data de nascimento: {d_nascimento[i]}")

                    input("\nPressione Enter para continuar...")
                    os.system('cls' if os.name == 'nt' else 'clear')
                    
                    x = 1
                    break

                else:
                    print("Nome ou número de matricula inválido.")
                    continue
            else:
                print("Nenhum aluno matriculado para busca ser realizada.")
                x = 1
                return 

                      
# def Excluir(data_data)
        
# def Editar(data_data)
        
# def Listar(data_data)
        
tarefa()
 