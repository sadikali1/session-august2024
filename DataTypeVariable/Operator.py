# +, -, /, *, %, //

'''
a = 10
b = 2

print(a+b)
print(a-b)
print(a*b)

a= 11
print(a/b)
print(a%b)

a = 20
b = 3
print(a//b)
'''
'''
# ==, !=, <, >, >=, <=
a = 10
b = 20
print(a == b)
print(a != b)
print(a<b)
print(a>b)
print(a>=b)
print(a<=b)
'''

# Assignment --
# =, +=, -=, *=, /=, %=, //=

'''
a = 10
#a +=20  #a = a + 20
#a -= 5  # a = a - 5
# a *= 5  # a = a * 5
# a /= 5 # a = a / 5
# a %=3  # a = a % 3
a //= 4  # a = a // 4
print(a)
'''

'''
# bitwise | , &
a= 10
b = 20
c = 30
#print(a > b & b > c)  # True & True = True
                      # False & True = False
                      # True & False = False
                      # False & False = False
print(a < b | b > c) # False | False = False
                     # True | False = True
                     # True & True = True
                     # False & True = False
'''

'''
# logical operator  and, or, not
a = 10
b = 20
c = 30
print(a < b and b > c)  # True & True = True
                        # False & True = False
                        # True & False = False
                        # False & False = False

print(a > b or b > c) # False | False = False
                     # True | False = True
                     # True & True = True
                     # False & True = True

print(not(True))
'''

'''
# membership operator -- in, not in
name = "Rajesh Kumar"
print('R' not in name)

x = [1, 2, 3,4]
y = ["One", "Two", "Thee"]
print(5 in x)
print("One" in y)
'''

# identity operator -- is, is not
a = 10
c = 20
print(a is c)



