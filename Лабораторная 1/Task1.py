import doctest


class ToyCar:
    def __init__(self, color: str, position: int, speed: int):
        """
        Создание объекта "Игрушечная машинка" в 1D игре
        :param color: Цвет машинки
        :param position: Координата положения машинки на числовой прямой
        :param speed: Параметр скорости изменения координаты машинки
        Пример:
        >>> red_car = ToyCar('red', 0, 1) # инициализация экземпляра класса: красная машина в центре прямой со скоростью 1
        """
        if not isinstance(color, str):
            raise TypeError(f"Color must be string not {type(color)}")
        self.color = color
        if not isinstance(position, int):
            raise TypeError(f"Position must be int not {type(position)}")
        self.position = position
        if not isinstance(speed, int):
            raise TypeError(f"Speed must be int not {type(speed)}")
        self.speed = speed

    def move(self) -> None:
        """
        Функция движения машины, к координате прибавляется значение скорости (self.position += self.speed)
        Пример:
        >>> car = ToyCar('red', 0, 1)
        >>> car.move()
        """
        ...

    def change_speed(self, speed: int) -> None:
        """
        Изменяет текущую скорость машины
        :param speed: Текущая скорость
        Пример:
        >>> car = ToyCar('red', 0, 1)
        >>> car.change_speed(2)
        """
        if not isinstance(speed, int):
            raise TypeError(f"Speed must be int not {type(speed)}")
        ...


class PaintBrush:
    def __init__(self, shape: str, color: str, color_depth: int):
        """
        Создание объекта "кисть" для фоторедактора
        :param shape: Форма кисти, выбирается из списка форм
        :param color: Цвет формы кисти
        :param color_depth: Глубина цвета или интенсивность, диапазон от 0 до 255
        Пример:
        >>> test_brush = PaintBrush("circle", "yellow", 240)
        """
        LIST_SHAPES = ['rectangle', 'circle', 'triangle', 'star']  # список всех допустимых форм кисти
        if shape not in LIST_SHAPES:
            raise ValueError(f"{shape} not in LIST_SHAPES")
        self.shape = shape
        if not isinstance(color, str):
            raise TypeError(f"Color must be int not {type(color)}")
        self.color = color
        if not isinstance(color_depth, int):
            raise TypeError(f"Color_depth must be int not {type(color_depth)}")
        if color_depth < 0 or color_depth > 255:
            raise ValueError("Color_depth must be from 0 to 255")
        self.color_depth = color_depth

    def change_color(self, new_color: str) -> None:
        """
        Изменяет цвет кисти
        :param new_color: Новый цвет
        Пример:
        >>> new_brush = PaintBrush("rectangle", "green", 120)
        >>> new_brush.change_color("blue")
        """
        if not isinstance(new_color, str):
            raise TypeError(f"New_color must be int not {type(new_color)}")
        ...

    def change_color_depth(self, new_color_depth: int) -> None:
        """
        Изменяет глубину цвета
        :param new_color_depth: Новое значение глубины цвета
        Пример:
        >>> new_brush = PaintBrush("rectangle", "green", 120)
        >>> new_brush.change_color_depth(0)
        """
        if not isinstance(new_color_depth, int):
            raise TypeError(f"New_color_depth must be int not {type(new_color_depth)}")
        if new_color_depth < 0 or new_color_depth > 255:
            raise ValueError("New_color_depth must be from 0 to 255")
        ...


class BankUser:
    def __init__(self, name: str, money: int):
        """
        Создание объекта "клиет банка"
        :param name: Информация о клиенте, его имя фамилия
        :param money: Денежные средства пользователя
        Пример:
        >>> user_1 = BankUser("Ivan Ivanov", 99999999)
        """
        if not isinstance(name, str):
            raise TypeError("Incorrect name")
        self.name = name
        if not isinstance(money, int):
            raise TypeError(f"Money must be int not {type(money)}")
        self.money = money

    def change_money(self, value) -> int:
        """
        Изменяет (добавляет или уменьшает) количество денег пользователя
        :param value: Значение на каторое изменяется счет клиента
        :return: Возвращает измененное количество средств на счету пользователя
        Пример:
        >>> user_2 = BankUser("Petr Petrov", 10000)
        >>> user_2.change_money(-5000)
        """
        if not isinstance(value, int):
            raise TypeError(f"Value must be int not {type(value)}")
        ...  # self.money += value
        return self.money

    def check_money(self) -> int:
        """
        Выводит текущее количество денег, а также сообщает если баланс отрицательный
        :return: Выводит текущее количество денег
        Пример:
        >>> user_3 = BankUser("Vasily Vasiliev", -10000)
        >>> user_3.check_money()
        """
        if self.money < 0:
            print("Отрицательный баланс, необходимо пополнить счет")
        return self.money


if __name__ == "__main__":
    doctest.testmod()
