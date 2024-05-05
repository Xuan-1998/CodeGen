def beauty(min_prime, is_bad):
    if is_bad:
        return -min_prime
    else:
        return min_prime

def find_min_prime(num):
    min_prime = num
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            min_prime = i
            break
    return min_prime

def calculate_beauty(arr, bad_primes):
    total_beauty = 0
    for num in arr:
        min_prime = find_min_prime(num)
        if num in bad_primes:
            is_bad = True
        else:
            is_bad = False
        beauty_score = beauty(min_prime, is_bad)
        total_beauty += beauty_score
    return total_beauty

n, m = map(int, input().split())
arr = list(map(int, input().split()))
bad_primes = list(map(int, input().split()))
print(max_beauty(n, m, arr, bad_primes))
