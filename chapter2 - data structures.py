# There are 2 sequence types in python
# first one is container sequences like list - tuples amd the second one is called flat sequences

import time
from random import random
import random
import sys
import bisect
from array import array
from collections import namedtuple
import array
listcomps = [i for i in range(5)]
print(listcomps)

# cartesian product example
ss = ["A", "B", "C"]
bb = [1, 2, 3, 4, 5, 6, 7, 8, 9]
listcomp = [(s, b) for s in ss
            for b in bb]

print(listcomp)


symbols = "^@#$>{}"
array = array.array("I", (ord(i) for i in symbols))
for i in array:
    print(i)

t = (11, 2)
quotient, remainder = divmod(*t)
print((quotient, remainder))


l = ("{A:15} | {B!r:} | {C:1=+7}".format(A="", B="st", C=-255555))
print('{:b}'.format(25))
print(l, end="")


print("everything {players[3]}".format(players=[4, 3, 2, 5, 4]))
print("salam {mo} sotoona ".format(6, mo=45))


City = namedtuple('City', ["province", "longtitude", "latitude"])
print(type(City))
city = City("Tehran", 15268984, 108794)
print(city)
california = ("CA", 2561, 82926569)
cal = city._make(california)
print(cal._fields())

l = list(range(8))
l[3::-2] = [8, 9]
print(l)

l = [[]] * 3
print(len(l))

l = ["bantttana", "gpe", "lemon", "apple"]
l.sort(reverse=False)
print(l)
print(sorted(l, key=len, reverse=True))
print(sorted(l, key=len))
print("------------")
print(sorted(l, key=len, reverse=True))


format_str = "{0:b} {0:^2d} {0:X}".format(14, 7, name=[14, 5, 6, 7, 8, 9, 90],)
print('{:-f}; {:+9.1f}'.format(3.14, +3.14))
print(len(format_str))
print(format_str)

HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
needles = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]

ROW_FMT = "{0:2d} @ {1:2d}      {2}{0:<2d}"


def demo(bisect_fn):
    for needle in reversed(needles):
        position = bisect_fn(HAYSTACK, needle)
        offset = position * "  |"
        print(ROW_FMT.format(needle, position, offset))


if __name__ == "__main__":
    if sys.argv[-1] == 'left':
        bisect_fn = bisect.bisect_left
    else:
        bisect_fn = bisect.bisect_right
    print("DEMO: ", bisect_fn.__name__)
    print("Haystack -> ", " ".join('%2d' % n for n in HAYSTACK))
    demo(bisect_fn)

narray = array("i", (i for i in range(10 ** 4)))
narray2 = array("i")
# with open("file.bin","wb") as fp:
#     narray.tofile(fp)
with open("file.bin", "rb") as fp:
    narray2.fromfile(fp, 10 ** 4)
for i in narray2:
    print(i)

print(narray2.typecode)


arr = array("d", (random() for i in range(10 ** 7)))
with open("file-bin.bin", "wb") as fp:
    arr.tofile(fp)

l = (random() for i in range(10 ** 7))
with open("file.txt", "w") as f:
    for i in l:
        m = f"{i}\n"
        f.write(m)

le = []
arr = array("d")

start = time.time()

with open("file-bin.bin", "rb") as fp:
    arr.fromfile(fp, 10 ** 7)

end = time.time()
print(f"Time elapsed -> {end - start}")

start2 = time.time()

with open("file.txt", "r") as fp:
    items = fp.read()
    for i in items:
        le.append(i)
end2 = time.time()
print(f"Time elapsed -> {end2 - start2}")

arr = array("h", [4, -3, 1, -2])
memv = memoryview(arr)
memv_cast = memv.cast("B")
print(memv_cast.tolist())
print(id(b"a"))

print(id(memv))
print(id(arr))

print(__builtins__.__dict__)



def country_tel(tel):
    if isinstance(tel , str):
        sub = [f"+{tel[0]}", tel[1:]]
    else:
        tel_to_str = str(tel)
        sub = [f"+{tel_to_str[0]}", tel_to_str[1:]]
    
    match sub:
        case ['+1', number]:
            print("calling from the US")
        case ['+5', number]:
            return "calling from Africa"
        case ['+3' | "+4", number]:
            return "calling from Europe" 
        case _:
            return "calling from the unknown continent"
        


flatfile_data = """
1905     raptor18-j     $1
1925     raptor18-m     $6
1935     raptor18-q     $5
1945     raptor18-e     $3
1965     raptor18-o     $10
"""

line_items = flatfile_data.split("\n")[1: -1]

year = slice(0,4)
mode = slice(0,21)
price = slice(24,28)
for item in line_items:
    print(item[year], item[price])

m = []
d = [[]] * 3
print(d)
print(d[0] is d[1])
        
let's play tic tac toe
board = []
for i in range(3):
    row = ["*"] * 3
    board.append(row)

while True:
    row = int(input("which row would you like to fill: ")) - 1 
    element = int(input("which element would you like to fill: ")) - 1

    is_board_empty = board[row][element] == "*"
    if is_board_empty:
        board[row][element] = "X"
        for i in board:
            print(i)
    else:
        print("this cell is already taken")
    
    if board[0][0] == board[1][1] == board[2][2]:
        print("you won the game")
        break
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i]:
            print("you won the game")
            break
        

a = "ali"
a += "m"
print()
        
from collections import deque

deck = deque(range(1,11), maxlen=10)
# print(deck)
# deck.append(4)
# print(deck)
# deck.appendleft(4)
# print(deck)
deck.rotate(-1)
print(4 in deck)
print(deck)

t = (2, 5, "t" ,[])
print(hash(t))