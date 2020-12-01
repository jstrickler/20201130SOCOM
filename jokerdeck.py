from carddeck import CardDeck

class Robot:
    def beep(self):
        print("Beep-beep")


class JokerDeck(CardDeck, Robot):

    def _make_deck(self):
        super()._make_deck()
        j1 = '1', 'JOKER'
        j2 = '2', 'JOKER'
        self._cards.append(j1)
        self._cards.append(j2)



