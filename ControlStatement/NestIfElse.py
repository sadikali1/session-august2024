age = int(input("Please enter age :"))
weight = int(input("Please enter weight in KG :"))

if age >= 18:
    if weight >= 45:
        print("He is eligible for blood donation")
    else:
        print("Weight is less than 45 os person is not eligible for blood donation")
else:
    print("Age is less than 18 so person is not eligible for blood donation")
    