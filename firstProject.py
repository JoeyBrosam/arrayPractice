print("Hello World!")
newListItem = 0
myList = [1, 2, 3]
for i in range(3):
    newListItem = int(input("Input a number:"))
    myList.append(newListItem)
for i in range(len(myList)):
    print(myList[i])