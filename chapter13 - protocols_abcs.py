# generally protocol specifies the set of methods witch an object must have 
# in order to fullfil a role. or to be named as a specific type

# partial Sequence Protocol
class Vowels():
    def __getitem__(self,i):
        return "AOEUI"[i]

vowels = Vowels()
vowels[2]

# we have 2 different type of protocols in python. dynamic and static protocol
# the primary differnece is that dynamic protocols are implicit and are known
# by interpreter itself. you can implement just part of them and your program still works 
# well , but in dynamic protocols you must implement all the required and decleared
# methods to be able to use dynamic typing.

# The Sequence abc is a formalized interface for sequences in python and it's implicitly 
# known to interpreter. you don't need to implement all it's methods to have a seq type.


# Here is an example of monkey patching - it is mainly about changing the 
# behaviour of a class at runtime without changing it's source code.
class BasketballTeam:
    def __init__(self) -> None:
        self.team = "John Andrew Zack Conor"


def subscriptable(self, position):
    team = self.team.split(" ")
    return team[position]

BasketballTeam.__getitem__ = subscriptable

t = BasketballTeam()
t[0]


# here is what fast-fail philosophy means and whent it'd be better to be used.