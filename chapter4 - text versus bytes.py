# simple encoding and decoding
d = "cafeη"
print(d)
dd = d.encode()
print(dd)
print(len(d))
print(len(dd))

a = "alireza"
c = b"alireza"
b = a.encode("ASCII")
if b == c:
    print("Encoding succesful.")



d = "cafeη".encode(encoding="utf-8")
print(d)

print(d[0])
print(d[:1])

