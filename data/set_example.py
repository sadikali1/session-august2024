a = {10, 20, 40, "Rahul", True, 100.50, 20, 50, 40}
b = {10,}
print(a)
print(type(a))
print(type(b))

#print(a[0])

a1 = [10, 20, 40, "Rahul", True, 100.50, 20, 50, 40]
print(a1)
print(set(a1))


a2 = set()
a3 = {}
print(type(a2))
print(type(a3))

a2.add(10)
a2.add(30)
a2.add("Rahul")
print(a2)

a2.update([40, 50])
print(a2)

a2.discard(100)
print(a2)

a2.remove(200)
print(a2)


'''
for value in a:
    print(value)
'''