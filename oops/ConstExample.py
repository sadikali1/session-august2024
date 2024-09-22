class ConstExample:
    count = 0
    col_code = "AB8963"

    # constractor
    def __init__(self, name, email, phone_number):
        self.name = name
        self.email =  email
        self.phone_number = phone_number
        ConstExample.count =  ConstExample.count + 1
        print("Constructor invoked automatically")

    def display(self):
        print(self.name, self.email, self.phone_number)


st = ConstExample("Scott", "scott@text.com", 89632896)
st.display()

st1 = ConstExample("Javed Alam", "javed@text.com", 9369263)
st1.display()

st2 = ConstExample("Rahul", "rahul@test.com", 983465986)
st2.display()

print(ConstExample.count)


# Parametrized constructor
# Default constructor, Non parametrized
