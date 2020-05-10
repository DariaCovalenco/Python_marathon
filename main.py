a = set('pecan')
print(a)
a = {'p', 'w', 'e', 'd'}
print(a)
a = {"a", "b", "c", "d"}
words = ["cold", "november","rain"]
set_words = set(words)
print(len(set_words))
set_words.remove("november")
print(set_words)
set_words.add("gr")
print(set_words)
second = ["move", "dance", "groove"]
a = set("good")
b = frozenset("bad")
print(a == b)

bs = b"bytes"
print("Байт".encode("utf-8"))
print(bytes("bytes", encoding="utf-8"))
print(bytes([52, 95, 100, 32, 18]))
print(chr(50), chr(20), chr(100))
print(b'\xd0\x91\xd0\xb0\xd0\xb9\xd1\x82\xd1\x8b'.decode('utf-8'))
lis = [1, 2, 3, 4, 5]
arr = bytes(lis)
print(arr)
arr = bytes()
print(arr)
List = [1, 2, 3, 4, 5]
arr = bytes(List)
print(arr)
d = {a: a ** 2 for a in range(7)}
print(d)
s = 'scrambledeggs'
print(s[3:5])
print(s[2:-2])
print(s[:6])
print(s[1:])
print(s[:])
print(s[::-1])
print(s[3:5:-1])
print(s[2::2])


