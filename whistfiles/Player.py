########################################################################
##
## CS 101
## Assignment 8
## Brendan O'Connor
## bmo7x9@mail.umkc.edu / brendan.oconnor.913@gmail.com
## Created 12/5/2015
## Due 12/6/2015
##
## PROBLEM : 
##
## ALGORITHM :
## class Player(object):
##     def PlayCard(self,hand,cardsPlayed,trump,position,tricksPlayed,nsScore,ewScore):
##        if cardsPlayed == []:
##             crd = highest card you have that isn't trump suit
##             return crd
##        else:
##             suit = cardsPlayed[0].Suit()
##             cardsInSuit = []
##             cardsInTrump = []
##             for c in hand:
##                 if c.Suit() == suit:
##                     cardsInSuit.append(c)
##                 if c.Suit() == trump:
##                     cardsInTrump.append(c)
##             if cardsInSuit == [] and cardsInTrump == []:
##                 return lowest card you have
##             if len(cardsPlayed) == 1:
##                 return lowest card that is still higher than starting card
##             if len(cardsPlayed) == 2:
##                 return lowest card that is still higher than starting card
##             if len(cardsPlayed) == 3:
##                 if teammate has winning card:
##                     play lowest card you have
##                 else:
##                     if you don't have a card to win the trick:
##                         play lowest card you have
##                     else:
##                         play the lowest ranked card that still wins the hand
##                 
##
## ERROR HANDLING:
##      
##
## OTHER COMMENTS:
##
##
########################################################################

import Card
import unittest
import inspect
import random
import pickle

#  1. Think before you program
#  2. A program is a human readable essay on problem solving executed by a computer
#  3. Best way to improve is to practice
#  4. Foolish consistency is the hobgoblin of little minds
#  5. Test code often and thouroughly 
#  6. If it is hard to write it is hard to read, add a comment
#  7. All input is evil until proven otherwise

# TODO Create your Player Class Here


class Player(object):
    def __init__(self):
        self.hand      = ()
        self.position  = ''
        self.cardCount = []


    def PlayCard(self,hand,cardsPlayed,trump,position,tricksPlayed,score):
        self.position = position
        self.hand = hand

        if len(cardsPlayed) == 0: #  You are leading this trick
            crd = random.choice(self.hand)
            return crd
        else: #  You are following this trick(follow suit or play a trump)
            suit = cardsPlayed[0].Suit()
            cardsInSuit = []
            cardsInTrump = []
            for c in self.hand:
                if c.Suit() == suit:
                    cardsInSuit.append(c)
                if c.Suit() == trump:
                    cardsInTrump.append(c)

            #  If you don't have a hand in suit or trump play the 
            #  smallest card you have because you will lose 
            #  the trick
            if len(cardsInSuit) == 0 and len(cardsInTrump) == 0:
                if not len(self.hand) == 0:
                    #  Min card in hand
                    return get_min(self.hand)

            if len(cardsPlayed) == 1:
                #  Construct a list of potential winning cards
                winningInSuit = []
                if not len(cardsInSuit) == 0:
                    for c in cardsInSuit:
                        if c > cardsPlayed[0]:
                            winningInSuit.append(c)
                
                if not len(winningInSuit) == 0:
                    return get_min(self.hand,suit)

                #  Play a trump if no in suits available
                winningInTrump = []
                if not len(cardsInTrump) == 0:
                    for c in cardsInTrump:
                        if cardsPlayed[0].Suit() == trump:
                            if c > cardsPlayed[0]:
                                winningInTrump.append(c)

                if not len(winningInTrump) == 0:
                    return get_min(self.hand,suit)

                #  If neither available just return the lowest card
                #  you have since you will lose
                return get_min(self.hand,suit)

            if len(cardsPlayed) == 2:
                #  Construct a list of potential winning cards
                #  Only play a winning card if it is to beat
                #  person at position two (person on other team)
                winningInSuit = []
                if not len(cardsInSuit) == 0:
                    for c in cardsInSuit:
                        if c > cardsPlayed[1]:
                            if cardsPlayed[1].Suit() != trump:
                                winningInSuit.append(c)

                if not len(winningInSuit) == 0:
                    return get_min(self.hand,suit)

                #  Play a trump if no in suits available
                winningInTrump = []
                if not len(cardsInTrump) == 0:
                    for c in cardsInTrump:
                        if cardsPlayed[1].Suit() == trump:
                            if c > cardsPlayed[1]:
                                winningInTrump.append(c)

                if not len(winningInTrump) == 0:
                    return get_min(self.hand,suit)

                #  If neither available just return the lowest card
                #  you have since you will lose
                return get_min(self.hand,suit)

            if len(cardsPlayed) == 3:

                #  If teammate has winning card play lowest card you have
                
                #  Teammate has Suit High
                if cardsPlayed[1].Suit() == suit:
                    if cardsPlayed[1] > cardsPlayed[0] and \
                    cardsPlayed[1] > cardsPlayed[2]:
                        if cardsPlayed[2].Suit() != trump and \
                        cardsPlayed[0].Suit() != trump:
                            if not len(self.hand) == 0:
                                # Min card in hand
                                return get_min(self.hand,suit)

                    #  If team member 2 of other team isn't in suit or trump 
                    #  don't compare his card rank
                    if cardsPlayed[1] > cardsPlayed[0] and \
                    (cardsPlayed[2].Suit() != suit and cardsPlayed[2].Suit()\
                    != trump):
                        if not len(self.hand) == 0:
                            return get_min(self.hand,suit)

                #  Trump or trump high
                if cardsPlayed[1].Suit() == trump:
                    # Trump high
                    if cardsPlayed[1] > cardsPlayed[0] and \
                    cardsPlayed[1] > cardsPlayed[2]:
                        if not len(self.hand) == 0:
                            return get_min(self.hand,suit)

                    #  Trump
                    #  If teammate has trump and other two don't
                    if cardsPlayed[0].Suit() != trump and\
                     cardsPlayed[2].Suit()!= trump:
                        if not len(self.hand) == 0:
                            return get_min(self.hand,suit)

                    #  If teammate has trump high on dealer
                    if cardsPlayed[0].Suit() == trump and \
                    cardsPlayed[2].Suit() != trump:
                        if cardsPlayed[1] > cardsPlayed[0]:
                            if not len(self.hand) == 0:
                                return get_min(self.hand,suit)

                    #  If teammate has trump high on dealer's teammate
                    if cardsPlayed[2].Suit() == trump\
                    and cardsPlayed[0].Suit() != trump:
                        if cardsPlayed[1] > cardsPlayed[2]:
                            if not len(self.hand) == 0:
                                return get_min(self.hand,suit)

                #  If your teammate doesn't have the winning card
                if not len(cardsInSuit) == 0:
                    #  If you have a card in suit to win play it
                    for c in cardsInSuit:
                        #  Make list of possible winning cards in suit
                        winningCards = []
                        if c > cardsPlayed[0] and c > cardsPlayed[2]:
                            #  Make sure the cards played aren't trump suit
                            if cardsPlayed[0].Suit() != trump or \
                            cardsPlayed[2].Suit() != trump:
                                winningCards.append(c)

                        #  Get the min of winningCards and return it
                        if not len(winningCards) == 0:
                            return get_min(self.hand,suit)

                #  If you don't have a card in suit play a trump to win
                #  if you have a trump card
                if cardsPlayed[0].Suit() != trump and \
                cardsPlayed[2].Suit() != trump:

                    if not len(cardsInTrump) == 0:
                        return get_min(self.hand,suit)
                else:
                    #  If they played trumps check to see if you can win
                    cardsToCheck = []
                    for c in [cardsPlayed[0],cardsPlayed[2]]:
                        if c.Suit() == trump:
                            cardsToCheck.append(c)

                    #  Construct a list of trumps that could win
                    winningTrump = []
                    if not len(cardsInTrump) == 0:
                        for c in cardsInTrump:
                            greater = True
                            #  Make sure cardsToCheck isn't empty
                            if not len(cardsToCheck) == 0:
                                for k in cardsToCheck:
                                    if c < k:
                                        greater = False
                                if greater:
                                    winningTrump.append(c)

                        if not len(winningTrump) == 0:
                            return get_min(self.hand,suit)

                    #  If we haven't returned a winning trump return
                    #  the lowest card in hand because we can't win
                    #  this trick
                return get_min(self.hand,suit)
            #suit = cardsPlayed[0].Suit()
            #return get_min(self.hand,suit)
            print("Exiting method without returning card")

def get_min(cardList,suit=''):
    """Gets the min of the card list given and returns the
    smallest card. 
    Input          : cardList - a list of cardsPlayed
    Output         : minCard - smallest card in cardList
    Error Handling : None
    """
    cards = list()
    for c in cardList:
        if c.Suit() == suit:
            cards.append(c)
    if suit == '':
        cards = list(cardList)
        cards = sorted(cards)
        return cards[0]
    elif len(cards) > 0:
        cards = sorted(cards)
        return cards[0]
    else:
        return random.choice(cardList)

# If this module is being run as main then begin testing.
# DO NOT CHANGE CODE BELOW THIS LINE
if __name__ == "__main__":

    card_suits = list("SHDC")
    card_ranks = list("AKQJT98765432")

    # Class used for testing.
    class TestWhistPlayerMethods(unittest.TestCase):
        def test_player_creation(self):
            """ Tests if the Player is an class that can be instanced """
            
            # There must be a WhistPlayer in the globals()
            self.assertTrue("Player" in globals(), "You must define a Player Class")

            # Whist player must be a class
            self.assertTrue(inspect.isclass(Player), "Player object must be a class")

            # The Player must be of type type.
            player = Player()
            self.assertIsInstance(player, Player)

        def test_PlayCard_creation(self):
            """ Tests that the Player has a PlayCard method with the proper number of parameters """            

            # Is there a playcard in the class.
            self.assertTrue("PlayCard" in Player.__dict__, "Player must have a PlayCard method")

            # Is playcard callable?
            self.assertTrue(callable(Player.PlayCard), "PlayCard should be a function")

            # Does playcard have correct number of parameters?
            self.assertEqual(len(inspect.getfullargspec(Player.PlayCard)[0]), 7, "There should be seven parameters for PlayCard method" )

        def test_PlayCard_returns_card(self):
            """ Given a single card to play, does the player play an instance of card? """

            players_cards = (Card.Card("D", "9"), )

            player = Player()
            return_card = player.PlayCard(players_cards, [], "C", "S", [], (0, 0))
            self.assertIsInstance(return_card, Card.Card, "PlayCard must return a card")
            

        def test_PlayCard_returns_lead_suit_card(self):
            """ If player has one of the trump cards, he must play one of the trump cards """
            trump = "D"
            lead_card = Card.Card("C", random.choice(card_ranks))

            # Player has one card that is the same card as the trump card.  Trump card is last card.
            players_cards = tuple((Card.Card(card[0], card[1]) for card in ['HA', 'D2', 'HJ', 'S9', 'H5', 'H2', 'D8', 'DA', 'SQ', 'H3', 'S7', 'S6', 'C9']))
            player = Player()
            return_card = player.PlayCard(players_cards, (lead_card, ), trump, "S", [], (0, 0))
            self.assertIsInstance(return_card, Card.Card, "PlayCard must return a card")
            #self.assertEqual(return_card, players_cards[-1], "The last card should be the one played.  It is the only trump card")

        def test_PlayCard_returns_card_if_no_lead_suit_available(self):
            """ If player has one of the trump cards, he must play one of the trump cards """
            trump = "D"
            lead_card = Card.Card("C", random.choice(card_ranks))

            # Player has one card that is the same card as the trump card.  Trump card is last card.
            players_cards = tuple((Card.Card(card[0], card[1]) for card in ['HA', 'D2', 'HJ', 'S9', 'H5', 'H2', 'D8', 'DA', 'SQ', 'H3', 'S7', 'S6', 'H9']))

            player = Player()
            return_card = player.PlayCard(players_cards, (lead_card, ), trump, "S", [], (0, 0))
            self.assertIsInstance(return_card, Card.Card, "PlayCard must return a card")

            # The return card can be any of the cards in the players hand.
            for card in players_cards:
                if card == return_card:
                    break
            else:
                self.fail("The card returned must be one of the cards the player had. {} returned".format(repr(return_card)))

        def test_PlayCard_returns_valid_option_for_mass_data(self):
            """ use a data file to test users data for a lot of possibilities 2860 to be exact """

            play_card_lines = pickle.load(open("example_hands.pik", "rb"))
            for hand, trick, trump_suit, player_pos, played, score, valid_cards in play_card_lines:
                player = Player()
                return_card = player.PlayCard(hand, trick, trump_suit, player_pos, played, score)
                self.assertTrue(return_card in valid_cards, "Played Invalid Card {} for hand:{}, trick{}, valid_cards:{}".format(repr(return_card), hand, trick, valid_cards))


    can_create_suite = unittest.TestSuite()
    can_create_suite.addTest(TestWhistPlayerMethods("test_player_creation"))

    test_runner = unittest.TextTestRunner()
    print("Testing Creation and type of Player")
    result = test_runner.run(can_create_suite)
    if result.wasSuccessful():

        can_call_playcard = unittest.TestSuite()
        can_call_playcard.addTest(TestWhistPlayerMethods("test_PlayCard_creation"))
        print("\n\nTest PlayCard is a method of Player")
        result = test_runner.run(can_call_playcard)

        # Test proper play with small examples
        if result.wasSuccessful():
            play_suite = unittest.TestSuite()
            play_suite.addTest(TestWhistPlayerMethods("test_PlayCard_returns_card"))
            play_suite.addTest(TestWhistPlayerMethods("test_PlayCard_returns_lead_suit_card"))
            play_suite.addTest(TestWhistPlayerMethods("test_PlayCard_returns_card_if_no_lead_suit_available"))
            print("\n\nTest PlayCard operates properly.")
            result = test_runner.run(play_suite)

            if result.wasSuccessful():
                play_suite = unittest.TestSuite()
                play_suite.addTest(TestWhistPlayerMethods("test_PlayCard_returns_valid_option_for_mass_data"))
                print("\n\nTest PlayCard operates properly for pickled data.")
                result = test_runner.run(play_suite)
