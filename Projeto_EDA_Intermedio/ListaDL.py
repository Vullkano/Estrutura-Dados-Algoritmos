#Lista Duplamente Ligada


from Node import *
import timeit
import random


class ListaDL:

    def __init__(self):
        self.__head = NewNode(None, None, None)
        self.__tail = NewNode(None, None, None)
        self.__head.next = self.__tail
        self.__tail.prev = self.__head
        self.__size = 0

    #Faz com que objetos desta classe possam ser subscritíveis. Exemplo: x[1:5:2] ou x[5]

    def __getitem__(self, index):
        if type(index) == int:
            if - self.__size > index or index >= self.__size:
                raise IndexError('list index out of range')
            if self.__size == 1:
                return self.__head
            if index < 0:
                perc = self.__tail
                count = -1
                while count > index:
                    perc = perc.prev
                    count -= 1
            else:
                perc = self.__head
                count = 0
                while count < index:
                    perc = perc.next
                    count += 1
            return perc
        else:
            if index.step == None:
                step = 1
            else:
                step = index.step
            if index.start == None:
                start = 0
            else:
                start = index.start
            if index.stop == None:
                stop = self.__size
            else:
                stop = index.stop
            if 0 > start or start >= self.__size or 0 > stop or stop > self.__size:
                raise IndexError('list index out of range')
            lista = ListaDL()
            perc = self.__head
            count = 0
            while count < start:
                perc = perc.next
                count += 1
            count_step = 0
            while count < stop:
                if count_step % step == 0:
                    lista.insert_last(perc.data)
                perc = perc.next
                count += 1
                count_step += 1
            return lista

    #Faz com que dois objetos desta classe possam ser sumados

    def __add__(self, other):
        list = ListaDL()
        for i in range(self.__size):
            list.insert_last(self[i].data)
        for i in range(other.__size):
            list.insert_last(other[i].data)
        return list

    def __len__(self):
        return self.__size

    #Permite que objetos desta lista possam ser convertidos em strings

    def __str__(self):
        txt = '['
        perc = self.__head
        count = 0
        while count <= self.__size - 1:
            txt += str(perc.data)
            txt += ', '
            perc = perc.next
            count += 1
        if txt[-1] == ' ':
            txt = txt[:-2]
        txt += ']'
        return txt

    @property
    def head(self):
        return self.__head.data

    @property
    def tail(self):
        return self.__tail.data

    @property
    def is_empty(self):
        return self.__size == 0

    #Insere objeto na cabeça da lista

    def insert_first(self, value):
        node = NewNode(value, None, None)
        if self.__size == 0:
            self.__head = node
            self.__size += 1
        elif self.__size == 1:
            if self.__head.data != None:
                self.__tail = self.__head
            self.__head = self.__tail.prev = node
            self.__head.next = self.__tail
            self.__size += 1
        else:
            head = self.__head
            self.__head = node
            node.next = head
            head.prev = node
            self.__size += 1

    #Insere objeto na cauda da lista

    def insert_last(self, value):
        node = NewNode(value, None, None)
        if self.__size == 0:
            self.insert_first(value)
        elif self.__size == 1:
            if self.__tail.data != None:
                self.__head = self.__tail
            self.__tail = self.__head.next = node
            self.__tail.prev = self.__head
            self.__size += 1
        else:
            tail = self.__tail
            self.__tail = node
            node.prev = tail
            tail.next = node
            self.__size += 1

    #Insere objetos no indice dado

    def insert_index(self, value, index):
        if index > self.__size:
            raise IndexError('list index out of range')
        elif index == self.__size:
            self.insert_last(value)
        elif index == 0:
            self.insert_first(value)
        else:
            half = self.__size // 2
            if index <= half:
                node = NewNode(value, None, None)
                perc = self.__head
                count = 1
                while count < index:
                    perc = perc.next
                    count += 1
                node.prev = perc
                node.next = perc.next
                perc.next.prev = node
                perc.next = node
                self.__size += 1
            else:
                node = NewNode(value, None, None)
                perc = self.__tail
                count = self.__size
                while count > index:
                    perc = perc.prev
                    count -= 1
                node.next = perc.next
                perc.next.prev = node
                perc.next = node
                node.prev = perc
                self.__size += 1

    #Remove objeto que se encontra no indice dado

    def remove_index(self, index):
        if self.__size == 0:
            raise IndexError('list index out of range')
        elif index == 0:
            self.delete_first()
            return
        elif index == self.__size - 1:
            self.delete_last()
            return
        else:
            x = self.__head
            count = 0
            while count < index - 1:
                x = x.next
                count += 1
            aux = x.next
            x.next = aux.next
            aux.next.prev = x
        self.__size -= 1

    #Remove o primeiro objeto da lista

    def delete_first(self):
        if self.__size == 0:
            raise IndexError('list index out of range')
        head = self.__head
        self.__head = head.next
        self.__head.prev = None
        self.__size -= 1

    #Remove o ultimo objeto da lista

    def delete_last(self):
        if self.__size == 0:
            raise IndexError('list index out of range')
        tail = self.__tail
        self.__tail = tail.prev
        self.__tail.next = None
        self.__size -= 1

    #Remove o primeiro objeto encontrado com o valor dado

    def remove_value(self, value):
        if self.__size == 0:
            raise ValueError('value not found')
        perc = self.__head
        count = 0
        while count <= self.__size - 1 and perc.data != value:
            perc = perc.next
            count += 1
        if count == self.__size:
            raise ValueError('value not found')
        self.remove_index(count)

    #Substitui o objeto no indice dado por outro objeto

    def replace_index(self, index, value):
        if index < 0 or index >= self.__size:
            raise IndexError('list index out of range')
        perc = self.__head
        count = 0
        while count < index:
            perc = perc.next
            count += 1
        perc.data = value

    #Retorna True se o valor dado existir e False caso contrário

    def exists(self, value):
        perc = self.__head
        count = 0
        while count < self.__size:
            if perc.data == value:
                return True
            perc = perc.next
            count += 1
        return False

    #Devolve o valor seguinte ao valor dado

    def after(self, value):
        perc = self.__head
        count = 0
        while count < self.__size:
            if perc.data == value:
                if perc is self.__tail:
                    raise ValueError('no object after tail')
                perc = perc.next
                return perc.data
            perc = perc.next
            count += 1
        raise ValueError('value not found')

    #Devolve o valor anterior ao valor dado

    def before(self, value):
        perc = self.__head
        count = 0
        while count < self.__size:
            if perc.data == value:
                if perc is self.__head:
                    raise ValueError('no object before head')
                perc = perc.prev
                return perc.data
            perc = perc.next
            count += 1
        raise ValueError('value not found')

    #Conta quantas vezes um valor aparece na lista

    def count_value(self, value):
        count = 0
        index = 0
        perc = self.__head
        while index < self.__size:
            if perc.data == value:
                count += 1
            perc = perc.next
            index += 1
        return count

    #Limpa a lista

    def remove_all(self):
        self.__head = NewNode(None, None, None)
        self.__tail = NewNode(None, None, None)
        self.__head.next =self.__tail
        self.__tail.prev = self.__head
        self.__size = 0

    def merge_sort(self):
        if self.__size > 1:
            left_lista = self[:self.__size // 2]
            right_lista = self[self.__size // 2:]
            left_lista.merge_sort()
            right_lista.merge_sort()
            l_index = 0
            r_index = 0
            m_index = 0
            while l_index < left_lista.__size and r_index < right_lista.__size:
                if left_lista[l_index].data < right_lista[r_index].data:
                    self[m_index].data = left_lista[l_index].data
                    l_index += 1
                else:
                    self[m_index].data = right_lista[r_index].data
                    r_index += 1
                m_index += 1
            while l_index < left_lista.__size:
                self[m_index].data = left_lista[l_index].data
                l_index += 1
                m_index += 1
            while r_index < right_lista.__size:
                self[m_index].data = right_lista[r_index].data
                r_index += 1
                m_index += 1

    def quick_sort(self):
        if self.__size <= 1:
            return
        else:
            comp = self[self.__size - 1]
            list = self[:self.__size - 1]
        lower_list = ListaDL()
        greater_list = ListaDL()
        for i in range(list.__size):
            if list[i].data <= comp.data:
                lower_list.insert_last(list[i].data)
            else:
                greater_list.insert_last(list[i].data)
        self.remove_all()
        lower_list.quick_sort()
        comp_list = ListaDL()
        comp_list.insert_first(comp.data)
        greater_list.quick_sort()
        lista = lower_list + comp_list + greater_list
        self.__size = lista.__size
        self.__head = lista.__head
        self.__tail = lista.__tail

    def insertion_sort(self):
        for i in range(1, self.__size):
            r = i
            while r > 0 and self[r].data < self[r - 1].data:
                self[r].data, self[r - 1].data = self[r - 1].data, self[r].data
                r -= 1

    def bubble_sort(self):
        for i in range(self.__size - 1, 0, -1):
            for r in range(i):
                if self[r].data > self[r + 1].data:
                    self[r].data, self[r + 1].data = self[r + 1].data, self[r].data

    def find_value(self, value):
        perc = self.__head
        count = 0
        while count < self.__size:
            if perc.data == value:
                return count
            perc = perc.next
            count += 1
        raise ValueError('value not found')

    def binary_search(self, value):
        #self.merge_sort()
        low = 0
        high = self.__size - 1
        while low <= high:
            mid = (high + low) // 2
            if self[mid].data < value:
                low = mid + 1
            elif self[mid].data > value:
                high = mid - 1
            else:
                return mid
        raise ValueError('value not found')

#Cria uma lista aleatória com o comprimento dado

def creat_random_list(length):
    lista = list(range(length))
    random.shuffle(lista)
    x = ListaDL()
    for i in lista:
        x.insert_last(i)
    return x

def timeit_sort(n_elements):
    print('Merge Sort:', sum(timeit.repeat(stmt = 'x.merge_sort()', setup=f'x = creat_random_list({n_elements})', globals=globals(), number=1, repeat=25)) / 25)
    print('Quick Sort', sum(timeit.repeat(stmt = 'x.quick_sort()', setup=f'x = creat_random_list({n_elements})', globals=globals(), number=1, repeat=25)) / 25)
    print('Insertion Sort:', sum(timeit.repeat(stmt = 'x.insertion_sort()', setup=f'x = creat_random_list({n_elements})', globals=globals(), number=1, repeat=25)) / 25)
    print('Bubble Sort:', sum(timeit.repeat(stmt = 'x.bubble_sort()', setup=f'x = creat_random_list({n_elements})', globals= globals(), number = 1, repeat = 25))/25)

def timeit_search(n_elements):
    print('Binary Search:', sum(timeit.repeat(stmt = 'x.binary_search(val)', setup=f'x = creat_random_list({n_elements});x.merge_sort();val = random.randint(0, {n_elements - 1})', globals=globals(), number=1, repeat=50)) / 50)
    print('linear Search:', sum(timeit.repeat(stmt = 'x.find_value(val)', setup=f'x = creat_random_list({n_elements});x.merge_sort();val = random.randint(0, {n_elements-1})', globals=globals(), number=1, repeat=50)) / 50)


#x = ListaDL()
#x.insert_last(1)
#x.insert_last(2)
#x.insert_last(3)
#x.insert_last(4)