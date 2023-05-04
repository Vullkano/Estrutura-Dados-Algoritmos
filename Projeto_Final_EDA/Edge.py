class Edge:
    def __init__(self, origem, destino, peso):
        self._origem = origem
        self._destino = destino
        self._peso = peso

    @property
    def peso(self):
        return self._peso

    def __hash__(self):
        return hash((self._origem, self._destino))

    def __str__(self):
        return f'{self._origem} -> {self._destino} = {self._peso}'

    def endpoints(self):
        return (self._origem, self._destino)

    def opposite(self, vertice):
        return self._destino if vertice is self._origem else self._origem

    def element(self):
        return self._peso

    def mostra_edge(self):
        print(f'({self._origem}, {self._destino}')

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return self._origem == other._origem and self._destino == other._destino