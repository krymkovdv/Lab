import doctest


class Table:
    def __init__(self,height: float, number_of_legs: int):
        """
                Создание и подготовка к работе объекта "Стол"

                :param height: высота стола
                :param number_of_legs: Количество ножек

                Примеры:
                >>> table1 = Table(50, 4)  # инициализация экземпляра класса
                """
        if not isinstance(height,(int,float)):
            raise TypeError
        if not height > 0:
            raise ValueError
        self.height = height

        if  not isinstance(number_of_legs,(int)):
            raise TypeError
        if not number_of_legs > 0:
            raise ValueError
        self.numbers_of_legs = number_of_legs

    def remove_some_legs(self) -> int:
        """
                Функция которая убирает несколько ножек

                :return: Количество ножек после операции
                примеры:
        >>> table1 = Table(50, 4)
        >>> table1.remove_some_legs()
               """
        ...
    def change_height(self)->float:
        """
                        Функция которая меняет высщту стола

                        :return: Высота стола после операции
                        примеры:
                >>> table1 = Table(50, 4)
                >>> table1.change_height()
                       """
        ...
    def add_some_legs(self)->int:
        """
                        Функция которая приделывает несколько ножек

                        :return: Количество ножек после операции
                        примеры:
                >>> table1 = Table(50, 4)
                >>> table1.add_some_legs()
                       """
        ...

class Chair:
    def __init__(self,number_of_legs: int,back_height: float):
        """
                       Создание и подготовка к работе объекта "Стул"

                       :param back_height: высота спинки стола
                       :param number_of_legs: Количество ножек

                       Примеры:
                       >>> chair1 = Chair(50, 4)  # инициализация экземпляра класса
                       """
        if not isinstance(back_height, (int, float)):
            raise TypeError
        if not back_height > 0:
            raise ValueError
        self.back_height = back_height

        if not isinstance(number_of_legs, (int)):
            raise TypeError
        if not number_of_legs > 0:
            raise ValueError
        self.numbers_of_legs = number_of_legs

    def remove_some_legs(self) -> int:
        """
                Функция которая убирает несколько ножек

                :return: Количество ножек после операции
                примеры:
        >>> chair1 = Chair(50, 4)
        >>> chair1.remove_some_legs()
               """
        ...

    def change_height(self) -> float:
        """
                        Функция которая меняет высоту спинки стула

                        :return: Высота спинки стула после операции
                        примеры:
                >>> chair1 = Chair(50, 4)
                >>> chair1.change_height()
                       """
        ...

    def add_some_legs(self) -> int:
        """
                        Функция которая приделывает несколько ножек

                        :return: Количество ножек после операции
                        примеры:
                >>> chair1 = Chair(50, 4)
                >>> chair1.add_some_legs()
                       """
        ...



class Packet:
    def __init__(self,has_a_hole: bool,volume: (float, int)):
        """
                       Создание и подготовка к работе объекта "Пакет"

                       :param has_a_hole: есть ли в нем дырка
                       :param volume: Свободный объем

                       Примеры:
                       >>> packet1 = Packet(False, 40)  # инициализация экземпляра класса
                       """
        if not isinstance(has_a_hole, (bool )):
            raise TypeError
        self.has_a_hale = has_a_hole

        if not isinstance(volume, (int,float)):
            raise TypeError
        if not volume > 0:
            raise ValueError
        self.volume = volume

    def add_some_items(self) -> float:
        """
                Функция которая добавляет несколько вещей в пакет

                :return: Незаполненный объем в пакете
                примеры:
        >>> packet1 = Packet(False, 40)
        >>> packet1.add_some_items()
               """
        ...

    def remove_some_items(self) -> float:
        """
                        Функция которая убирает несколько вещей из пакета

                        :return: Незаполненный объем в пакете
                        примеры:
                >>> packet1 = Packet(False, 40)
                >>> packet1.remove_some_items()
                       """
        ...

    def make_a_hole(self) -> int:
        """
                        Функция которая делает отверстие в пакете если он целый

                        :return: Целый пакет или нет
                        примеры:
                >>> packet1 = Packet(True, 40)
                >>> packet1.make_a_hole()
                       """
        ...





if __name__ == "__main__":
    doctest.testmod()
