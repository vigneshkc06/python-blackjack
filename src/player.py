class Player():
    def __init__(self, amount, hand, bet=0):
        self.amount = amount
        self.hand = hand
        self.bet = bet

    def place_bet(self, bet):
        if bet > self.amount:
            raise ValueError("Sorry cant place bet!!")
        self.bet = bet
        print("Bet placed")

    def won(self):
        self.amount += 2 * self.bet
        print("Player won")

    def lost(self):
        self.amount -= self.bet
        print("Player lost")

    def draw(self):
        self.amount += self.bet
        print("It is a draw")

    def __str__(self):
        return f'Player balance is {self.amount}'
