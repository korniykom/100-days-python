import random

import art

print(art.logo)


def print_current_game_state():
    player_cards = ",".join(str(card) for card in player_hand)

    print(f"\tYour card: [{player_cards}], current score: {player_score}")
    print(f"\tComputer's first card: {computer_hand[0]}")

game_is_running = True

deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


while game_is_running:

    choice = input("Do you want to play game of Blackjack? Type 'y' or 'n'    ")

    player_hand = [deck[random.randint(0, len(deck) - 1)], deck[random.randint(0, len(deck) - 1)]]
    player_score = player_hand[0] + player_hand[1]

    if player_score > 21 and 11 in player_hand:
        player_hand[player_hand.index(11)] = 1

    computer_hand = [deck[random.randint(0, len(deck) - 1)], deck[random.randint(0, len(deck) - 1)]]
    computer_score = computer_hand[0] + computer_hand[1]

    if computer_score > 21 and 11 in computer_hand:
        computer_hand[computer_hand.index(11)] = 1

    if choice == "n":
        game_is_running = False
    elif choice != "n" and choice != "y":
        continue

    print_current_game_state()

    get_cards = input("Type 'y' to get another card, type 'n' to pass:\t")
    if(get_cards == "y") :
        while get_cards == "y":

            new_card = deck[random.randint(0, len(deck) - 1)]
            player_hand.append(new_card)
            player_score += new_card
            print_current_game_state()
            if player_score > 21:
                break
            get_cards = input("Type 'y' to get another card, type 'n' to pass:\t")

    if player_score > 21:
        print("You went over. You lose 😭")
        print(f"Computer score: {computer_score}")
        continue
    elif computer_score > player_score:
        print("You lose")
        print(f"Computer score: {computer_score}")
        continue
    while computer_score < player_score and computer_score < 21:
        computer_score += deck[random.randint(0, len(deck) - 1)]

    if computer_score > 21:
        print("You won")
        print(f"Computer score: {computer_score}")
        continue

    if computer_score > player_score:
        print("You lose")
        print(f"Computer score: {computer_score}")
        continue
    else:
        print("You won")
        print(f"Computer score: {computer_score}")
        continue