# There are 2 sequence types in python
# first one is container sequences like list - tuples amd the second one is called flat sequences

# listcomps = [i for i in range(5)]
# print(listcomps)

# cartesian product example
# ss = ["A","B","C"]
# bb = [1,2,3,4,5,6,7,8,9]
# listcomp = [(s,b) for s in ss
#                   for b in bb]

# print(listcomp)


# import array
# symbols = "^@#$>{}"
# array = array.array("I",(ord(i) for i in symbols))
# for i in array:
#     print(i)

# t = (11,2)
# quotient , remainder = divmod(*t)
# print((quotient,remainder))



# l = ("{A:15} | {B!r:} | {C:1=+7}".format(A="",B="st",C=-255555))
# print('{:b}'.format(25))
# print(l,end="")


# print("everything {players[3]}".format(players=[4,3,2,5,4]))
# print("salam {mo} sotoona ".format(6,mo=45))

# from collections import namedtuple

# City = namedtuple('City',["province","longtitude","latitude"])
# print(type(City))
# city = City("Tehran",15268984,108794)
# print(city)
# california = ("CA",2561,82926569)
# cal = city._make(california)
# print(cal._fields())

# l = list(range(8))
# l[3::-2] = [8,9]
# print(l)

# l = [[]] * 3
# print(len(l))

# l = ["bantttana","gpe","lemon","apple"]
# l.sort(reverse=False)
# print(l)
# print(sorted(l,key=len,reverse=True))
# print(sorted(l,key=len))
# print("------------")
# print(sorted(l,key=len,reverse=True))



# format_str = "{0:b} {0:^2d} {0:X}".format(14,7,name=[14,5,6,7,8,9,90],)
# print('{:-f}; {:+9.1f}'.format(3.14, +3.14))
# print(len(format_str))
# print(format_str) 
from array import array
# import bisect
# import sys

# HAYSTACK = [1,4,5,6,8,12,15,20,21,23,23,26,29,30]
# needles = [0,1,2,5,8,10,22,23,29,30,31]

# ROW_FMT = "{0:2d} @ {1:2d}      {2}{0:<2d}"

# def demo(bisect_fn):
#     for needle in reversed(needles):
#         position = bisect_fn(HAYSTACK,needle)
#         offset = position * "  |"
#         print(ROW_FMT.format(needle,position,offset))


# if __name__ == "__main__":
#     if sys.argv[-1] == 'left':
#         bisect_fn = bisect.bisect_left
#     else:
#         bisect_fn =  bisect.bisect_right
#     print("DEMO: ",bisect_fn.__name__)
#     print("Haystack -> "," ".join('%2d' % n for n in HAYSTACK))
#     demo(bisect_fn)

# import random
# narray = array("i",(i for i in range(10 ** 4)))
# narray2 = array("i")
# # with open("file.bin","wb") as fp:
# #     narray.tofile(fp)
# with open("file.bin","rb") as fp:
#     narray2.fromfile(fp,10 ** 4)
# for i in narray2:
#     print(i)

# print(narray2.typecode)
from random import random


arr = array("d",(random() for i in range(10 ** 7)))
with open("file-bin.bin","wb") as fp:
    arr.tofile(fp)

l = (random() for i in range(10 ** 7))
with open("file.txt","w") as f:
    for i in l:
        m = f"{i}\n"
        f.write(m)

import time
le = []
arr = array("d")

start = time.time()

with open("file-bin.bin","rb") as fp:
    arr.fromfile(fp,10 ** 7)

end = time.time()
print(f"Time elapsed -> {end - start}")

start2 = time.time()

with open("file.txt","r") as fp:
    items = fp.read()
    for i in items:
        le.append(i)
end2 = time.time()
print(f"Time elapsed -> {end2 - start2}")