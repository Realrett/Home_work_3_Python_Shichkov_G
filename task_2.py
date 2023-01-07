# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
list = [2, 8, 16, 32, 51, 44, 74, 88]

def multy_list(list):
    l = len(list)//2 + 1 if len(list) % 2 != 0 else len(list)//2
    new_list = [list[i]*list[len(list)-i-1] for i in range(l)]
    print(new_list)

multy_list(list)
