import os #os.system('cls' if os.name == 'nt' else 'clear')

cpf = [] #0
cell = [] #1
nome = [] #2
id_curso = [] #3
matricula = [] #4
nome_curso = [] #5
d_nascimento = [] #6
lista_cursos = [1,2,3,4,5,6,7,8,9] #7
 
#### ENTRADA ########

def tarefa():
    executando = True

    while executando:
        data_data = obter_tarefa()

        if data_data is None:
            break
        
        executando = call(data_data)

def obter_tarefa():
    while True:
        tarefa = input("\nO que deseja fazer?\n\n1 - Adicionar aluno \n2 - Buscar aluno \n3 - Excluir aluno \n4 - Editar aluno \n5 - Listar alunos\n:")
       
        if tarefa == "1":
            tarefa = 1
            
            tarefa_nome = "Adicionar"

            limpar_terminal()
            
            return tarefa, tarefa_nome
                    
        elif tarefa == "2":  
            tarefa = 2
            tarefa_nome = "Buscar"

            limpar_terminal()
            
            return tarefa, tarefa_nome         
            
        elif tarefa == "3":
            tarefa = 3
            tarefa_nome = "Excluir"

            limpar_terminal()
            
            return tarefa, tarefa_nome
                    
        elif tarefa == "4":
            tarefa = 4
            tarefa_nome = "Editar"

            limpar_terminal()
            
            return tarefa, tarefa_nome 

        elif tarefa == "5":
            tarefa = 5
            tarefa_nome = "Listar"

            limpar_terminal()

            return tarefa, tarefa_nome
        
        else:
            limpar_terminal()
            continue

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def call(data_data):
    tarefa = data_data[0]

    if tarefa == 1:
        Adicionar(data_data)
    elif tarefa == 2:
        Buscar(data_data)
    elif tarefa == 3:
        Excluir(data_data)
    elif tarefa == 4:
        Editar(data_data)
    else:
        Listar(data_data)

    continuar = input("Deseja continuar? (S/N): ")
    limpar_terminal()
    return continuar.upper() == 'S'

#### PROCESSAMENTO SAÍDA ###########

def Adicionar(data_data):

    lista_cursos = [1,2,3,4,5,6,7,8,9]
    x = 0
    i = 0

    tarefa_nome = data_data[1]

    #adicionar input("Pressione Enter para continuar...")
               #limpar_terminal()  
    #depois de erros

    #adicinar limpar_terminal() no antes de inputs

    while x == 0: #CPF

        print(f"\ncomando: {tarefa_nome}\n")

        print("Digite X para voltar para o menu.\n")  
        cpf_in = input("Digite seu CPF:")      

        if cpf_in in ["X","x"]:
            x = 1
            break

        if len(cpf_in) != 11:

            limpar_terminal()
            print("CPF inválido. #001#")
            continue 

        try:
            int(cpf_in)
            str(cpf_in)
        except:
            limpar_terminal()
            print("CPF inválido. #002#")
            continue

        if cpf_in in cpf:

            limpar_terminal()
            print("Aluno já é matriculado. #003#")
            x = 1
            break

        cpf.append(cpf_in)
        limpar_terminal()
        break               
                        
    while x == 0: #NOME

        nome_in = input("\nDigite o nome completo: ")

        if nome_in.upper() == 'X':
            x = 1
            break
        
        if len(nome_in) <= 2:
            limpar_terminal()
            print("Nome inválido. #004#\n")
            continue
        
        nome_teste = nome_in.split(" ")
        
        if len(nome_teste) < 2:
            limpar_terminal()
            print("Nome inválido. #005#\n")
            continue
        
        nome.append(nome_in)
        limpar_terminal()
        break                                 

    while x == 0: #CURSO

        curso_in = input("\n\nSI - 1\nADS - 2\nLogística - 3\nGestão de RH - 4\nLogística AMS - 5\nGestão portuária - 6\nCiência de dados - 7\nGestão empresarial - 8\nProcessos gerenciais - 9\n\nCurso: ")
        if curso_in in ["X","x"]:
            x = 1
            break
        try:
            curso_in = int(curso_in)
        except:
            limpar_terminal()
            print("Curso inválido. #006#")
            continue
        
        if curso_in in lista_cursos:
            if curso_in == 1:
                curso_name = "Sistemas para internet"
            
            elif curso_in == 2:
                curso_name = "Análise de Desenvolvimento de Sistemas"
            
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
                limpar_terminal()
                print("#Erro #404#") ; x = 1 ; break
            
            id_curso.append(curso_in)
            nome_curso.append(curso_name)
            limpar_terminal()
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
            limpar_terminal()
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
        limpar_terminal()
        break 
        
    while x == 0: #MATRICULA
        
        cpf_matricula = int(cpf_in)
        curso_in = int(curso_in)
        matricula_out = len(matricula)+1
        matricula_out ='{:05d}'.format(matricula_out)

        limpar_terminal()
        print(f"\n\nA matricula do novo aluno é: {matricula_out}\n")

        input("Pressione Enter para continuar...")

        matricula.append(matricula_out)
        x = 1
        break

def Buscar(data_data):

    x = 0
    i = 0

    tarefa_nome = data_data[1]

    while x == 0:

        if len(matricula) != 0:

            print(f"\ncomando: {tarefa_nome}\n")

            print("Digite X para voltar para o menu.\n") 
            busca_in = input("Digite o nome completo ou a matricula do aluno: \n")

            if busca_in in ["X","x"]:
                break

            if busca_in in nome or matricula:

                try:
                    i = nome.index(busca_in)
                except:
                    i = matricula.index(busca_in)

                limpar_terminal()
                print()

                print(f"CPF: {cpf[i]}")
                print(f"Curso: {nome_curso[i]}")
                print(f"Celular: {cell[i]}")      
                print(f"Matricula: {matricula[i]}")         
                print(f"Nome completo: {nome[i]}")
                print(f"Data de nascimento: {d_nascimento[i]}")

                input("\nPressione Enter para continuar...")
                limpar_terminal()
                break
            else:
                print("Nome ou matricula inválida.")
                continue
        else:
            print("Nenhum aluno cadastrado no sistema para ser excluído.")
            break
                
def Excluir(data_data):

    i = 0
    x = 0

    tarefa_nome = data_data[1]

    while x == 0:

        print(f"\ncomando: {tarefa_nome}\n")

        if len(matricula) != 0:

            print("Digite X para voltar para o menu.\n") 
            excluir_in = input("Digite o nome completo ou a matricula do aluno: \n")

            if excluir_in in ["X","x"]:
                x = 1
                break

            elif excluir_in in nome or matricula:

                try:
                    i = nome.index(excluir_in)
                except:
                    i = matricula.index(excluir_in)

                del(cpf[i])
                del(cell[i])
                del(nome[i])
                del(id_curso[i])
                del(matricula[i])
                del(nome_curso[i])
                del(d_nascimento[i])

                limpar_terminal()
                print("Dados deletados com sucesso.\n")
                input("Pressione Enter para continuar...")
                limpar_terminal()
                break
            else:
                print("Nome ou matricula inválida.")
                limpar_terminal()
                continue

        else:
            print("Nenhum aluno cadastrado no sistema para ser excluído.")
            break
          
def Editar(data_data):

    x = 0

    tarefa_nome = data_data[1]

    while x == 0:

        print(f"\ncomando: {tarefa_nome}\n")

        if len(matricula) != 0:

            print("Digite X para voltar para o menu.\n")            
            editar_in = input("O que deseja editar? \n\n1 - CPF\n2 - Celular\n3 - Nome\n4 - Matricula\n5 - Curso\n6 - Data de nascimento\n: \n")
            
            if editar_in in ["X","x"]:
                break
            
            if editar_in in ["1","2","3","4","5","6"]:
                limpar_terminal()
                aluno_in = input("Digite o nome completo ou a matricula do aluno:")

                if aluno_in in nome or matricula:

                    try:
                        i = nome.index(aluno_in)
                    except:
                        i = matricula.index(aluno_in)
              
                    if editar_in == "1":

                        print(f"atual:{cpf[i]}\n")

                        edit = input("Editado:")

                        cpf.insert(i,edit)

                        limpar_terminal()
                        print("Valor editado com sucesso.\n")
                        input("Pressione Enter para continuar...")
                        limpar_terminal()
                        break                            
                
                    elif editar_in == "2":

                        print(f"atual:{cell[i]}\n")

                        edit = input("Editado:")

                        cell.insert(i,edit)

                        limpar_terminal()
                        print("Valor editado com sucesso.\n")
                        input("Pressione Enter para continuar...")
                        limpar_terminal()
                        break                            
                
                    elif editar_in == "3":

                        print(f"atual:{nome[i]}\n")

                        edit = input("Editado:")

                        nome.insert(i,edit)

                        limpar_terminal()
                        print("Valor editado com sucesso.\n")
                        input("Pressione Enter para continuar...")
                        limpar_terminal()
                        break                            

                    elif editar_in == "4":

                        print(f"atual:{matricula[i]}\n")

                        edit = input("Editado:")

                        matricula.insert(i,edit)

                        limpar_terminal()
                        print("Valor editado com sucesso.\n")
                        input("Pressione Enter para continuar...")
                        limpar_terminal()
                        break                            
                
                    elif editar_in == "5":

                        print(f"atual:{nome_curso[i]}\n")

                        edit = input("Editado:")

                        nome_curso.insert(i,edit)

                        limpar_terminal()
                        print("Valor editado com sucesso.\n")
                        input("Pressione Enter para continuar...")
                        limpar_terminal()
                        break                            
                

                    elif editar_in == "6":

                        print(f"atual:{d_nascimento[i]}\n")

                        edit = input("Editado:")

                        d_nascimento.insert(i,edit)

                        limpar_terminal()
                        print("Valor editado com sucesso.\n")
                        input("Pressione Enter para continuar...")
                        limpar_terminal()
                        break                            
                

                    else:
                        print("Erro inesperado, tente novamente.")        
                        input("Pressione Enter para continuar...")                    
                
                else:
                    print("Nome inválido ou matricula inválida.")   
                    input("Pressione Enter para continuar...")
                    limpar_terminal()                
                    continue

            else:
                print("Comando inválido.\n")
                input("Pressione Enter para continuar...")
                limpar_terminal()
                continue
        else:
            print("Nenhum aluno cadastrado no sistema para ser editado.")
            input("Pressione Enter para continuar...")
            limpar_terminal()
            break
        
def Listar(data_data):

    x = 0
    tarefa_nome = data_data[1]

    print(f"\ncomando: {tarefa_nome}\n")

    if len(matricula) != 0:
        i = 0
        for indice in matricula:
            print(f"//Matricula: {matricula[i]}//\n\nCPF: {cpf[i]}\nNome: {nome[i]}\nId_curso: {id_curso[i]}\nNome_curso: {nome_curso[i]}\nCelular: {cell[i]}\nD_nascimento: {d_nascimento[i]}")
            print("---------------------------------------------------------")
            i = i + 1

        input("Pressione Enter para continuar...")
        limpar_terminal()

    else:
        print("Nenhum aluno cadastrado no sistema para ser listado.")
        input("Pressione Enter para continuar...")
     
tarefa()
