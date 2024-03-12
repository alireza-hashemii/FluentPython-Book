from dataclasses import dataclass
from collections import namedtuple
from typing import NamedTuple
# we have 3 primary ways to create dataclasses. First 2 of them
# are collections.namedtuple and typing.NamedTuple. Tiny differences 
# could be spot between them. In addition, the last one is dataclass  
# decorator provided by dataclasses module.

Point = namedtuple("Point", ["x", "y"])
math_qa = Point(3,5)


Book = namedtuple("Book", ["pages", "author", "sales"],defaults=["N/A","N/A","N/A"])
favourite_book = Book()

Perfume = namedtuple("Perfume", ["price", "capacity", "name"])
perf = Perfume()