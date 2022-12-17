class Player:
    def __init__(self, deck, war_hand, side_deck, num_wins, num_losses):
        self.deck = deck
        self.side_deck = side_deck
        self.num_wins = num_wins
        self.war_hand = war_hand
        self.num_losses = num_losses

    def has_cards(self):
        if(len(self.deck) > 0 or len(self.side_deck) > 0):
            return True
        return False

    def has_cards_for_war(self):
        if(len(self.deck) >= 4 or len(self.side_deck) >= 4):
            return True
        elif len(self.deck) + len(self.side_deck) >= 4:
            return True
        return False

    def draw_card(self, index_pos):

        if len(self.deck) != 0:
            # print("MAIN DECK + " + str(len(self.deck)))

            card = self.deck[index_pos]

            # Remove card from main deck
            del self.deck[index_pos]

            self.war_hand.append(card)
            return card

        elif len(self.side_deck) != 0 and len(self.deck) == 0:
            # print("SIDE DECK + " + str(len(self.deck)))
            card = self.side_deck[index_pos]

            # Remove card from side_deck
            del self.side_deck[index_pos]

            self.war_hand.append(card)
            return card
