# def deco(func):
#     def target():
#         print("befor it runs")
#         func()
#         print("after it runs")
        
#     return target


# @deco
# def s():
#     print('salam')

# s()


# registry = []

# def register(func):
#     print(f'running register {func}')
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
#     print('registery ->', registry)
#     f1()
#     f2()
#     f3()

# if __name__ == "__main__":
#     main()

b = 6
def fun1(a):
    
    print(a)
    print(b)
    b = 9

fun1(3)
print(b)