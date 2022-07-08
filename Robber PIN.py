""" Alright, detective, one of our colleagues successfully observed our target person, Robby the robber. We followed him to a secret warehouse, where we assume to find all the stolen stuff. The door to this warehouse is secured by an electronic combination lock. Unfortunately our spy isn't sure about the PIN he saw, when Robby entered it.

The keypad has the following layout:

┌───┬───┬───┐
│ 1 │ 2 │ 3 │
├───┼───┼───┤
│ 4 │ 5 │ 6 │
├───┼───┼───┤
│ 7 │ 8 │ 9 │
└───┼───┼───┘
    │ 0 │
    └───┘

He noted the PIN 1357, but he also said, it is possible that each of the digits he saw could actually be another adjacent digit (horizontally or vertically, but not diagonally). E.g. instead of the 1 it could also be the 2 or 4. And instead of the 5 it could also be the 2, 4, 6 or 8.

He also mentioned, he knows this kind of locks. You can enter an unlimited amount of wrong PINs, they never finally lock the system or sound the alarm. That's why we can try out all possible (*) variations.

* possible in sense of: the observed PIN itself and all variations considering the adjacent digits

Can you help us to find all those variations? It would be nice to have a function, that returns an array (or a list in Java/Kotlin and C#) of all variations for an observed PIN with a length of 1 to 8 digits. We could name the function getPINs (get_pins in python, GetPINs in C#). But please note that all PINs, the observed one and also the results, must be strings, because of potentially leading '0's. We already prepared some test cases for you.

Detective, we are counting on you!

test.describe('example tests')
expectations = [('8', ['5','7','8','9','0']),
                ('11',["11", "22", "44", "12", "21", "14", "41", "24", "42"]),
                ('369', ["339","366","399","658","636","258","268","669","668","266","369","398","256","296","259","368","638","396","238","356","659","639","666","359","336","299","338","696","269","358","656","698","699","298","236","239"])]

for tup in expectations:
  test.assert_equals(sorted(get_pins(tup[0])), sorted(tup[1]), 'PIN: ' + tup[0]) """

# def get_pins(observed):

import itertools 

# KEY AS DICT
num_map = {'0' : [8, 0],
          '1' : [1, 2, 4],
          '2' : [1, 2, 3, 5],
          '3' : [2, 3, 6],
          '4' : [1, 4, 7, 5],
          '5' : [2, 4, 5, 6, 8],
          '6' : [3, 5, 6, 9],
          '7' : [4, 7, 8],
          '8' : [5, 7, 8, 9, 0],
          '9' : [6, 8, 9]}

# print(num_map)

def concatenate_list(badlist):
    return(''.join(map(str,badlist)))

def get_pins(observed):
  observed_list = list(observed)
  
  poss_primary = [num_map[n] for n in observed_list]

  combos_list = list(itertools.product(*poss_primary))
  combos_output = [concatenate_list(m) for m in combos_list]
  return combos_output


  # [''.join(n) for n in combos_list]
  # print(list(itertools.product(num_map['3'],num_map['6'])))


print(get_pins('12'))
# print(list(itertools.product(num_map['3'],num_map['6'])))








'''PIN: 369: 
['236', '238', '256', '258', '266', '268', '296', '298', '336', '338', '356', '358', '366', '368', '396', '398', '636', '638', '656', '658', '666', '668', '696', '698'] should equal 
['236', '238', '239', '256', '258', '259', '266', '268', '269', '296', '298', '299', '336', '338', '339', '356', '358', '359', '366', '368', '369', '396', '398', '399', '636', '638', '639', '656', '658', '659', '666', '668', '669', '696', '698', '699']'''