import random
import time


class Player:

    def __init__(self, money=1200):

        self.deck = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10,
                     10, 10, 10, 'J', 'J', 'J', 'J', 'Q', 'Q', 'Q', 'Q', 'K', 'K', 'K', 'K', 'A', 'A', 'A', 'A']
        self.hand = []
        self.balance = money

    # Single Arg constructor - Contructs new deck as well as amn empty hand and your entered balance

    def deal_card(self):

        x = random.randrange(0, (len(self.deck) - 1))

        rand_index_value = self.deck[x]

        return rand_index_value
    # method used the random functions to deal a single random card

    def deal_hand(self):

        obj_1 = Player()

        c1 = obj_1.deal_card()
        c2 = obj_1.deal_card()

        self.hand.append(c1)
        self.hand.append(c2)

    # Deals the 2 random cards for your hand

    def __str__(self):

        return str(self.hand) + '          ' + 'Balance: ' + str(self.balance)

    # String representation of object
    def card_vals(self):

        tot_val = 0

        nums_list = [2, 3, 4, 5, 6, 7, 8, 9, 10]

        face_list = ['J', 'Q', 'K']

        for i in self.hand:

            if i in nums_list:

                tot_val += i

            elif i in face_list:

                tot_val += 10

            else:

                if tot_val + 11 > 21:

                    tot_val += 1

                else:

                    tot_val += 11

        return tot_val

    # method returns the cumulative value of your hand - considers face cards and aces

    def bust_check(self, play_obj):

        x = play_obj.card_vals()

        if x <= 21:

            return False

        else:

            return True

    # Checks if you bust and go above 21

    def card_hit(self):

        obj_1 = Player()

        card1_new = obj_1.deal_card()

        self.hand.append(card1_new)

    # When you want to hit this method adds another card to your hand

    def getbalance(self):

        return self.balance

    # simple getter used to return your current balance

    def make_win_bet(self, bet, tf):

        if tf:

            self.balance = self.balance - bet

        else:

            self.balance = self.balance + bet

    # This method determins if you won the round and adds your bet onto your total

    def clear_hand(self):

        self.hand.clear()
    # simple method - used to clear your hand


class Dealer:

    def __init__(self):

        self.deck = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10,
                     10, 10, 10, 'J', 'J', 'J', 'J', 'Q', 'Q', 'Q', 'Q', 'K', 'K', 'K', 'K', 'A', 'A', 'A', 'A']
        self.hand = []

    # zero arg construtor - used to construct new deck as well as empty hand for dealer

    def __str__(self):

        return str(self.hand)

    # string representation of object

    def card_vals(self):

        tot_val = 0

        nums_list = [2, 3, 4, 5, 6, 7, 8, 9, 10]

        face_list = ['J', 'Q', 'K']

        for i in self.hand:

            if i in nums_list:

                tot_val += i

            elif i in face_list:

                tot_val += 10

            else:

                if tot_val + 11 > 21:

                    tot_val += 1

                else:

                    tot_val += 11

        return tot_val

    # used to count value of cards in dealers hand

    def deal_card_to_hand(self):

        x = random.randrange(0, (len(self.deck) - 1))

        rand_index_value = self.deck[x]

        self.hand.append(rand_index_value)
    # This method simply deals another card to the dealers hand


class GameDriver:
    x = int(input('Enter money into your balance, max deposit of $5000 '))
    # gstartobj = Player(x)
    p1 = Player(x)
    # Enter balance money used to determine when game over or won

    p_hold = 0
    # counter variable used to determine when loop should end

    while p_hold == 0:

        # current_balance = gstartobj.getbalance()
        # p1 = Player(current_balance)
        dealer1 = Dealer()
        # contructs a new object every time the loop runs

        print('Your hand:')
        print(p1)
        print('')
        print('Dealer hand:')
        print(dealer1)
        print('----------------------')
        # initial print of empty hands, used to show current balance

        new_bet = int(input('Enter bet amount '))

        while new_bet > p1.getbalance():
            new_bet = int(input('Enter bet amount '))
        # new bet, while loop used to assure bet is less than balance
        print('----------------------')

        p1.deal_hand()
        cval1 = p1.card_vals()

        dealer1.deal_card_to_hand()
        cval2 = dealer1.card_vals()
        # deal two cards to your hand and get card vals, deal 1 card to dealer hand get card vals

        print('Your hand:')
        print(p1)
        print(cval1)
        print('Bet:', new_bet)
        print('')
        print('Dealer hand:')
        print(dealer1)
        print(cval2)
        print('----------------------')
        # print out new dealed hands, show what hand is with card vals

        countb_after = 0

        while input('Hit or Stand? ') == 'Hit':

            p1.card_hit()
            cval3 = p1.card_vals()

            print('Your hand:')
            print(p1)
            print(cval3)
            print('Bet:', new_bet)
            print('')
            print('Dealer hand:')
            print(dealer1)
            print(cval2)
            print('----------------------')

            tf = p1.bust_check(p1)
            countb_after = p1.card_vals()

            if tf:

                print('You busted, Dealer Wins')
                print('----------------------')

                p1.make_win_bet(new_bet, tf)
                p1.clear_hand()

                if p1.getbalance() > 20000 or p1.getbalance() == 0:

                    if p1.getbalance() > 20000:
                        print('Game won, you banckrupted the casino!          ' + 'Balance: ' + str(p1.getbalance()))
                        print('----------------------')

                    if p1.getbalance() == 0:
                        print('Game Over, you went bankrupt!          ' + 'Balance: ' + str(p1.getbalance()))
                        print('----------------------')

                    p_hold = p_hold + 1

                break
        # Hit or stand method - Asks player if they want to hit or stand - other stuff inside to consider if player busts or if the game ends

        if countb_after > 21:
            continue
        else:
            print('----------------------')
        # Used to determin reset of while loop if player busted

        count2 = 0

        while count2 == 0:

            time.sleep(1.5)

            dealer1.deal_card_to_hand()
            cval4 = dealer1.card_vals()

            cval3 = p1.card_vals()

            print('Your hand:')
            print(p1)
            print(cval3)
            print('Bet:', new_bet)
            print('')
            print('Dealer hand:')
            print(dealer1)
            print(cval4)
            print('----------------------')

            if dealer1.card_vals() >= 17:
                count2 = count2 + 1

        if dealer1.card_vals() > 21:

            print('Dealer busted, You Win')
            print('----------------------')

            p1.make_win_bet(new_bet, False)
            p1.clear_hand()

            if p1.getbalance() > 20000 or p1.getbalance() == 0:

                if p1.getbalance() > 20000:
                    print('Game won, you banckrupted the casino!          ' + 'Balance: ' + str(p1.getbalance()))
                    print('----------------------')

                if p1.getbalance() == 0:
                    print('Game Over, you went bankrupt!          ' + 'Balance: ' + str(p1.getbalance()))
                    print('----------------------')

                p_hold = p_hold + 1

            continue
        # Used to determine Dealer hitting and standing - follows all the designated rules for a dealer

        if p1.card_vals() > dealer1.card_vals():

            print('Round Won!')
            p1.make_win_bet(new_bet, False)
            p1.clear_hand()

        elif p1.card_vals() < dealer1.card_vals():

            print('Round Lost!')
            p1.make_win_bet(new_bet, True)
            p1.clear_hand()

        else:

            print('Round is a push!')
            p1.clear_hand()
        # If either player doesn't bust, used to determine who won at the end of the round or if it was a push(tie)

        print('----------------------')

        if p1.getbalance() > 20000 or p1.getbalance() == 0:

            if p1.getbalance() > 20000:
                print('Game won, you banckrupted the casino!          ' + 'Balance: ' + str(p1.getbalance()))
                print('----------------------')

            if p1.getbalance() == 0:
                print('Game Over, you went bankrupt!          ' + 'Balance: ' + str(p1.getbalance()))
                print('----------------------')

            p_hold = p_hold + 1
        # Following a situation where both players don't bust, used to determine if player won or lost the game

