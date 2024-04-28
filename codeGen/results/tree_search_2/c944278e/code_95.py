def find_winners(n):
    max_phase = 2**n - 1
    memo = {}

    def recursive_find(phase, current_winner):
        if phase == max_phase:
            return [current_winner]

        if (phase, current_winner) in memo:
            return memo[(phase, current_winner)]

        winners = []

        for i in range(n):
            if (phase >> i) & 1:  # If the ith bit is 1
                new_winner = current_winner | (1 << i)
                winners.extend(recursive_find(phase - 2**i, new_winner))
            else:
                winners.append(current_winner)

        memo[(phase, current_winner)] = winners
        return winners

    return recursive_find(0, 0)

n = int(input())  # Input n
winners = find_winners(n)
print(*sorted(winners), sep='\n')
