# my_list = [1,2,34,5,7,8,90,0,3,67,89,35,2]


# res_list = list(filter(lambda x: x % 2 == 0, my_list))
# print(res_list)

# # for el in res_list:
# #     print(el, end=' ')
# # print()

# res_list=[]
# f = lambda x: x % 2 == 0
# for el in my_list:
#     if f(el):
#         res_list.append(el)
# print(res_list)



# res_list = list(map(lambda x: x ** 2 , my_list))
# print(res_list)
# res_list=[]
# f = lambda x: x ** 2
# for el in my_list:
#     res_list.append(f(el))
# print(res_list)


# my_list = [1,2,34,5,7,8,90,0,3,67,89,35,2]
# numbers = input('Введите цифры через пробел').split()
# print(numbers)
# res_list = list(map(int , numbers))
# print(res_list)
# print([int(el) for el in numbers])



# my_list = [1,2,34,5,7,8,90,0,3,67,89,35,2]
# numbers = input('Введите цифры через пробел').split()
# print(numbers)
# res_list = list(map(int , numbers))
# print(res_list)
# print([int(el) for el in numbers])



# 2) Есть код:
# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transformed_values = list(map(transformation, values))
# if values == transformed_values:
#          print(‘ok’)
# else:
#          print(‘fail’)
# - В переменную transformation нужно прописать такую функцию, что бы в переменной transformed_values получилась копия списка values

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

# s = lambda cur_tuple: cur_tuple[0] * cur_tuple[1]
#
# max_s = s(orbits[0])
# find_tuple = orbits[0]
#
# for cur_orbit in orbits[1:]:
#     if cur_orbit[0] != cur_orbit[1]:
#         cur_s = s(cur_orbit)
#         if cur_s > max_s:
#             max_s = cur_s
#             find_tuple = cur_orbit
#
# print(find_tuple)


# 1) Планеты вращаются вокруг звезд по эллиптическим орбитам. Назовем самой далекой планетой ту, орбита которой имеет самую большую площадь. 
# Напишите функцию find_farthest_orbit(list_of_orbits), которая среди списка орбит планет найдет ту, по которой вращается самая далекая планета. 
# Круговые орбиты не учитывайте: вы знаете, что у вашей звезды таких планет нет, зато искусственные спутники были были запущены на круговые 
# орбиты. Результатом функции должен быть кортеж, содержащий длины полуосей эллипса орбиты самой далекой планеты. Каждая орбита представляет 
# из себя кортеж из пары чисел - полуосей ее эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b, где a и b - длины полуосей эллипса. 
# При решении задачи используйте списочные выражения. Подсказка: проще всего будет найти эллипс в два шага: сначала вычислить самую большую 
# площадь эллипса, а затем найти и сам эллипс, имеющий такую  площадь. Гарантируется, что самая далекая планета ровно одна

# 2) - Дан список размеров(длина, ширина) эллипсов 
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# Напишите функцию find_farthest_orbit(list_of_orbits), которая находит площадь самого большого эллипса и возвращает кортеж с его размерами.
# Площадь эллипса вычисляется по формуле S = pi*a*b, где a и b – длины и ширина осей эллипса
# -   Площадь кругов учитывать не нужно, т.е если у эллипса a == b, то это круг.
# При решении задачи используйте списочные выражения.
# Гарантируется, что самый большой эллипс всего один

# Ввод:
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))
# Вывод: 
# 2.5 10


# def find_farthest_orbit(list_of_orbits):
#     filter_orbits = list(filter(lambda cur_orbit: cur_orbit[0] != cur_orbit[1], list_of_orbits))
#     tuple_s = list(map(lambda cur_orbit: cur_orbit[0] * cur_orbit[1], filter_orbits))
#     max_s = max(tuple_s)
#     i_max_s = tuple_s.index(max_s)
#     return filter_orbits[i_max_s]

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

# print(find_farthest_orbit(orbits))

# Напишите функцию same_by(characteristic, objects), которая проверяет, все ли объекты имеют одинаковое 
# значение некоторой характеристики, и возвращают True, если это так. Если значение характеристики для разных объектов отличается 
# - то False. Для пустого набора объектов, функция должна возвращать True. Аргумент characteristic - это функция, которая принимает 
# объект и вычисляет его характеристику.
