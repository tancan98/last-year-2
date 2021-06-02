Python 3.3.3 (v3.3.3:c3896275c0f6, Nov 18 2013, 21:19:30) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
#set of questions that are asked
#question 1

    print("\nQuestion: 1|score:{}".format(score))
    ans=input("What is the smallest country in the world?\na.Monaco\nb.Vatican City\nc.Tuvalu \nYour answer : ")
    if ans == 'vatican city' or ans == 'b'or == 'Vatican City' or == 'B':
        print("Correct")
        score+=1
