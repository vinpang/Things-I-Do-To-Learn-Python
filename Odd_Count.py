'''Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.
Examples

[7] should return 7, because it occurs 1 time (which is odd).
[0] should return 0, because it occurs 1 time (which is odd).
[1,1,2] should return 2, because it occurs 1 time (which is odd).
[0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
[1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).'''

'''def find_it(seq):
    counter = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
    for n in seq:
        if n in counter:
            counter[n] += 1'''
            
# counter has now counted everything
# ALTERNATIVELY

def find_it(seq):
    counter = {}
    for n in seq:
        if n in counter:
            counter[n] += 1
        else:
            counter[n] = 1
        # this adds terms each time eliminating need for a pre-filled dictionary
    ''' # VERSION 1
    # detect odd numbers
    remainder_counter = {k: v % 2 for k, v in counter.items()}
    for x in remainder_counter:
    #      if remainder_counter[x] == 1:
       if bool(remainder_counter[x]) == True:
            return x'''

    # VERSION 2 - SIMPLIFIED
    for i in counter:
        if bool(counter[i] % 2) == True:
            return i

print(find_it([1,2,2,3,3,3,4,3,3,3,2,2,1,6,7,6,7]))