print ("opening instructions")

firstorsecond = input("would you like to go first? Enter Y or N")
if firstorsecond == "Y":
    print ("I will go second")
else:
    print ("I will go first")

numberofpiecesleft = 23
print ('there are 23 pieces. You may take 1, or 2, or 3 ')
while True:
    playertake = int(input("how many pieces will you take?"))
    numberofpiecesleft = numberofpiecesleft - playertake
    print ("there are " + str(numberofpiecesleft) + " left")
    computertake = numberofpiecesleft % 4
    print("I will take " + str(computertake))
    numberofpiecesleft = numberofpiecesleft - computertake
    print ("there are " + str(numberofpiecesleft) + " left")
    if numberofpiecesleft == 0:
        print("I win")
        break

'''
It seems that even the player is following the rules, the computer makes new rules

ould you like to go first? Enter Y or Nn
I will go first
there are 23 pieces. You may take 1, or 2, or 
how many pieces will you take?2
there are 21 left
I will take 1
there are 20 left
how many pieces will you take?1
there are 19 left
I will take 3
there are 16 left
how many pieces will you take?1
there are 15 left
I will take 3
there are 12 left
how many pieces will you take?2
there are 10 left
I will take 2
there are 8 left
how many pieces will you take?4
there are 4 left
I will take 0
there are 4 left
how many pieces will you take?

how many pieces will you take?0
there are 4 left
I will take 0
there are 4 left
how many pieces will you take?0
there are 4 left
I will take 0
there are 4 left
how many pieces will you take?

'''