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

# def make_averager():
#     total = 0
#     count = 0
#     def averager(__new_value):
#         nonlocal count, total
#         count += 1
#         total += __new_value
#         return total / count
#     return averager

# d = make_averager()
# print(d(34))


# import time

# def clock(func):
#     def clocked(*args):
#         start = time.perf_counter()
#         result = func(*args)
#         elapsed = time.perf_counter() - start
#         name = func.__name__
#         arg_str = " ".join(str(arg) for arg in args)
#         print(f"[Elapsed Time: {elapsed:0.8f}s] {name}({arg_str} -> {result!r})")
#         return result
#     return clocked



# @clock
# def fibonacci(n):
#     if n < 2:
#         return n
#     return fibonacci(n - 2) + fibonacci(n - 1)

# print(fibonacci([6]))

# import time
# def track(func):
#     items = {
#         "Models": ['F8', 'I20', "S12"],
#         "Quantity": [34,30,32],
#         "Last_sold": [None, None, None]
#     }

#     def change_warehousee(*args):
#         nonlocal items
#         particular_object = int(items["Models"].index(args[0]))
#         items["Quantity"][particular_object] += 1

    
#         item_chosen = items.get(args[0])
#         function = func(item_chosen)
#         print(items)
#         return function
        
#     return change_warehousee

# @track
# def shop(item: any):
#     return "It is added to the cart"



# print(shop("I20"))
