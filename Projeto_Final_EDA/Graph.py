from Edge import *
from Vertex import *

class Graph:
    # Construtor do Grafo que inicializa os atributos directed, number e vertices
    def __init__(self, directed=False):
        self._directed = directed
        self._number = 0
        self._vertices = {}

    def __str__(self):
        s = ''
        for v in self._vertices:
            s += str(v._elemento) + ': '
            for e in self._vertices[v]:
                s += str(self._vertices[v][e]) + '  '
            s += '\n'
        return s

    def insert_vertex(self, x=None):
        if isinstance(x, Vertex):
            for i in self._vertices:
                if x == i:
                    return x
            self._vertices[x] = {}
            self._number += 1
            return x
        else:
            v = Vertex(x)
            for i in self._vertices:
                if v == i:
                    return v
            self._vertices[v] = {}
            self._number += 1
            return v

    def insert_edge(self, origem, destino, peso=None):
        if not isinstance(origem, Vertex) and not isinstance(destino, Vertex):
            for i in self._vertices:
                if i._elemento == origem:
                    origem = i
                elif i._elemento == destino:
                    destino = i
                if isinstance(origem, Vertex) and isinstance(destino, Vertex):
                    break
        e = Edge(origem, destino, peso)
        self._vertices[origem][destino] = e  # vai colocar nas incidências de u
        self._vertices[destino][origem] = e

    def incident_edges(self, v, outgoing=True):
        '''Gerador: indica todas as arestas (outgoing) incidentes em v
        Se for um grafo dirigido e outgoing for False, devolve as arestas em incoming
        '''
        for edge in self._vertices[v].values():  # para todas as arestas relativas a v:
            if not self._directed:
                yield edge
            else:  # senão deve ir procurar em todas as arestas para saber quais entram ou saiem
                x, y = edge.endpoints()
                if (outgoing and x == v) or (not outgoing and y == v):
                    yield edge

    def is_directed(self):
        return self._directed  # True se os dois contentores são distintos

    def vertex_count(self):
        return self._number

    def vertices(self):
        return self._vertices.keys()

    def edge_count(self):
        total = sum(len(self._vertices[v]) for v in self._vertices)
        return total if self._directed else total // 2

    def edges(self):
        '''Devolve o conjunto de todas as arestas do Grafo'''
        result = set()  # avoid double-reporting edges in undirected graph
        for secondary_map in self._vertices.values():
            result.update(secondary_map.values())  # add edges to resulting set
        return result

    def get_edge(self, u, v):
        '''Devolve a aresta que liga u e v ou None se não forem adjacentes'''
        edge = self._vertices[u].get(v)  # returns None se não existir aresta alguma entre u e v
        if edge != None and self._directed:  # se é dirigido
            _, x = edge.endpoints  # vai confirmar se é u --> v
            if x != v:
                edge = None
        return edge

    def degree(self, v, outgoing=True):
        '''quantidade de arestas incidentes no vértice v
        Se for um grafo dirigido, conta apenas as arestas outcoming ou em incoming, de acordo com o valor de outgoing
        '''
        adj = self._vertices
        if not self._directed:
            count = len(adj[v])
        else:
            count = 0
            for edge in adj[v].values():
                x, y = edge.endpoints()
                if (outgoing and x == v) or (not outgoing and y == v):
                    count += 1
        return count

    def remove_edge(self, u, v):
        '''Remove a aresta entre u e v '''
        if u in self._vertices.keys() and v in self._vertices[u].keys():
            del self._vertices[u][v]
            del self._vertices[v][u]

    def remove_vertex(self, v):
        '''remove o vértice v'''
        # remover todas as arestas de [v]
        # remover todas as arestas com v noutros vertices
        # remover o vértice
        lst = [i for i in self.incident_edges(v)]
        for i in lst:
            x, y = i.endpoints()
            self.remove_edge(x, y)
        del self._vertices[v]
        return v

    def kruskals(self):
        ed = set()
        for i in self._vertices:
            for v in self._vertices[i]:
                ed.update([self._vertices[i][v]])
        ed = sorted(ed, key=lambda item: item._peso)
        unions = ([], [])
        for edge in ed:
            ori = None
            des = None
            exists = False
            for v in unions[1]:
                if (edge._origem in v and edge._destino in v):
                    exists = True
                    break
                if (edge._origem in v):
                    ori = v
                elif (edge._destino in v):
                    des = v
                if ori != None and des != None:
                    break
            if exists:
                continue
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
        unions_flat = []
        for i in unions[1]:
            for r in i:
                unions_flat.append(r)
        if len(unions_flat) < self._number:
            a = 0
            for i in self._vertices:
                if not i in unions_flat:
                    alone.append(i)
                    a += 1
                if len(unions[1]) == self._number + a:
                    break
        self._vertices = {}
        self._number = 0
        for v in unions_flat:
            self.insert_vertex(v)
        for v in alone:
            self.insert_vertex(v)
        for e in unions[0]:
            self.insert_edge(e._origem, e._destino, e._peso)

    def cluster(self, k):
        if k < 2:
            raise ValueError('invalid k')
        self.kruskals()
        ed = set()
        for i in self._vertices:
            for v in self._vertices[i]:
                ed.update([self._vertices[i][v]])
        ed = sorted(ed, key=lambda item: item._peso)
        for i in range(1, k):
            del self._vertices[ed[-i]._origem][ed[-i]._destino]
            del self._vertices[ed[-i]._destino][ed[-i]._origem]


if __name__ == "__main__":

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
    myG.insert_edge(2, 1, 5)

    myG.cluster(2)
