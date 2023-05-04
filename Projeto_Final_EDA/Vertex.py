class Vertex:
    # Contrutor do Vertex - só tem um atributo elemento que guarda o objeto que pretendenmos guardar nesse vértice
    def __init__(self, x):
        '''O vértice será inserido no Grafo usando o método insert_vertex(x) que cria um Vertex'''
        self._elemento = x

    # Getter para obter a identificação de um Vértice feito chamando as funções hash() e id() do Python
    # Procurar na documentação do Python o que fazem as funções hash() e id()
    def __hash__(self):
        # devolve um inteiro que identifica este vértice como uma chave num dicionário
        return hash(self._elemento)

    # Função que devolve o objeto guardado no Vértice em string
    def __str__(self):
        return '{0}'.format(self._elemento)

    # Função booleana que diz se um Vértice de elemento x dado é igual ao Vértice em que estamos (o do self)
    # É obrigatório definir a função __eq__ quando se define a função __hash__
    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return self._elemento == other._elemento  # x é um objeto- quero saber com esta função
        # se é igual ao objeto que está guadado no self

    @property
    def elemento(self):
        '''Devolve o elemento neste vértice'''
        return self._elemento