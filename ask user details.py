#This is a simple quiz
#initial score


score = 0
#Ask for name
def greet():
    global name
    while True:
        name = input("Please enter your name : ")
        if name.isalpha():
            break
        print("Enter alphabets only")
greet()

#Ask for age
while True:
    age = input("Please enter your age : ")
    if age.isnumeric():
        break
    print("Enter Numbers only")
