import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def Main():

    def sum(a,b,c):
        return a + b + c

    def printBoard(xstate, zstate):
            zero =  'X' if xstate[0] else ('O' if zstate[0] else 0)
            one = 'X' if xstate[1] else ('O' if zstate[1] else 1)
            two = 'X' if xstate[2] else ('O' if zstate[2] else 2)
            three = 'X' if xstate[3] else ('O' if zstate[3] else 3)
            four = 'X' if xstate[4] else ('O' if zstate[4] else 4)
            five = 'X' if xstate[5] else ('O' if zstate[5] else 5)
            six = 'X' if xstate[6] else ('O' if zstate[6] else 6)
            seven = 'X' if xstate[7] else ('O' if zstate[7] else 7)
            eight = 'X' if xstate[8] else ('O' if zstate[8] else 8)

            print(f"{zero} | {one} | {two}")
            print(f"--|---|--")
            print(f"{three} | {four} | {five}")
            print(f"--|---|--")
            print(f"{six} | {seven} | {eight}")    

    def checkwin(xstate,zstate):
        wins = [[0,1,2,], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
        for win in wins:
            if(sum(xstate[win[0]], xstate[win[1]], xstate[win[2]]) == 3):
                print(f"{x} Wins The Game!")
                speak(f"{x} Wins The Game!")
                return 1
            if(sum(zstate[win[0]], zstate[win[1]], zstate[win[2]]) == 3):
                print(f"{o} Wins The Game!")
                speak(f"{o} Wins The Game!")
                return 1
        return -1

    if __name__ == "__main__":
        xstate = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        zstate = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        turn = 1 # 1 for X and 0 for O
        speak("Welcome To Ooo Xxx OX Game")
        print("Welcome To Ooo Xxx OX Game")
        speak("Enter X Player name:")
        x = input("Enter X Player name: ")  
        speak("Enter O Player name:")
        o = input("Enter O Player name: ")
        

        while(True):
            printBoard(xstate, zstate)
            if(turn == 1):
                print(f"{x} Chance - X")
                value = int(input("Enter a value: "))
                xstate[value] = 1
            else:
                print(f"{o} Chance - O")
                value = int(input("Enter a value: "))           
                zstate[value] = 1
            cw = checkwin(xstate,zstate)
            if(cw != -1):   
                print("Match Over")
                speak("Match Over")
                break
            turn = 1 - turn

        inp = input("q To Exit, r To Restart: ")
        if inp == "q":
            speak("Thanks For Playing")
            print("Thanks For Playing")
            exit()
        elif inp == "r":
            print("Restarting The game...")
            speak("Restarting The game...")
            Main()


Main()



