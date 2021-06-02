

#set of questions that are asked
#question 1

    print("\nQuestion: 1|score:{}".format(score))
    ans=input("What is the smallest country in the world?\na.Monaco\nb.Vatican City\nc.Tuvalu \nYour answer : ").lower()
    if ans == 'vatican city' or ans == 'b':
        print("Correct")
        score+=1
