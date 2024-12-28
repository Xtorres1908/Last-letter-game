import enchant 
#This function helps in indentifing if it is a real word or not, don't forget to install enchant
#use pip pyenchant 
def isword(word):
    d = enchant.Dict("en_US") 
    return d.check(word)
    
#This the code for the game, here a and b represents player 1 and player 2.
def lastletter(a,b):
    l=[]
    print("Hey, player 1 is:",a,",","player 2 is:",b)
    print("The Rules are: ")
    print("1.Player 1 will enter a word and then player 2 must enter another word starting from the last letter of the word given by the player 1, and game shall go on")
    print("2.Don't forget about the time!")
    
    for i in range(1):
        player1=input("Enter your word player-1: ")
        l.append(player1)
        check = isword(player1)
        if check==True:
            player2=input("Enter your word player-2: ")
        else:
            print("Oh!,",a,"you lose and the winner is: ",b)
            
    while True:
        check = isword(player2)
        if player2[0]==player1[-1] and player2 not in l and check==True:
            l.append(player2)
            player1=input("Enter your word player-1: ")
            check= isword(player1)
            if player1[0]==player2[-1] and player1 not in l and check==True:
                l.append(player1)
                player2=input("Enter your word player-2: ")
            else:
                print("Oh!,",a,"you lose and the winner is: ",b)
                break
        else:
            print("Oh!,",b,"you lose and the winner is: ",a)
            break
#Here you can try the code for yourself!
x = input("Enter the first player name: ")
y= input("Enter the second player name: ")
lastletter(x,y)
