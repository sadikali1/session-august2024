from oops.A import A

class B(A):

    def printB(self):
        print("B child class method printed")


b = B()
b.printB()
b.printA()