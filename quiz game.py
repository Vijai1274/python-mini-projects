print("WELCOME TO QUIZ GAME")
ready = input("Are you ready to play? ")
score=0

if(ready.lower()=="yes"):
    print ("Okay lets play!")

    question1 = input("Q.no:1 What is the full form of TNPSC? ")
    if (question1.lower() == "tamilnadu public service commission"):
        print ("Correct")
        score+=1
    else:
        print("Incorrect")

    question2 = input("Q.no:2 What is the full form of UPSC? ")
    if (question2.lower() == "union public service commission"):
        print ("Correct")
        score+=1
    else:
        print("Incorrect")

    question3 = input("Q.no:3 What is the full form of TNUSRB? ")
    if (question3.lower() == "tamilnadu uniformed services requirement board"):
        print ("Correct")
        score+=1
    else:
        print("Incorrect")

    question4 = input("Q.no:4 What is the full form of SSC? ")
    if (question4.lower() == "staff selection commission"):
        print ("Correct")
        score+=1
    else:
        print("Incorrect")

    question5 = input("Q.no:5 What is the full form of TET? ")
    if (question5.lower() == "teacher eligibility test"):
        print ("Correct")
        score+=1
    else:
        print("Incorrect")

    question6 = input("Q.no:6 What is the full form of PSC? ")
    if (question6.lower() == "public service commission"):
        print ("Correct")
        score+=1
    else:
        print("Incorrect")

    question7 = input("Q.no:7 What is the full form of IPS? ")
    if (question7.lower() == "indian police service"):
        print ("Correct")
        score+=1
    else:
        print("Incorrect")

    question8 = input("Q.no:8 What is the full form of IFS? ")
    if (question8.lower() == "indian forest service"):
        print ("Correct")
        score+=1
    else:
        print("Incorrect")

    question9 = input("Q.no:9 What is the full form of IAS? ")
    if (question9.lower() == "indian administrative service"):
        print ("Correct")
        score+=1
    else:
        print("Incorrect")

    question10 = input("Q.no:10 What is the full form of IAF? ")
    if (question10.lower() == "indian air force"):
        print ("Correct")
        score+=1
    else:
        print("Incorrect")

else:
    quit()


print("Total Score: "+str(score))
if (score==10):
    print("Fantastic")

elif(score==9):
    print("Awesome")

elif(score==8):
    print("Wonderful")

elif(score==7):
    print("Beautiful")

elif(score==6):
    print("Marvelous")

elif(score==5):
    print("Wonderful")

elif(score==4):
    print("Good")

elif(score==3):
    print("Nice")

elif(score==2):
    print("Not bad")

elif(score==1):
    print("Try to score more")

else:
    print("Better luck next time")

print("Score percentage: "+str((score/10)*100)+"%")