import random 


suits = ('❤︎', '✦', '♠︎', '♣')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
value = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Card (): 
    
    def __init__ (self,suit,rank):
        self.suit = suit 
        self.rank = rank
        self.value = value[rank] #references the value dictionary which we defined above using user provided rank 
    
    def __str__(self):
        return self.rank + ' of ' + self.suit
        #sample: Two of hearts

class Deck(): 
    
    def __init__(self):
        #create a deck of 52 cards
        #this is a placeholder variable
        self.all_cards = [] #emptylist w/o import from user
        
        for suit in suits:
            for rank in ranks:
                #create the card objects
                created_card = Card(suit,rank) #each card is unique
                self.all_cards.append(created_card)
                
    def shuffle(self):
        #we just want to internally shuffle cards
        random.shuffle(self.all_cards)
        #doesn't return anything, does everything in place
        
    #dealing cards
    def deal_one(self):
        return self.all_cards.pop()
    
class Player():
    
    def __init__(self,name):
        self.name = name
        self.all_cards = [] #empty player hand
    
    #add or remove cards
    def remove_one (self):
        return self.all_cards.pop(0)
        
    def add_cards (self,new_card):
        #new_card can be 1 or more
        
        #for multiple
        if type(new_card) == type([]):
            self.all_cards.extend(new_card)
            
        #for 1 card
        else:
            self.all_cards.append(new_card)
    
    def __str__(self):
        return (f'Player {self.name} has {len(self.all_cards)} cards.')
    
player1 = Player('One')
player2 = Player('Two')

#setup deck, shuffle
new_deck = Deck()
new_deck.shuffle()

#split deck between 2 players
for x in range(26): #half of 52 cards
    player1.add_cards(new_deck.deal_one())
    player2.add_cards(new_deck.deal_one())

game_on = True
#while game_on

# round counter
round_num =0
    
while game_on: 
    round_num += 1 #round 1 up to ...
    print (f'****ROUND {round_num}****')
    
    #winner/loser checker
    if len(player1.all_cards)==0:   #all of player1's cards
        print ('Player 1 has lost. PLAYER 2 WINS!')
        game_on = False
        break
    if len(player2.all_cards)==0:
        print ('Player 2 has lost. PLAYER 1 WINS!')
        game_on = False
        break
    
    #STARTING NEW ROUND
    player1_cards = [] #current cards in play/ onhand
    #we remove 1 card from all_cards then add it in onhand cards
    player1_cards.append(player1.remove_one())
    
    player2_cards = []
    player2_cards.append(player2.remove_one())
    
    #while at war (tie!)
    # 3 situations:
    # Player1 > Player2
    # Player1 < Player2
    # Player1 == Player2
    
    #rules: each player needs to draw five additional cards if there is a tie.
    #player will lose if they dont have atleast 5 cards to win at the war
    at_war = True
    
    while at_war:
        
        #we use -1 position bc it is the last card put in the table
        if player1_cards[-1].value > player2_cards[-1].value:
            player1.add_cards(player1_cards) #gets all their cards back
            player1.add_cards(player2_cards) #takes opponents cards too
            at_war = False
            
        elif player1_cards[-1].value < player2_cards[-1].value:
            player2.add_cards(player1_cards) #takes opponents cards too
            player2.add_cards(player2_cards) #gets all their cards back
            
            at_war = False
            
        else: #at_war is still true, cards are equal
            print('WAR!')
            if len(player1.all_cards) <5:
                print('Player 1 has not enough cards, player lost')
                print('Player 2 wins!')
                game_on = False
                break
                
            if len(player2.all_cards) <5:
                print('Player 2 has not enough cards, player lost')
                print('Player 1 wins!')
                game_on = False
                break
            else: 
                #draw additional cards (5 cards)
                for num in range(5):
                    player1_cards.append(player1.remove_one())
                    player2_cards.append(player2.remove_one())