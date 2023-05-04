import csv
import random

import matplotlib.pyplot as plt
import networkx as nx

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

gr.cluster(10)

g = nx.Graph()

unions = [[], []]
for edge in gr.edges():
    ori = None
    des = None
    for v in unions[1]:
        if (edge._origem in v):
            ori = v
        elif (edge._destino in v):
            des = v
        if ori != None and des != None:
            break
    if ori != None and des == None:
        ori.append(edge._origem)
        ori.append(edge._destino)
    elif ori == None and des != None:
        des.append(edge._origem)
        des.append(edge._destino)
    elif ori == None and des == None:
        unions[1].append([edge._origem, edge._destino])
    else:
        fin = ori + des
        unions[1].append(fin)
        unions[1].remove(ori)
        unions[1].remove(des)
    unions[0].append(edge)
alone = []
unions_flat = [v for i in unions[1] for v in i]
unions_flat = set(unions_flat)
if len(unions_flat) < gr._number:
    a = 0
    for i in gr._vertices:
        if not i in unions_flat:
            alone.append(i)
        if len(unions_flat) + len(alone) == gr._number:
            break
unions[1] = [set(i) for i in unions[1]]
unions[1] = unions[1] + [[i] for i in alone]
color_map = []
print(alone)
print(gr)
for e in unions[1]:
    color = str("#" + ''.join([random.choice('0123456789ABCDEF') for i in range(6)]))
    for v in e:
        color_map.append(color)
        g.add_node(v)
for e in unions[0]:
    g.add_edge(e._origem, e._destino, weight=e._peso)
nx.draw(g, node_color=color_map)
plt.show()
