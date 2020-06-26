

"""
Algorithm:
1. Take the input string, 's'
2. Set the varaibles 'j', 'i' to '0' and 'l' to length of the string.
3. Check if j is less than l-1. If yes, goto step3, else quit.
4. if the adjacent characters s[i] and s[i+1] are equal, goto step5. else goto step7.
5. If 'i' is '0'. slice the string to s[i+2:] and equate it to s. Else, skip those two characters and
equate to s.
6. Increment the 'j' value by 2. Goto, step4.
7. Increment the 'i', 'j' values by 1 each. Goto, step4.

"""

def superReducedString(s):
    i = 0
    l = len(s)
    j = 0
    while j < l-1:
        if s[i] == s[i+1]:
            if i == 0:
                s = s[i+2:]
            else:
                s = s[:i] + s[i+2:]
            j += 2
        else:
            i += 1
            j += 1
    return s

print('Reduced string of aaabbcddeeeaghhh is {}'.format(superReducedString('aaabbcddeeeaghhh')))
reduced_string = superReducedString(input('Enter a string : \n'))
print('Reduced string is {}'.format(reduced_string))