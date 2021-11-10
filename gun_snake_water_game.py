# Gun , Snake , Water : Mini game !!!
import random
def game(comp, player):
    if comp == player: # checking wheather both are equal or not !!!
        return None
        
    elif comp == 'w':
        if player == 's':
            return True
        elif player == 'g':
            return False
            
    elif comp == 'g':
        if player == 'w':
            return True
        elif player == 's':
            return False
            
    elif comp == 's':
        if player == 'g':
            return True
        elif player =='w':
            return False
            
rand = random.randint(1, 3) # Computer is selecting random string ...
print("Computer's turn !!!  Gun(1), Water(2), Snake(3) ")
if rand == 1:
    comp = 'g'
elif rand == 2:
    comp = 'w'
else:
    comp = 's'
    
player = (input('Pic carefully!  \n Gun(g), Water(w), Snake(s) ')) # player is selecting on its turn ... 
Result = game(comp, player)
if Result == None:
    print('Match Tied !!!')
elif Result == True:
    print('Player has won this match, Congrats!!! ') # Player has won the match ...
else:
    print('Player has lost this match, Sorry \n Plz try again ... ')



