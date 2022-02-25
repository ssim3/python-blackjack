import random

# Call to create instance of Player / add a new player
class Player:

    def __init__(self, input_name, input_cash):
        self.name = input_name
        self.cash = input_cash

    def __repr__(self):
        info = "Name = {} \nCash = {}".format(self.name, self.cash)
        return info

    def bet(self, bet_value):
        self.cash -= bet_value

    def win(self, winnings):
        self.cash += winnings


def intro():

    print("""  
888888ba  dP    dP d888888P dP     dP   .88888.  888888ba      888888ba  dP         .d888888   a88888b. dP     dP        dP  .d888888   a88888b. dP     dP 
 88    `8b Y8.  .8P    88    88     88  d8'   `8b 88    `8b     88    `8b 88        d8'    88  d8'   `88 88   .d8'        88 d8'    88  d8'   `88 88   .d8' 
a88aaaa8P'  Y8aa8P     88    88aaaaa88a 88     88 88     88    a88aaaa8P' 88        88aaaaa88a 88        88aaa8P'         88 88aaaaa88a 88        88aaa8P'  
 88           88       88    88     88  88     88 88     88     88   `8b. 88        88     88  88        88   `8b.        88 88     88  88        88   `8b. 
 88           88       88    88     88  Y8.   .8P 88     88     88    .88 88        88     88  Y8.   .88 88     88 88.  .d8P 88     88  Y8.   .88 88     88 
 dP           dP       dP    dP     dP   `8888P'  dP     dP     88888888P 88888888P 88     88   Y88888P' dP     dP  `Y8888'  88     88   Y88888P' dP     dP  """)

    try:
        player_count = int(input("\n\n WELCOME! PLEASE ENTER THE NUMBER OF PLAYERS: "))
    except ValueError:
        print("Invalid input!")
        intro()

    players = []

    #loops through player_count and gets name and cash of each player
    # Adds each "Player" to list of players
    for i in range(player_count):
        name = input("\nPlayer {}, input your name: ".format(i + 1))
        cash = int(input("Player {}, input your cash: ".format(i + 1)))
        players.append(Player(name, cash))

    for i in players:
        print(i) 
    
    return players

def game(player_list):

    cards = {"Ace of Clubs": 1, "Ace of Diamonds": 1, "Ace of Hearts": 1, "Ace of Spades": 1, 
    "2 of Clubs": 2, "2 of Diamonds": 2, "2 of Hearts": 2, "2 of Spades": 2,
    "3 of Clubs": 3, "3 of Diamonds": 3, "3 of Hearts": 3, "3 of Spades": 3,
    "4 of Clubs": 4, "4 of Diamonds": 4, "4 of Hearts": 4, "4 of Spades": 4,
    "5 of Clubs": 5, "5 of Diamonds": 5, "5 of Hearts": 5, "5 of Spades": 5,
    "6 of Clubs": 6, "6 of Diamonds": 6, "6 of Hearts": 6, "6 of Spades": 6,
    "7 of Clubs": 7, "7 of Diamonds": 7, "7 of Hearts": 7, "7 of Spades": 7,
    "8 of Clubs": 8, "8 of Diamonds": 8, "8 of Hearts": 8, "8 of Spades": 8,
    "9 of Clubs": 9, "9 of Diamonds": 9, "9 of Hearts": 9, "9 of Spades": 9,
    "10 of Clubs": 10, "10 of Diamonds": 10, "10 of Hearts": 10, "10 of Spades": 10,
    "King of Clubs": 10, "King of Diamonds": 10, "King of Hearts": 10, "King of Spades": 10,
    "Queen of Clubs": 10, "Queen of Diamonds": 10, "Queen of Hearts": 10, "Queen of Spades": 10,
    "Jack of Clubs": 10, "Jack of Diamonds": 10, "Jack of Hearts": 10, "Jack of Spades": 10}

    dealer = Player("Dealer", 1000000000)
    bet = int(input("\nEnter your bet (Maximum 100000): "))
    
    valid_players = []

    # SUBTRACTING THE BETS FROM EACH PLAYER
    for i in player_list:
        # Makes sure player has enough money
        if (i.cash > bet):
            i.bet(bet)
            valid_players.append(i)          
        else:
            print("{} is too broke to bet, removed from the game.".format(i.name))
        
            
    print(valid_players)

    print("\n ------------------------------------- ")
    print("\nCARDS WILL NOW BE DRAWN!")

    


    

        
    



players = intro()
game(players)
