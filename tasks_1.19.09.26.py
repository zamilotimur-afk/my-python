#Задача_1
def square(n):
    return n ** 2
square(6)

#Задача_2
def add(a, b):
    return (a + b)
add(3, 7)

#Задача_3
def get_evens(n):
    a  = []
    for k in n:
        if k % 2 == 0:
            a.append(k)
    return a
get_evens([1, 2, 3, 4, 5])

#Задача_4
def get_length(n):
    return len(n)
get_length("hello")

#Задача_5
def to_upper(n):
    return n.upper
to_upper("hello")

#Задача_6
def sum_list(n):
    count = 0
    for k in n:
        count+=k
    return count
sum_list([1, 2, 3, 4])

#Задача_7
def tuple_length(n):
    count = 0
    for k in n:
        count += 1
    return count
tuple_length((1, 2, 3))

#Задача_8
def get_keys(n):
    return list(n.keys())
get_keys({"a": 1, "b": 2})

#Задача_9
def count_vowels(n):
    count = 0
    a = ['a', 'e', 'i', 'o', 'u']
    for k in a:
        if k in n:
            count+=1
    return count
count_vowels("hello")

#Задача_10
def find_max(n):
    return max(n)
find_max([1, 5, 3, 9, 2])