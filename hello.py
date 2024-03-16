def add_to_list(num, items=None):
    if items is None:
        items = list()
        items.append(num)
        print(items)
    else:
        items.append(num)
        print(items)

add_to_list(5)
add_to_list(10)
add_to_list(15)