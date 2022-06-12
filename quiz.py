name = input("Please tell me your name: ")
score = 0

print("Welcome to my game", name)

playing = input("Would you like to play? ").lower()
if playing != "yes":
    print("Okey, " + str(name) + "." + " Goodbye.")
    exit()
else:
    print("Okay! Let's play!", name + ":)")
print(" ")
answer = input("What does CPU stands for?")

if answer == "central processing unit":
    print("Correct answer!")
    score = score+1
else:
    print("Incorrect ansswer. Better luck next time!")
print(" ")
print("Your have scored", score, ",please proceed to the next question", name)
print(" ")
answer = input("What does GPU stands for? ").lower()
if answer == ("graphics processing unit"):
    print("Correct answer! ", name, " ")
    score = score+1
else:
    print("Incorrect ansswer. Better luck next time!")
print("Your have scored", score, ",please proceed to the next question", name)
print(" ")

answer = input("What is lauren's date of birth? ").lower()
if answer == ("09/07/2016"):
    score = score+1
else:
    print("Incorrect ansswer. Better luck next time!")
#print ("Your have scored", score, "out of 3," ,name, "." + "see your result below")
print(" ")

print("Your have scored", score, ",out of 3 questions", name)

gender = input("are you a boy or a girl? ")
print(" ")

if score > 2:
    print("Your overrall score is not bad")
else:
    print("Do better next time", gender)
