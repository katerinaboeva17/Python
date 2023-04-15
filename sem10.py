# 1. Создать класс, описывающий человека. Должны быть поля для имени, фамилии и возраста.
# Создать экземпляр и вывести информацию о человеке.
# 2. Доработать предыдущий класс, чтобы вся информация о человеке была доступна при вызове str над экземпляром.
# 3. Добавить метод greet, вызов котоого будет выводить в консоль информацию о человеке в формате
# "Привет, меня зовут Василий Петров, мне 12 лет".
# 4. Добавить атрибут grades, в котором будет храниться список оценок.
# Создать список учеников, заполняя оценки случайными числами и вывести о них информацию в порядке убывания среднего балла.

# 5. Создайте класс прямоугольник Rectangle. 
# Метод _init_  принимает принимает две точки - левый верхний и правый нижний угол.
# Каждая точка представлена экземпляром класса Point. 
# Реализуйте методы вачисления площади и периметра прямоугольника.

# 6. Добавьте в класс Rectangle метод has_point. 
# Метод принимает точку на плоскости и возвращает True, если точка находится внутри прямоугольника
# и False в противном случае.

# from statistics import mean
# class Human:
#     def __init__(self, name, surname, age, grades: list):
#         self.name = name
#         self.surname = surname
#         self.age = age
#         self.grades = grades
#     def greet(self):
#         print(f'Привет, меня зовут {self.name} {self.surname}, мне {self.age} лет.')
#     def __str__(self) -> str:
#         return f'{self.name} {self.surname}, {self.age}'
#     def sred_ball(self):
#         sred = mean(self.grades)
#         return sred
#     def __repr__(self) -> str:
#         return f'{self.name} {self.surname}, {self.sred_ball()}'
#     def add_grades(self):
#         import random
#         n = random.randint(1, 6)
#         self.grades.append(n)

# ivan = Human('Иван', 'Петров', 12, [5, 4, 3, 4])
# maks = Human('Максим', 'Иванов', 13, [5, 2, 3, 4])
# alex = Human('Алексей', 'Харитонов', 12, [4, 4, 5, 4])
# peoples = [ivan, maks, alex]
# for item in peoples:
#     item.add_grades()
# new_peoples = sorted(peoples, key=lambda x: x.sred_ball(), reverse=True)
# print(new_peoples)

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
# class Rectangle:
#     def __init__(self, left_up, right_down):
#         self.left_up = left_up
#         self.right_down = right_down
#     def get_perimetr(self):
#         return (abs(self.left_up.x - self.right_down.x) + abs(self.left_up.y - self.right_down.y))*2
#     def get_sguare(self):
#         return abs(self.left_up.x - self.right_down.x) * abs(self.left_up.y - self.right_down.y)
#     def has_point(self):
#         point_x = int(input('x = '))
#         point_y = int(input('y = '))
#         if (self.left_up.x < point_x < self.right_down.x) and (self.right_down.y < point_y < self.left_up.y):
#             return True
#         else:
#             return False
# point1 = Point(2, 3)
# point2 = Point(5, 6) 
# rect = Rectangle(point1, point2)
# print(rect.get_perimetr())
# print(rect.get_sguare())
# print(rect.has_point())

# Home work
# Напишите класс Dragon (Дракон), экземпляр которого при инициализации принимaет аргументы:
# рост, огнеопасность, цвет.

# Класс обеспечивает выполнение методов (dr — экземпляр класса)
# экземпляры можно сравнивать: сначала по росту. затем по огнеопасности, затем по цвету по алфавиту

# экземпляры класса можно складывать: dr2 =dr + dr1. при этом возвращается новый экземпляр со значениями атрибутов:

# цвет меньший по алфавиту;
# рост - среднее арифметическое из двух округлённое до целого вниз,
# огнеопасность - большее из двух;

# из экземпляра класса можно вычесть число: dr -= number, из роста вычитается целая честь от деления роста на число, к
# огнеопасности прибавляется остаток от деления огнеопасности на число;

# Экземпляр можно вызвать с аргументом-строкой - возвращается строка-аргумент, повторенная количество раз, равное
# значению атрибута огнеопасность;

# change_color() - вызывается c аргументом - цветом, на который нужно поменять имеющийся цвет

# str- возвращает строку:
# Dragon with height «рост», danger <огнеопасность> and color «цвет».

# repr- возвращaет строку:
# Dragon(‹рост>, <огнеопасность>, <цвет>)

# class Dragon():
#     def __init__(self, height, fire_resist, color):
#         self.height = height
#         self.fire_resist = fire_resist
#         self.color = color
#     def __eq__(self, other):
#         if (self.height == other.height) and (self.fire_resist == other.fire_resist) and (self.color == other.color):
#             return True
#         else:
#             return False
#     def __add__(self, other):
#         import math
#         color2 = min(self.color, other.color)
#         height2 = math.floor((self.height + other.height)/2)
#         fire_resist2 = max(self.fire_resist, other.fire_resist)
#         dr2 = Dragon(height2, fire_resist2, color2)
#         return(dr2)
#     def __repr__(self) -> str:
#         return f'Dragon {self.height}, {self.fire_resist}, {self. color} '
#     def str(self):
#         return f'Dragon with height {self.height}, danger {self.fire_resist} and color {self.color}'
#     def change_color(self):
#         new_color = input('Введите новый цвет: ')
#         self.color = new_color
#         return self
#     def __sub__(self, number):
#         number = int(input('Введите число: '))
#         self.height = self.height - int(self.height / number)
#         self.fire_resist = self.fire_resist + self.fire_resist % number
#         return self
#     def str1(self):
#         string = input('Введите строку: ')
#         print(string * self.fire_resist)
    
# dr = Dragon(69, 5, 'brown')
# dr1 = Dragon(69, 5, 'gray')





