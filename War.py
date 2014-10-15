import Cards


class WarCard(Cards.Card):
    def get_value(self):
        value = WarCard.RANKS.index(self.rank) + 1
        return int(value)


class WarDeck(Cards.Deck):
    """A deck of cards"""
    def populate(self):
        for suit in WarCard.SUITS:
            for rank in WarCard.RANKS:
                self.add(WarCard(rank, suit))

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def deal(self, hands, per_hand=1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print "can't continue deal. Out of cards!"


def analyze(win, lose):
    if win > lose:
        print "you won the war!"
    elif win < lose:
        print "you lost the war!"
    else:
        print "The war resulted in a stalemate!"


def main():
    player_hand = Cards.Hand()
    opponent_hand = Cards.Hand()
    deck1 = WarDeck()
    deck1.populate()
    deck1.shuffle()
    deck1.deal((player_hand, opponent_hand), 26)

#print player_hand
#print opponent_hand

    win = 0
    lose = 0
    tie = 0
    x = 0

    while x != 26:
        if WarCard.get_value(player_hand.cards[x]) > WarCard.get_value(opponent_hand.cards[x]):
            print "Win!"
            win += 1
        elif WarCard.get_value(player_hand.cards[x]) < WarCard.get_value(opponent_hand.cards[x]):
            print "Lose!"
            lose += 1
        else:
            print "Tie!"
            tie += 1
        x += 1

    print "Wins: ", win
    print "Losses: ", lose
    print "Ties: ", tie

    analyze(win, lose)
    raw_input("Press enter to exit")

main()
