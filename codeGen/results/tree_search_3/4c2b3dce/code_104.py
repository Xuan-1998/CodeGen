from collections import defaultdict

memo = defaultdict(lambda: [False, False])

def can_find_ab_ba(s):
    for i in range(len(s)):
        if s[i] == 'A':
            prev_state = (True, False)
        elif s[i] == 'B':
            prev_state = (False, True)

        curr_char = s[i]

        # Check if we've already seen this state
        if memo[prev_state][0] and memo[prev_state][1]:
            return "YES"

        # Check if 'AB' or 'BA' can be found in the remaining part of the string
        if (curr_char == 'A' and not memo[prev_state][0]) or \
           (curr_char == 'B' and not memo[prev_state][1]):
            if i < len(s) - 1:
                memo[prev_state] = can_find_ab_ba(s[i+1:])
        else:
            memo[prev_state] = [True, True]

    return "NO"

input_s = input()
print(can_find_ab_ba(input_s))
