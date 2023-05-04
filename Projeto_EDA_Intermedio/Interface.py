#Rodar código para construir gráficos relativos aos diferentes tipos de sort

import PySimpleGUI as sg
import graficos_sort

sg.theme('DarkGray9')

layout = [
    [sg.Text('Escolha o método de ordenação:'), sg.Combo(['Merge Sort', 'Quick Sort', 'Insertion Sort', 'Bubble Sort', 'Todos'],key='sort_type', readonly=True), sg.Text('Inválido', text_color='red', visible=False, key='inv_sort_type')],
    [sg.Text('Nº de elementos:',size=(15,1), tooltip='Nº de elementos da maior cadeia'),sg.Combo([i for i in range(25, 501) if i % 25 == 0],key='n_elements', tooltip='Nº de elementos da maior cadeia', size=(6,1)), sg.Text('Inválido', text_color='red', visible=False, key='inv_n_elements')],
    [sg.Text('Nº de repetições:',size=(15,1), tooltip='Nº de repetições realizadas pelo timeit'), sg.Combo([1, 3, 5, 10, 25, 50],key='n_repetitions', size=(6,1), tooltip='Nº de repetições realizadas pelo timeit'), sg.Text('Inválido', text_color='red', visible=False, key='inv_n_repetitions')],
    [sg.Text('Salto:',size=(15,1),tooltip='De quantos em quantos elementos o timeit vai realmente ser calculado'),sg.Combo([1, 5, 10, 25], key='jump', size=(6, 1),tooltip='De quantos em quantos elementos o timeit vai realmente ser calculado'),sg.Text('Inválido', text_color='red', visible=False, key='inv_jump')],
    [sg.Text('Nº elementos ticks:',size=(15,1), tooltip='De quanto em quanto "saltam" os valores do Nº de elementos na base de cada tabela'),sg.Combo([10, 25, 50], key='xticks_num', size=(6, 1),tooltip='De quanto em quanto "saltam" os valores do Nº de elementos na base de cada tabela'),sg.Text('Inválido', text_color='red', visible=False, key='inv_xticks_num')],
    [sg.Text('Tempo ticks:',size=(15,1),tooltip='De quanto em quanto "saltam" os valores do Tempo na lateral de cada tabela'),sg.Combo([0.005,0.01, 0.05, 0.1, 0.2, 0.5, 1.0, 1.5, 2.0], key='yticks_num', size=(6, 1),tooltip='De quanto em quanto "saltam" os valores do Tempo na lateral de cada tabela'),sg.Text('Inválido', text_color='red', visible=False, key='inv_yticks_num')],
    [sg.Text('Tipo de lista:'),sg.Radio('ListaDL', 'list_tyoe', key='ListaDL', tooltip='Lista Duplamente Ligada'),sg.Radio('ListaDLC', 'list_tyoe', key='ListaDLC', tooltip='Lista Duplamente Ligada Circular'),sg.Radio('Ambos', 'list_tyoe', key='ambos'), sg.Text('Inválido', text_color='red', visible=False, key='inv_list_type')],
    [sg.Text()],
    [sg.Button('Criar gráfico', size=(15,1))],
    [sg.Text()],
    [sg.Text('Dicas:')],
    [sg.Text('Quanto maior o nª de elementos maior o tempo de precessamento')],
    [sg.Text('Quanto maior o nª de repetições maior o tempo de precessamento (gráfico desenhado com maior precisão)')],
    [sg.Text('Quanto menor o salto maior o tempo de precessamento (gráfico desenhado com maior precisão)')],
    [sg.Text('O nº de repetições tem de ser superior a 1 para o máximo, mínimo e média serem visiveis separadamente no gráfico')]
]

window = sg.Window('Criador de gráficos', layout)

while True:
    event, values = window.read()
    if event == 'Criar gráfico':
        for i in list(values)[:-3]:
            window['inv_' + i].Update(visible=False)
        window['inv_list_type'].Update(visible=False)
        valid = True
        for i in list(values)[1:-4]:
            try:
                if int(values[i]) < 0:
                    window['inv_' + i].Update(visible=True)
                    valid = False
            except:
                window['inv_' + i].Update(visible=True)
                valid = False
        try:
            if float(values[list(values)[-4]]) < 0:
                window['inv_yticks_num'].Update(visible=True)
                valid = False
        except:
            window['inv_yticks_num'].Update(visible=True)
            valid = False
        if not values['ListaDL'] and not values['ListaDLC'] and not values['ambos']:
            window['inv_list_type'].Update(visible=True)
            valid=False
        if values['sort_type'] == '':
            window['inv_sort_type'].Update(visible=True)
            valid = False
        if valid:
            for i in list(values)[-3:]:
                if values[i]:
                    list_type_c = i
                    break
            if values['sort_type'] == 'Todos':
                if not values['ambos']:
                    graficos_sort.plot_gene_all(values['n_elements'], values['n_repetitions'], values['jump'], values['xticks_num'], values['yticks_num'], list_type_c)
                else:
                    graficos_sort.plot_gene_all_list_comp(values['n_elements'], values['n_repetitions'], values['jump'], values['xticks_num'], values['yticks_num'])
            else:
                if not values['ambos']:

                    graficos_sort.plot_gene(values['sort_type'], values['n_elements'], values['n_repetitions'], values['jump'], values['xticks_num'], values['yticks_num'],list_type_c)
                else:
                    graficos_sort.plot_gene_list_comp(values['sort_type'], values['n_elements'], values['n_repetitions'],values['jump'], values['xticks_num'], values['yticks_num'])
    elif event == sg.WIN_CLOSED:
        break

window.close()