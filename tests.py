# dictionary of tests, one for each function in the project spec; in each case, list a number of function calls (as a str), and the correct output for each

# Version: 1.0
# Created 29/4/17



test_cases = {
    "comp101_phase_type":
    [
        # two sets of three of same value (basic case)
        ("""submission.comp101_phase_type([['9D', '9S', '9D'], ['0D', '0S', '0D']])""", 1), 
        # two sets of three of same value (case where value is the same)
        ("""submission.comp101_phase_type([['9D', '9S', '9D'], ['9H', '9S', '9H']])""", 1), 
        # two sets of three of same value, with Wilds
        ("""submission.comp101_phase_type([['9D', '9S', 'AD'], ['6D', 'AS', 'AD']])""", 1), 
        # INVALID version of two sets of three, as one set is all Wilds
        ("""submission.comp101_phase_type([['9D', '9S', 'AD'], ['AC', 'AS', 'AD']])""", None), 

        # one set of seven cards of same suit (basic case)
        ("""submission.comp101_phase_type([['9D', '7D', '9D', '2D', '0D', '0D', 'KD']])""", 2), 
        # one set of seven cards of same suit (with Wilds)
        ("""submission.comp101_phase_type([['9D', '7D', 'AH', '2D', '0D', 'AS', 'KD']])""", 2), 
        # INVALID set of seven cards of same suit (as ALL Wilds)
        ("""submission.comp101_phase_type([['AD', 'AD', 'AH', 'AH', 'AS', 'AS', 'AC']])""", None), 
        # INVALID one set of cards of same suit, as wrong number
        ("""submission.comp101_phase_type([['9D', '7D', 'AH', '2D', '0D', 'AS', 'KD', 'JD']])""", None), 

        # two sets of four of same value (basic case)
        ("""submission.comp101_phase_type([['9D', '9S', '9D', '9C'], ['0D', '0S', '0D', '0H']])""", 3), 
        # two sets of four of same value (case where value is the same)
        ("""submission.comp101_phase_type([['9D', '9S', '9D', '9C'], ['9H', '9S', '9H', '9C']])""", 3), 
        # two sets of four of same value, with Wilds
        ("""submission.comp101_phase_type([['9D', '9S', 'AD', '9H'], ['6D', 'AS', 'AD', 'AH']])""", 3), 
        # INVALID version of two sets of four, as one set is all Wilds
        ("""submission.comp101_phase_type([['9D', '9S', 'AD', '9H'], ['AC', 'AS', 'AD', 'AH']])""", None), 

        # one run of eight cards (basic case)
        ("""submission.comp101_phase_type([['2D', '3C', '4D', '5S', '6C', '7D', '8H', '9C']])""", 4), 
        # INVALID run of eight cards (out of order)
        ("""submission.comp101_phase_type([['3C', '2D', '4D', '5S', '6C', '7D', '8H', '9C']])""", None), 
        # one run of eight cards (with Wilds)
        ("""submission.comp101_phase_type([['2D', '3C', 'AD', '5S', '6C', '7D', '8H', 'AC']])""", 4), 
        # one run of eight cards (with Wilds, incl at start)
        ("""submission.comp101_phase_type([['AH', 'AC', 'AD', '5S', '6C', '7D', '8H', 'AC']])""", 4), 
        # INVALID run of eight cards (first Wild assigned to invalid value)
        ("""submission.comp101_phase_type([['AD', '2D', '3C', 'AD', '5S', '6C', '7D', '8HD']])""", None), 

        # one run of four cards of same colour + one set of four of same value (basic case)
        ("""submission.comp101_phase_type([['2D', '3H', '4D', '5D'], ['7C', '7D', '7H', '7C']])""", 5), 
        # one run of four cards of same colour + one set of four of same value (with Wilds)
        ("""submission.comp101_phase_type([['AD', '3H', '4D', '5D'], ['7C', '7D', 'AH', '7C']])""", 5), 
        # INVALID run of four cards of same colour + one set of four of same value (order wrong)
        ("""submission.comp101_phase_type([['7C', '7D', '7H', '7C'], ['2D', '3H', '4D', '5D']])""", None), 
        # IVALID run of four cards of same colour + one set of four of same value (Wild in run assigned to invalid value)
        ("""submission.comp101_phase_type([['AC', 'AD', '3H', '4D'], ['7C', '7D', 'AH', '7C']])""", None), 
        # one run of four cards of same colour + one set of four of same value (with Wilds)
        ("""submission.comp101_phase_type([['AD', '3D', '4D', '5D'], ['7C', '7D', 'AH', '7C']])""", 5), 
        # INVALID run of four cards of same colour + one set of four of same value (run out of order)
        ("""submission.comp101_phase_type([['AD', '4D', '3D', '5D'], ['7C', '7D', 'AH', '7C']])""", None), 

        # INVALID phase (set of three and set of four)
        ("""submission.comp101_phase_type([['9D', '9S', 'AD'], ['AC', 'AS', 'AD', 'AH']])""", None), 
    ],
    "comp101_is_valid_play":
    [
        # play Phase 1
        ("""submission.comp101_is_valid_play((2, [['2S', '2S', '2C'], ['AS', '5S', '5S']]), 0, [[], [], [], []], [(0, [(1, 'JS')])], [0, 0, 0, 0], ['AS', '2S', '2S', '2C', '5S', '5S', '7S', '8S', '9S', '0S', 'JS'])""", True),
        # INVALID attempt to play Phase 1 (as already on Phase 2)
        ("""submission.comp101_is_valid_play((2, [['2S', '2S', '2C'], ['AS', '5S', '5S']]), 0, [[], [], [], []], [(0, [(1, 'JS')])], [1, 0, 0, 0], ['AS', '2S', '2S', '2C', '5S', '5S', '7S', '8S', '9S', '0S', 'JS'])""", False),
        # INVALID attempt to play Phase 1 (as doesn't hold the necessary cards)
        ("""submission.comp101_is_valid_play((2, [['2S', '2S', '2C'], ['AS', '5S', '5S']]), 0, [[], [], [], []], [(0, [(1, 'JS')])], [1, 0, 0, 0], ['KS', '2S', '2S', '2C', '5S', '5S', '7S', '8S', '9S', '0S', 'JS'])""", False),
        # play Phase 2
        ("""submission.comp101_is_valid_play((2, [['2S', '2S', '9S', 'AS', '5S', '5S', 'JS']]), 0, [[], [], [], []], [(0, [(1, 'JS')])], [1, 0, 0, 0], ['AS', '2S', '2S', '2C', '5S', '5S', '7S', '8S', '9S', '0S', 'JS'])""", True),

        # place card on own phase (set of three)
        ("""submission.comp101_is_valid_play((3, ('AD', (1, 0, 3))), 1, [[], (1, [['2S', '2S', '2C'], ['AS', '5S', '5S']]), [], []], [(0, [(1, 'JS'), (4, 'JS')]), (1, [(1, 'JS'), (2, [['2S', '2S', '2C'], ['AS', '5S', '5S']])])], [0, 1, 0, 0], ['AD', '8S', '9S', '0S', 'JS'])""", True),
        # place card on own phase (set of three)
        ("""submission.comp101_is_valid_play((3, ('AD', (1, 1, 0))), 1, [[], (1, [['2S', '2S', '2C'], ['AS', '5S', '5S']]), [], []], [(0, [(1, 'JS'), (4, 'JS')]), (1, [(1, 'JS'), (2, [['2S', '2S', '2C'], ['AS', '5S', '5S']])])], [0, 1, 0, 0], ['AD', '8S', '9S', '0S', 'JS'])""", True),
        # place card on own phase (set of same suit)
        ("""submission.comp101_is_valid_play((3, ('JS', (1, 0, 0))), 1, [[], (2, [['2S', '2S', 'AS', '5S', '5S', '7S', 'JS']]), [], []], [(0, [(1, 'JS'), (4, 'JS')]), (1, [(1, 'JS'), (2, [['2S', '2S', 'AS', '5S', '5S', '7S', 'JS']])])], [0, 2, 0, 0], ['5D', '0S', 'JS', 'KC'])""", True),
        # INVALID attempt to place card on own phase (wrong suit)
        ("""submission.comp101_is_valid_play((3, ('KC', (1, 0, 0))), 1, [[], (2, [['2S', '2S', 'AS', '5S', '5S', '7S', 'JS']]), [], []], [(0, [(1, 'JS'), (4, 'JS')]), (1, [(1, 'JS'), (2, [['2S', '2S', 'AS', '5S', '5S', '7S', 'JS']])])], [0, 2, 0, 0], ['5D', '0S', 'JS', 'KC'])""", False),
        # place card on own phase (set of four)
        ("""submission.comp101_is_valid_play((3, ('5D', (1, 1, 0))), 1, [[], (3, [['2S', '2S', '2C', '2H'], ['AS', '5S', '5S', '5H']]), [], []], [(0, [(1, 'JS'), (4, 'JS')]), (1, [(1, 'JS'), (2, [['2S', '2S', '2C', '2H'], ['AS', '5S', '5S', '5H']])])], [0, 3, 0, 0], ['5D', '0S', 'JS'])""", True),
        # INVALID attempt to place card on own phase (index incorrect)
        ("""submission.comp101_is_valid_play((3, ('AD', (1, 0, 4))), 1, [[], (1, [['2S', '2S', '2C'], ['AS', '5S', '5S']]), [], []], [(0, [(1, 'JS'), (4, 'JS')]), (1, [(1, 'JS'), (2, [['2S', '2S', '2C'], ['AS', '5S', '5S']])])], [0, 1, 0, 0], ['AD', '8S', '9S', '0S', 'JS'])""", False),
        # INVALID attempt to place card on own phase (group ID incorrect)
        ("""submission.comp101_is_valid_play((3, ('2H', (1, 1, 3))), 1, [[], (1, [['2S', '2S', '2C'], ['AS', '5S', '5S']]), [], []], [(0, [(1, 'JS'), (4, 'JS')]), (1, [(1, 'JS'), (2, [['2S', '2S', '2C'], ['AS', '5S', '5S']])])], [0, 1, 0, 0], ['2H', '8S', '9S', '0S', 'JS'])""", False),
        # INVALID attempt to place card on Player 0's phase (hasn't picked up card yet)
        ("""submission.comp101_is_valid_play((3, ('2C', (0, 1, 3))), 1, [[['2S', '2S', '2C'], ['AS', '5S', '5S']], [], [], []], [(0, [(1, 'JS'), (2, [['2S', '2S', '2C'], ['AS', '5S', '5S']])])], [1, 0, 0, 0], ['AD', '2C', '2H', '2H', '5H', '5D', '7S', '8S', '9S', '0S', 'JS'])""", False),
        # INVALID attempt to place card on Player 0's phase (hasn't got own phase yet)
        ("""submission.comp101_is_valid_play((3, ('2C', (0, 1, 3))), 1, [[['2S', '2S', '2C'], ['AS', '5S', '5S']], [], [], []], [(0, [(1, 'JS'), (2, [['2S', '2S', '2C'], ['AS', '5S', '5S']])]), (1, [(1, '0S')])], [1, 0, 0, 0], ['AD', '2C', '2H', '2H', '5H', '5D', '7S', '8S', '9S', '0S', 'JS'])""", False),
        
    ],


}
