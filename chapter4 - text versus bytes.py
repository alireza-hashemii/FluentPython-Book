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


name = "welcome必"
by = bytes(name, encoding="utf_8")
# print(by[0])
# print(by[-1])
# print(len(by))


# different ways of instanciating binary types
f = bytes("hello", encoding="utf_8")

s1 = 'café'
s2 = 'cafe\N{COMBINING ACUTE ACCENT}'
print(s2)


from unicodedata import normalize, name
ohm = '\u2126'
ohm_c = normalize('NFC', ohm)
print(ohm == ohm_c)
print(normalize("NFC", ohm) == ohm_c)