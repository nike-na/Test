# # Нахождение делителей числа
# n = int(input())
# i = 1
# s = []
# while i * i <= n:
#     if n % i == 0:
#         s.append(i)             # младший делитель
#         if i != n // i:
#             s.append(n // i)    # старший делитель
#     i += 1
# s.sort()
# print(s)
# ****************************************************************************************
# Найбольший общий делитель
# a, b = map(int, input().split())  # Ввод чисел
# a1, b1 = a, b                     # для НОК
# while b > 0:
#     a, b = b, a % b
# print(f'НОД - {a}')
# print(f'НОК - {a1 * b1 / a}')      # На всякий случай: Произведение(умножить) вводимых чисел делим на НОД

# ******************************************************************************
# r, res = int(input()), 0
# for i in range(r):
#     m, c = map(int, input().split())
#     res = res + 1 if m > c else res - 1 if m < c else res
# print('Misha' if res > 0 else 'Chris' if res < 0 else 'Friendship is magic!^^')
# ***************************************************************************
# n = input()
# for i in range(len(n) // 2):
#     n = n.replace('()', '').replace('[]', '').replace('{}', '')
# print('YES' if not n else 'NO')
# ************************************************************************
# Удаление дубликатов списка
# s = input().split()
# j, f = [], []
# for i in s:
#     if i.lower() not in j:
#         j.append(i.lower())
#         f.append(i)
# print(*f)
# *************************************************************************
# Сумма цифр 4-х значных цифр
# a = 0
# for i in range(1000, 10000):
#     x = i
#     s = 0
#     while x > 0:
#         s += x % 10
#         x //= 10
#     if s == 20:
#         a += i
# print(a)
# ****************************************************************************
# Сортировка пузырьком
# n, c = int(input()), list(map(int, input().split()))
# count = 0
# for j in range(n - 1):
#     for i in range(n - 1 - j):
#         if c[i] > c[i + 1]:
#             c[i], c[i + 1] = c[i + 1], c[i]
#             count += 1
# print(*c)
# print(count)
# ******************************************************************************
# Сортировка вставками
# n = int(input())
# c = list(map(int, input().split()))
# count = 0
# for j in range(1, n):
#     for i in range(j, 0, -1):
#         if c[i] < c[i - 1]:
#             c[i], c[i - 1] = c[i - 1], c[i]
#             count += 1
# print(count)
# print(*c)
# ****************************************************
# x = []
# n, m = map(int, input().split())
# for i in range(n):
#     x.append(list(map(int, input().split())))
# for i in range(n):
#     for j in range(1, m + 1):
#         print(x[i][-j], end=' ')
#     print()
# Sample Input 1:
# 3 4
# 5 9 2 6
# 6 2 4 3
# 1 2 8 7
# Sample Output 1:
# 6 2 9 5
# 3 4 2 6
# 7 8 2 1
# ************************************************************************
# Обход по строкам потом по столбцам
# a, b = map(int, input().split())
# m = [list(input()) for _ in range(a)]
# s = [[False] * b for _ in range(a)]
# for i in range(a):
#     if 'S' not in m[i]:
#         for j in range(b):
#             s[i][j] = True
# for j in range(b):
#     f = False
#     for i in range(a):
#         if m[i][j] == 'S':
#             f = True
#             break
#     if not f:
#         for i in range(a):
#             s[i][j] = True
# count = 0
# for i in s:
#     count += i.count(True)
# print(count)
# *******************************************************
# Словарь переводчик
# words = {}
# for i in range(5):
#     s = input('Введите английское слово: ')
#     if s in words:
#         print("Слово", s, 'переводится как', words[s])
#     else:
#         print("Введите перевод слова", s)
#         words[s] = input()
# print(words)
# *******************************************************
# Сравнение строк
# d, f = {}, {}
# for i in (a := input()):
#     d[i] = d.get(i, 0) + 1
# for i in (b := input()):
#     f[i] = f.get(i, 0) + 1
# print('Yes' if d == f else 'No')
# *************************************************************
# Перенос списка в словарь
# persons = [
#     ('Allison Hill', 334053, 'M', '1635644202'),
#     ('Megan Mcclain', 191161, 'F', '2101101595'),
#     ('Brandon Hall', 731262, 'M', '6054749119'),
#     ('Michelle Miles', 539898, 'M', '1355368461'),
#     ('Donald Booth', 895667, 'M', '7736670978'),
#     ('Gina Moore', 900581, 'F', '7018476624'),
#     ('James Howard', 460663, 'F', '5461900982'),
#     ('Monica Herrera', 496922, 'M', '2955495768'),
#     ('Sandra Montgomery', 479201, 'M', '5111859731'),
#     ('Amber Perez', 403445, 'M', '0602870126')
# ]
# d = {}
# for person in persons:
#     d[person[0]] = {'salary': person[1], 'gender': person[2], 'passport': person[3]}
# print(d)
# *********************   или     ************************
# data = {}
# for name, salary, gender, passport in persons:
#     data[name] = {'salary': salary, 'gender': gender, 'passport': passport}
# *************************************************************************************
# Сортировка имен в словаре
# data = {
#     "my_friends": {
#         "count": 10,
#         "people": [{
#             "first_name": "Kurt",
#             "id": 621547005,
#             "last_name": "Cobain",
#             "bdate": "31.8.2005"
#         }, {
#             "first_name": "Виолетта",
#             "id": 484200150,
#             "last_name": "Кастилио",
#         }, {
#             "first_name": "Иринка",
#             "id": 21886133,
#             "last_name": "Бушуева",
#             "bdate": "28.8.1942"
#         }, {
#             "first_name": "Данил",
#             "id": 282456573,
#             "last_name": "Греков",
#             "bdate": "4.7.2002"
#         }, {
#             "first_name": "Валентин",
#             "id": 184902932,
#             "last_name": "Долматов",
#             "bdate": "25.5"
#         }, {
#             "first_name": "Евгений",
#             "id": 620469646,
#             "last_name": "Шапорин",
#             "bdate": "6.12.1982"
#         }, {
#             "first_name": "Ангелина",
#             "id": 622328862,
#             "last_name": "Краснова",
#             "bdate": "4.11.1995"
#         }, {
#             "first_name": "Иван",
#             "id": 576015198,
#             "last_name": "Вирин",
#             "bdate": "2.2.1915"
#         }, {
#             "first_name": "Паша",
#             "id": 386922406,
#             "last_name": "Воронов",
#             "bdate": "27.9"
#         }, {
#             "first_name": "Ольга",
#             "id": 622170942,
#             "last_name": "Савченкова",
#             "bdate": "20.12"
#         }]
#     }
#
# }
# s = [i['first_name'] for i in data['my_friends']['people']]
# print(*sorted(s), sep='\n')
# *************************************************************
# Функция format_name_list должна вернуть строку, в которой все имена из списка разделяются запятой
# кроме последних двух имен, они должны быть разделены союзом "и".
# Если в списке нет ни одного имени, функция должна вернуть пустую строку.
# def format_name_list(names: list):
#     if len(names) >= 2:
#         return ', '.join(i['name'] for i in names[:-1]) + ' и ' + names[-1]['name']
#     if len(names) == 1:
#         return names[0]['name']
#     return ''
# *********************************************************************************
# def shift_letter(letter: str, shift: int) -> str:
#     'Функция сдвигает символ letter на shift позиций'
#     return chr((ord(letter) - 97 + shift) % 26 + 97)
# *********************************************************************************
# def get_word_indices(strings: list[str]) -> dict:
#     '''Функция возвращает словарь, где ключи — это уникальные слова из
#       списка строк в нижнем регистре, а значения —
#       это списки индексов строк, в которых эти слова встречаются'''
#     d = {}
#     for index, value in enumerate(strings):
#         for i in value.lower().split():
#             d[i] = d.get(i, []) + [index]
#     return d
# ******************************************************************************************
# def create_matrix(size: int = 3, up_fill: int = 0, down_fill: int = 0) -> list:
#     '''Функция create_matrix должна возвращать квадратную матрицу размером size х size,
#      на диагонали которой располагаются числа от 1 до size.
#      Все остальные элементы заполнены согласно параметрам up_fill и down_fill'''
#     return [[up_fill if i>j else down_fill if i<j else i+1 for i in range(size)] for j in range(size)]
# ********************************************************************************************
# def print_goods(*args:tuple|str) -> tuple:
#     s = [i for i in args if type(i) is str and i]
#     if s:
#         print(*[f'{i}. {n}' for i, n in enumerate(s, 1)], sep='\n')
#     else:
#         print('Нет покупок')
# Программа должна вывести следующее:
# print_goods(1, True, 'Грушечка', '', 'Pineapple')
# 1. Грушечка
# 2. Pineapple
# *********************************************************************************
# def list_sum_recursive(a):
#     '''НИСХОДЯЩАЯ РЕКУРСИЯ
#     Главный признак: есть отложенное действие, в данном случае - сложение.
#     (Чтобы сложить первый элемент списка с суммой остальных элементов, нужно дождаться,
#     когда list_sum_recursive(a[1:]) вернет результат. Поэтому первое слагаемое уходит в стек,
#     затем в стек уходит второе слагаемое и т. д.)
#     Когда происходит обнуление суммы: при выполнении граничного условия рекурсии (пустой список).
#     Все слагаемые в это время уже в стеке.
#     Частичные суммы: неизвестны до выполнения граничного условия рекурсии.
#     '''
#     if not a: return 0 # граничное условие рекурсии
#     return a[0] + list_sum_recursive(a[1:]) # рекурсивное правило
# **********************************************************************************
# d = {}
# for _ in range(int(input())):
#     number, name = input().split()
#     d.setdefault(name,[]).append(number)
# for _ in range(int(input())):
#     print(*d.get(input(),['Неизвестный номер']))
# *************************************************************************************
# d = {'Дили':set(), 'Вили':set(), 'Били':set()}
# while (s := input())!='конец':
#     n, k = s.split(': ')
#     d[n].add(k)
# [print(f'Количество уникальных комментаторов у {i} - {len(j)}') for i, j in sorted(d.items(), key= lambda x: -len(x[1]))]
# d = {'Дили': set(), 'Вили': set(), 'Били': set()}
# while 'конец' not in (s := input().split(': ')):
#     d.setdefault(s[0], set()).add(s[1])
# for i, j in sorted(d.items(), key=lambda x: -len(x[1])):
#     print(f'Количество уникальных комментаторов у {i} - {len(j)}')
# ******************************************************************************************************
# def create_accumulator():
#     f = 0
#     def summa(s):
#         nonlocal f
#         f += s
#         return f
#     return summa
# summator_1 = create_accumulator()
# print(summator_1(1)) # печатает 1
# print(summator_1(5)) # печатает 6
# print(summator_1(2)) # печатает 8
# ***************************************************************************************************
# def multiply(f):
#     def multi(s):
#         return f*s
#     return multi
# f_2 = multiply(2)
# print("Умножение 2 на 5 =", f_2(5)) #10
# print("Умножение 2 на 15 =", f_2(15)) #30
# *******************************************************************************************
# def longest_word_in_file(file_name: str) -> str:
#     file = open(file_name, 'r', encoding='utf-8')
#     x = file.read().split()
#     return sorted([i.strip(p) for i in x], key=len)[-1]
#
# print(longest_word_in_file('file_name.txt'))
# ************************************************************************************
# with open('words.txt', encoding='utf-8') as w:
#     s = set()
#     for i in w.read().upper().split():
#         if i.endswith('ЕЯ'):
#             s.add(i)
#     print(*sorted(s, key=lambda x: (len(x), x)), sep='\n')
# ----или----
# with open('words.txt', encoding='utf-8') as w:
#     [print(i) for i in sorted(set(w.read().upper().split()), key=lambda x: (len(x), x)) if i.endswith('ЕЯ')]
#
# ***********************************************************************************
# import json
#
# with open('group_people.json', encoding='utf-8') as file:
#     group = json.load(file)
#
#     for i in group:
#         print(i['id_group'], sum(j['gender'] == 'Female' and j['year'] > 1977 for j in i['people']))
# *******************************************************************************************************
# В этой задаче вам необходимо раскодировать текст, находящийся в данном текстовом файле.
# Ключ для декодирования располагается в json-файле. В качестве ответа нужно просто отправить
# получившийся текст.  И обратите внимание, что раскодировать нужно только лишь буквы,
# все остальные символы(цифры, знаки пунктуации и т.д.) необходимо выводить как есть.
# import json
#
# with open('Alphabet.json') as al, open('Abracadabra__1_.txt') as abra:
#     alpha = json.load(al)
#     for i in abra.read():
#         print(alpha.get(i, i), end='')
# *******************************************************************************************************
# import json
#
# people = '''[{"name": "Haley Whitney", "country": "British Indian Ocean Territory (Chagos Archipelago)", "age": 54},
# {"name": "Matthew King", "country": "Colombia", "age": 34},
# {"name": "Sean Sullivan", "country": "Mayotte", "age": 40},
# {"name": "Christian Crawford", "country": "Russian Federation", "age": 29},
# {"name": "Sarah Contreras", "country": "Honduras", "age": 82},
# {"name": "Danielle Williams", "country": "Togo", "age": 91},
# {"name": "Jonathan Wilson", "country": "Tunisia", "age": 49}]'''
# file = json.loads(people)
# [print(i['name'], i['country'], i['age'], sep=', ') for i in sorted(file, key=lambda x: (x['age'], x['name']))]
# ******************************************************************************************************************
# def gen_fibonacci_numbers(n):
#     a, b = 1, 1
#     for i in range(n):
#         yield a
#         a, b = b, a + b
# ****************************************************************************************************
# def my_range_gen(start=0, stop=0, step=1):
#     if step == 0 or stop != 0 and start > stop and step > 0 or start < stop and step < 0:
#         return
#     elif stop == 0:
#         stop = start
#         start = 0
#     elif stop != 0:
#         stop = abs(stop - start)
#     while stop > 0:
#         yield start
#         start += step
#         stop -= abs(step)
# ----или-----
# def my_range_gen(start=0, stop=0, step=1):
#     if stop == 0:
#         stop = start
#         start = 0
#     while (start - stop) * step < 0:
#         yield start
#         start += step
# *****************************************************************************************************
# list_x = [25, 48, 23, 13]
# list_y = [-9, 17, 41, 47]
# list_w = [9, -26, 3, 21]
# print(list(map(lambda x, y, w: x ** 2 - x * y * w + w ** 4, list_x, list_y, list_w)))
# **************************************************************************************************
# days = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve']
# print(*sorted(filter(lambda x: len(x) == 4 or x[0] == 'S', days)), sep='\n')
# ***********************************************************************************************
# keys = ['Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety', 'One hundred']
# values = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# result = dict(zip(keys, values))
# print(result)
# *******************************************************************************************************
# def zip_with_function(l: list, func) -> list:
#     return list(map(lambda x: func(*x), zip(*l)))
# ****************************************************************************************************
# def find_keys(**kwargs):
#     return sorted([i for i in kwargs if isinstance(kwargs[i], (list, tuple))], key=str.lower)
#
# print(find_keys(t=[4, 5], W=[5, 3], A=(3, 2), a={2, 3}, b=[4]))
# ****************************************************************************************************
# print(all(['a' in i.lower() for i in input().split()]))
# ***********************************************************************************************
# print(any(i.lower().endswith('ought') for i in input().split()))
# ***********************************************************************************************
# def create_counter():
#     count = 0
#
#     def increment(value: int = 1):
#         nonlocal count
#         count += value
#         return count
#
#     def decrement(value: int = 1):
#         nonlocal count
#         count -= value
#         return count
#
#     return increment, decrement
# inc_1, dec_1 = create_counter()
# print(inc_1())  # увеличиваем на 1
# print(inc_1(2))  # увеличиваем на 2
# print(inc_1(3))  # увеличиваем на 3
# print(dec_1())  # уменьшаем на 1
# print(dec_1())  # уменьшаем на 1
# *****************************************************************************************************
# class Laptop:
#     def __init__(self, brand=None, model=None, price=None):
#         self.brand = brand
#         self.model = model
#         self.price = price
#         self.laptop_name = f'{brand} {model}'
#
# laptop1 = Laptop()
# laptop2 = Laptop()
# print(laptop1.__dict__)
# *****************************************************************************************************
# class SoccerPlayer:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#         self.goals = 0
#         self.assists = 0
#
#     def score(self, goals=1):
#         self.goals += goals
#
#     def make_assist(self, assists=1):
#         self.assists += assists
#
#     def statistics(self):
#         print(f'{self.surname} {self.name} - голы: {self.goals}, передачи: {self.assists}')
# ************************************************************************************************
# class Person:
#
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#
#     def full_name(self):
#         return f'{self.last_name} {self.first_name}'
#
#     def is_adult(self):
#         return self.age >= 18
# *****************************************************************************************************
# persons = [
#     ('Allison Hill', 334053, 'M', '1635644202'),
#     ('Megan Mcclain', 191161, 'F', '2101101595'),
#     ('Brandon Hall', 731262, 'M', '6054749119'),
#     ('Michelle Miles', 539898, 'M', '1355368461'),
#     ('Donald Booth', 895667, 'M', '7736670978'),
#     ('Gina Moore', 900581, 'F', '7018476624'),
#     ('James Howard', 460663, 'F', '5461900982'),
#     ('Monica Herrera', 496922, 'M', '2955495768'),
#     ('Sandra Montgomery', 479201, 'M', '5111859731'),
#     ('Amber Perez', 403445, 'M', '0602870126')
# ]
# class Worker:
#
#     def __init__(self, name, salary, gender, passport):
#         self.name = name
#         self.salary = salary
#         self.gender = gender
#         self.passport = passport
#
#     def get_info(self):
#         print(f'Worker {self.name}; passport-{self.passport}')
#
#
# worker_objects = []
#
# for i in persons:
#     worker_objects.append(Worker(*i))
#
# for i in worker_objects:
#     i.get_info()
# ***************************************************************************************************
# class CustomLabel:
#     def __init__(self, text, **kwargs):
#         self.text = text
#         self.__dict__.update(kwargs)
#
#     def config(self, **kwargs):
#         self.__dict__.update(kwargs)
#
#
# # Ниже код для проверки методов класса CustomLabel
# label1 = CustomLabel(text="Hello Python", fg="#eee", bg="#333")
# label2 = CustomLabel(text="Username")
# label3 = CustomLabel(text="Password", font=("Comic Sans MS", 24, "bold"), bd=20, bg='#ffaaaa')
# label4 = CustomLabel(text="Hello", bd=20, bg='#ffaaaa')
# label5 = CustomLabel(text="qwwerty", a=20, b='#ffaaaa', r=[3, 4, 5, 6], p=32)
#
# assert label1.__dict__ == {'text': 'Hello Python', 'fg': '#eee', 'bg': '#333'}
# assert label2.__dict__ == {'text': 'Username'}
# assert label3.__dict__ == {'text': 'Password', 'font': ('Comic Sans MS', 24, 'bold'), 'bd': 20, 'bg': '#ffaaaa'}
# assert label4.__dict__ == {'text': 'Hello', 'bd': 20, 'bg': '#ffaaaa'}
# assert label5.__dict__ == {'text': 'qwwerty', 'a': 20, 'b': '#ffaaaa', 'r': [3, 4, 5, 6], 'p': 32}
#
# print(label1.__dict__)
# print(label2.__dict__)
# print(label3.__dict__)
# print(label4.__dict__)
# print(label5.__dict__)
#
# label4.config(color='red', bd=100)
# label5.config(color='red', bd=100, a=32, b=432, p=100, z=432)
#
# assert label4.__dict__ == {'text': 'Hello', 'bd': 100, 'bg': '#ffaaaa', 'color': 'red'}
# assert label5.__dict__ == {'text': 'qwwerty', 'a': 32, 'b': 432, 'r': [3, 4, 5, 6], 'p': 100,
#                            'color': 'red', 'bd': 100, 'z': 432}
# *************************************************************************************************
# class Player:
#     def __init__(self):
#         self.name = input('Name: ')
#
#     def choose(self):
#         self.choice = input(f"{self.name}, choose rock, "
#                             f"paper or scissors: ").lower()
#
#
# class Game:
#     def __init__(self, player1, player2):
#         self.player1 = player1
#         self.player2 = player2
#         self.rules = {
#             "rock": "scissors",
#             "paper": "rock",
#             "scissors": "paper"
#         }
#
#     def get_winner(self):
#         if self.player1.choice == self.player2.choice:
#             return None
#         elif self.rules[self.player1.choice] == self.player2.choice:
#             return self.player1
#         else:
#             return self.player2
#
#     def play(self):
#         self.player1.choose()
#         self.player2.choose()
#         winner = self.get_winner()
#         if winner:
#             print(f"{winner.name} победил!")
#         else:
#             print("У нас ничья.")
#
#
# # Пример использования
# p1 = Player()
# p2 = Player()
# game = Game(p1, p2)
# game.play()
# **********************************************************************************
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def display_person_info(self):
#         print(f'Person: {self.name}, {self.age}')
#
#
# class Company:
#     def __init__(self, company_name, location):
#         self.company_name = company_name
#         self.location = location
#
#     def display_company_info(self):
#         print(f'Company: {self.company_name}, {self.location}')
#
#
# class Employee:
#     def __init__(self, name, age, company_name, location):
#         self.personal_data = Person(name, age)
#         self.work = Company(company_name, location)
#
#
# emp = Employee('Jessica', 28, 'Google', 'Atlanta')
# emp.personal_data.display_person_info()
# print(emp.personal_data.age)
# ****************************************************************************
# class Task:
#     def __init__(self, name, description, status=False):
#         self.name = name
#         self.description = description
#         self.status = status
#
#     def display(self):
#         print(f'{self.name} (Сделана)' if self.status else f'{self.name} (Не сделана)')
#
#
# class TaskList:
#     def __init__(self):
#         self.tasks = []
#
#     def add_task(self, task):
#         self.tasks.append(task)
#
#     def remove_task(self, task):
#         self.tasks.remove(task)
#
#
# class TaskManager:
#     def __init__(self, task_list):
#         self.task_list = task_list
#
#     def mark_done(self, task):
#         task.status = True
#
#     def mark_undone(self, task):
#         task.status = False
#
#     def show_tasks(self):
#         for i in self.task_list.tasks:
#             i.display()
# **********************************************************************************************
# class Student:
#     def __init__(self, name, age, branch):
#         self.__name = name
#         self.__age = age
#         self.__branch = branch
#
#     def __display_details(self):
#         print(f'Имя: {self.__name}\nВозраст: {self.__age}\nНаправление: {self.__branch}')
#
#     def access_private_method(self):
#         self.__display_details()
# *******************************************************************************************
# class Notebook:
#     def __init__(self, notes):
#         self._notes = notes
#
#     @property
#     def notes_list(self):
#         [print(f'{i}.{j}') for i, j in enumerate(self._notes, 1)]
# *************************************************************************************************
# class File:
#     def __init__(self, size):
#         self._size_in_bytes = size
#
#     @property
#     def size(self):
#         if self._size_in_bytes < 2**10:
#             return f'{self._size_in_bytes} B'
#         elif self._size_in_bytes < 2**20:
#             return f'{self._size_in_bytes/2**10:.2f} KB'
#         elif self._size_in_bytes < 2**30:
#             return f'{self._size_in_bytes/2**20:.2f} MB'
#         else:
#             return f'{self._size_in_bytes/2**30:.2f} GB'
#
#     @size.setter
#     def size(self, size):
#         self._size_in_bytes = size
# ********************************************************************************
# class Money:
#     def __init__(self, dollars, cents):
#         self.total_cents = dollars * 100 + cents
#
#     @property
#     def dollars(self):
#         return self.total_cents // 100
#
#     @dollars.setter
#     def dollars(self, dollars):
#         if isinstance(dollars, int) and dollars >= 0:
#             self.total_cents = dollars * 100 + self.cents
#         else:
#             print('Error dollars')
#
#     @property
#     def cents(self):
#         return self.total_cents % 100
#
#     @cents.setter
#     def cents(self, cents):
#         if isinstance(cents, int) and 0 <= cents < 100:
#             self.total_cents = cents + self.dollars * 100
#         else:
#             print('Error cents')
#
#     def __str__(self):
#         return f'Ваше состояние составляет {self.dollars} долларов {self.cents} центов'
# *******************************************************************************************
# class AppConfig:
#     data = {}
#
#     @classmethod
#     def load_config(cls, js_load):
#         with open(js_load) as file:
#             cls.data = json.load(file)
#
#     @classmethod
#     def get_config(cls, key):
#         keys = key.split('.')
#         value = cls.data
#         for i in keys:
#             if i in value:
#                 value = value[i]
#             else:
#                 return None
#         return value
# **********************************************************************************************
# class User:
#     def __init__(self, name, role):
#         self.name = name
#         self.role = role
#
#
# class Access:
#     __access_list = ['admin', 'developer']
#
#
#     @staticmethod
#     def __check_access(role):
#         return role in Access.__access_list
#
#     @staticmethod
#     def get_access(user):
#         if not isinstance(user, User):
#             print('AccessTypeError')
#         elif Access.__check_access(user.role):
#             print(f'User {user.name}: success')
#         else:
#             print('AccessDenied')
# **************************************************************************
# from string import digits
#
#
# class User:
#     def __init__(self, login, password):
#         self.__login = login
#         self.password = password
#
#
#     @property
#     def password(self):
#         s = input('Введите секрет, чтоб увидить пароль: ')
#         if s == self.__secret:
#             return self.__password
#         return 'ОТКАЗ'
#
#     @staticmethod
#     def __number_in(password):
#         for i in digits:
#             if i in password:
#                 return True
#         return False
#
#     @staticmethod
#     def __bad_password(password):
#         with open('bad.txt', encoding='utf-8') as file:
#             bad = file.read().split()
#         if password in bad:
#             return False
#         return True
#
#     @password.setter
#     def password(self, value):
#         print("SET")
#         if len(value) < 8:
#             raise 'Пароль должен быть минимум 8 символов'
#         if not User.__number_in(value):
#             raise 'Пароль должен должен содержать одну цифру'
#         if not User.__bad_password(value):
#             raise 'Пароль примитивный'
#         self.__password = value
#         self.__secret = input('Введите секрет для доступа к паролю: ')
# ************************************************************************************************
# class Registration:
#     def __init__(self, login, password):
#         self.login = login
#         self.password = password
#
#     @property
#     def login(self):
#         return self.__login
#
#     @login.setter
#     def login(self, value):
#         if not isinstance(value, str):
#             raise TypeError
#         if not value.count('@') == 1:
#             raise ValueError
#         if not value[value.index('@'):].count('.') == 1:
#             raise ValueError
#         self.__login = value
#
#     @property
#     def password(self):
#         return self.__password
#
#     @staticmethod
#     def is_include_digit(password):
#         return any(map(str.isdigit, password))
#
#     @staticmethod
#     def is_include_all_register(password: str):
#         return any(map(str.isupper, password)) and any(map(str.islower, password))
#
#     @staticmethod
#     def is_include_only_latin(password: str):
#         return all(i.isalpha() or i.isdigit() for i in password)
#
#
#     @staticmethod
#     def check_password_dictionary(password: str):
#         with open('easy_passwords.txt') as file:
#             return password in file.read()
#
#     @password.setter
#     def password(self, value):
#         if not isinstance(value, str):
#             raise TypeError('Пароль должен быть строкой')
#         if not 4 < len(value) < 12:
#             raise ValueError('Пароль должен быть длиннее 4 и меньше 12 символов')
#         if not Registration.is_include_digit(value):
#             raise ValueError('Пароль должен содержать хотя бы одну цифру')
#         if not Registration.is_include_all_register(value):
#             raise ValueError('Пароль должен содержать хотя бы один символ верхнего и нижнего регистра')
#         if not Registration.is_include_only_latin(value):
#             raise ValueError('Пароль должен содержать только латинский алфавит')
#         if Registration.check_password_dictionary(value):
#             raise ValueError('Ваш пароль содержится в списке самых легких')
#         self.__password = value
# ******************************************************************************************
# class File:
#     def __init__(self, name):
#         self.name = name
#         self.in_trash = False
#         self.is_deleted = False
#
#     def restore_from_trash(self):
#         print(f'Файл {self.name} восстановлен из корзины')
#         self.in_trash = False
#
#     def remove(self):
#         print(f'Файл {self.name} был удален')
#         self.is_deleted = True
#
#     def read(self):
#         if self.is_deleted:
#             print(f'ErrorReadFileDeleted({self.name})')
#             return
#         elif self.in_trash:
#             print(f'ErrorReadFileTrashed({self.name})')
#             return
#         else:
#             print(f'Прочитали все содержимое файла {self.name}')
#
#     def write(self, content):
#         if self.is_deleted:
#             print(f'ErrorWriteFileDeleted({self.name})')
#             return
#         elif self.in_trash:
#             print(f'ErrorWriteFileTrashed({self.name})')
#             return
#         else:
#             print(f'Записали значение {content} в файл {self.name}')
#
#
# class Trash:
#     content = []
#
#     @staticmethod
#     def add(file):
#         if not isinstance(file, File):
#             print('В корзину можно добавлять только файл')
#             return
#         Trash.content.append(file)
#         file.in_trash = True
#
#     @staticmethod
#     def clear():
#         print('Очищаем корзину')
#         for i in Trash.content:
#             i.remove()
#         Trash.content.clear()
#         print('Корзина пуста')
#
#     @staticmethod
#     def restore():
#         print('Восстанавливаем файлы из корзины')
#         for i in Trash.content:
#             i.restore_from_trash()
#         Trash.content.clear()
#         print('Корзина пуста')
# *************************************************************************************
# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#
# class User:
#     def __init__(self, login, balance=0):
#         self.login = login
#         self.balance = balance
#
#     def __str__(self):
#         return f'Пользователь {self.login}, баланс - {self.balance}'
#
#     @property
#     def balance(self):
#         return self.__balance
#
#     @balance.setter
#     def balance(self, value):
#         self.__balance = value
#
#     def deposit(self, value):
#         self.__balance += value
#
#     def is_money_enough(self, value):
#         return value <= self.__balance
#
#     def payment(self, value):
#         if self.is_money_enough(value):
#             self.__balance -= value
#             return True
#         else:
#             print('Не хватает средств на балансе. Пополните счет')
#             return False
#
#
# class Cart:
#     def __init__(self, user):
#         self.user = user
#         self.__total = 0
#         self.goods = {}
#
#     def add(self, product, quantity=1):
#         self.goods[product] = self.goods.get(product, 0) + quantity
#         self.__total += product.price * quantity
#
#     def remove(self, product, quantity=1):
#         if self.goods[product] >= quantity:
#             self.goods[product] -= quantity
#             self.__total -= product.price * quantity
#         else:
#             self.__total -= product.price * self.goods[product]
#             del self.goods[product]
#
#     @property
#     def total(self):
#         return self.__total
#
#     def order(self):
#         if self.user.payment(self.total):
#             print('Заказ оплачен')
#         else:
#             print('Проблема с оплатой')
#
#     def print_check(self):
#         print('---Your check---')
#         for i in sorted(self.goods, key=lambda x: x.name):
#             print(f'{i.name} {i.price} {self.goods[i]} {i.price * self.goods[i]}')
#         print(f'---Total: {self.total}---')
# **********************************************************************************************
# class GroceryItem:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#
#     def __str__(self):
#         return f'Name: {self.name}\nPrice: {self.price}\nQuantity: {self.quantity}'
#
#     def __repr__(self):
#         return f'GroceryItem({self.name}, {self.price}, {self.quantity})'
# ******************************************************************************************
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def __add__(self, other):
#         return Rectangle(self.width + other.width, self.height + other.height)
#
#     def __str__(self):
#         return f'Rectangle({self.width}x{self.height})'
# ****************************************************************************************
# class Vector:
#     def __init__(self, *args):
#         self.values = sorted(i for i in args if type(i) == int)
#
#     def __str__(self):
#         if self.values:
#             return f'Вектор{tuple(self.values)}'
#         return 'Пустой вектор'
#
#     def __add__(self, other):
#         if isinstance(other, int):
#             return Vector(*(i + other for i in self.values))
#         elif isinstance(other, Vector):
#             if len(other.values) == len(self.values):
#                 return Vector(*(sum(i) for i in zip(self.values, other.values)))
#             print('Сложение векторов разной длины недопустимо')
#         else:
#             print(f'Вектор нельзя сложить с {other}')
#
#     def __mul__(self, other):
#         if isinstance(other, int):
#             return Vector(*(i * other for i in self.values))
#         elif isinstance(other, Vector):
#             if len(other.values) == len(self.values):
#                 return Vector(*(i[0]*i[1] for i in zip(self.values, other.values)))
#             print('Умножение векторов разной длины недопустимо')
#         else:
#             print(f'Вектор нельзя умножать с {other}')
# ***********************************************************************************


