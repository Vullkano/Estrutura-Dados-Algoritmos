import networkx as nx

from Graph import *

myG = Graph()

myG.insert_vertex(0)
myG.insert_vertex(1)
myG.insert_vertex(2)
myG.insert_vertex(3)
myG.insert_vertex(4)
myG.insert_vertex(5)

myG.insert_edge(0, 4, 25)
myG.insert_edge(0, 1, 5)
myG.insert_edge(0, 2, 3)
myG.insert_edge(1, 3, 1)
myG.insert_edge(1, 4, 15)
myG.insert_edge(4, 2, 7)
myG.insert_edge(4, 3, 11)
myG.insert_edge(5, 1, 1)
myG.insert_edge(5, 3, 5)
myG.insert_edge(5, 2, 10)
myG.insert_edge(4, 5, 7)

myG.kruskals()

g = nx.Graph()
for i in myG.edges():
    g.add_edge(i._origem, i._destino, weight=i._peso)
pos = nx.spring_layout(g)
nx.draw_networkx(g, pos)
labels = nx.get_edge_attributes(g, 'weight')
nx.draw_networkx_edge_labels(g, pos, edge_labels=labels)

# Ou, mais simples
# g = nx.Graph()
# for i in myG.edges():
#     g.add_edge(i._origem, i._destino, weight=i._peso)
# nx.draw(g, with_labels=True)
# matplotlib.pyplot.show()
