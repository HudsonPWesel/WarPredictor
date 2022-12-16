import numpy as np
import pandas as pd

master_deck = []


def main():
    """Start of program...!"""
    try:
        i: int = int(input("Please enter the amount of trials to run: "))
    except:
        return
    run(i)
    
def run(epochs: int):
    """Run the simulation a set amount of times"""
    for i in range(1, epochs+1):
        # % Program Finished
        print(str(i) + " | " + "{:.2f}".format((i/epochs)*100) + "%")
        # Run one simulation (Saves output globally)
        simulate_game()

def set_decks():
    for i in range (4):
        for j in range (2, 15):
            master_deck.append(j)
    print(len(master_deck))
    print(len(master_deck[0:26]))
(master_deck[26:])
    
            
def simulate_game():
    set_decks()
    

            
    # Shuffle Deck 
    np.random.shuffle(master_deck)

        
if __name__ == '__main__':
    main()