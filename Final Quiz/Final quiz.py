from random import shuffle
import datetime
import time
x=datetime.datetime.now()

#initial score
score = 0

questions=[
[
    "What is the smallest country in the world?",
    {'answer':'b','option':'\na.Monaco \nb.Vatican City\nc.Tuvalu'}
    ],

[
    "Which country is the origin of the cocktail Mojito?",
    {'answer':'a','option':'\na.Cuba \nb.Mexico \nc.Columbia '}
    ],


[
    "Who was the NBA MVP in 2016?",
    {'answer':'a','option':'\na.Steph Curry \nb.Lebron James\nc.James Harden  '}
    ],    
   
[
    "What was Britney Spears’ first single called?",
    {'answer':'c','option':'\na.Ooh La La \nb.Outrageous\nc.Baby One More Time  '}
    ],    
   

[
    "What's the biggest animal in the world?",
    {'answer':'b','option':'\na.Elephant\nb.Blue Whale \nc.Megaladon '}
    ],    
     


[
    "What is the most populated country ?",
    {'answer':'c','option':'\na.India \nb.Russia \nc.China  '}
    ],    
     
[
    "Name the Coffee shop in US sitcom Friends?",
    {'answer':'a','option':'\na.Central Perks \nb.Starbucks \nc.Coffee Club '}
    ],    

[
    "How many permanent teeth does a dog have?",
    {'answer':'b','option':'\na.22 \nb.42 \nc.32 '}
    ],    
[
    "At which venue is the British Grand Prix held?",
    {'answer':'a','option':'\na.Silverstone \nb.Anglesey Circuit \nc.Thruxton  '}
    ],

[
    "What is the capital city of Australia?",
    {'answer':'c','option':'\na.Sydney \nb.Melbourne \nc.Canberra  '}

    ]
]

shuffle(questions)
#This is a simple quiz

#Ask for name
def greet():
    global name
    while True:
        name = input("Please enter your name : ")
        if name.replace(' ','').isalpha():
            break
        print("Enter alphabets only")


def age(): #To ask for user's age
    global age
    while True:
        age = (input("Please Write Your Age : "))
        if age.replace(' ','').isnumeric(): #Ignores spaces
            if 3< int(age)<100:
                break
            else:
                print("Sorry you are not in the age group to play this quiz.") #Does not allo ages between 3 and 100
                exit()
        else:
            print("You have entered an ivalid input") #Error message



#Ask if they are ready to take the quiz
def status():
    while True:
        status = input("Are you ready to take this general knowledge quiz ?: \na. Yes \nb. No \n=>")
        if status == 'no' or status == 'n' or status == 'b': 
            print("See you next time.")
            exit()
        if status == 'yes' or status == 'y' or status == 'a':
            print("Thats Amazing.")
            print("  ")
            break


def rounds():
    global r , total
    while True:
        try:
            r = int(input("\nPlease enter how many rounds do you want to play there are a total of 10 round at max. : "))
            print("...................................................")
            if 0<r<=10:
                break
            else:
                print("Please enter the rounds in 1-10 only")
        except:
            print('Please enter rounds in numbers only (The max is 10)')
print("  ")

print('*****************************************************************')

print("    ")
print("#################################################################")
print("#################################################################")
print("    ")
print("                 WELCOME TO MY GENERAL KNOWLEDGE QUIZ")
print("    ")
print("-----------------------------------------------------------------")
print("-----------------------------------------------------------------")
print("    ")


print("#################################################################")

print("      -------------- Date & Time -------------- ")
print("             ",x,"                   ")
print("----------- This is a quiz by Ishaan Sonar ------------")

print("#################################################################")
print("    ")
print("    ")


#Calling The Fuction



greet()#calling the greet function
age()#calling the age function
status()#calling the status function
rounds()#calling the rounds function

## score mechanics
while r >0:
    
    data = questions[0]
    q = data[0]
    data =data[1]
    answer = data['answer']
    option = data['option']

    print(q)
            else:
                print("**********************************************************")
                print("The Answer You have Chosen Is Not Correct. The Right Answer Is ",answer)    
                print("**********************************************************")
                print("=======")
                print("your score is",score)
                print("=======")


            del questions[0]
            r-=1
            break
        else:
            print("please enter the alphabet for the chosen option")
           

           
                   


print("Your Final Score Is",score)
print("Thanks For Playing")
    print(option)
    while True:
        user_answers = input("Please enter your answer here : ").lower().replace(' ','')
        if user_answers =='a' or user_answers == 'b' or user_answers == 'c' :
            if user_answers == answer:
                print("***************************")
                print("Nice You Got It Right Answer ")
                print("***************************")
                score +=1
                print("=======")
                print("your score is",score)
                print("=======")
            else:
                print("**********************************************************")
                print("The Answer You have Chosen Is Not Correct. The Right Answer Is ",answer)    
                print("**********************************************************")
                print("=======")
                print("your score is",score)
                print("=======")


            del questions[0]
            r-=1
            break
        else:
            print("please enter the alphabet for the chosen option")
           

           
                   


print("Your Final Score Is",score)
print("Thanks For Playing")









        






















        














