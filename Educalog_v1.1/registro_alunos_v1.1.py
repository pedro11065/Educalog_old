#VERSÃO 1.1 DO EDUCALOG → GERENCIADOR DE ALUNOS
#UPDATE → Reformulação da estrutura de armazenamento de dados para a futura integração com o banco de dados
#PostGreSQL nas atualizações futuras.

#import psycopg2
#from psycopg2 import Error
import os
#----------------------------------#
#DADOS → Onde todos os dados gerados serão armazenados.

def database():#DATABASE# Função responsável por armazenar os dados gerados em um banco de dados PostGreSQL

    cpf = [] #0
    tel = [] #1
    nome = [] #2
    id_curso = [] #3
    matricula = [] #4
    nome_curso = [] #5
    d_nascimento = [] #6

    return cpf, tel, nome, id_curso, matricula, nome_curso, d_nascimento

database = database()

def dados(): #Armazenas algumas lits importantes para o funcionamento do código.

    #add_curso
    lista_cursos = [1,2,3,4,5,6,7,8,9] #0

    #add_nasc
    meses_31 = [1,3,5,7,8,10,12] #1

    ano_bissexto = [1924,1928,1932,1936,1940,1944,1948,1952,1956,1960,1964,1968,
                    1972,1976,1980,1984,1988,1992,1996,2000,2004,2008,2012, 2016,2020,2024] #2

    return lista_cursos, meses_31, ano_bissexto 

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

def educalog(): #logo da educalog
    print("") 
    print("░█▀▀▀ ░█▀▀▄ ░█─░█ ░█▀▀█ ─█▀▀█ ░█─── ░█▀▀▀█ ░█▀▀█")
    print("░█▀▀▀ ░█─░█ ░█─░█ ░█─── ░█▄▄█ ░█─── ░█──░█ ░█─▄▄")
    print("░█▄▄▄ ░█▄▄▀ ─▀▄▄▀ ░█▄▄█ ░█─░█ ░█▄▄█ ░█▄▄▄█ ░█▄▄█")

#----------------------------------#

#VEROFICAÇÕES → Funções responsáveis pelas verificações de entradas no sistema-

def verificador_cpf(cpf_in): #Verifica o CPF 
    
    def cpf_x1(cpf_in):

        try:
            cpf = cpf_in

            contagem_letra = 0 ; multiplicador = 10 ; contagem = 8
            valor_multi = []

            while contagem_letra <= contagem:

                numero_str = cpf[contagem_letra]
                numero_int = (int(numero_str))

                valor = numero_int*multiplicador

                valor_multi.append(valor)

                #proxima letra                         #menos um a ser multiplicado
                contagem_letra = contagem_letra + 1  ; multiplicador = multiplicador - 1 

                continue

            soma_numero = 0

            for num in valor_multi:
                soma_numero += num

            resultado_full = soma_numero * 10
            resultado_final_x1 = resultado_full % 11

            if str(resultado_final_x1) == cpf_in[9]:
                None               
            else:
                return False
        except:
            return False   
        return True  
#---------------------------------------------------   
    def cpf_x2(cpf_in):

        try:
            cpf = cpf_in

            contagem_letra = 0 ; multiplicador = 11 ; contagem = 9
            valor_multi = []

            while contagem_letra <= contagem:

                numero_int = cpf[contagem_letra]
                numero = (int(numero_int))

                valor = numero*multiplicador

                valor_multi.append(valor)

                #proxima letra             #menos um a ser multiplicado
                contagem_letra = contagem_letra + 1  ; multiplicador = multiplicador - 1 

                continue

            soma_numero = 0

            for num in valor_multi:
                soma_numero += num

            resultado_full = soma_numero * 10
            resultado_final_x2 = resultado_full % 11

            if str(resultado_final_x2) == cpf_in[10]:
                None               
            else:
                return False
        except:
            return False   
        return True     
#---------------------------------------------------        
    def exec_verificador_cpf():

        if cpf_x1(cpf_in):      


            if cpf_x2(cpf_in):
                None

            else:
                limpar_terminal()

                print("Erro, CPF inválido.#602")
                input("Clique em qualquer tecla para continuar...")
                return False
        else:

            limpar_terminal()

            print("Erro, CPF inválido.#601")
            input("Clique em qualquer tecla para continuar...")
            return False
        
        return True
#---------------------------------------------------      
    if exec_verificador_cpf():
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
                
                educalog()

                print
                tarefa = input("\n Como podemos lhe ajudar?\n\n 1 - Adicionar aluno \n 2 - Buscar aluno \n 3 - Excluir aluno \n 4 - Editar aluno \n 5 - Listar alunos\n:")
            
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
            Buscar(database, data)
        elif tarefa == 3:
            Excluir(database, data)
        elif tarefa == 4:
            Editar(database, data)
        else:
            Listar(database, data)

    #----------------------------------#

    # PROCESSOS → Vão realizar o que foi escolhido no menu pelo usúario.

    def Adicionar(data):#Adiciona um aluno novo ao sistema.

        def add_cpf(database, data):#CPF do aluno novo. // subprocesso
            
            cpf_data = database[0]

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
                
                if verificador_cpf(cpf_in):
                            None
                else:
                    limpar_terminal()
                    continue          
                
                cpf_data.append(cpf_in)
                limpar_terminal()

                print(cpf_data)
                
                return True

            return False
        
        def add_nome(database, data):#Nome completo do aluno novo. // subprocesso
            
            nome_data = database[2]

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
    
        def add_curso(database, dados, data):#Curso do aluno novo. // subprocesso

            while True:

                id_curso_data = database[3]
                nome_curso_data = database[5]
                lista_cursos = dados[0]

                print(lista_cursos)

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
        
        def add_nasc(database, dados, data):#Data de nascimento do aluno novo. // subprocesso

            d_nascimento_data = database[6]
            meses_31 = dados[1]
            ano_bissexto = dados[2]

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

        def add_tel(database, data):#Telefone do aluno novo. // subprocesso

            tel_data = database[1]

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

        def new_matricula(database):#CPF do aluno novo. // subprocesso

            matricula_data = database[4]

            cpf_data = database[0]
            ultimo_cpf_data = cpf_data[-1]

            id_curso_data = database[3]
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
            
            if add_cpf(database,data): #Se for True...
                limpar_terminal()
    
                if add_nome(database,data):
                    limpar_terminal()

                    if add_curso(database, dados, data):
                        limpar_terminal()

                        if add_nasc(database, dados, data):
                            limpar_terminal()

                            if add_tel(database, data):
                                limpar_terminal()
                                new_matricula(database)
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
        
    def Buscar(database, data):#Buscar aluno no Sistema

        def exec_buscar(database, data):
                
            cpf_data = database[0] 
            tel_data = database[1] 
            nome_data = database[2]
            id_curso_data = database[3]
            matricula_data = database[4] 
            nome_curso_data = database[5] 
            d_nascimento_data = database[6] 

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

                            try:
                                i = matricula_data.index(busca_in)
                            except:
                                limpar_terminal()
                                print("Número de matricula ou nome inválido.")
                                input("Insira qualquer valor para continuar...")
                                limpar_terminal()
                                continue

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

        exec_buscar(database, data)

    #||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

    def Excluir(database, data):#Excluir dados de um aluno

        def exec_excluir(database, data):

            cpf_data = database[0] 
            tel_data = database[1] 
            nome_data = database[2]
            id_curso_data = database[3]
            matricula_data = database[4] 
            nome_curso_data = database[5] 
            d_nascimento_data = database[6] 

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

        exec_excluir(database, data)

    #||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
        
    def Editar(database, data):#Editar os dados e um aluno

        def exec_editar(database, data):

            cpf_data = database[0] 
            tel_data = database[1] 
            nome_data = database[2]
            id_curso_data = database[3]
            matricula_data = database[4] 
            nome_curso_data = database[5] 
            d_nascimento_data = database[6] 

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

        exec_editar(database, data)

    #||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

    def Listar(database, data):#Lista todos os alunos e seus respectivos dados

        def exec_listar(database, data):

            cpf_data = database[0] 
            tel_data = database[1] 
            nome_data = database[2]
            id_curso_data = database[3]
            matricula_data = database[4] 
            nome_curso_data = database[5] 
            d_nascimento_data = database[6] 

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
        
        exec_listar(database, data)
        
    # ==========================================================#

    main()

