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


from functools import reduce
from operator import add

# two diffrent ways of adding numbers from 0 to 99

print(reduce(add,range(100)))

print(sum(range(100)))

