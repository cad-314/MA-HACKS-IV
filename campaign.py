import time
global gold
global apples
apples = 0
gold = 0

def start():
    print ("Hello and welcome!") #print out hello
    name = input("What's your name:") #ask for player's name
    print ("Welcome, "+name+"!") #says welcome
    print ("The objective of this game is to collect apples.") #tells objective
    print ("After collecting the apples you sell them.") #explain game more
    choice = input("Do you want to play Y/N?") #ask if you want to play
    if choice == "Y": #starts game if you want to play
        begin() #goes to next function to start game
    if choice == "N": #ends games if you don't want to
        print ("Okay, bye...") #says bye


def begin():
    global apples #define global variables inside all functions
    global gold #define global variables inside all functions
    print ("Let's get started!") #says to get started
    if gold > 99: #you win if you have more than 99 gold
        print ("You've Won the game!") #print that you have won
        play = input("Do you want to play again?") #asks to win again
        if play =="Y": #restarts game if you want
            start()
        if play =="N": #ends games if you want
            print ("Congrats again!")
    pick = input("Do you want to pick an apple Y/N?") #asks if you want to pick an apple
    if pick == "Y": #if you want to pick
        time.sleep(1) #wait a second
        print ("You pick an apple.") #says you picked an apple
        apples=apples+1 #adds 1 to apple count
        print ("You currently have, ",apples," apples") #says how many apples you hvae
        begin() #starts again to see if you want to pick more
    if pick == "N": #moves on to selling apples if you don't want to pick more
        sell = input("Do you want to sell your apples Y/N?") #asks if you want to sell your apples
        if sell == "Y": #if you want to sell them
            global gold #gets the global variable gold
            global apples #gets the global variable apples
            print ("You currently have, ",apples," apples") #says how many apples you have
            print ("You have sold your apples.") #tells you you have sold you apples
            #gold_multiplier = 99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
            gold_multiplier = 10
            gold=apples*gold_multiplier #converts apples to gold
            apples=0 #sets apples for 0
            print ("Your gold is now:",gold) #says how many gold you have
            play = input("Do you want to play again?") #asks to win again
            if play =="Y": #restarts game if you want
                start()
            if play =="N": #ends games if you want
                print ("Ok. Good bye!")   
        if sell == "N": #if you don't want to sell apples, end game
             play = input("Do you want to play again?") #asks to win again
             if play =="Y": #restarts game if you want
                 start()
             if play =="N": #ends games if you want
                 print ("Ok. Good bye!")

start() #starts game
