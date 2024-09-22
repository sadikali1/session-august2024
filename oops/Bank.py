class Bank():

    def getroi(self):
        return 10;

class BankOfAmerica(Bank):

    def getroi(self):
        return 8

class ICICI(Bank):

    def getroi(self):
        return 9

bank = Bank()
print(bank.getroi())

b = BankOfAmerica()
print(b.getroi())

c = ICICI()
print(c.getroi())
