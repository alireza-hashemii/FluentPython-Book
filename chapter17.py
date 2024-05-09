# import re
import reprlib

# RE_WORD = re.compile(r'\w+')


# class Sentence:

#     def __init__(self, text) -> None:
#        self.text = text
#        self.words = RE_WORD.findall(text)

#     def __getitem__(self, index):
#         return self.words[index]

#     def __len__(self):
#         return len(self.words) 
    
#     def __repr__(self):
#         return "Sentence(%s)" % reprlib.repr(self.text)
    

# s = Sentence("I have been waiting for this brother.")
# print(s)
# for i in s:
#     print(i)

class Econvert:
    def __init__(self, email:str) -> None:
        self.email = list(email)
    
    def __len__(self):
        return len(self.email)

    def __repr__(self):
        return "Econvert(%s)" % reprlib.repr(self.email)
    
    def __iter__(self):
        pass
    
eml = Econvert("myson_sepehr@gmail.com")

from collections import abc
try:
    iter(eml)
except TypeError:
    print("Not Iterable")

print(isinstance(eml, abc.Iterable))