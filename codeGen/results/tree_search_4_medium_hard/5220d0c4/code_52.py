def max_beauty(n, primes, bad_primes):
    # Create a dictionary to store the memoized beauty values
    dp = {0: 0}

    for i in range(1, n + 1):
        if primes[i]:
            # If the current number is a good prime, update the state as (i+1, v)
            new_state = (i + 1, dp.get(i - 1, 0) + 1)
        else:
            # If it's a bad prime, update the state as min((i+1, v), (n-1, 0))
            new_state = min((i + 1, dp.get(i - 1, 0)), (n, 0))

        # Update the memoized beauty values
        for j in range(new_state[0], i, -1):
            if primes[j]:
                break
            else:
                dp[j] = new_state[1]

    return dp[n]

# Read input from stdin
n, m = map(int, input().split())
primes = list(map(int, input().split()))
bad_primes = list(map(int, input().split()))

print(max_beauty(n, primes, bad_primes))
