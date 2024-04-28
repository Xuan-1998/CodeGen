import itertools

def solve():
    n = int(input())
    s = input()

    # Initialize memoization dictionary
    memo = {}

    def is_winning(perm):
        if perm in memo:
            return memo[perm]

        total = 0
        prev_skill = 0
        for i, team in enumerate(perm):
            if s[i] == '1':
                total += int('2'**n - 1 >> (n - 1 - i))  # Calculate the skill level of the current team
            else:
                total -= prev_skill
            prev_skill = total

        return total >= 0

    winning_teams = [p for p in itertools.permutations(range(2**n)) if is_winning(p)]

    print('\n'.join(map(str, sorted(winning_teams))))

solve()
