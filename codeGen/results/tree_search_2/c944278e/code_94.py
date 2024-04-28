from functools import lru_cache

@lru_cache(None)
def dp(phase, skill):
    if phase == 2**n - 1:  # base case: only one winning team
        return [skill]
    
    winners = []
    for next_skill in range(2**n):  # iterate over all possible next skills
        if (skill & next_skill) > 0:  # if the current skill is greater than or equal to the next skill
            winners.extend(dp(phase + 1, next_skill))
    
    return winners

def find_winners(n):
    s = input()  # read the binary string from stdin
    n = len(s)
    winners = dp(0, 0)  # initialize the DP table
    for i in range(n):
        bit = int(s[i])
        winners = [skill for skill in winners if (bit & 1) == 1]
        winners = sorted(list(set(winners)))  # remove duplicates and sort
    
    return winners

n = int(input())  # read the integer n from stdin
print(*find_winners(n), sep='\n')  # print all winning teams, one per line
