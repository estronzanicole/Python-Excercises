import sys
import random


ans = True 

while ans: 
    question = input("Ask the Magic ball a question (press enter to quit)")

    answers = random.randit(1, 8)

    if question == "":
        sys.ext()
    
    elif answers == 1:
        print("It is certain")
    
    elif answers == 2:
        print("Outlook is good")
    
    elif answers == 3:
        print("You may rely on it")

    elif answers == 4:
        print("Never")

    elif answers == 5:
        print("Ask again later")

    elif answers == 6:
        print("I think you are on to something, but ask again later")

    elif answers == 7:
        print("dont quit your job")

    elif answers == 8:
        print("hell no")