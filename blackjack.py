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


    
