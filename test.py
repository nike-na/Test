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

# import json
#
#
# json_string = '''
# {
#     "customers":
#     [
#         {
#             "userid": 123456,
#             "username": "Allie Hsu",
#             "phone": [
#                 "000-001-0002",
#                 "000-002-0002"
#             ],
#             "is_vip": true
#         },
#         {
#             "userid": 223678,
#             "username": "Donald Duck",
#             "phone": null,
#             "is_vip": false
#         }
#     ]
# }
# '''
# data = json.loads(json_string)
# data['customers'][0]['username']=2
# data = json.dumps(data, indent=2)
# print(data)
#
# with open('words.txt', encoding='utf-8') as w:
#     [print(i) for i in sorted(set(w.read().upper().split()), key=lambda x: (len(x), x)) if i.endswith('ЕЯ')]

# def from_hex_to_rgb(color: str) -> tuple:
#     return int(color[1:3], 16), int(color[3:5], 16), int(color[5:], 16)
#
#
# colors = ['#B22222', '#DC143C', '#FF0000', '#FF6347', '#FF7F50', '#CD5C5C', '#F08080', '#E9967A',
#           '#FA8072', '#FFA07A', '#FF4500', '#FF8C00', '#FFA500', '#FFD700', '#B8860B', '#DAA520',
#           '#EEE8AA', '#BDB76B', '#F0E68C', '#808000', '#FFFF00', '#9ACD32', '#556B2F', '#6B8E23',
#           '#7CFC00', '#7FFF00', '#ADFF2F']
#
# for red, green, blue in map(from_hex_to_rgb, colors):
#     print(f"Red={red}, Green={green}, Blue={blue}")

# keys = ['Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety', 'One hundred']
# values = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# result = dict(zip(keys, values))

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
#
#
# inc_1, dec_1 = create_counter()
# print(inc_1())  # увеличиваем на 1
# print(inc_1(2))  # увеличиваем на 2
# print(inc_1(3))  # увеличиваем на 3
# print(dec_1())  # уменьшаем на 1
# print(dec_1())  # уменьшаем на 1

