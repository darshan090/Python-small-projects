print("Welcome to my quiz game!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()
    
print("Okay let's play :)")
score = 0

answer = input("What does CPU stands for? ")
if  answer.lower() == "central processing unit":
    print("Correct answer")
    score+=1
else:
    print("Incorrect!")
answer = input("What does GPU stand for? ")
if  answer.lower() == "graphics processing unit":
    print("Correct answer")
    score+=1
else:
    print("Incorrect!")
answer = input("What does RAM stand for? ")
if  answer.lower() == "random access memory":
    print("Correct answer")
    score+=1
else:
    print("Incorrect!")
answer = input("What does PSU stand for? ")
if  answer.lower() == "power supply":
    print("Correct answer")
    score+=1
else:
    print("Incorrect!")
    
print("you got " + str(score) + " questions correct")
print("you got " + str((score/4)*100) + "%")