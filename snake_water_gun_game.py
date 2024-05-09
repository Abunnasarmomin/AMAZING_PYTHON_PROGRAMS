#                         Snake Water Gun Game                                #

import random #Importing random
def gamewin(comp, p):
    #If two values are equal declare a tie!
    if comp == p:
        return None
    
    #Check for all possibilities when computer chose s
    elif comp == 's':
        if p == 'w':
            return False
        elif p == 'g':
            return True
        
    #Check for all possibilities when computer chose w    
    elif comp == 'w':
        if p == 'g':
            return False
        elif p == 's':
            return True
        
    #Check for all possibilities when computer chose g    
    elif comp == 'g':
        if p == 's':
            return False
        elif p == 'w':
            return True

print("comp Turn: Snake(s) Water(w) or Gun(g)?")
randNo = random.randint(1, 3) #Select random value between 1,2,3
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'        

p = input("Your Turn: Snake(s) Water(w) or Gun(g)?")
a = gamewin(comp, p) #This function decides who win and who lose!
print("computer chose",comp)
print("player chose",p)
if a == None:
    print("The game is a tie!")
elif a:
    print("You win")
else:
    print("You Lose!")    

