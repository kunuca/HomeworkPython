# В списке хранятся числа. Нужно выбрать только чётные числа и составить список пар
# (число; квадрат числа).
# Пример: 1 2 3 5 8 15 23 38
# Получить: [(2, 4), (8, 64), (38, 1444)]

# data=[1,2,3, 5, 8, 15, 23, 38]
# res=list()
# for i in data:
#     if i%2==0:
#         res. append((i, i**2))
# print(res)


## ИЛИ 

# def select(f, col):
#     return [f(x) for x in col]

# def where(f, col):
#     return [x for x in col if f(x)]

# data=[1,2,3, 5, 8, 15, 23, 38]
# res=select(int, data)
# print(res)
# res=where(lambda x:x%2==0, res)
# print(res)
# res=list(select(lambda x:(x, x**2), res))
# print(res)

#    С использованием map
# def where(f, col):
#     return [x for x in col if f(x)]

# data=[1,2,3, 5, 8, 15, 23, 38]
# res=map(int, data)
# print(res)
# res=where(lambda x:x%2==0, res)
# print(res)
# res=list(map(lambda x:(x, x**2), res))
# print(res)

#   С использованием map и filter 
# data=[1,2,3, 5, 8, 15, 23, 38]
# res=map(int, data)
# print(res)
# res=filter(lambda x:x%2==0, res)
# print(res)
# res=list(map(lambda x:(x, x**2), res))
# print(res)

###  ФУНКЦИЯ map
# list_1=[x for x in range(1,20)]
# print(list_1)
# list_1=list(map(lambda x:x+10, list_1))

## C клавиатуры вводится некий набор чисел, в качестве разделителя используется
# пробел. Этот набор чисел будет считан в качестве строки. Как превратить list строк в list чисел?
# data='15 156 96 3 5 8 52 5'
# print(data)
# # data=data.split()
# # print(data)
# data=list(map(int, data.split()))
# print(data)


###  ФУНКЦИЯ filter 
# data=[15, 65, 9, 36, 175]
# res=list(filter(lambda x:x%10==5, data))
# print(res)


###   ФУНКЦИЯ zip 
# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111, 222, 333]
# data = list(zip(users, ids, salary))
# print(data) # [('user1', 4, 111), ('user2', 5, 222), ('user3', 333)]

###   ФУНКЦИЯ enumerate
# users = ['user1', 'user2', 'user3']
# data = list(enumerate(users)
# print(data) # [(0, 'user1'), (1, 'user2'), (2, 'user3))]


###РАБОТА С ФАЙЛАМИ
# Режим a
# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a') # здесь указываем режим, в котором будем работать
# data.writelines(colors) # разделителей не будет
# data.close()

# Режим r
# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()

# Режим w
# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'w')
# data.writelines(colors) # разделителей не будет
# data.close()
