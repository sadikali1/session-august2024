def fun(n1, n2=30, n3=40):
    print("First number :", n1)
    print("Second number :", n2)
    print("Third number :", n3)



fun(10)
fun(20, 40)
fun(n1=200, n3=100)


def fun1(*arg_list):
    for i in arg_list:
        print(i)


fun1("Apple", "Orange", "Banana", 1, 2, 4)