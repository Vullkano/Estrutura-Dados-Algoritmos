#Rodar o código para construir gráfico que compara os tipos de search
#Parametros podem ser alterados quando a função está a ser chamada em baixo


import timeit
import matplotlib.pyplot as plt
import ListaDLC
import ListaDL
import random


def plot_timeit_search_comp(n_elements, n_repetitions, jump, xticks_num, yticks_num):


    n_elements = int(n_elements)  # Nº de elementos da maior cadeia
    n_repetitions = int(n_repetitions)  # Nº de repetições realizadas pelo timeit (quanto maior o nº mais precisos serão os gráficos)
    jump = int(jump)  # De quantos em quantos o timeit vai realmente ser calculado (quanto menor o nº mais precosos serão os gráficos)
    xticks_num = int(xticks_num)  # De quanto em quanto "saltam" os valores do Nº de elementos na base de cada tabela
    yticks_num = float(yticks_num)  # De quanto em quanto "saltam" os valores do Tempo na lateral de cada tabela


    Binary_search_y_axis_ListaDLC = []
    Linear_search_y_axis_ListaDLC = []
    Binary_search_y_axis_ListaDL = []
    Linear_search_y_axis_ListaDL = []
    x_axis = []

    #Criar listas que dão origem aos gráficos

    for i in list(range(1, n_elements + 1))[::jump]:
        x_axis.append(i)
        Binary_search_y_axis_ListaDLC.append(sum(timeit.repeat(stmt='x.binary_search(val)', setup=f'x = ListaDLC.creat_random_list({i});x.merge_sort();val = random.randint(0, {i - 1})', globals=globals(), number=1, repeat=n_repetitions)) / n_repetitions)
        Linear_search_y_axis_ListaDLC.append(sum(timeit.repeat(stmt='x.find_value(val)', setup=f'x = ListaDLC.creat_random_list({i});x.merge_sort();val = random.randint(0, {i - 1})', globals=globals(), number=1, repeat=n_repetitions)) / n_repetitions)
        Binary_search_y_axis_ListaDL.append(sum(timeit.repeat(stmt='x.binary_search(val)', setup=f'x = ListaDL.creat_random_list({i});x.merge_sort();val = random.randint(0, {i - 1})', globals=globals(), number=1, repeat=n_repetitions)) / n_repetitions)
        Linear_search_y_axis_ListaDL.append(sum(timeit.repeat(stmt='x.find_value(val)', setup=f'x = ListaDL.creat_random_list({i});x.merge_sort();val = random.randint(0, {i - 1})', globals=globals(), number=1, repeat=n_repetitions)) / n_repetitions)
        print(f'Progresso: {i} de {n_elements} elementos')


    if n_elements % jump != 0:
        x_axis.append(n_elements)
        Binary_search_y_axis_ListaDLC.append(sum(timeit.repeat(stmt='x.binary_search(val)',
                                                               setup=f'x = ListaDLC.creat_random_list({n_elements});x.merge_sort();val = random.randint(0, {n_elements - 1})',
                                                               globals=globals(), number=1,
                                                               repeat=n_repetitions)) / n_repetitions)
        Linear_search_y_axis_ListaDLC.append(sum(timeit.repeat(stmt='x.find_value(val)',
                                                               setup=f'x = ListaDLC.creat_random_list({n_elements});x.merge_sort();val = random.randint(0, {n_elements - 1})',
                                                               globals=globals(), number=1,
                                                               repeat=n_repetitions)) / n_repetitions)
        Binary_search_y_axis_ListaDL.append(sum(timeit.repeat(stmt='x.binary_search(val)',
                                                              setup=f'x = ListaDL.creat_random_list({n_elements});x.merge_sort();val = random.randint(0, {n_elements - 1})',
                                                              globals=globals(), number=1,
                                                              repeat=n_repetitions)) / n_repetitions)
        Linear_search_y_axis_ListaDL.append(sum(timeit.repeat(stmt='x.find_value(val)',
                                                              setup=f'x = ListaDL.creat_random_list({n_elements});x.merge_sort();val = random.randint(0, {n_elements - 1})',
                                                              globals=globals(), number=1,
                                                              repeat=n_repetitions)) / n_repetitions)
        print(f'Progresso: {n_elements} de {n_elements} elementos')

    # Definir os eixos

    xticks = []
    x = 1
    while x <= n_elements:
        xticks.append(x)
        x += xticks_num
    yticks = []
    y = 0
    while y <= max(Binary_search_y_axis_ListaDLC + Linear_search_y_axis_ListaDLC + Binary_search_y_axis_ListaDL + Linear_search_y_axis_ListaDL) + yticks_num:
        yticks.append(y)
        y += yticks_num

    # Defenir gráfico

    plt.style.use('grayscale')
    fig, ax = plt.subplots()
    ax.set(xlabel='Nº de elementos', ylabel='Tempo (s)')
    ax.axis([1, n_elements, 0, max(yticks)])
    ax.grid(True)
    fig.suptitle('Linear Search vs Binary Search', fontweight='bold', fontsize=20)

    # Legenda

    plt.xticks(xticks)
    plt.yticks(yticks)
    ax.plot(x_axis, Binary_search_y_axis_ListaDLC, color='purple', label='Binary search - ListaDLC', linewidth=2.25)
    ax.plot(x_axis, Linear_search_y_axis_ListaDLC, color='orange', label='Linear search - ListaDLC', linewidth=2.25)
    ax.plot(x_axis, Binary_search_y_axis_ListaDL, color='red', label='Binary search - ListaDL', linewidth=2.25)
    ax.plot(x_axis, Linear_search_y_axis_ListaDL, color='blue', label='Linear search - ListaDL', linewidth=2.25)
    ax.legend(loc='upper left')


    plt.get_current_fig_manager().window.state("zoomed")
    plt.show()


plot_timeit_search_comp(100, 5, 1, 10, 0.00001)