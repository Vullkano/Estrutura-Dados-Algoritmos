import csv

import networkx as nx
from networkx.algorithms.community import k_clique_communities, kernighan_lin_bisection

from Graph import *

gr = Graph()
dados = []
dados_limpos = []

with open('facebook_network.csv', encoding='utf-8') as arquivo:
    tabela = csv.reader(arquivo, delimiter=',')
    for i in tabela:
        dados.append([i[0], i[1], int(i[2])])
    for i in dados:
        repetido = False
        if len(dados_limpos) == 0:
            dados_limpos.append([i[0], i[1], int(i[2])])
        else:
            for v in dados_limpos:
                if (v[0] == i[0] and v[1] == i[1]) or (v[0] == i[1] and v[1] == i[0]):
                    v[2] += i[2]
                    repetido = True
                    break
            if not repetido:
                dados_limpos.append([i[0], i[1], i[2]])

for i in dados_limpos:
    gr.insert_vertex(i[0])
    gr.insert_vertex(i[1])
    gr.insert_edge(i[0], i[1], int(i[2]))

gr.kruskals()

g = nx.Graph()
for i in gr.edges():
    g.add_edge(str(i._origem), str(i._destino), weight=i._peso)
# pos = nx.spring_layout(g)
# nx.draw_networkx(g, pos)
# labels = nx.get_edge_attributes(g, 'weight')
# nx.draw_networkx_edge_labels(g, pos, edge_labels=labels)
nx.draw_networkx(g)

# A = list(k_clique_communities(g, 15))
# B = list(kernighan_lin_bisection(g))
