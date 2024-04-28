def winners(n, s):
    # Base case: if there are no more games left, return the current team as a winner
    if n == 0:
        return [int(s)]

    # Initialize the memoization table
    memo = {}

    def dp(i):
        if i not in memo:
            if (s[i] == '1' and sum(int(x) for x in s[:i]) < 2**(n-1)) or \
               (s[i] == '0' and sum(int(x) for x in s[:i]) >= 2**(n-1)):
                memo[i] = [int(s)]
            else:
                winners_left = dp(i+1)
                if s[i] == '1':
                    winners_right = set()
                    for winner in winners_left:
                        winners_right.update(winner + [str(2**i)])
                else:
                    winners_right = {winner - [str(2**i)] for winner in winners_left}
                memo[i] = list(set(winners_left) | winners_right)

        return memo[i]

    # Main function to find the winning teams
    def main():
        n = int(input())
        s = input()
        winners_set = dp(0)
        winners_set.sort(key=lambda x: int(x))
        print('\n'.join(map(str, winners_set)))

    if __name__ == "__main__":
        main()
