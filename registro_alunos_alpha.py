#VERSÃO ALPHA DO EDUCALOG → GERENCIADOR DE ALUNOS
#by Pedro Quix


import os
#next update → Caso eu saia da operação durante a adição de um aluno novo, impedir que informações sejam registradas erroniamente.
#----------------------------------#
#DADOS → Onde todos os dados gerados serão armazenados.

def dados(): #"BANCO DE DADOS" #Armazena os dados em lists.

    cpf = [] #0
    tel = [] #1
    nome = [] #2
    id_curso = [] #3
    matricula = [] #4
    nome_curso = [] #5
    d_nascimento = [] #6

    #add_curso
    lista_cursos = [1,2,3,4,5,6,7,8,9] #7

    #add_nasc
    meses_31 = [1,3,5,7,8,10,12] #8

    ano_bissexto = [1924,1928,1932,1936,1940,1944,1948,1952,1956,1960,1964,1968,
                    1972,1976,1980,1984,1988,1992,1996,2000,2004,2008,2012, 2016,2020,2024] #9

    return cpf, tel, nome, id_curso, matricula, nome_curso, d_nascimento, lista_cursos, meses_31, ano_bissexto

dados = dados()

#----------------------------------#

#FUNÇÕES SIGLA → Economizam linhas e dão um aspecto mais limpo para o programa.(eu que inventei o nome "Funções sigla" ksksks)
    
def limpar_terminal(): #limpa o terminal
    os.system('cls' if os.name == 'nt' else 'clear')

def comando(data):#Mostra qual processo está sendo executado. 
    print(f"\ncomando: {data[1]}\n")

def print_exit():#Mostra a mensagem que indica como retornar para o menu.
    print("Digite X para voltar para o menu.\n")  

def exit(p=None):#Retorna um True ou False para sair do while e voltar para o menu
    
    if p in ["X","x"]:     
        return True
    else:
        return False

#----------------------------------#

    #INÍCIO → Funções mãe, responsáveis por inicializar os sistemas e as operações.

while True: #Looping

    def main(): #Menu principal e funções inicializadoras.
    
        def obter_tarefa(): #O QUE VAI SER REALIZADO? → MENU

            while True:
                limpar_terminal()
                
                print("  ＥＤＵＣＡＬＯＧ")
 
                print
                tarefa = input("\nComo podemos lhe ajudar?\n\n1 - Adicionar aluno \n2 - Buscar aluno \n3 - Excluir aluno \n4 - Editar aluno \n5 - Listar alunos\n:")
            
                if tarefa == "1": #ADICIONAR

                    tarefa = 1 ; tarefa_nome = "Adicionar"
                    limpar_terminal()
                    return tarefa, tarefa_nome
                            
                elif tarefa == "2": #BUSCAR

                    tarefa = 2 ; tarefa_nome = "Buscar"
                    limpar_terminal()
                    return tarefa, tarefa_nome         
                    
                elif tarefa == "3": #EXCLUIR
                    
                    tarefa = 3 ; tarefa_nome = "Excluir"
                    limpar_terminal()
                    return tarefa, tarefa_nome
                            
                elif tarefa == "4": #EDITAR

                    tarefa = 4 ; tarefa_nome = "Editar"
                    limpar_terminal()
                    return tarefa, tarefa_nome 

                elif tarefa == "5": #LISTAR
                    tarefa = 5 ; tarefa_nome = "Listar"
                    limpar_terminal()
                    return tarefa, tarefa_nome
                
                else: #erro      
                    limpar_terminal()
                    print("Resposta inválida, somente 1, 2, 3, 4 ou 5.")
                    continue

        data = obter_tarefa() 

        executar_funcoes(data)

    # ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ 
            
    def executar_funcoes(data):#Executa as funções processos que vão executar a sequência de comandos necessária de acordo ao pedido do usuário(dentro de start())

        tarefa = data[0]

        if tarefa == 1:
            Adicionar(data)
        elif tarefa == 2:
            Buscar(dados, data)
        elif tarefa == 3:
            Excluir(dados, data)
        elif tarefa == 4:
            Editar(dados, data)
        else:
            Listar(dados, data)

    #----------------------------------#

    # PROCESSOS → Vão realizar o que foi escolhido no menu pelo usúario.

    def Adicionar(data):#Adiciona um aluno novo ao sistema.

        def add_cpf(dados, data):#CPF do aluno novo. // subprocesso
            
            cpf_data = dados[0]

            while True:            
                comando(data) ; print_exit()

                cpf_in = input("Digite seu CPF:")     

                if exit(cpf_in) == True:
                    limpar_terminal(); break
                
                if cpf_in in cpf_data:

                    limpar_terminal()
                    print("Aluno já é matriculado. #001#")
                    input("Pressione Enter para continuar...")
                    break
                if len(cpf_in) != 11:

                    limpar_terminal()
                    print("CPF inválido. #002#")
                    input("Pressione Enter para continuar...")
                    continue            
                try:

                    int(cpf_in)
                    str(cpf_in)
                except:

                    limpar_terminal()
                    print("CPF inválido. #003#")
                    input("Pressione Enter para continuar...")
                    continue
                
                cpf_data.append(cpf_in)
                limpar_terminal()

                print(cpf_data)
                
                return True

            return False
        
        def add_nome(dados, data):#Nome completo do aluno novo. // subprocesso
            
            nome_data = dados[2]

            while True:            
                comando(data) ; print_exit()

                nome_in = input("Digite seu nome completo:")     

                if exit(nome_in) == True:
                    limpar_terminal() ; break
                
                try:
                    nome_teste = nome_in.split(" ")
                except:
                    break

                if len(nome_teste) <= 2:
                    limpar_terminal()
                    print("Nome inválido. #004#\n")
                    input("Pressione Enter para continuar...")
                    continue 

                for palavra in nome_teste:
                    if any(char.isdigit() for char in palavra):#Se tiver algum número em alguma palavra de nome_teste, vai dar break
                        limpar_terminal()
                        print("O nome contém um ou mais números.")
                        input("Pressione Enter para continuar...")
                        
                        break         

                nome_data.append(nome_in)
                limpar_terminal()

                return True
            
            return False
    
        def add_curso(dados, data):#Curso do aluno novo. // subprocesso

            while True:

                id_curso_data = dados[3]
                nome_curso_data = dados[5]
                lista_cursos = dados[7]

                comando(data) ; print_exit()

                curso_in = input("\n\nSI - 1\nADS - 2\nLogística - 3\nGestão de RH - 4\nLogística AMS - 5\nGestão portuária - 6\nCiência de dados - 7\nGestão empresarial - 8\nProcessos gerenciais - 9\n\nCurso: ")

                if exit(curso_in) == True:
                    limpar_terminal(); break
                
                try:
                    curso_in = int(curso_in)
                except:
                    limpar_terminal() ; print("Curso inválido. #006#")
                    input("Pressione Enter para continuar...")
                    continue
                
                if curso_in in lista_cursos:
                    
                    match curso_in:

                        case 1:
                            nome_curso = "Sistemas para internet"
                        
                        case 2:
                            nome_curso = "Análise de Desenvolvimento de Sistemas"
                        
                        case 3:
                            nome_curso = "Logística"
                        
                        case 4:
                            nome_curso = "Gestão de RH"
                        
                        case 5:
                            nome_curso = "Logística AMS"
                        
                        case 6:
                            nome_curso = "Gestão portuária"
                        
                        case 7:
                            nome_curso = "Ciência de dados"

                        case 8:
                            nome_curso = "Gestão empresarial"

                        case 9:
                            nome_curso = "Processos gerenciais"
                        
                        case _:
                            limpar_terminal()
                            print("#Erro #404#") ; x = 1 
                            input("Pressione Enter para continuar...")
                            break
                    
                    id_curso_data.append(curso_in)
                    nome_curso_data.append(nome_curso)

                    limpar_terminal()

                    return True

                else:
                    print("Curso Inválido. #007#")
                    input("Pressione Enter para continuar...")
                    continue

            return False
        
        def add_nasc(dados, data):#Data de nascimento do aluno novo. // subprocesso

            d_nascimento_data = dados[6]
            meses_31 = dados[8]
            ano_bissexto = dados[9]

            i = 0

            while True:            
                comando(data) ; print_exit()

                nasc_in = input("Digite sua data de nascimento(Ex:13/03/2006):")     

                if exit(nasc_in) == True:
                    limpar_terminal(); break
                

                if len(nasc_in) == 10:
                    try:
                        datas = nasc_in.split("/")     
                    except:    
                        print("Ano de nascimento inválido. #008#")  
                        input("Pressione Enter para continuar...") 
                        continue
                            
                    try:
                        nasc_teste = datas[0]+datas[1]+datas[2]
                        nasc_teste = int(nasc_teste) 
                    except:
                        print("Data de nascimento inválida. #009#")
                        input("Pressione Enter para continuar...")
                        continue

                    dia = int(datas[0])
                    mes = int(datas[1])
                    ano = int(datas[2])


                    if dia > 29 and mes == 2 and ano in ano_bissexto: #fevereiro bissesto
                        print("Dia inválido. #010#")
                        input("Pressione Enter para continuar...")
                        continue

                    elif dia > 28 and mes == 2 and ano not in ano_bissexto: #feveireiro não bissesto
                        print("Dia inválido. #011#")
                        input("Pressione Enter para continuar...")
                        continue

                    elif dia == 31 and mes not in meses_31: #meses com 31 dias
                        print("Dia inválido. #012#")
                        input("Pressione Enter para continuar...")
                        continue

                    elif dia > 31: #resto dos dias
                        print("Dia inválido. #013#")
                        input("Pressione Enter para continuar...")
                        continue

                    elif mes > 12:
                        print("Mes inválido. #014#")
                        input("Pressione Enter para continuar...")
                        continue

                    elif ano > 2008:
                        print("Ano inválido. #015#")
                        input("Pressione Enter para continuar...")
                        continue
                    
                    d_nascimento_data.append(nasc_in)
                    limpar_terminal()
                    
                    return True

                if i > 4:
                    print("Você é tá zoando né?")
                    input("Pressione Enter para continuar...")
                    continue
                else:
                    print("Data de nascimento inválida. #016#")
                    input("Pressione Enter para continuar...")
                    i = i + 1
                    continue
            
            return False

        def add_tel(dados, data):#Telefone do aluno novo. // subprocesso

            tel_data = dados[1]

            while True:

                comando(data) ; print_exit()

                tel_in = input("Digite seu número de telefone:")     

                if exit(tel_in) == True:
                    limpar_terminal(); break

                try:
                    tel_in = int(tel_in)
                    tel_in = str(tel_in)
                except:
                    print("Número de telefone inválido. #017#")
                    input("Pressione Enter para continuar...")
                    continue
                
                tel_len = len(tel_in)
                tel_len = str(tel_len)

                if len(tel_len) in  ["10", "11"]:
                    print("Número de telefone inválido.#018#")
                    input("Pressione Enter para continuar...")
                    continue

                tel_data.append(tel_in)
                limpar_terminal()

                return True
            
            return False       

        def new_matricula(dados,data):#CPF do aluno novo. // subprocesso

            matricula_data = dados[4]

            cpf_data = dados[0]
            ultimo_cpf_data = cpf_data[-1]

            id_curso_data = dados[3]
            ultimo_id_curso_data = id_curso_data[-1]

            cpf_matricula = int(ultimo_cpf_data)
            curso_in = int(ultimo_id_curso_data)

            matricula_out = len(matricula_data)+1
            matricula_out ='{:05d}'.format(matricula_out)

            limpar_terminal()

            print(f"\n\nA matricula do novo aluno é: {matricula_out}\n")

            input("Pressione Enter para continuar...")

            matricula_data.append(matricula_out)

            return True

        def exec_adicionar():# // subprocesso

            limpar_terminal()
            
            if add_cpf(dados, data): #Se for True...
                limpar_terminal()

                if add_nome(dados, data):
                    limpar_terminal()

                    if add_curso(dados, data):
                        limpar_terminal()

                        if add_nasc(dados, data):
                            limpar_terminal()

                            if add_tel(dados, data):
                                limpar_terminal()
                                new_matricula(dados, data)
                                main()

                            else: #Se for False...
                                main() #...Essa função é executada.

                        else:   

                            main()

                    else:  

                        main()

                else:

                    main()

            else:    

                main() 

        exec_adicionar()

    #|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||| (separar processos)
        
    def Buscar(dados, data):#Buscar aluno no Sistema

        def exec_buscar(dados, data):
                
            cpf_data = dados[0] 
            tel_data = dados[1] 
            nome_data = dados[2]
            id_curso_data = dados[3]
            matricula_data = dados[4] 
            nome_curso_data = dados[5] 
            d_nascimento_data = dados[6] 

            while True:            

                if len(matricula_data) != 0:

                    limpar_terminal(); comando(data) ; print_exit()

                    busca_in = input("Digite o nome completo ou a matricula do aluno: \n")

                    if exit(busca_in) == True:
                        limpar_terminal(); break

                    if busca_in in nome_data or matricula_data:

                        try:
                            i = nome_data.index(busca_in)
                        except:
                            i = matricula_data.index(busca_in)

                        limpar_terminal()
                        print()

                        print(f"CPF: {cpf_data[i]}")
                        print(f"Curso: {nome_curso_data[i]}")
                        print(f"Celular: {tel_data[i]}")      
                        print(f"Matricula: {matricula_data[i]}")         
                        print(f"Nome completo: {nome_data[i]}")
                        print(f"Data de nascimento: {d_nascimento_data[i]}")

                        input("\nPressione Enter para continuar...")
                        limpar_terminal()
                        
                        return
                    
                    else:
                        print("Nome ou matricula inválida.")
                        input("Pressione Enter para continuar...")
                        continue
                else:
                    print("Nenhum aluno cadastrado no sistema para ser excluído.")
                    input("Pressione Enter para continuar...")
                    break
            return

        exec_buscar(dados, data)

    #||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

    def Excluir(dados, data):#Excluir dados de um aluno

        def exec_excluir(dados, data):

            cpf_data = dados[0] 
            tel_data = dados[1] 
            nome_data = dados[2]
            id_curso_data = dados[3]
            matricula_data = dados[4] 
            nome_curso_data = dados[5] 
            d_nascimento_data = dados[6] 

            while True:

                limpar_terminal()
                comando(data); print_exit()

                if len(matricula_data) != 0:

                    excluir_in = input("Digite o nome completo ou a matricula do aluno: \n")

                    if exit(excluir_in) == True:
                        limpar_terminal(); break


                    elif excluir_in in nome_data or matricula_data:

                        try:
                            i = nome_data.index(excluir_in)
                        except:
                            i = matricula_data.index(excluir_in)

                        del(cpf_data[i])
                        del(tel_data[i])
                        del(nome_data[i])
                        del(id_curso_data[i])
                        del(matricula_data[i])
                        del(nome_curso_data[i])
                        del(d_nascimento_data[i])

                        limpar_terminal()
                        print("Dados deletados com sucesso.\n")
                        input("Pressione Enter para continuar...")
                        limpar_terminal()
                        break
                    else:
                        print("Nome ou matricula inválida.")
                        input("Pressione Enter para continuar...")
                        limpar_terminal()
                        continue

                else:
                    print("Nenhum aluno cadastrado no sistema para ser excluído.")
                    input("Pressione Enter para continuar...")
                    break

            return    

        exec_excluir(dados, data)

    #||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
        
    def Editar(dados, data):#Editar os dados e um aluno

        def exec_editar(dados, data):

            cpf_data = dados[0] 
            tel_data = dados[1] 
            nome_data = dados[2]
            id_curso_data = dados[3]
            matricula_data = dados[4] 
            nome_curso_data = dados[5] 
            d_nascimento_data = dados[6] 

            while True:

                comando(data) ; print_exit()

                if len(matricula_data) != 0:
            
                    editar_in = input("O que deseja editar? \n\n1 - CPF\n2 - Celular\n3 - Nome\n4 - Matricula\n5 - Curso\n6 - Data de nascimento\n: \n")
                    
                    if exit(editar_in) == True:
                        limpar_terminal(); break
                    
                    if editar_in in ["1","2","3","4","5","6"]:
                        limpar_terminal()
                        aluno_in = input("Digite o nome completo ou a matricula do aluno:")

                        if aluno_in in nome_data or matricula_data:

                            try:
                                i = nome_data.index(aluno_in)
                            except:
                                i = matricula_data.index(aluno_in)
                    
                            if editar_in == "1":

                                print(f"atual:{cpf_data[i]}\n")

                                edit = input("Editado:")

                                cpf_data.insert(i,edit)

                                limpar_terminal()
                                print("Valor editado com sucesso.\n")
                                input("Pressione Enter para continuar...")
                                limpar_terminal()
                                break                            
                        
                            elif editar_in == "2":

                                print(f"atual:{tel_data[i]}\n")

                                edit = input("Editado:")

                                tel_data.insert(i,edit)

                                limpar_terminal()
                                print("Valor editado com sucesso.\n")
                                input("Pressione Enter para continuar...")
                                limpar_terminal()
                                break                            
                        
                            elif editar_in == "3":

                                print(f"atual:{nome_data[i]}\n")

                                edit = input("Editado:")

                                nome_data.insert(i,edit)

                                limpar_terminal()
                                print("Valor editado com sucesso.\n")
                                input("Pressione Enter para continuar...")
                                limpar_terminal()
                                break                            

                            elif editar_in == "4":

                                print(f"atual:{matricula_data[i]}\n")

                                edit = input("Editado:")

                                matricula_data.insert(i,edit)

                                limpar_terminal()
                                print("Valor editado com sucesso.\n")
                                input("Pressione Enter para continuar...")
                                limpar_terminal()
                                break                            
                        
                            elif editar_in == "5":

                                print(f"atual:{nome_curso_data[i]}\n")

                                edit = input("Editado:")

                                nome_curso_data.insert(i,edit)

                                limpar_terminal()
                                print("Valor editado com sucesso.\n")
                                input("Pressione Enter para continuar...")
                                limpar_terminal()
                                break                            
                        

                            elif editar_in == "6":

                                print(f"atual:{d_nascimento_data[i]}\n")

                                edit = input("Editado:")

                                d_nascimento_data.insert(i,edit)

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
            return

        exec_editar(dados, data)

    #||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

    def Listar(dados, data):

        def exec_listar(dados, data):

            cpf_data = dados[0] 
            tel_data = dados[1] 
            nome_data = dados[2]
            id_curso_data = dados[3]
            matricula_data = dados[4] 
            nome_curso_data = dados[5] 
            d_nascimento_data = dados[6] 

            limpar_terminal()
            comando(data)

            if len(matricula_data) != 0:
                i = 0
                for indice in matricula_data:
                    print(f"//Matricula: {matricula_data[i]}//\n\nCPF: {cpf_data[i]}\nNome: {nome_data[i]}\nId_curso: {id_curso_data[i]}\nNome_curso: {nome_curso_data[i]}\nCelular: {tel_data[i]}\nD_nascimento: {d_nascimento_data[i]}")
                    print("---------------------------------------------------------")
                    i = i + 1

                input("Pressione Enter para continuar...")
                limpar_terminal()
                return

            else:
                print("Nenhum aluno cadastrado no sistema para ser listado.")
                input("Pressione Enter para continuar...")
                return
        
        exec_listar(dados, data)
        
    # ==========================================================#

    main()

