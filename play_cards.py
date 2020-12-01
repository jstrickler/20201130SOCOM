
from carddeck import CardDeck
from jokerdeck import JokerDeck


d1 = CardDeck("Lisa")

d1.shuffle()

for i in range(5):
    print(d1.draw())

print(d1.dealer)
print(d1.get_dealer())

d1.dealer = "Marcia"
print(d1.dealer)

d1.set_dealer('Fred')
print(d1.dealer)

print(d1)

print(d1.get_suits())

print(CardDeck.get_suits())


CardDeck.scream()
d1.scream()

j1 = JokerDeck("Alfred")
print(j1.dealer)
j1.shuffle()
print(j1)
print()

print(d1.cards, '\n')
print(j1.cards)

j1.beep()

print(CardDeck.mro())
print(JokerDeck.mro())

print(len(d1), len(j1))
print(d1, j1)   # print(str(d1), str(j1)

print(repr(d1), repr(j1))
j2 = JokerDeck("Wally")

result = d1 + j1 + j2  # CardDeck.__add__(CardDeck.__add__(d1, j1), j2)
print(result)

print(d1 / j1)
