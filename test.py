# Создаем класс Person
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        return f"Меня зовут {self.name}, мне {self.age} лет, я {self.gender}."

# Создаем объект класса Person
person = Person("Анна", 25, "женщина")

# Вызываем метод introduce() и выводим результат
print(person.introduce())
         