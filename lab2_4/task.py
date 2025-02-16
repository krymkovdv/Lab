class Car:
    '''Базовый класс

    Атрибуты:
        brand: str
        model: str
    '''

    def __init__(self: "Car",brand: str,model: str) -> None:
        '''Инициализация объекта Car'''
        self.brand = brand
        self.model = model

    def get_info(self: "Car") -> str:
        '''Возвращаяет информацию о марке и модели автомобиля'''
        return f"{self.brand} {self.model}"

    def __str__(self: "Car") -> str:
        '''Возвращает строковое представление Car'''
        return f"Car(brand = {self.brand}, model = {self.model})"

    def __repr__(self: "Car") -> str:
        '''Возвращает репрезентацию для отладки'''
        return f"Car(brand = {self.brand}, model = {self.model})"


class PassengerCar(Car):
    '''Дочерний класс класса Car
    Атрибуты:
    brand: str
    model: str
    weight: float
    '''
    def __init__(self: "PassengerCar", brand: str, model: str, weight: float) -> None:
        '''Инициализация объекта PassengerCar'''
        super().__init__(brand, model)
        self.weight = weight

    def get_info(self: "PassengerCar") -> str:
        '''Возвращает информацию о марке, модели и весе автомобиля'''
        initial_info = super().get_info()
        return f"{initial_info} {self.weight}"
        '''Перегружается для добавления информации о весе автомобиля'''

    def __str__(self: "PassengerCar") -> str:
        '''Возвращает строковое представление PassengerCar'''
        return f"PassengerCar(brand = {self.brand}, model = {self.model}, weight = {self.weight})"

    def __repr__(self: "PassengerCar") -> str:
        '''Возвращает репрезентацию для отладки'''
        return f"PassengerCar(brand = {self.brand}, model = {self.model}, weight = {self.weight})"


class Truck(Car):
    '''Дочерний класс класса Car
    Атрибуты:
    brand: str
    model: str
    speed: float
    '''
    def __init__(self: "Truck", brand: str,model: str, speed: float) -> None:
        '''Инициализация объекта Truck'''
        super().__init__(brand, model)
        self.speed = speed

    def get_info(self: "Truck") -> str:
        '''Возвращает информацию о марке, модели и скорости автомобиля'''
        initial_info = super().get_info()
        return f"{initial_info} {self.speed}"
        '''Перегружается для добавления информации о скорости автомобиля'''

    def __str__(self: "Truck") -> str:
        '''Возвращает сткроковое представление Truck'''
        return f"Truck(brand = {self.brand}, model = {self.model}, speed = {self.speed})"

    def __repr__(self: "Truck") -> str:
        '''Возвращает репрезентацию для отладки'''
        return f"Truck(brand = {self.brand}, model = {self.model}, speed = {self.speed})"

if __name__ == "__main__":
    print(PassengerCar("BMW","M5", 2000).get_info())










