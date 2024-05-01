import sys

def solve(n):
    dp = {}
    def memoized_function(state):
        if state not in dp:
            if state == 'winning':
                result = [1]
            else:
                result = []
            for i, bit in enumerate(s):
                if bit == '1':
                    if i < n-1:
                        new_state = 'winning' if state == 'losing' else 'losing'
                        result.extend(memoized_function(new_state))
                    else:
                        result.append(1)
                elif bit == '0':
                    continue
            dp[state] = result
        return dp[state]

    winning_teams = []
    for s in range(2**n):
        s = bin(s)[2:].zfill(n)  # Convert to binary and pad with zeros if necessary
        if memoized_function('winning'):
            winning_teams.append(s)

    return sorted(winning_teams)


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    print(*solve(n), sep='\n')
