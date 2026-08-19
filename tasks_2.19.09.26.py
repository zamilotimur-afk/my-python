#Задача_1
def is_prime(n):
    if n > 2:
        print("False")

#Задача_2
def get_common(list1, list2):
    a = set(list1).intersection(list2)
    return list(a)
get_common([1, 2, 3, 4], [3, 4, 5, 6])

#Задача_3
def count_words(text):

#Задача_4
def reverse_words(text):
    b = []
    a = text.split(" ")
    for k in a:
        b = " ".join(k[::-1])
    return b
reverse_words("Hello world from Python") 

#Задача_5
def is_palindrome(text):
    a = text.lower().replace(" ", "")
    return a == a[::-1]
is_palindrome("А роза упала на лапу Азора")

#Задача_6
def sum_of_squares(*n):
    a = []
    for k in n:
        a.append(k**2)
    return sum(a)
sum_of_squares(1, 2, 3) 

#Задача_7
def get_unique_sorted(*n):
    a = sorted(set(n))
    return a
get_unique_sorted(5, 1, 3, 2, 5, 4, 3)

#Задача_8
def merge_dicts(dict1, dict2):
    return dict1 | dict2
merge_dicts({"a": 1, "b": 2}, {"b": 3, "c": 4})

#Задача_9
def count_case(text):
    a = 0
    b = 0
    for k in text:
        if k.isupper():
            a+=1
        elif k.islower():
            b+=1
    print("upper:", a , "lower:", b)
count_case("Hello World")

#Задача_10
def filter_long_words(words, n):
    a = []
    for k in words:
        if len(k) > n:
            a.append(k)
    return a
filter_long_words(["cat", "elephant", "dog", "giraffe"], 4)
