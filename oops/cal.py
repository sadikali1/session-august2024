class Calulaion1():

    def mul(self, a, b):
       return a * b;

class Display():

    def display(self, value):
        print(value)

class Divide(Calulaion1, Display):

    def divid(self, a, b):
       return  a/b


d = Divide()
result = d.divid(20, 5)
d.display(result)

result1= d.mul(20, 5)
d.display(result1)


# Parent class, Supper class, Base class
# child class, subclass, derived class