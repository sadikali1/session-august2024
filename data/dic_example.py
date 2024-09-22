a = {}
b = {1:10, 2:30, 3:50, "A":"Rajesh", 3:"Rahul",  4:"Rahul"}

print(type(a))
print(b[3])
print(b[4])

b[1] = "Arif"
b[5] = "Javed"
print(b)

del b[1]
#del b[1]
#b.pop(3)

#b.clear()
print(b)


#del b
#print(b)

for key, value in b.items():
    print(key, value)