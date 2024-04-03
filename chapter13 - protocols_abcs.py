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