import Tarefa


# É necessário importar o python file com o nome Tarefa

class Pilha:

    def __init__(self):
        # A base da minha pilha vai ser uma lista
        self.__pilha = []

    def add(self, task):
        # Para adicionar um objeto (Tarefa) temos de fazer um "append" na lista (futura pilha)
        self.__pilha.append(task)

    def is_empty(self):
        # Se a pilha não tiver objetos, está vazia
        return len(self.__pilha) == 0

    def get_last(self):
        # Verificar se a pilha não está vazia para não dar erro
        if self.is_empty():
            return 'Não existe nehuma tarefa por realizar'
        print(self.__pilha[-1])

    def remove_last(self):
        # Verificar se a pilha não está vazia para não dar erro
        if self.is_empty():
            return 'Pilha Vazia'
        # O X vai guardar o valor da última tarefa da pilha que foi eliminado pelo pop
        # De seguida é realizado um print() da tarefa para aparecer no menu()
        x = self.__pilha.pop(-1)
        print('Tarefa realizada --> ', end='')
        print(x)

    def number_of_tasks(self, sector):
        # Obrigar a que o sector seja colocado de forma correta
        if sector != 'RC' and sector != 'RP' and sector != 'QC':
            return None
        # O x vai corresponder ao número de tarefas do sector
        x = 0
        for i in self.__pilha:
            if i.sector == sector:
                x += 1
        # Será realizado um print() com o número de tarefas e o sector correspondente
        print(f'\nExistem {x} tarefas do tipo {sector}:')
        # Vai fazer Print() de todas as tarefas desse sector
        for i in self.__pilha:
            if i.sector == sector:
                print(i)

    def __len__(self):
        # Número de objetos da pilha
        return len(self.__pilha)

    def __str__(self):
        # Verificar se a pilha não está vazia para não dar erro
        if self.is_empty():
            return 'Pilha Vazia'
        # x vai ser uma string vazia onde, no final, irá ter todas as Tarefas da pilha
        x = ''
        # Na pilha, a última tarefa a entrar é a primeira a sair
        for i in self.__pilha[::-1]:
            x += f'- ID do trabalhador: {i.ide}; Secção: {i.sector}; BI: {i.bi}; Horário: {i.time}\n'
        return x

    # - - Interface - -

    # Estas funções servem para facilitar o processo da interface, pois, é necessário retornar alguma coisa
    # Estas funções são muito paarecidas com as anteriores, mas possuem um return, em vez de print()

    def number_of_tasks_interface(self, sector):
        if sector != 'RC' and sector != 'RP' and sector != 'QC':
            return None
        y = ''
        x = 0
        for i in self.__pilha:
            if i.sector == sector:
                x += 1
        y += f'\nExiste/em {x} tarefas do tipo {sector}:\n'
        for i in self.__pilha:
            if i.sector == sector:
                y += ' - '
                y += f'ID do trabalhador: {i.ide}; Secção: {i.sector}; BI: {i.bi}; Horário: {i.time}\n'
        return y

    def remove_last_interface(self):
        if self.is_empty():
            return 'Pilha Vazia'
        x = self.__pilha.pop(-1)
        return f'ID do trabalhador: {x.ide}; Secção: {x.sector}; BI: {x.bi}; Horário: {x.time}'

    def get_last_interface(self):
        if self.is_empty():
            return 'Não existe nehuma tarefa por realizar'
        for i in self.__pilha[::-1]:
            return f'ID do trabalhador: {i.ide}; Secção: {i.sector}; BI: {i.bi}; Horário: {i.time}'

    # - - Extra - -

    # Estas são as funções extras, que têm, como objetivo, importar e exportar as tarefas para um ficheiro.txt

    def exportar_ficheiros(self):
        # Inicialmente devemos abrir o ficheiro
        # Optei por fazer um overwright das Tarefas para não as repetir
        f = open('Tarefas_incompletas.txt', 'w')
        # De seguida, fiz um loop na pilha, e comecei a escrever as tarefas com o formato __str__ da "Tarefa"
        # O \n serve para dar espaço e haver várias linhas
        for i in self.__pilha:
            f.write(str(i) + '\n')
        # De seguida limpei a pilha inicial
        self.__pilha = []
        # No fim, fechei o ficheiro
        f.close()

    def importar_ficheiros(self):
        # Inicialmente devemos abrir o ficheiro
        # O programa irá apenas ler o ficheiro
        f = open('Tarefas_incompletas.txt', 'r')
        # Criei uma lista vazia
        listinha = []
        # Faço um loop no ficheiro
        for line in f:
            # O .strip irá tirar o /n
            strip_lines = line.strip()
            # O .split(';') vai dividir as strings peles ;
            corte = strip_lines.split(';')
            listinha.append(corte)
        for i in listinha:
            # De seguida faço um loop na listinha e colocar as respetivas caracteristicas na calsse Tarefa
            # Depois adiciono á lista original
            self.__pilha.append(Tarefa.Tarefa(i[0], i[1], i[2], i[3]))
        # No fim, fechei o ficheiro
        f.close()


p = Pilha()
p.add(Tarefa.t1)
p.add(Tarefa.t2)
p.add(Tarefa.t3)
