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



#Ask if they are ready to take the quiz
status = input("Are you ready to take this general knowledge quiz :{}?: \na. Yes \nb. No \n=>".format( name)).lower()

#What if the user is not ready
if status == 'no' or status == 'n': 
    print("See you next time.")
    
#what if the user is ready
if status == 'yes' or status == 'y' or status == 'a':
    print("Welcome to the quiz.")

#set of questions that are asked
#question 1

    print("\nQuestion: 1|score:{}".format(score))
    ans=input("What is the smallest country in the world?\na.Monaco\nb.Vatican City\nc.Tuvalu \nYour answer : ").lower()
    if ans == 'vatican city' or ans == 'b':
        print("Correct")
        score+=1
        print("Your score is",score)
    else:
        print("Oops incorrect the correct answer is Vatican city : ")
        if score <=0:
            score = 0
            print("Your score is",score)

#question 2

    print("\nQuestion: 2|score:{}".format(score))
    ans=input("Which country is the origin of the cocktail Mojito?\na.Cuba\nb.Mexico\nc.Columbia \nYour answer : ").lower()
    if ans == 'cuba' or ans == 'a':
        print("Correct")
        score+=1
        print("Your score is",score)
    else:
        print("Oops incorrect the correct answer is Cuba: ")
        if score <=0:
            score = 0
            print("Your score is",score)

#question 3

    print("\nQuestion: 3|score:{}".format(score))
    ans=input("Who was the NBA MVP in 2016?\na.Steph Curry\nb.Lebron James\nc.James Harden \nYour answer : ").lower()
    if ans == 'steph curry' or ans == 'a':
        print("Correct")
        score+=1
        print("Your score is",score)
    else:
        print("Oops incorrect the correct answer is Steph Curry: ")
        if score <=0:
            score = 0
            print("Your score is",score)
#question 4

    print("\nQuestion: 4|score:{}".format(score))
    ans=input("What was Britney Spears’ first single called?\na.Ooh La La\nb.Outrageous\nc.Baby One More Time\nYour answer : ").lower()
    if ans == 'baby one more time' or ans == 'c':
        print("Correct")
        score+=1
        print("Your score is",score)
    else:
        print("Oops incorrect the correct answer is Baby One More Time: ")
        if score <=0:
            score = 0
            print("Your score is",score)

    
#question 5

    print("\nQuestion: 5|score:{}".format(score))
    ans=input("What's the biggest animal in the world??\na.Elephant\nb.Blue Whale\nc.Megaladon\nYour answer : ").lower()
    if ans == 'blue whale' or ans == 'b':
        print("Correct")
        score+=1
        print("Your score is",score)
    else:
        print("Oops incorrect the correct answer is Blue Whale: ")
        if score <=0:
            score = 0
            print("Your score is",score)





#question 6

    print("\nQuestion: 6|score:{}".format(score))
    ans=input("What is the most populated country??\na.India\nb.Russia.\nc.China\nYour answer : ").lower()
    if ans == 'china' or ans == 'c':
        print("Correct")
        score+=1
        print("Your score is",score)
    else:
        print("Oops incorrect the correct answer is China: ")
        if score <=0:
            score = 0
            print("Your score is",score)




#question 7

    print("\nQuestion: 7|score:{}".format(score))
    ans=input("Name the Coffee shop in US sitcom Friends??\na.Central Perk\nb.Starbucks.\nc.Coffee Club\nYour answer : ").lower()
    if ans == 'central perk' or ans == 'a':
        print("Correct")
        score+=1
        print("Your score is",score)
    else:
        print("Oops incorrect the correct answer is Central Perk: ")
        if score <=0:
            score = 0
            print("Your score is",score)



#question 8

    print("\nQuestion: 8|score:{}".format(score))
    ans=input("How many permanent teeth does a dog have??\na.32\nb.42.\nc.22\nYour answer : ").lower()
    if ans == '42' or ans == 'b':
        print("Correct")
        score+=1
        print("Your score is",score)
    else:
        print("Oops incorrect the correct answer is 42: ")
        if score <=0:
            score = 0
            print("Your score is",score)



#question 9

    print("\nQuestion: 9|score:{}".format(score))
    ans=input("At which venue is the British Grand Prix held???\na.Silverstone\nb.Anglesey Circuit.\nc.Thruxton\nYour answer : ").lower()
    if ans == 'Silverstone' or ans == 'a':
        print("Correct")
        score+=1
        print("Your score is",score)
    else:
        print("Oops incorrect the correct answer is Silverstone: ")
        if score <=0:
            score = 0
            print("Your score is",score)



#question 10

    print("\nQuestion: 10|score:{}".format(score))
    ans=input("What is the capital city of Australia??\na.Sydney\nb.Melbourne.\nc.Canberra\nYour answer : ").lower()
    if ans == 'canberra' or ans == 'c':
        print("Correct")
        score+=1
        print("Your score is",score)
    else:
        print("Oops incorrect the correct answer is Canberra: ")
        if score <=0:
            score = 0
            print("Your score is",score)




print("Your Final Score Is",score)
print("Thanks For Playing : ")





        














