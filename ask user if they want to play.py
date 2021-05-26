This is a simple quiz
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



#Ask if they are ready to take the quiz
status = input("Are you ready to take this general knowledge quiz :{}?: \na. Yes \nb. No \n=>".format( name)).lower()

#What if the user is not ready
if status == 'no' or status == 'n': 
    print("See you next time.")
    
#what if the user is ready
if status == 'yes' or status == 'y' or status == 'a':
    print("Welcome to the quiz.")

