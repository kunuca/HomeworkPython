# Задача №17. Дан список чисел. Определите, сколько в нем 
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
# from random import randint
# size=int(input("Введите размер списка - "))

# list_1=[]
# for _ in range(size):
#     list_1.append(randint(-5,5))
    
# print(list_1)
# # list_2=[randint(-5,5) for _ in range(size)]

# result=set(list_1)
# print()
# print(result)
# n=len(result)
# print()
# print(f"Количество уникальных эмлементов в списке {n}")
    # ИЛИ 
# print(len(set([randint(-5,5) for _ in range(size)])))


# Дана последовательность из N целых чисел и число K. 
# Необходимо сдвинуть всю последовательность 
# (сдвиг - циклический) на K элементов вправо, 
# K – положительное число.
# Input:   [1, 2, 3, 4, 5] k = 3
# Output:  [3, 4, 5, 1, 2]
# from random import randint
# list_1=[randint(1,) for _ in range(randint(5,10))]

# list_1=[1, 2, 3, 4, 5]
# print(list_1)
# k=int(input('Введите число:'))

# for _ in range(k):
#     last_el=list_1.pop()
#     list_1.insert(0, last_el)
# print(list_1)
# print(list_1[-k:]+list_1[:-k])

# Напишите программу для печати всех уникальных значений 
# в словаре. 
# Input:  [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, 
#          {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, 
#          {"VIII":"S007"}] 
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
# from random import randint
# list_dicts=[{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, 
#          {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, 
#          {"VIII":"S007"}]
# unique_values=set()

# for cur_dict in list_dicts:
#     for key in cur_dict:
#         unique_values.add(cur_dict[key].strip())

# print(unique_values)
    #  ИЛИ
# unique_values=set()

# for cur_dict in list_dicts:
#     for key in cur_dict.keys():
#         unique_values.add(cur_dict[key].strip())

# print(unique_values)
    # ИЛИ
# unique_values=set()

# for cur_dict in list_dicts:
#     for value in cur_dict.values():
#         unique_values.add(value.strip())

# print(unique_values)
    # ИЛИ
# unique_values=set()

# for cur_dict in list_dicts:
#     for key in cur_dict:
#         unique_values.add(*cur_dict.values())

# print(unique_values)
    # ИЛИ
# unique_values=set()

# for cur_dict in list_dicts:
#     unique_values.update(cur_dict.values())

# print(unique_values)


# Дан массив, состоящий из целых чисел. 
# Напишите программу, которая подсчитает количество 
# элементов массива, больших предыдущего (элемента 
# с предыдущим номером) 
# Input: [0, -1, 5, 2, 3]
# Output: 2 

list_1=[0, -1, 5, 2, 3]
count=0
for i in range(len(list_1)-1):
    if list_1[i]<list_1[i+1]:
        count+=1
print(count)
    # ИЛИ
print(sum([1 for i in range(len(list_1) - 1) if list_1[i] < list_1[i + 1]]))