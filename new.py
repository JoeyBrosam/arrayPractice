#tshrit = ["Small", "Medium", "Large"]
#price = [8, 9, 12]

#for i in range(len(tshrit)):
#    print(tshirt[i])
#    print(price[i])
tshirts = [["small", 8], ["medium", 9], ["large", 12]]

for i in range(len(tshirts)):
    print(tshirts[i][0], tshirts[i][1])

#string formatting
name = "Fido"
age = 10
#print(name + " is " + str(age) + " years old")
#print("{} is {} years old".format(name, age))
print(f"{name} is {age} years old")