class NewNode:
    def __init__(self, data, prev, next):
        self.__data = data
        self.__prev = prev
        self.__next = next

    @property
    def data(self):
        return self.__data

    @property
    def prev(self):
        return self.__prev

    @property
    def next(self):
        return self.__next

    @data.setter
    def data(self, new_data):
        self.__data = new_data

    @prev.setter
    def prev(self, new_prev):
        self.__prev = new_prev

    @next.setter
    def next(self, new_next):
        self.__next = new_next
