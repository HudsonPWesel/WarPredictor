from Player import Player
import numpy as np
import pandas as pd
import sys


master_deck = []
player_one = Player([], [], [], 0, 0)
player_two = Player([], [], [], 0, 0)

num_single_wars = [0]
num_double_wars = [0]
num_total_wars = [0]
num_concated_wars = [0]
num_draws = [0]
war_counter = 0


def main():
    """Start of program...!"""
    try:
        i: int = int(input("Please enter the amount of trials to run: "))
    except:
        return
    run(i)


def display_DataFrame():
    # MAKE DYNAMIC FRAME
    print(
        pd.DataFrame({
            "Single-Wars": num_single_wars,
            "Double-Wars": num_double_wars,
            "Concated-Wars": num_concated_wars,
            "Total-Wars": num_total_wars,
            "Player-1-Wins": player_one.num_wins,
            "Player-2-Wins": player_two.num_wins,
            "Draws": num_draws,

        })
    )


def run(epochs: int):
    """Run the simulation a set amount of times"""
    for i in range(1, epochs+1):
        print(str(i) + " | " + "{:.2f}".format((i/epochs)*100) + "%")
        # % Program Finished

        # Run one simulation (Saves output globally)
        simulate()
    display_DataFrame()


def simulate():
    set_decks()
    simulate_game()


def set_decks():
    # Clear Player's Deck From Prev. Game
    player_one.deck.clear()
    player_two.deck.clear()

    # Clear Player's Side-Deck From Prev Game
    player_one.side_deck.clear()
    player_two.side_deck.clear()

    for i in range(4):
        for j in range(2, 15):
            master_deck.append(j)

    np.random.shuffle(master_deck)

    # Set Player Decksp
    player_one.deck = master_deck[0:26]
    player_two.deck = master_deck[26:]


def win_round(winning_player, losing_player):
    # Draw Cards

    for i in winning_player.war_hand:
        winning_player.side_deck.append(i)
    for j in losing_player.war_hand:
        winning_player.side_deck.append(j)
        # Clear Side Deck
    print(len(winning_player.side_deck))
    print(len(losing_player.side_deck))
    # Add Drawn Cards to war_hand
    winning_player.war_hand.clear()
    losing_player.war_hand.clear()


def score_nth_war():
    global war_counter, num_single_wars, num_double_wars, num_concated_wars
    if(war_counter == 1):
        num_single_wars[0] += 1
        num_total_wars[0] += 1
    elif(war_counter == 2):
        num_double_wars[0] += 1
        num_total_wars[0] += 1
    else:
        num_concated_wars[0] += 1
        num_total_wars[0] += 1


def play_war():
    # Draw next three cards
    global war_counter
    if(player_one.has_cards_for_war() and player_two.has_cards_for_war()):
        for i in range(4):
            player_one.draw_card(0)
            player_two.draw_card(0)

        simulate_round(
            (player_one.war_hand[-1]), (player_two.war_hand[-1]))

    elif(player_one.has_cards_for_war()):
        win_round(player_one, player_two)
        return

    elif(player_two.has_cards_for_war()):
        win_round(player_two, player_one)
        return


def simulate_round(player_one_war_card, player_two_war_card):
    if(player_one_war_card > player_two_war_card):
        win_round(player_one, player_two)

    elif(player_two_war_card > player_one_war_card):
        win_round(player_two, player_one)

    else:
        global war_counter
        war_counter += 1
        score_nth_war()
        play_war()


def calc_win_losses():
    # Did player_one lose?
    if(player_one.has_cards()):
        player_one.num_wins += 1

    # Did player_two lose?
    elif(player_two.has_cards()):
        player_two.num_wins += 1

    # They Drawed!
    else:
        num_draws += 1


def simulate_game():

    current_card_index = 0

    # End of each while loop represents one round of play
    while(player_one.has_cards() and player_two.has_cards()):
        player_one_war_card = player_one.draw_card(current_card_index)
        player_two_war_card = player_two.draw_card(current_card_index)
        simulate_round(player_one_war_card,
                       player_two_war_card)
        global war_counter
        war_counter = 0
    calc_win_losses()

    # Reset_counter


    # Shuffle Deck
if __name__ == '__main__':
    main()
