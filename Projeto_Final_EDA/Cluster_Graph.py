import matplotlib.pyplot as plt
import networkx as nx
import random

from Graph import *

gr = Graph()


gr.insert_vertex(0)
gr.insert_vertex(1)
gr.insert_vertex(2)
gr.insert_vertex(3)
gr.insert_vertex(4)
gr.insert_vertex(5)

gr.insert_edge(0, 4, 25)
gr.insert_edge(0, 1, 5)
gr.insert_edge(0, 2, 3)
gr.insert_edge(1, 3, 1)
gr.insert_edge(1, 4, 15)
gr.insert_edge(4, 2, 7)
gr.insert_edge(4, 3, 11)
gr.insert_edge(5, 1, 1)
gr.insert_edge(5, 3, 5)
gr.insert_edge(5, 2, 10)
gr.insert_edge(4, 5, 7)

#gr = gr.kruskals()
gr.cluster(2)

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
nx.draw(g, with_labels=True, node_color=color_map)
plt.show()
