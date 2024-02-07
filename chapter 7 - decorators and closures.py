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


registry = []

def register(func):
    print(f'running register {func()}')
    registry.append(func)
    return func

@register
def f1():
    print('running f1()')

@register
def f2():
    print('running f2()')

@register
def f3():
    print('running f3()')

def main():
    print('running main()')
    print('registery ->', registry)

if __name__ == "__main__":
    main()

