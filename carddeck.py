import random

class CardDeck:
    SUITS = 'Clubs Diamonds Hearts Spades'.split()
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

    def __init__(self, dealer):
        # members
        self._dealer = None
        self._cards = None

        self.dealer = dealer
        self._make_deck()

    # not used as much in Python....
    def get_dealer(self):
        return self._dealer

    def set_dealer(self, dealer):
        if isinstance(dealer, str):
            self._dealer = dealer
        else:
            raise TypeError("Dealer must be a string")

    @property
    def dealer(self):  # getter property   PUBLIC
        return self._dealer   # PRIVATE

    @dealer.setter
    def dealer(self, dealer):  # setter property
        if isinstance(dealer, str):
            self._dealer = dealer
        else:
            raise TypeError("Dealer must be a string")

    def _make_deck(self):
        self._cards = []
        for suit in self.SUITS:    # CardDeck.SUITS
            for rank in self.RANKS:
                card = rank, suit
                self._cards.append(card)

    def shuffle(self):
        random.shuffle(self._cards)

    # instance method
    def draw(self):
        return self._cards.pop()

    @classmethod
    def get_suits(cls):
        return cls.SUITS

    @staticmethod
    def scream():
        print("AAAAAAAAAAHHHHHHHHHHHHHHH")

    @property
    def cards(self):
        return self._cards

    def __len__(self):
        return len(self._cards)

    def __str__(self):
        my_type = type(self)
        my_name = my_type.__name__
        return f"{my_name}: {self.dealer}/{len(self)}"

    def __repr__(self):
        my_type = type(self)
        my_name = my_type.__name__
        return f"{my_name}('{self.dealer}')"

    def __add__(self, other):
        my_type = type(self)  # CardDeck or JokerDeck
        tmp = my_type(self.dealer)   # CardDeck(self.dealer) or JokerDeck(self.dealer)
        tmp._cards = self._cards + other.cards
        return tmp

    def __truediv__(self, other):
        return 42
