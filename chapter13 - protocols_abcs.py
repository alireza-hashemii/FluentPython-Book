# generally protocol specifies the set of methods witch an object must have 
# in order to fullfil a role. or to be named as a specific type

# partial Sequence Protocol
class Vowels():
    def __getitem__(self,i):
        return "AOEUI"[i]

vowels = Vowels()
vowels[2]