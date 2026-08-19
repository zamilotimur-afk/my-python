#Задача_1
def square(n):
    return n ** 2
square(6)

#Задача_2
def add(a, b):
    return (a + b)
add(3, 7)

#Задача_3
def get_evens(*n):
    a  = []
    for k in n:
        if k % 2 == 0:
            a.append(k)
    return a
get_evens(1, 2, 3, 4, 5)