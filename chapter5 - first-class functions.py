def salam():
    print("Hello")

def s(rm):
    print(rm,"salam")


s(salam)


def fact(num):
    return 1 if num < 2 else num * fact(num - 1)


print(list(map(fact,range(6))))
# alternative with list comps 
print([fact(n) for n in range(6)])

print(list(map(fact, filter(lambda n: n % 2, range(6)))))

print(bool(3 % 2))

def custom_reverse(ent):
    return ent[::-1]

list_words = ["amir","sepehr","behnam","mohammad","saghar","sepide"]
f=  sorted(list_words,key=custom_reverse)
print(f)


from functools import reduce
from operator import add

# two diffrent ways for adding numbers from 0 to 99

print(reduce(add,range(100)))

print(sum(range(100)))

def if_odd(num:int,num2):
    return num * num2

f = reduce(if_odd,range(1,4))
print(f)


names = ["aireza","mohammad","sepide","maria","Jack","natalie"]

def inout(nm):
    if len(nm) > 5:
        return nm
    return None


print(list(map(inout,names)))


list = ["sepehr","Xaraza","abbass","pedram","sara","sophia","kiarash"]
print(sorted(list,key=lambda item: item[::-1]))

import random
from typing import Any

class BingoCage:
    def __init__(self,items):
        self._items = list(items)
        random.shuffle(self._items)
    
    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('Pick from vacant empty cage')
        
    def __call__(self):
        return self.pick() 

first_bingo = BingoCage(range(7))
print(first_bingo())


def fact(num):
    return 1 if num < 2 else num * fact(num - 1)

class A:
    pass

obj = A()
print(set(dir(fact))  - set(dir(obj)))

def tag(name, *content, cls=None, **attrs):
    if cls is not None:
        attrs["class"] = cls
    
    if attrs:
        attrs_str = " ".join(' %s="%s"' % (attr,value) for attr,value in sorted(attrs.items()))
    else:
        attrs_str = ''
    
    if content:
        return "".join("<%s %s >%s</%s>" % (name,attrs_str,content[0],name))
    
    else:
        return "<%s %s ></%s>" % (name,attrs_str,name)
    
tag1 = tag("p","is that working really?",cls="border-radius",textalign="justify")
print(tag1)


def how_func_works(* , p = None):
    print(p)


how_func_works(p=4)


# generaly we have 5 types of arguments in python
# 1-keyword argument 2-positional argument 3-arbitrary keyword argument 
# 4- arbitrary positional argument 5- default argument 

# ! Note that some resources have considered option 3 and 4 as a single option

# We make positional-only args with / sign.moreover keyword-only
# args can be declared by the usage of * (asterisk sign)


def clip(text:str , max_len=80):
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ',max_len)
            if space_before >= 0:
                end = space_after
    if end is None:
        end = len(text)
    
    return text[:end].rstrip()

clip_func = clip("alireza hashemi hastam ashegh bazi babache ha",max_len=20)
print(clip_func)
from inspect import signature
def introspection(*args, **kwargs):
    sign = signature(introspection)
    print(sign.bind(4,6))

introspection(4,7,5,v=5,b=7)

from functools import reduce
from operator import mul

def fact_lambda(n):
    return reduce(mul,range(1,n+1))

print(fact_lambda(5))

from operator import itemgetter, attrgetter
vecinity_data = [
    ("Japan","Jp",34000000,(43563,-7613834)),
    ("The Us","Us",32643346,(353,4151834)),
    ("Australia","Aus",5476934,(453,-9762434)),
    ("England","Eng",4364242222,(4533,1764834)),
]

for city in sorted(vecinity_data, key=itemgetter(1)):
    print(city)

from operator import mul
from functools import partial

triple = partial(mul,2)

print(triple(4))


# Edition 2
from coordinates import Coordinate

beijing = Coordinate(35.45,58.34, order=["lan","lon"])

shanghai = Coordinate(35.45,58.34, order=["lan","lon"])

print(beijing == shanghai)

from typing import NamedTuple
class Coordinate(NamedTuple):
    lat: float
    lon: float

    def __str__(self):
        ns = 'N' if self.lat >= 0 else 'S'
        we = 'E' if self.lon >= 0 else 'W'
        return f'{abs(self.lat):.1f}°{ns}, {abs(self.lon):.1f}°{we}'


tehran = Coordinate(**{"lat":45, "lon":23})
print(tehran)

from dataclasses import dataclass
# frozen
# kw_only
# __match_args__
@dataclass(frozen=True, kw_only=False,)
class Coordinate:
    lat: float
    lon: float

    def todo(self):
        self.lan = None
    
    def __str__(self):
        ns = 'N' if self.lat >= 0 else 'S'
        we = 'E' if self.lon >= 0 else 'W'
        return f'{abs(self.lat):.1f}°{ns}, {abs(self.lon):.1f}°{we}'


rome = Coordinate(23,53)
print(rome.__match_args__)

import typing
class Coordinate(typing.NamedTuple):
    a: int
    b: float = 1.1
    c = "salam"
 
baa = Coordinate(3)
baa.v = 4


