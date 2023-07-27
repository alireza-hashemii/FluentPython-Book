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

# class Student:
#     def __init__(self,num:int ,name:str) -> None:
#         self.number = num
#         self.name = name
#     def __eq__(self) -> bool:
#         return True
#
# class Person:
#     def __init__(self,name:str) -> None:
#         self.height = int(34.5)
#         self.name = str(name)
#
#     def __eq__(self,name) -> bool:
#         return self.name == name


# code = [
#     (98, "tehran"),
#     (13, "china"),
#     (1, "usa"),
# ]
# country_codes = {country: code for code, country in code}
# # print(country_codes)
# print("hello friend")


# example_dict = {
#     "name": "alireza",
#     "lastname": "hashemi",
# }

# print((example_dict["name"]))
# print(example_dict.get("r", "key was not found."))


# import sys
# import re

# WORD_RE = re.compile("\w+")
# index = {}

# with open(sys.argv[1]) as fp:
#     for line_no, line in enumerate(fp,1):
#         for match in WORD_RE.finditer(line):
#             word = match.group()
#             column_no = match.start() + 1
#             location = (line_no,column_no)
#             index.setdefault(word,[]).append(location)
# print(index)

# get function od dict provides a chance to have a default value if dict wasn't found.
#! dict = {
#!     "name": "alireza",
#!     "lname": "hashemi",
#! }
#! print(dict.get("nasme","Key was not found"))
#! print(dict["name"])


# from collections.abc import MutableMapping, Mapping

# dict = {
#     1: 4
# }


# print(isinstance(dict, MutableMapping))


# class specializd_dict(dict):
#     def __init__(self):
#         pass


# d1 = specializd_dict()
# print(isinstance(d1,specializd_dict))

# t = "alireza"
# print(hash(t))
# y  = b"45"
# print(type(y))
# print(hash())

# various wayes of making a dictionary in python
# d_way1 = dict(hello="message", number=9)
# d_way2 = dict(zip(["one","two"],[3,6,9]))

# print(d_way1.update([("d", 5)]))
# print(d_way1)

# handeling missing keys in dicts
import re
import sys

# PATTERN = re.compile("\w+")
# index = {}
# with open(sys.argv[1], encoding="utf-8") as f:
#     for line_no, line in enumerate(f, start=1):
#         for match in PATTERN.finditer(line):
#             word = match.group()
#             column_no = match.start() + 1
#             location = (line_no, column_no)
#             index.setdefault(word, []).append(location)

# for word in sorted(index):
#     print(word, index[word])

# from collections import defaultdict

# PATTERN = re.compile("\w+")
# index = defaultdict(list)
# with open(sys.argv[1], encoding="utf-8") as f:
#     for line_no, line in enumerate(f, start=1):
#         for match in PATTERN.finditer(line):
#             word = match.group()
#             column_no = match.start() + 1
#             location = (line_no, column_no)
#             index[word].append(location)

# for word in sorted(index):
#     print(word, index[word])


# class MyDict(dict):
#     def __init_subclass__(cls) -> None:
#         return super().__init_subclass__()

#     def __missing__(self, key):
#         return f"Not a valid key {key}"


# d1 = MyDict([("2", "two"), ("4", "four")])
# print('4' in d1)

# class StrKey(dict):

#     def __missing__(self, key):
#         if isinstance(key, str):
#             raise KeyError(key)
#         return self[str(key)]

#     def get(self, key, default=None):
#         try:
#             return self[key]
#         except KeyError:
#             return default

#     def __contains__(self, key):
#         return key in self.keys() or str(key) in self.keys()


# d1 = StrKey([("2", "two"), ("4", "four")])
# print(29 in d1)
# print(d1.__contains__(2))


# from collections import OrderedDict

# D = OrderedDict([("7",7),("4",2)])
# print(D)

# import builtins
# from collections import ChainMap


# pylookup = ChainMap(locals(),globals(),vars(builtins))
# print(pylookup)


# set1 = {9, 5, 3}
# set2 = {1, 3}

# print(len(set1))
# print(len(set2))
# print("---------------------")
# print(len(set1 & set2))


# count = 0
# for member in set1:
#     if member in set2:
#         count += 1
# from dis import dis

# s = frozenset([4,5,2,8,96,34,57])
# print(s._hash())


# d = {
#     : "salam"
# }