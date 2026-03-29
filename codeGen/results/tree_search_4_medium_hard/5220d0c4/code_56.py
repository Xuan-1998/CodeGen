dp = {}
def solve(state):
    i, j, f = state
    if (i, j, f) in dp:
        return dp[(i, j, f)]
    
    beauty = 0
    for k in range(i, j+1):
        if is_prime(k):
            if not f or is_good_prime(k):
                beauty += k
            else:
                beauty -= k
    
    if i == j:
        return beauty
    elif f:
        dp[(i, j, f)] = max(solve((i, k-1, True)) for k in range(i+1, j+1))
    else:
        dp[(i, j, f)] = solve((i, j-1, False))
    
    return beauty

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_good_prime(n):
    # You can implement your logic here to determine whether a prime number is good or bad
    pass

n, m = map(int, input().split())
nums = list(map(int, input().split()))
bad_primes = list(map(int, input().split()))

print(solve((0, n-1, False)))
