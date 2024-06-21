import random

card = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_hand = []
comp_hand = []

for i in range(2):
    player_hand.append(random.choice(card))
    comp_hand.append(random.choice(card))

def stats():
    ace()
    print(f"Your cards: {player_hand}, current score: {sum(player_hand)}")
    print(f"Computer cards: {[comp_hand[0]]}")

def outcome():
    player_score = sum(player_hand)
    comp_score = sum(comp_hand)
    if player_score > 21:
        print("You lose, you busted!")
    elif comp_score > 21:
        print("Computer busts, you win!")
    elif player_score > comp_score:
        print("You win!")
    elif player_score < comp_score:
        print("You lose!")
    else:
        print("It's a tie!")

def ace():
    for i in range(len(player_hand)):
        if player_hand[i] == 11 and sum(player_hand) > 21:
            player_hand[i] = 1
    for i in range(len(comp_hand)):
        if comp_hand[i] == 11 and sum(comp_hand) > 21:
            comp_hand[i] = 1

def begin():
    end = False
    play_choice = input("Would you like to play a game of Blackjack? 'y' or 'n': ")
    if play_choice == "y":
        stats()
        while not end:
            if sum(player_hand) < 21:
                ask = input("Would you like another card? 'y' or 'n': ")
                if ask == "y":
                    player_hand.append(random.choice(card))
                    ace()
                    stats()
                    if sum(player_hand) > 21:
                        end = True
                        print(f"Your cards: {player_hand}, current score: {sum(player_hand)}")
                        print(f"Computer cards: {comp_hand}, computer score: {sum(comp_hand)}")
                        print("You lose, you busted!")
                elif ask == "n":
                    print(f"Your cards: {player_hand}, current score: {sum(player_hand)}")
                    print(f"Computer cards: {comp_hand}, computer score: {sum(comp_hand)}")
                    while sum(comp_hand) < 17:
                        comp_hand.append(random.choice(card))
                        ace()
                    print(f"Your cards: {player_hand}, current score: {sum(player_hand)}")
                    print(f"Computer cards: {comp_hand}, computer score: {sum(comp_hand)}")
                    end = True
                    outcome()
            elif sum(player_hand) == 21:
                end = True
                print("You Win with Blackjack!")
            else:
                ace()
                if sum(player_hand) > 21:
                    end = True
                    print("You Lose, you busted!")

begin()