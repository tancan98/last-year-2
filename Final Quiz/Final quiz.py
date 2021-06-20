from random import shuffle
import datetime
import time
x=datetime.datetime.now()

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


#This is a simple quiz
#initial score

score = 0
#Ask for name
def greet():
    global name
    while True:
        name = input("Please enter your name : ")
        if name.replace(' ','').isalpha():
            break
        print("Enter alphabets only")
greet()

#Ask for age
while True:
    age = input("Please enter your age : ")
    if age.replace(' ','').isnumeric():
        break
    print("Enter Numbers only")

    
    
    #Ask if they are ready to take the quiz
status = input("Are you ready to take this general knowledge quiz :{}?: \na. Yes \nb. No \n=>".format( name)).lower()

#What if the user is not ready
if status == 'no' or status == 'n' or status == 'b': 
    print("See you next time.")
    exit()
        
    
#what if the user is ready
if status == 'yes' or status == 'y' or status == 'a':
    print("Thats Amazing.")


def rounds():
    global r , total
    while True:
        try:
            r = int(input("\nPlease enter how many rounds do you want to play there are a total of 10 round at max. : "))
            if 0<r<=10:
                break
            else:
                print("Please enter the rounds in 1-10 only")
        except:
            print('Please enter rounds in numbers only (The max is 10)')

print('*****************************************************************')      

print("----------- WELCOME TO MY QUIZ ------------")
      
print('*****************************************************************')     
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

rounds()
## score mechanics
while r >0:
    
    data = questions[0]
    q = data[0]
    data =data[1]
    answer = data['answer']
    option = data['option']

    print(q)
    print(option)
    while True:
        user_answers = input("Please enter your answer here : ").lower().replace(' ','')
        if user_answers =='a' or user_answers == 'b' or user_answers == 'c' :
            if user_answers == answer:
                print("***************************")
                print("nice you got it right ")
                print("***************************")
                score +=1
                print("=======")
                print("your score is",score)
                print("=======")
            else:
                print("**********************************************************")
                print("oops the answer you have chosen is not correct. The right answer is ",answer)    
                print("**********************************************************")
                print("=======")
                print("your score is",score)
                print("=======")


            del questions[0]
            r-=1
            break
        else:
            print("please enter the alphabet for the chosen option")
           

           
                   


print("\nCongratulations {}!".format(name))
print("Your Final Score Is",score)
print("Thanks For Playing")







        














