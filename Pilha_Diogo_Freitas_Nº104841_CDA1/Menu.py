from time import sleep

import Pilha_de_Tarefas
import Tarefa


# Aqui encontra-se a função menu que, inserido as opções pedidas de forma correta, irá realizar várias funções
# As funções aqui usadas encontram na python file "Pilha_de_Tarefas"
# Tem o método try/exception para, caso algo dê erro, o programar 'fingir' que vai reiniciar
# Existem 9 opções possiveis (de 0 a 8) e caso seja insirido o 0, o menu fecha

def menu():
    y = '\n--- Loja do Cidadão ---\n'
    s = 0
    while s != len(y):
        s = 0
        for i in y:
            print(i, end='')
            sleep(0.05)
            s += 1
    try:
        print('\n'
              '1 - Registar uma nova Tarefa\n'
              '2 - Obter uma cópia da última tarefa\n'
              '3 - Remover a última tarefa\n'
              '4 - Obter o número de tarefas num dado sector ainda por tratar\n'
              '5 - Número total de tarefas por realizar\n'
              '6 - Devolver uma lista de todos as tarefas na pilha\n'
              '7 - Exportar tarefas para um bloco de notas\n'
              '8 - Importar tarefas do bloco de notas\n'
              '0 - Fechar programa')
        y = input('Insira o número da opção que pretende fazer')
        while int(y) != 0:
            if int(y) == 1:
                print()
                x = input('Insira a Identificação do trabalhador que realizou a tarefa\n')
                while not x.isnumeric():
                    print('Valor Inválido, Insira um número')
                    x = input('Insira a Identificação do trabalhador que realizou a tarefa\n')
                y = input('Insira o número de id civil\n')
                while not y.isnumeric():
                    print('Valor Inválido, Insira um número')
                    y = input('Insira o número de id civil\n')
                print('A tarefa corresponde a que Secção da loja de cidadão ?')
                print('\n'
                      '1 - Criação / Renovação do cartão de cidadão\n'
                      '2 - Criação / Renovação do passaporte\n'
                      '3 - Questões judiciais\n')
                z = input('Insira o valor correspondente á secção')
                while z != '1' and z != '2' and z != '3':
                    print('Valor Inválido!')
                    print('\n'
                          '1 - Criação / Renovação do cartão de cidadão\n'
                          '2 - Criação / Renovação do passaporte\n'
                          '3 - Questões judiciais\n')
                    z = input('Insira o valor correspondente á secção')
                if int(z) == 1:
                    tarefa = Tarefa.Tarefa(str('T' + x), 'RC', y)
                    Pilha_de_Tarefas.p.add(tarefa)
                if int(z) == 2:
                    tarefa = Tarefa.Tarefa(str('T' + x), 'RP', y)
                    Pilha_de_Tarefas.p.add(tarefa)
                if int(z) == 3:
                    tarefa = Tarefa.Tarefa(str('T' + x), 'QC', y)
                    Pilha_de_Tarefas.p.add(tarefa)
                print('\n- - - Tarefa criada com sucesso - - -\n')

            elif int(y) == 2:
                if Pilha_de_Tarefas.p.__len__() == 0:
                    print('Não existem Tarefas na pilha')
                else:
                    print('\nCópia da última tarefa:')
                    print('-- ', end='')
                    Pilha_de_Tarefas.p.get_last()

            elif int(y) == 3:
                Pilha_de_Tarefas.p.remove_last()

            elif int(y) == 4:
                print('Pretende visionar as tarefas correspondentes a que Secção da loja de cidadão ?')
                print('\n'
                      '1 - Criação / Renovação do cartão de cidadão\n'
                      '2 - Criação / Renovação do passaporte\n'
                      '3 - Questões judiciais\n')
                z = input('Insira o valor correspondente á secção')
                while z != '1' and z != '2' and z != '3':
                    print('Valor Inválido!')
                    print('\n'
                          '1 - Criação / Renovação do cartão de cidadão\n'
                          '2 - Criação / Renovação do passaporte\n'
                          '3 - Questões judiciais\n')
                    z = input('Insira o valor correspondente á secção')
                if int(z) == 1:
                    Pilha_de_Tarefas.p.number_of_tasks('RC')
                if int(z) == 2:
                    Pilha_de_Tarefas.p.number_of_tasks('RP')
                if int(z) == 3:
                    Pilha_de_Tarefas.p.number_of_tasks('QC')

            elif int(y) == 5:
                if Pilha_de_Tarefas.p.__len__() == 0:
                    print('\nAs tarefas já foram todas realizadas\n')
                else:
                    print(f'\nAinda existem {Pilha_de_Tarefas.p.__len__()} tarefas por realizar!\n')

            elif int(y) == 6:
                print('\nTarefas Existentes na Pilha:\n')
                print(Pilha_de_Tarefas.p)

            elif int(y) == 7:
                Pilha_de_Tarefas.p.exportar_ficheiros()
                print('\n- - - Tarefas exportadas com sucesso - - -\n')

            elif int(y) == 8:
                Pilha_de_Tarefas.p.importar_ficheiros()
                print('\n- - - Tarefas importadas com sucesso - - -\n')

            else:
                print('\n--ERRO--\n'
                      '--ERRO--\n'
                      '--Essa opção não existe--')
                for c in '\nR-e-i-n-i-c-i-a-n-d-o\n':
                    print(c, end='')
                    sleep(0.1)

            print('\n'
                  '1 - Registar uma nova Tarefa\n'
                  '2 - Obter uma cópia da última tarefa\n'
                  '3 - Remover a última tarefa\n'
                  '4 - Obter o número de tarefas num dado sector ainda por tratar\n'
                  '5 - Número total de tarefas por realizar\n'
                  '6 - Devolver uma lista de todos as tarefas na pilha\n'
                  '7 - Exportar tarefas para um bloco de notas \n'
                  '8 - Importar tarefas do bloco de notas\n'
                  '0 - Fechar programa')
            y = input('Insira o número da opção que pretende fazer')
        return

    except ValueError:
        print('\nÉ necessário escolher um dos números!')
        for c in '\nR-e-i-n-i-c-i-a-n-d-o\n':
            print(c, end='')
            sleep(0.1)
        menu()
