
height = float(input("enter your height in m: "))
weight = int(input("enter your weight in kg: "))


#print(int((weight / height) * height))
bmi = int(weight / height ** 2)
print(bmi)