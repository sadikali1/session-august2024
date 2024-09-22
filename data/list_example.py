a = [10, 20, False, True, "Raj Kiran", "Ramesh", "Javed" ]
b = [20, 10, False, True, "Raj Kiran", "Ramesh", "Javed" ]

'''
print(a == b)

print(type(a))
print(a)
print(a[1])

a[1] = "30"
print(a)
'''

# slicing
'''
print(a[1:3])
print(a[:])
print(a[3:5:2])

print(a[-1])
print(a[-7])
print(a[-6:-2])
print(a[-4:-2])
'''

a[0] = "Rajesh"
print(a)
a[1:3] = [30, 50]
print(a)
a[-6] = "Aakib"
#del a
#del a[0]
#del a[1:3]
print(a)

# l = a * 2
#print(l)

a1 = [10, 30, 40]
a2 = ["Ram", "Ajay", "John"]
# addition of two list
l = a1 + a2
print(l)
print(len(l))

# iteration of list
for a in l:
    print(a)

# checking value in list
print(10 in l)
print(50 in l)

# Append value
l.append("Scott")
print(l)

# delete value
l.remove(40)
print(l)

l1 = [10, 96, 43, 56, 3, 600, 44, 34]
print(max(l1))
print(min(l1))


# a list are in order
# list value can be access using index
# the list is mutable type
# number of various element can be store in a list

