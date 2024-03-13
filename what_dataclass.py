from dataclasses import dataclass
from collections import namedtuple
from typing import NamedTuple
from dataclasses import field
from typing import ClassVar
# we have 3 primary ways to create dataclasses. First 2 of them
# are collections.namedtuple and typing.NamedTuple. Tiny differences 
# could be spot between them. In addition, the last one is dataclass  
# decorator provided by dataclasses  module.

Point = namedtuple("Point", ["x", "y"])
math_qa = Point(3,5)

Book = namedtuple("Book", ["pages", "author", "sales"],defaults=["N/A","N/A","N/A"])
favourite_book = Book()

Perfume = namedtuple("Perfume", ["price", "capacity", "name"])
perf = Perfume(34,250,"Dioe")
perf.capacity






@dataclass
class ClubMember:
    name: str
    # Note: don't pust mutuable types as parameters default value under any circumstance
    guests: list = field(default_factory=list)


# if you put type hint for a class field(variable) it will be 
# automatically converted into an instance field. so currently the best 
# way is to use ClassVar from typing module. Note that this just happens
# while you're working with @dataclass. 
@dataclass
class HackerClubMemeber(ClubMember):
    all_handles: ClassVar[set[str]] = set()
    handle: str = ""
# if you want to add some functionality for init special method in @dataclass, 
# you could use __post_init__ and it gets run right after the init generated by dataclass.
    def __post_init__(self):
        cls = self.__class__
        if self.handle == "":
            self.handle = self.name.split()[0]
        if self.handle in cls.all_handles:
            msg = f"the handle {self.handle} is already taken"
            raise ValueError(msg)
        cls.all_handles.add(self.handle)

ins = HackerClubMemeber("John Doe")
instance = HackerClubMemeber("John Surgey", handle="Johny")
