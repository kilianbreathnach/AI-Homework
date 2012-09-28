# Checkers game for Artificial Intelligence class in Courant, Fall 2012
#
# Layout ahead given my Prof. Geiger in first draft
#
#
# States S(a, b)=0,1,2,3,4; respectively empty, red, black, kingred,
# kingblack
#
# Variable RB: RB=0 -> red, RB=1 -> black
#
# Variable FB: FB=0 -> backward, FB=1 -> forward

from checker_funcs import *


def simulate_game()
    MAX_PLAY = 100
    round_count = 1

    S = initialise_game()
    '''S are the states of play,
    here initialised to some starting point.'''

    while round_count <= MAX_PLAY:
        S = expand(S, 0))
        '''
        RB is the variable keeping track of whose turn it is.
        0 is red's turn.
        '''
        if S == 0:
            '''Red loses if no possible moves.'''
            round_count = MAX_PLAY
            drawflag = 0
        else:
            S = expand(S, 1)
            '''Black plays'''

            if S == 0:
                '''Black can't move'''
                round_count = MAX_PLAY
                drawflag = 0

        round_count += 1

        if round_count > MAX_PLAY:
            print "Agree to draw"
            '''After maximum moves played'''


