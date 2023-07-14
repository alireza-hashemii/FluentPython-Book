# when a tuple is hashable
# hashable_tuple = (3,6,(7,9))
# print(hash(hashable_tuple))

# unhashable_tuple =(4,7,[8,3])
# print(hash(unhashable_tuple))

# list is not hashble
# list = [6,7]
# list2 = list
# print(list == list2)

# a simple checker

class Student:
    def __init__(self,num:int ,name:str) -> None:
        self.number = num
        self.name = name
    def __eq__(self) -> bool:
        return True

class Person:
    def __init__(self,name:str) -> None:
        self.height = int(34.5)
        self.name = str(name)

    def __eq__(self,name) -> bool:
        return self.name == name


code = [
    (98,"tehran"),
    (13,"china"),
    (1,"usa"),
]
country_codes = {country:code for code,country in code}
print(country_codes)