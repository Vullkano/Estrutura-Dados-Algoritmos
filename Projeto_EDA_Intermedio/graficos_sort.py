#Rodar o códico do ficheiro gráfico_sort_gui para construir os gráficos

import timeit
import matplotlib.pyplot as plt
import ListaDLC
import ListaDL

def plot_gene_all(n_elements,n_repetitions, jump, xticks_num, yticks_num, list_type):


    n_elements = int(n_elements)  # Nº de elementos da maior cadeia
    n_repetitions = int(n_repetitions)  # Nº de repetições realizadas pelo timeit (quanto maior o nº mais precisos serão os gráficos)
    jump = int(jump)  # De quantos em quantos o timeit vai realmente ser calculado (quanto menor o nº mais precosos serão os gráficos)
    xticks_num = int(xticks_num)  # De quanto em quanto "saltam" os valores do Nº de elementos na base de cada tabela
    yticks_num = float(yticks_num)  # De quanto em quanto "saltam" os valores do Tempo na lateral de cada tabela


    merge_y_axis = []
    quick_y_axis = []
    insertion_y_axis = []
    bubble_y_axis = []
    x_axis = []

    #Criar listas que dão origem aos gráficos

    for i in list(range(n_elements + 1))[::jump]:
        x_axis.append(i)
        merge_values = timeit.repeat(stmt='x.merge_sort()', setup=f'x = {list_type}.creat_random_list({i})', globals=globals(),number=1, repeat=n_repetitions)
        merge_y_axis.append([sum(merge_values) / n_repetitions, max(merge_values), min(merge_values)])
        quick_values = timeit.repeat(stmt = 'x.quick_sort()', setup= f'x = {list_type}.creat_random_list({i})', globals=globals(), number=1, repeat=n_repetitions)
        quick_y_axis.append([sum(quick_values) / n_repetitions, max(quick_values),min(quick_values)])
        insertion_values = timeit.repeat(stmt = 'x.insertion_sort()', setup= f'x = {list_type}.creat_random_list({i})', globals=globals(), number=1, repeat=n_repetitions)
        insertion_y_axis.append([sum(insertion_values) / n_repetitions, max(insertion_values), min(insertion_values)])
        bubble_values = timeit.repeat(stmt = 'x.bubble_sort()', setup= f'x = {list_type}.creat_random_list({i})', globals=globals(), number=1, repeat=n_repetitions)
        bubble_y_axis.append([sum(bubble_values) / n_repetitions, max(bubble_values), min(bubble_values)])
        print(f'Progresso: {i} de {n_elements} elementos')
    if n_elements % jump != 0:
        x_axis.append(n_elements)
        merge_values = timeit.repeat(stmt='x.merge_sort()', setup=f'x = {list_type}.creat_random_list({n_elements})',globals=globals(), number=1, repeat=n_repetitions)
        merge_y_axis.append([sum(merge_values) / n_repetitions, max(merge_values), min(merge_values)])
        quick_values = timeit.repeat(stmt='x.quick_sort()', setup=f'x = {list_type}.creat_random_list({n_elements})',globals=globals(), number=1, repeat=n_repetitions)
        quick_y_axis.append([sum(quick_values) / n_repetitions, max(quick_values), min(quick_values)])
        insertion_values = timeit.repeat(stmt='x.insertion_sort()', setup=f'x = {list_type}.creat_random_list({n_elements})',globals=globals(), number=1, repeat=n_repetitions)
        insertion_y_axis.append([sum(insertion_values) / n_repetitions, max(insertion_values), min(insertion_values)])
        bubble_values = timeit.repeat(stmt='x.bubble_sort()', setup=f'x = {list_type}.creat_random_list({n_elements})',globals=globals(), number=1, repeat=n_repetitions)
        bubble_y_axis.append([sum(bubble_values) / n_repetitions, max(bubble_values), min(bubble_values)])
        print(f'Progresso: {n_elements} de {n_elements} elementos')

    #Criar listas que definem as distâncias entre cada valor de x e y

    xticks = []
    x = 0
    while x <= n_elements:
        xticks.append(x)
        x += xticks_num
    yticks = []
    y = 0
    while y <= max([i[1] for i in merge_y_axis] +[i[1] for i in quick_y_axis]+[i[1] for i in insertion_y_axis]+[i[1] for i in bubble_y_axis]) + yticks_num:
        yticks.append(y)
        y += yticks_num

    #Defenir disposição dos gráficos

    plt.style.use('grayscale')
    fig, axs = plt.subplots(2,2)
    props = dict(facecolor='#ffffff', alpha=0.75)
    max_list = [[[i[1] for i in merge_y_axis], [i[1] for i in quick_y_axis]], [[i[1] for i in insertion_y_axis], [i[1] for i in bubble_y_axis]]]
    for i in [0,1]:
        for j in [0,1]:
            axs[i,j].set(xlabel='Nº de elementos', ylabel='Tempo (s)')
            axs[i,j].axis([0, n_elements, 0, max(yticks)])
            axs[i,j].grid(True, color = 'black')
            plt.text(0.02, 0.75, f'Maior tempo: {max(max_list[i][j])} s', transform=axs[i,j].transAxes, fontsize=10,verticalalignment='top', bbox=props)
    fig.suptitle(f'Tempo por nº de elementos na lista\n{list_type}', fontweight ='bold', fontsize = 20)

    #Merge Sort

    plt.sca(axs[0, 0])
    plt.xticks(xticks)
    plt.yticks(yticks)
    axs[0, 0].set_title('Merge Sort', fontsize = 16, fontweight ='bold')
    axs[0, 0].plot(x_axis, [i[0] for i in merge_y_axis], color = 'y', label = 'Média', linewidth = 2.25, linestyle='--')
    axs[0, 0].plot(x_axis, [i[1] for i in merge_y_axis], color = 'r', label = 'Máximo', linewidth = 2.25)
    axs[0, 0].plot(x_axis, [i[2] for i in merge_y_axis], color = 'g', label = 'Mínimo', linewidth = 2.25)
    axs[0, 0].legend(loc='upper left')

    #Quick Sort

    plt.sca(axs[0, 1])
    plt.xticks(xticks)
    plt.yticks(yticks)
    axs[0, 1].set_title('Quick Sort', fontsize = 16, fontweight ='bold')
    axs[0, 1].plot(x_axis, [i[0] for i in quick_y_axis], color = 'y', label = 'Média', linewidth = 2.25, linestyle='--')
    axs[0, 1].plot(x_axis, [i[1] for i in quick_y_axis], color = 'r', label = 'Máximo', linewidth = 2.25)
    axs[0, 1].plot(x_axis, [i[2] for i in quick_y_axis], color = 'g', label = 'Mínimo', linewidth = 2.25)
    axs[0, 1].legend(loc='upper left')

    #Insertion Sort

    plt.sca(axs[1, 0])
    plt.xticks(xticks)
    plt.yticks(yticks)
    axs[1, 0].set_title('Insertion Sort', fontsize = 16, fontweight ='bold')
    axs[1, 0].plot(x_axis, [i[0] for i in insertion_y_axis], color = 'y', label = 'Média', linewidth = 2.25, linestyle='--')
    axs[1, 0].plot(x_axis, [i[1] for i in insertion_y_axis], color = 'r', label = 'Máximo', linewidth = 2.25)
    axs[1, 0].plot(x_axis, [i[2] for i in insertion_y_axis], color = 'g', label = 'Mínimo', linewidth = 2.25)
    axs[1, 0].legend(loc='upper left')

    #Bubble Sort

    plt.sca(axs[1, 1])
    plt.xticks(xticks)
    plt.yticks(yticks)
    axs[1, 1].set_title('Bubble Sort', fontsize = 16, fontweight ='bold')
    axs[1, 1].plot(x_axis, [i[0] for i in bubble_y_axis], color = 'y', label = 'Média', linewidth = 2.25, linestyle='--')
    axs[1, 1].plot(x_axis, [i[1] for i in bubble_y_axis], color = 'r', label = 'Máximo', linewidth = 2.25)
    axs[1, 1].plot(x_axis, [i[2] for i in bubble_y_axis], color = 'g', label = 'Mínimo', linewidth = 2.25)
    axs[1, 1].legend(loc='upper left')


    plt.get_current_fig_manager().window.state("zoomed")
    plt.show()

#=======================================================================================================================


def plot_gene(sort_type, n_elements,n_repetitions, jump, xticks_num, yticks_num, list_type):


    sort_type_func = (sort_type[:sort_type.find(' ')] + '_' + sort_type[sort_type.find(' ') + 1:]).lower()
    n_elements = int(n_elements)  # Nº de elementos da maior cadeia
    n_repetitions = int(n_repetitions)  # Nº de repetições realizadas pelo timeit (quanto maior o nº mais precisos serão os gráficos)
    jump = int(jump)  # De quantos em quantos o timeit vai realmente ser calculado (quanto menor o nº mais precosos serão os gráficos)
    xticks_num = int(xticks_num)  # De quanto em quanto "saltam" os valores do Nº de elementos na base de cada tabela
    yticks_num = float(yticks_num)  # De quanto em quanto "saltam" os valores do Tempo na lateral de cada tabela


    y_axis = []
    x_axis = []

    #Criar listas que dão origem ao gráfico

    for i in list(range(n_elements + 1))[::jump]:
        x_axis.append(i)
        y_values = timeit.repeat(stmt=f'x.{sort_type_func}()', setup=f'x = {list_type}.creat_random_list({i})', globals=globals(),number=1, repeat=n_repetitions)
        y_axis.append([sum(y_values) / n_repetitions, max(y_values), min(y_values)])
        print(f'Progresso: {i} de {n_elements} elementos')
    if n_elements % jump != 0:
        x_axis.append(n_elements)
        y_values = timeit.repeat(stmt=f'x.{sort_type_func}()', setup=f'x = {list_type}.creat_random_list({n_elements})',globals=globals(), number=1, repeat=n_repetitions)
        y_axis.append([sum(y_values) / n_repetitions, max(y_values), min(y_values)])
        print(f'Progresso: {n_elements} de {n_elements} elementos')

    #Criar listas que definem as distâncias entre cada valor de x e y

    xticks = []
    x = 0
    while x <= n_elements:
        xticks.append(x)
        x += xticks_num
    yticks = []
    y = 0
    while y <= max([i[1] for i in y_axis]) + yticks_num:
        yticks.append(y)
        y += yticks_num

    #Defenir gráfico

    plt.style.use('grayscale')
    props = dict(facecolor='#ffffff', alpha=0.75)
    fig, ax = plt.subplots()
    ax.set(xlabel='Nº de elementos', ylabel='Tempo (s)')
    ax.axis([0, n_elements, 0, max(yticks)])
    lista = [i[1] for i in y_axis]
    plt.text(0.01, 0.87, f'Maior tempo: {max(lista)} s', transform=ax.transAxes, fontsize=10,verticalalignment='top', bbox=props)
    ax.grid(True)
    fig.suptitle(f'Tempo por nº de elementos na lista\n{list_type}', fontweight ='bold', fontsize = 20)

    #Sort Plot

    plt.xticks(xticks)
    plt.yticks(yticks)
    ax.set_title(sort_type, fontsize = 16, fontweight ='bold')
    ax.plot(x_axis, [i[0] for i in y_axis], color = 'y', label = 'Média', linewidth = 2.25, linestyle='--')
    ax.plot(x_axis, [i[1] for i in y_axis], color = 'r', label = 'Máximo', linewidth = 2.25)
    ax.plot(x_axis, [i[2] for i in y_axis], color = 'g', label = 'Mínimo', linewidth = 2.25)
    ax.legend(loc='upper left')


    plt.get_current_fig_manager().window.state("zoomed")
    plt.show()

#=======================================================================================================================

def plot_gene_list_comp(sort_type, n_elements,n_repetitions, jump, xticks_num, yticks_num):


    sort_type_func = (sort_type[:sort_type.find(' ')] + '_' + sort_type[sort_type.find(' ') + 1:]).lower()
    n_elements = int(n_elements)  # Nº de elementos da maior cadeia
    n_repetitions = int(n_repetitions)  # Nº de repetições realizadas pelo timeit (quanto maior o nº mais precisos serão os gráficos)
    jump = int(jump)  # De quantos em quantos o timeit vai realmente ser calculado (quanto menor o nº mais precosos serão os gráficos)
    xticks_num = int(xticks_num)  # De quanto em quanto "saltam" os valores do Nº de elementos na base de cada tabela
    yticks_num = float(yticks_num)  # De quanto em quanto "saltam" os valores do Tempo na lateral de cada tabela


    y_values_ListaDL = []
    y_values_ListaDLC = []
    x_axis = []

    #Criar listas que dão origem ao gráfico

    for i in list(range(n_elements + 1))[::jump]:
        x_axis.append(i)
        y_values_ListaDL.append(sum(timeit.repeat(stmt=f'x.{sort_type_func}()', setup=f'x = ListaDL.creat_random_list({i})', globals=globals(),number=1, repeat=n_repetitions)) / n_repetitions)
        y_values_ListaDLC.append(sum(timeit.repeat(stmt=f'x.{sort_type_func}()', setup=f'x = ListaDLC.creat_random_list({i})', globals=globals(),number=1, repeat=n_repetitions)) / n_repetitions)
        print(f'Progresso: {i} de {n_elements} elementos')
    if n_elements % jump != 0:
        x_axis.append(n_elements)
        y_values_ListaDL.append(sum(timeit.repeat(stmt=f'x.{sort_type_func}()', setup=f'x = ListaDL.creat_random_list({i})',globals=globals(), number=1, repeat=n_repetitions)) / n_repetitions)
        y_values_ListaDLC.append(sum(timeit.repeat(stmt=f'x.{sort_type_func}()', setup=f'x = ListaDLC.creat_random_list({i})',globals=globals(), number=1, repeat=n_repetitions)) / n_repetitions)
        print(f'Progresso: {n_elements} de {n_elements} elementos')

    #Criar listas que definem as distâncias entre cada valor de x e y

    xticks = []
    x = 0
    while x <= n_elements:
        xticks.append(x)
        x += xticks_num
    yticks = []
    y = 0
    while y <= max(y_values_ListaDL + y_values_ListaDLC) + yticks_num:
        yticks.append(y)
        y += yticks_num

    #Defenir gráfico

    plt.style.use('grayscale')
    props = dict(facecolor='#ffffff', alpha=0.75)
    fig, ax = plt.subplots()
    ax.set(xlabel='Nº de elementos', ylabel='Tempo (s)')
    ax.axis([0, n_elements, 0, max(yticks)])
    plt.text(0.01, 0.87, f'Maior tempo: {max(y_values_ListaDL + y_values_ListaDLC)} s', transform=ax.transAxes, fontsize=10,verticalalignment='top', bbox=props)
    ax.grid(True)
    fig.suptitle('Tempo por nº de elementos na lista', fontweight ='bold', fontsize = 20)

    #Sort Plot

    plt.xticks(xticks)
    plt.yticks(yticks)
    ax.set_title(sort_type, fontsize = 16, fontweight ='bold')
    ax.plot(x_axis, y_values_ListaDL, color = 'purple', label = 'ListaDL', linewidth = 2.25)
    ax.plot(x_axis, y_values_ListaDLC, color = 'orange', label = 'ListaDLC', linewidth = 2.25)
    ax.legend(loc='upper left')


    plt.get_current_fig_manager().window.state("zoomed")
    plt.show()

#=======================================================================================================================

def plot_gene_all_list_comp(n_elements,n_repetitions, jump, xticks_num, yticks_num):


    n_elements = int(n_elements)  # Nº de elementos da maior cadeia
    n_repetitions = int(n_repetitions)  # Nº de repetições realizadas pelo timeit (quanto maior o nº mais precisos serão os gráficos)
    jump = int(jump)  # De quantos em quantos o timeit vai realmente ser calculado (quanto menor o nº mais precosos serão os gráficos)
    xticks_num = int(xticks_num)  # De quanto em quanto "saltam" os valores do Nº de elementos na base de cada tabela
    yticks_num = float(yticks_num)  # De quanto em quanto "saltam" os valores do Tempo na lateral de cada tabela


    merge_y_axis_ListaDL = []
    merge_y_axis_ListaDLC = []
    quick_y_axis_ListaDL = []
    quick_y_axis_ListaDLC = []
    insertion_y_axis_ListaDL = []
    insertion_y_axis_ListaDLC = []
    bubble_y_axis_ListaDL = []
    bubble_y_axis_ListaDLC = []
    x_axis = []

    #Criar listas que dão origem aos gráficos

    for i in list(range(n_elements + 1))[::jump]:
        x_axis.append(i)
        merge_y_axis_ListaDL.append(sum(timeit.repeat(stmt='x.merge_sort()', setup=f'x = ListaDL.creat_random_list({i})', globals=globals(),number=1, repeat=n_repetitions)) / n_repetitions)
        merge_y_axis_ListaDLC.append(sum(timeit.repeat(stmt='x.merge_sort()', setup=f'x = ListaDLC.creat_random_list({i})', globals=globals(),number=1, repeat=n_repetitions)) / n_repetitions)
        quick_y_axis_ListaDL.append(sum(timeit.repeat(stmt = 'x.quick_sort()', setup= f'x = ListaDL.creat_random_list({i})', globals=globals(), number=1, repeat=n_repetitions)) / n_repetitions)
        quick_y_axis_ListaDLC.append(sum(timeit.repeat(stmt = 'x.quick_sort()', setup= f'x = ListaDLC.creat_random_list({i})', globals=globals(), number=1, repeat=n_repetitions)) / n_repetitions)
        insertion_y_axis_ListaDL.append(sum(timeit.repeat(stmt = 'x.insertion_sort()', setup= f'x = ListaDL.creat_random_list({i})', globals=globals(), number=1, repeat=n_repetitions)) / n_repetitions)
        insertion_y_axis_ListaDLC.append(sum(timeit.repeat(stmt = 'x.insertion_sort()', setup= f'x = ListaDLC.creat_random_list({i})', globals=globals(), number=1, repeat=n_repetitions)) / n_repetitions)
        bubble_y_axis_ListaDL.append(sum(timeit.repeat(stmt = 'x.bubble_sort()', setup= f'x = ListaDL.creat_random_list({i})', globals=globals(), number=1, repeat=n_repetitions)) / n_repetitions)
        bubble_y_axis_ListaDLC.append(sum(timeit.repeat(stmt = 'x.bubble_sort()', setup= f'x = ListaDLC.creat_random_list({i})', globals=globals(), number=1, repeat=n_repetitions)) / n_repetitions)
        print(f'Progresso: {i} de {n_elements} elementos')
    if n_elements % jump != 0:
        x_axis.append(n_elements)
        merge_y_axis_ListaDL.append(sum(timeit.repeat(stmt='x.merge_sort()',setup=f'x = ListaDL.creat_random_list({n_elements})', globals=globals(),number=1, repeat=n_repetitions)) / n_repetitions)
        merge_y_axis_ListaDLC.append(sum(timeit.repeat(stmt='x.merge_sort()',setup=f'x = ListaDLC.creat_random_list({n_elements})', globals=globals(),number=1, repeat=n_repetitions)) / n_repetitions)
        quick_y_axis_ListaDL.append(sum(timeit.repeat(stmt='x.quick_sort()', setup=f'x = ListaDL.creat_random_list({n_elements})', globals=globals(),number=1, repeat=n_repetitions)) / n_repetitions)
        quick_y_axis_ListaDLC.append(sum(timeit.repeat(stmt='x.quick_sort()', setup=f'x = ListaDLC.creat_random_list({n_elements})', globals=globals(),number=1, repeat=n_repetitions)) / n_repetitions)
        insertion_y_axis_ListaDL.append(sum(timeit.repeat(stmt='x.insertion_sort()', setup=f'x = ListaDL.creat_random_list({n_elements})', globals=globals(),number=1, repeat=n_repetitions)) / n_repetitions)
        insertion_y_axis_ListaDLC.append(sum(timeit.repeat(stmt='x.insertion_sort()', setup=f'x = ListaDLC.creat_random_list({n_elements})',globals=globals(), number=1, repeat=n_repetitions)) / n_repetitions)
        bubble_y_axis_ListaDL.append(sum(timeit.repeat(stmt='x.bubble_sort()', setup=f'x = ListaDL.creat_random_list({n_elements})', globals=globals(),number=1, repeat=n_repetitions)) / n_repetitions)
        bubble_y_axis_ListaDLC.append(sum(timeit.repeat(stmt='x.bubble_sort()', setup=f'x = ListaDLC.creat_random_list({n_elements})', globals=globals(),number=1, repeat=n_repetitions)) / n_repetitions)
        print(f'Progresso: {n_elements} de {n_elements} elementos')

    #Criar listas que definem as distâncias entre cada valor de x e y

    xticks = []
    x = 0
    while x <= n_elements:
        xticks.append(x)
        x += xticks_num
    yticks = []
    y = 0
    while y <= max(merge_y_axis_ListaDL + merge_y_axis_ListaDLC + quick_y_axis_ListaDL + quick_y_axis_ListaDLC + insertion_y_axis_ListaDL + insertion_y_axis_ListaDLC + bubble_y_axis_ListaDL + bubble_y_axis_ListaDLC) + yticks_num:
        yticks.append(y)
        y += yticks_num

    #Defenir disposição dos gráficos

    plt.style.use('grayscale')
    fig, axs = plt.subplots(2,2)
    props = dict(facecolor='#ffffff', alpha=0.75)
    lista = [[merge_y_axis_ListaDL + merge_y_axis_ListaDLC, quick_y_axis_ListaDL + quick_y_axis_ListaDLC],[insertion_y_axis_ListaDL + insertion_y_axis_ListaDLC, bubble_y_axis_ListaDL + bubble_y_axis_ListaDLC]]
    for i in [0,1]:
        for j in [0,1]:
            axs[i,j].set(xlabel='Nº de elementos', ylabel='Tempo (s)')
            axs[i,j].axis([0, n_elements, 0, max(yticks)])
            axs[i,j].grid(True)
            plt.text(0.02, 0.75, f'Maior tempo: {max(lista[i][j])} s', transform=axs[i,j].transAxes, fontsize=10,verticalalignment='top', bbox=props)
    fig.suptitle('Tempo por nº de elementos na lista', fontweight ='bold', fontsize = 20)

    #Merge Sort

    plt.sca(axs[0, 0])
    plt.xticks(xticks)
    plt.yticks(yticks)
    axs[0, 0].set_title('Merge Sort', fontsize = 16, fontweight ='bold')
    axs[0, 0].plot(x_axis,merge_y_axis_ListaDL, color = 'purple', label = 'ListaDL', linewidth = 2.25)
    axs[0, 0].plot(x_axis, merge_y_axis_ListaDLC, color = 'orange', label = 'ListaDLC', linewidth = 2.25)
    axs[0, 0].legend(loc='upper left')

    #Quick Sort

    plt.sca(axs[0, 1])
    plt.xticks(xticks)
    plt.yticks(yticks)
    axs[0, 1].set_title('Quick Sort', fontsize = 16, fontweight ='bold')
    axs[0, 1].plot(x_axis, quick_y_axis_ListaDL, color = 'purple', label = 'ListaDL', linewidth = 2.25)
    axs[0, 1].plot(x_axis, quick_y_axis_ListaDLC, color = 'orange', label = 'ListaDLC', linewidth = 2.25)
    axs[0, 1].legend(loc='upper left')

    #Insertion Sort

    plt.sca(axs[1, 0])
    plt.xticks(xticks)
    plt.yticks(yticks)
    axs[1, 0].set_title('Insertion Sort', fontsize = 16, fontweight ='bold')
    axs[1, 0].plot(x_axis, insertion_y_axis_ListaDL, color = 'purple', label = 'ListaDL', linewidth = 2.25)
    axs[1, 0].plot(x_axis, insertion_y_axis_ListaDLC, color = 'orange', label = 'ListaDLC', linewidth = 2.25)
    axs[1, 0].legend(loc='upper left')

    #Bubble Sort

    plt.sca(axs[1, 1])
    plt.xticks(xticks)
    plt.yticks(yticks)
    axs[1, 1].set_title('Bubble Sort', fontsize = 16, fontweight ='bold')
    axs[1, 1].plot(x_axis, bubble_y_axis_ListaDL, color = 'purple', label = 'ListaDL', linewidth = 2.25)
    axs[1, 1].plot(x_axis, bubble_y_axis_ListaDLC, color = 'orange', label = 'ListaDLC', linewidth = 2.25)
    axs[1, 1].legend(loc='upper left')


    plt.get_current_fig_manager().window.state("zoomed")
    plt.show()

#plot_gene_all(100, 5, 10, 10, 0.01,'ListaDL')
#plot_gene('Bubble Sort', 10000,1, 1, 1, 1)