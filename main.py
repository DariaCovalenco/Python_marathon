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



print('hello')

S1 = 'love'
S2 = 'bug'
print(S1+S2)
print('bagel' * 3)
my_str = "cupcake"
s = 'cheese'
print(s[3:5])
s = 'redvelvet'
print(s[2: :2])
print(my_str[0])
print(my_str[-1])

l = [5, 6, 7]
l. append(8)
print(l)
list.reverse (l)
print(l)
l.remove(7)
print(l)

x=9
y=8
print(x + y)
print (x * y)
print(x % y)
print(x // y)
print(divmod(x, y))
print(x ** y)
abs(2)
print(pow(x, y, 2))
print(divmod(x, y))

a = [9, 8, 7, 6]
print(a[0])
print(a[2])
print(a[1:])
print(a[: :2])
print (a[-2::-1])
print('{2}, {1}, {0}'.format('a', 'b', 'c'))
print ("To be done: {plans[0]}".format(plans = [1, 2, 3]))

a = (8, 7, 6, 5, 4, 3, 3, 2)
print(a.__sizeof__())
print(tuple("hollywood"))
print(a[2])
print(a[:-2])
print(a[3:5])

book = {"term": "DNA", "number": 33, "name": "Lucia"}
print(book["name"], book["term"])
print(book.keys())
print(book.copy())
print(book.items())
print(book.values())
print(book.update({"face": 5, "lips": 3}))
print(book)
print(book.clear())
print(book)
bookie = book.copy()
print(bookie)