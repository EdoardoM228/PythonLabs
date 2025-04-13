class Pet:
    def __init__(self, name, breed, age):
        self._name = name
        self._breed = breed
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, value):
        self._breed = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Возраст не может быть отрицательным")
        self._age = value

    def sound(self):
        raise NotImplementedError("Метод sound должен быть переопределен в дочернем классе")

    @property
    def make_sound(self):
        return f"{self.name} говорит: {self.sound()}"


class Cat(Pet):
    def __init__(self, name, breed, age, favorite_toy):
        super().__init__(name, breed, age)
        self._favorite_toy = favorite_toy

    @property
    def favorite_toy(self):
        return self._favorite_toy

    @favorite_toy.setter
    def favorite_toy(self, value):
        self._favorite_toy = value

    def play(self):
        return f"{self.name} играет с {self.favorite_toy}"

    def sound(self):
        return "Meow!"


class Dog(Pet):
    def __init__(self, name, breed, age, trick):
        super().__init__(name, breed, age)
        self._trick = trick

    @property
    def trick(self):
        return self._trick

    @trick.setter
    def trick(self, value):
        self._trick = value

    def perform_trick(self):
        return f"{self.name} выполняет трюк: {self.trick}"

    def sound(self):
        return "Woof!"


# Пример использования:
cat = Cat("Лара", "Кошка", 3, "мячик")
dog = Dog("Рекс", "Собака", 5, "крутит хвост")

print(cat.name)  # Лара
print(cat.play())  # Лара играет с мячик
print(cat.make_sound)  # Лара говорит: Meow!

print(dog.name)  # Рекс
print(dog.perform_trick())  # Рекс выполняет трюк: крутит хвост
print(dog.make_sound)  # Рекс говорит: Woof!
