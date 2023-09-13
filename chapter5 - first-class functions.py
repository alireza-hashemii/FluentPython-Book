# def salam():
#     print("Hello")

# def s(rm):
#     print(rm,"salam")


# s(salam)


# def fact(num):
#     return 1 if num < 2 else num * fact(num - 1)


# print(list(map(fact,range(6))))
# # alternative with list comps 
# print([fact(n) for n in range(6)])

# print(list(map(fact, filter(lambda n: n % 2, range(6)))))

# print(bool(3 % 2))

# def custom_reverse(ent):
#     return ent[::-1]

# list_words = ["amir","sepehr","behnam","mohammad","saghar","sepide"]
# f=  sorted(list_words,key=custom_reverse)
# print(f)


# from functools import reduce
# from operator import add

# # two diffrent ways for adding numbers from 0 to 99

# print(reduce(add,range(100)))

# print(sum(range(100)))

# def if_odd(num:int,num2):
#     return num * num2

# f = reduce(if_odd,range(1,4))
# print(f)


# names = ["aireza","mohammad","sepide","maria","Jack","natalie"]

# def inout(nm):
#     if len(nm) > 5:
#         return nm
#     return None


# print(list(map(inout,names)))


# list = ["sepehr","Xaraza","abbass","pedram","sara","sophia","kiarash"]
# print(sorted(list,key=lambda item: item[::-1]))

# import random
# from typing import Any

# class BingoCage:
#     def __init__(self,items):
#         self._items = list(items)
#         random.shuffle(self._items)
    
#     def pick(self):
#         try:
#             return self._items.pop()
#         except IndexError:
#             raise LookupError('Pick from vacant empty cage')
        
#     def __call__(self):
#         return self.pick() 

# first_bingo = BingoCage(range(7))
# print(first_bingo())


def fact(num):
    return 1 if num < 2 else num * fact(num - 1)

class A:
    pass

obj = A()
print(set(dir(fact))  - set(dir(obj)))