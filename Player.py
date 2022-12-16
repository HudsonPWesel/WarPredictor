class Player:
    def __init__(self, deck, war_hand, num_doublewars, num_concatenated_wars, num_wins, num_losses):
        self.deck = deck
        self.num_doublewars = num_doublewars
        self.num_concatenatedwars = num_concatenated_wars
        self.num_wins = num_wins
        self.war_hand = war_hand
        self.num_losses = num_losses