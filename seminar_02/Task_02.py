#'''Напишите программу которая принимает на вход число N и выдает последовательность из N членов 
#для N = 5: 1, -3, 9, -27, 81'''


'''print('Введите число N')
n = int(input())


def num_(n):
    for i in range(n):
        num = (-3) **i
        print(num, end = ' ')


num_(n)'''

#'''Для натурального n создать список состоящий из элементов последовательности 3n + 1
 #для n = 6: {4, 7, 10, 13, 16, 19}'''


'''n = 6


def num_list(n):
    temp = []
    for i in range(1, n + 1):
        temp.append((i*3) + 1)
    print(temp)


num_list(n)'''

#'''Напишите программу в которой пользователь будет задавать две строки , а программа - определить количество вхождений одной строки в другую.
 
# hjkfhhfkwjhkjh kjkljlk -> 2'''


'''a = 'aaaaabaaabaaaaaba'
b = 'aba'
def f(a,b):
    count = 0
    for i in range(len(a) - len(b)):
        if b == a[i:i + len(b)]:
            count += 1
    return count


print(f(a,b))'''
