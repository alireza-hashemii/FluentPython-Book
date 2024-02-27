
# from dis import dis
# from collections import ChainMap
# import builtins
# from collections import OrderedDict
# from collections import defaultdict
# from collections.abc import MutableMapping, Mapping
# import re
# import sys
# hashable_tuple = (3, 6, (7, 9))
# print(hash(hashable_tuple))

# unhashable_tuple = (4, 7, [8, 3])
# print(hash(unhashable_tuple))


# list = [6, 7]
# list2 = list
# print(list == list2)


# class Student:
#     def __init__(self, num: int, name: str) -> None:
#         self.number = num
#         self.name = name

#     def __eq__(self) -> bool:
#         return True


# class Person:
#     def __init__(self, name: str) -> None:
#         self.height = int(34.5)
#         self.name = str(name)

#     def __eq__(self, name) -> bool:
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


# WORD_RE = re.compile("\w+")
# index = {}

# with open(sys.argv[1]) as fp:
#     for line_no, line in enumerate(fp, 1):
#         for match in WORD_RE.finditer(line):
#             word = match.group()
#             column_no = match.start() + 1
#             location = (line_no, column_no)
#             index.setdefault(word, []).append(location)
# print(index)


# dict = {
#     "name": "alireza",
#     "lname": "hashemi",
# }
# print(dict.get("nasme", "Key was not found"))
# print(dict["name"])


# dict = {
#     1: 4
# }


# print(isinstance(dict, MutableMapping))


# class specializd_dict(dict):
#     def __init__(self):
#         pass


# d1 = specializd_dict()
# print(isinstance(d1, specializd_dict))

# t = "alireza"
# print(hash(t))
# y = b"45"
# print(type(y))
# print(hash())


# d_way1 = dict(hello="message", number=9)
# d_way2 = dict(zip(["one", "two"], [3, 6, 9]))

# print(d_way1.update([("d", 5)]))
# print(d_way1)


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


# D = OrderedDict([("7", 7), ("4", 2)])
# print(D)


# pylookup = ChainMap(locals(), globals(), vars(builtins))
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

# s = frozenset([4, 5, 2, 8, 96, 34, 57])
# print(s._hash())


# d = {
#     "l": "salam"
# }



# dial_codes = [ 
#     (880, 'Bangladesh'),
#     (55, 'Brazil'),
#     (86, 'China'),
#     (91, 'India'),
#     (62, 'Indonesia'),
#     (81, 'Japan'),
#     (234, 'Nigeria'),
#     (92, 'Pakistan'),
#     (7, 'Russia'),
#     (1, 'United States'),
# ]
# dict_comp = {country:code for code,country in dial_codes}
# print(dict_comp)

# newversion_dcomp = {country:code for code,country in dial_codes if code < 70}
# print(newversion_dcomp)


# def key(**kwargs):
#     return kwargs

# returned = key(**{"a":4,"b":5},**{"aa":9,"p":0})
# print(returned)


# d1 = {"a":1, "b":2}
# d2 = {"a":3, "b":5 , "c":4}

# print(d1 | d2)

# d1 |= d2
# print(d1)