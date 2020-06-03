from player import Player
from dealer import Dealer
from dealer import draw


def user_input(question):
    amount = 0
    while True:
        try:
            amount = int(input(question))
        except ValueError:
            continue
        else:
            break
    return amount


def replay():
    ans = ''
    while ans.lower() not in ['y', 'n']:
        ans = input("Do you want to play again(y/n) :")
    return ans


def user_bet(player):
    while True:
        try:
            bet = user_input("How much you want to bet :")
            player.place_bet(bet)
        except ValueError:
            print(f"cannot place bet greater than {player.amount}")
            continue
        else:
            break


def game_play(player, dealer):
    while player.hand <= 21 and dealer.hand <= 21:
        choice = input("Do you want to hit (y/n) :")
        if choice == 'y':
            player.hand += draw()
            dealer.hand += draw()
        else:
            break
        print(f'player hand has {player.hand}')
    if player.hand > 21:
        player.lost()
    elif player.hand > dealer.hand or dealer.hand > 21:
        player.won()
    else:
        player.draw()
    print(f'Player had {player.hand} and dealer had {dealer.hand}')
    print(player)


def start_game():
    print("Welcome to the Black Jack")
    dealer = Dealer()
    amount = user_input("Enter your amount :")
    while True:
        player = construct_player(draw(), amount)
        print(f"Dealer starts with {dealer.hand}")
        user_bet(player)
        game_play(player, dealer)
        ans = replay()
        if ans == 'n':
            break


def construct_player(start_hand, amount):
    player = Player(amount, start_hand)
    print(f"Player starts with hand {start_hand}")
    return player


if __name__ == '__main__':
    start_game()
