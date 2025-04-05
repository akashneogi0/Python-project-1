#We all have played snake, water gun game in our childhood. If you haven’t, google the
#rules of this game and write a python program capable of playing this game with the
#user

import random

def rps(n):
    
    comp=random.choice([1,2,3])

    if(n==1 and comp==3):
        print(f"You: Rock    Computer: Rock ")
        print("Draw")
    
    elif(n==2 and comp==1):
        print(f"You: Scissor   Computer: Scissor ")
        print("Draw")
    
    elif(n==3 and comp==2):
        print(f"You: Paper   Computer: Paper ")
        print("Draw")

    elif(n==1 and comp==2):
        print(f"You: Rock    Computer: Paper ")
        print("Computer wins")

    elif(n==2 and comp==3):
        print(f"You: Scissor    Computer: Rock ")
        print("Computer wins")

    elif(n==3 and comp==1):
        print(f"You: Paper    Computer: Scissor ")
        print("Computer wins")

    elif(n==1 and comp==1):
        print(f"You: Rock    Computer: Scissor ")
        print("You win")

    elif(n==2 and comp==2):
        print(f"You: Scissor    Computer: Paper ")
        print("You win")

    elif(n==3 and comp==3):
        print(f"You: Paper    Computer: Rock ")
        print("You win")

    ro()



def ro():

    r=input("Retry? Y/N: " )
    if r.lower()=="n":
        exit
    
    elif r.lower()=="y":
        retry()


    else:
        print("Press Y for retry N for cancel")
        ro()




    
    
   


def retry():
    dict={"r":1,"s":2,"p":3}
    cdict={"rock":3,"scissor":1,"paper":2}



    n=input("Enter R for Rock, S for Scrissor, P for Paper \n")



    if n.lower() != "p" and n.lower() !="s" and n.lower()!="r":
        print("Something went wrong, only enter R for Rock, S for Scrissor, P for Paper ")
        ro()

        

    

    else:
        user=dict[n]
        rps(user)


    


    

retry()
