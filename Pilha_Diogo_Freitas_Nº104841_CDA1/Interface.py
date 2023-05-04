import PySimpleGUI as sg

import Pilha_de_Tarefas
import Tarefa


# Em baixo criei 3 funções, cada uma sendo uma 'interface' com as suas respetivas caracterisitcas

def criar_janela_inicial():
    sg.theme('DarkBlue14')
    layout = [
        [sg.Text('Clique na que opção que pretende realizar', size=(110, 2), font=('Times New Roman', 15),
                 justification='c', text_color='Red')],
        [sg.Button('Registar uma nova Tarefa', size=(80, 2), font=('Times New Roman', 12))],
        [sg.Button('Obter uma cópia da última tarefa', size=(80, 2), font=('Times New Roman', 12))],
        [sg.Button('Remover a última tarefa', size=(80, 2), font=('Times New Roman', 12))],
        [sg.Button('Obter o número de tarefas num dado sector ainda por tratar', size=(80, 2),
                   font=('Times New Roman', 12))],
        [sg.Button('Número total de tarefas por realizar', size=(80, 2), font=('Times New Roman', 12))],
        [sg.Button('Devolver uma lista de todos as tarefas na pilha', size=(80, 2), font=('Times New Roman', 12))],
        [sg.Button('Exportar tarefas para um bloco de notas', size=(80, 2), font=('Times New Roman', 12))],
        [sg.Button('Importar tarefas do bloco de notas', size=(80, 2), font=('Times New Roman', 12))],
        [sg.Button('Exit', size=(80, 2), font=('Times New Roman', 12))]
    ]
    return sg.Window('Lobby', layout=layout, element_justification='c', finalize=True)


def janela_tarefas():
    sg.theme('DarkBlue14')
    layout2 = [
        [sg.Text('Clique na que opção que pretende realizar', size=(100, 2), font=('Times New Roman', 15),
                 justification='c', text_color='Red')],
        [sg.Text('ID do trabalhador', size=(40, 1), font=('Times New Roman', 12), justification='right', key='Ide'),
         sg.Input(), sg.Text('', size=(40, 1), font=('Times New Roman', 12), justification='left', key='-KEY_IDE-')],
        [sg.Text('Número de identificação do documento', size=(40, 1), font=('Times New Roman', 12),
                 justification='right', key='BI'),
         sg.Input(), sg.Text('', size=(40, 1), font=('Times New Roman', 12), justification='left', key='-KEY_BI-')],
        [sg.Radio('RC', 'sector', key='RC', default=True), sg.Radio('QC', 'sector', key='QC', default=False),
         sg.Radio('RP', 'sector', key='RP', default=False)],
        [sg.Button('Voltar', size=(40, 2), font=('Times New Roman', 12)),
         sg.Button('Adicionar', size=(40, 2), font=('Times New Roman', 12))]
    ]
    return sg.Window('Adicionar tarefas', layout=layout2, element_justification='c', finalize=True)


def janela_sectors():
    sg.theme('DarkBlue14')
    layout3 = [
        [sg.Text('Selecione o/os sectores pretendidos para Visualizar as suas terefas respetivas', size=(80, 2),
                 font=('Times New Roman', 15),
                 justification='c', text_color='Red')],
        [sg.Checkbox('RC', size=(10, 2), key='RC')], [sg.Checkbox('QC', size=(10, 2), key='QC')],
        [sg.Checkbox('RP', size=(10, 2), key='RP')],
        [sg.Button('Voltar', size=(40, 2), font=('Times New Roman', 12)),
         sg.Button('Visualizar', size=(40, 2), font=('Times New Roman', 12))]
    ]
    return sg.Window('Visualizar os Sectores', layout=layout3, element_justification='c', finalize=True)


# Apesar de exsitir 3 janelas, só a janela do lobby é que irá abrir
janela1, janela2, janela3 = criar_janela_inicial(), None, None

# Criar um loop para a interface ficar aberta
# Neste loop irão existir vários botões, locais para escrever e caixas para se selecionar
# Todas as ações do utilizador, e os input, serão gravados para serem realizadas várias funções
while True:
    windows, event, values = sg.read_all_windows()
    # A interface irá fechar se clicar na cruz ou em exit
    if windows == janela1 and (event == sg.WIN_CLOSED or event == 'Exit'):
        break

    elif windows == janela2 and event == sg.WIN_CLOSED:
        break

    elif windows == janela3 and event == sg.WIN_CLOSED:
        break

    elif windows == janela1 and event == 'Registar uma nova Tarefa':
        janela2 = janela_tarefas()
        janela1.hide()
    elif windows == janela2 and event == 'Voltar':
        janela2.hide()
        janela1.un_hide()
    elif windows == janela2 and event == 'Adicionar':
        if values[0] == '' or not values[0].isdigit():
            windows['-KEY_IDE-'].update('Insira um número válido', text_color='RED')
        ide = values[0]
        ide_t = 'T' + str(ide)
        if values[1] == '' or not values[1].isdigit():
            windows['-KEY_BI-'].update('Insira um número válido', text_color='RED')
        bi = values[1]
        if values['RC'] is True:
            sector = 'RC'
        elif values['RP'] is True:
            sector = 'RP'
        elif values['QC'] is True:
            sector = 'QC'
        if values[0].isdigit() and values[1].isdigit():
            windows['-KEY_IDE-'].update('')
            windows['-KEY_BI-'].update('')
            a = Tarefa.Tarefa(ide_t, sector, bi)
            Pilha_de_Tarefas.p.add(a)
            sg.popup(' --- Tarefa adicionada com sucesso --- ', font=('Times New Roman', 12),
                     title='Tarefa adicionada com sucesso')

    elif windows == janela1 and event == 'Obter uma cópia da última tarefa':
        if Pilha_de_Tarefas.p.__len__() > 0:
            sg.popup('Cópia da última tarefa:', Pilha_de_Tarefas.p.get_last_interface(), font=('Times New Roman', 12),
                     title='Última Tarefa')
        elif Pilha_de_Tarefas.p.__len__() == 0:
            sg.popup(Pilha_de_Tarefas.p.get_last_interface(), font=('Times New Roman', 12),
                     title='Sem Tarefas')

    elif windows == janela1 and event == 'Remover a última tarefa':
        if Pilha_de_Tarefas.p.__len__() > 0:
            sg.popup('Parabéns, a seguinte tarefa foi concluida:', Pilha_de_Tarefas.p.remove_last_interface(),
                     font=('Times New Roman', 12), title='Tarefa finalizada')
        elif Pilha_de_Tarefas.p.__len__() == 0:
            sg.popup('As Tarefas já foram todas realizadas', font=('Times New Roman', 12),
                     title='Tarefas')

    elif windows == janela1 and event == 'Obter o número de tarefas num dado sector ainda por tratar':
        janela3 = janela_sectors()
        janela1.hide()
    elif windows == janela3 and event == 'Voltar':
        janela3.hide()
        janela1.un_hide()
    elif windows == janela3 and event == 'Visualizar':
        if values['RC'] == True and values['QC'] == False and values['RP'] == False:
            sg.popup(Pilha_de_Tarefas.p.number_of_tasks_interface('RC'), font=('Times New Roman', 12), title='Tarefas')
        elif values['QC'] == True and values['RC'] == False and values['RP'] == False:
            sg.popup(Pilha_de_Tarefas.p.number_of_tasks_interface('QC'), font=('Times New Roman', 12), title='Tarefas')
        elif values['RP'] == True and values['QC'] == False and values['RC'] == False:
            sg.popup(Pilha_de_Tarefas.p.number_of_tasks_interface('RP'), font=('Times New Roman', 12), title='Tarefas')
        elif values['RC'] == True and values['QC'] == True and values['RP'] == False:
            sg.popup(Pilha_de_Tarefas.p.number_of_tasks_interface('RC'),
                     (Pilha_de_Tarefas.p.number_of_tasks_interface('QC')), font=('Times New Roman', 12),
                     title='Tarefas')
        elif values['RC'] == True and values['QC'] == False and values['RP'] == True:
            sg.popup(Pilha_de_Tarefas.p.number_of_tasks_interface('RC'),
                     (Pilha_de_Tarefas.p.number_of_tasks_interface('RP')), font=('Times New Roman', 12),
                     title='Tarefas')
        elif values['RC'] == False and values['QC'] == True and values['RP'] == True:
            sg.popup(Pilha_de_Tarefas.p.number_of_tasks_interface('QC'),
                     (Pilha_de_Tarefas.p.number_of_tasks_interface('RP')), font=('Times New Roman', 12),
                     title='Tarefas')
        elif values['RC'] == True and values['QC'] == True and values['RP'] == True:
            sg.popup(Pilha_de_Tarefas.p.number_of_tasks_interface('RC'),
                     Pilha_de_Tarefas.p.number_of_tasks_interface('QC'),
                     (Pilha_de_Tarefas.p.number_of_tasks_interface('RP')), font=('Times New Roman', 12),
                     title='Tarefas')

    elif windows == janela1 and event == 'Número total de tarefas por realizar':
        if Pilha_de_Tarefas.p.__len__() == 0:
            sg.popup('\nAs tarefas já foram todas realizadas\n', font=('Times New Roman', 12), title='- Parabéns -')
        elif Pilha_de_Tarefas.p.__len__() > 0:
            sg.popup(f'\nAinda existem {Pilha_de_Tarefas.p.__len__()} tarefas por realizar!\n',
                     font=('Times New Roman', 12), title='Tarefas')

    elif windows == janela1 and event == 'Devolver uma lista de todos as tarefas na pilha':
        sg.popup(Pilha_de_Tarefas.p.__str__(), title='Pilha de Tarefas', font=('Times New Roman', 12))

    elif windows == janela1 and event == 'Exportar tarefas para um bloco de notas':
        Pilha_de_Tarefas.p.exportar_ficheiros()

    elif windows == janela1 and event == 'Importar tarefas do bloco de notas':
        Pilha_de_Tarefas.p.importar_ficheiros()

janela1.close()
janela2.close()
janela3.close()
