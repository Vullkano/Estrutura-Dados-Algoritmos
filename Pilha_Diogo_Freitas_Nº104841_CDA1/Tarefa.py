import datetime


class Tarefa:

    def __init__(self, identificacao, sector, bi, time=datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')):
        # Este assert serve para obrigar a que seja colocado apenas umas das strings referidas
        # Não foi colocado mais nenhum assert, pois, as restantes variáveis vão ser controladas pelo menu e a interface
        assert sector == 'RC' or sector == 'RP' or sector == 'QC'
        self.__ide = str(identificacao)
        self.__sector = sector
        self.__bi = bi
        self.__time = time

    # O @property serviu para me facilitar na funções mais á frente
    @property
    def ide(self):
        return self.__ide

    @property
    def sector(self):
        return self.__sector

    @property
    def bi(self):
        return self.__bi

    @property
    def time(self):
        return self.__time

    # A função __str__ serve, principalmente, para aparecer no ficheiro mais á frente, para simplificar
    # Caso se faça print de alguma tarefa, irá aparecer neste formato
    def __str__(self):
        return f'{self.__ide};{self.__sector};{self.__bi};{self.__time}'


t1 = Tarefa('T324783297', 'RC', 32132121)
t2 = Tarefa('T455535335', 'RP', 12121234)
t3 = Tarefa('T157585390', 'QC', 10098187)
