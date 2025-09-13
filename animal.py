class Cat:  # Создаём класс Cat (кот)
    name = None      # Имя кота (по умолчанию None)
    age = None       # Возраст кота (по умолчанию None)
    isHappy = None   # Счастлив ли кот (по умолчанию None)

    def __init__(self, name, age, isHappy):  # Конструктор, вызывается при создании объекта
        self.set_data(name, age, isHappy)
        self.get_data()


    def set_data(self, name, age, isHappy):   # Метод для изменения данных кота
        self.name = name
        self.age = age
        self.isHappy = isHappy

    def get_data(self):  # Метод для вывода данных о коте
        print(self.name, 'age:', self.age, ". Happy:", self.isHappy)

# Создаём двух котов с начальными данными через конструктор
cat1 = Cat('Kuzia', 3, True)
cat2 = Cat('Persik', 4, False)

# # Выводим данные о каждом коте
# cat1.get_data()
# cat2.get_data()