import os
import random

def calc_hand(hand):
    noaces = [c for c in hand if c != 'A']
    aces = [c for c in hand if c == 'A']

    sum = 0

    for card in noaces:
        if card in 'JQK':
            sum += 10
        else:
            sum += int(card)

    for card in aces:
        if sum > 10:
            sum += 1
        else:
            sum += 11

    return sum

while True:
    cards = [
        '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',
        '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',
        '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',
        '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'
    ]

    random.shuffle(cards)

    dealer = []
    player = []

    player.append(cards.pop())
    dealer.append(cards.pop())
    player.append(cards.pop())
    dealer.append(cards.pop())

    first_hand = True
    standing = False

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')

        player_score = calc_hand(player)
        dealer_score = calc_hand(dealer)

        if standing:
            print('Dealer Cards: [{}] \nDealer Score: ({})\n'.format(']['.join(dealer), dealer_score))
        else:
            print('Dealer Cards: [{}][?]\n'.format(dealer[0]))

        print('Your Cards:   [{}] \nPlayer Score: ({})\n'.format(']['.join(player), player_score))

        if standing:
            if dealer_score > 21:
                print('Dealer busted.\nYou won!\n')
            elif player_score == dealer_score:
                print('Push.\nIt\'s a draw\n')
            elif player_score > dealer_score:
                print('You beat the dealer.\nYou won!\n')
            else:
                print('Dealer won. \nYou lost.\n')

            input('Play again? Hit enter to continue.\n')
            break

        if first_hand and player_score == 21:
            print('Blackjack!\n You won!\n')
            input('Play again? Hit enter to continue.\n')
            break

        if player_score > 21:
            print('Bust.\nYou lost.\n')
            input('Play again? Hit enter to continue.\n')
            break

        print('What would you like to do?')
        print(' [1] Hit')
        print(' [2] Stand\n')

        choice = input('Your choice: \n')

        first_hand = False

        if choice == '1':
            player.append(cards.pop())
        elif choice == '2':
            standing = True
            while calc_hand(dealer) <= 16:
                dealer.append(cards.pop())