# registry = [] 

# def register(func): 
#     print(f'running register({func})') 
#     registry.append(func) 
#     return func 

# @register 
# def f1():
#     print('running f1()')

# @register
# def f2():
#     print('running f2()')

# def f3(): 
#     print('running f3()')


# def main(): 
#     print('running main()')
#     print('registry ->', registry)
#     f1()
#     f2()
#     f3()

# if __name__ == '__main__':
#     main() 



# def f(a):
#     print(a)
#     print(b)
# b  = 6
# f(3)

# b = 4
# def f2(a):
#     global b
#     print(a)
#     print(b)
#     b = 6

# f2(3)
# print(b)

# from typing import Any


# class Averager():
#     def __init__(self) -> None:
#         self.series = []

#     def __call__(self, __new_value) -> Any:
#         self.series.append(__new_value)
#         total = sum(self.series)
#         return total / len(self.series)

# av = Averager()


# def make_averager():
#     series = []
#     def averager(__new_value):
#         series.append(__new_value)
#         total = sum(series)
#         return total / len(series)
#     return averager

# d = make_averager()
# print(d(15))
# print(d(3))
# print(d(8))

# print(d.__code__.co_varnames)
# print(d.__code__.co_freevars)
# print(d.__closure__[0].cell_contents)