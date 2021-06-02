#Ask for name
while True:
    name = input("Please enter your name : ")
    if name.isalpha():
        break
    print("Enter alphabets only")


#Ask for age
while True:
    age = input("Please enter your age : ")
    if age.isnumeric():
        break
    print("Enter Numbers only")
