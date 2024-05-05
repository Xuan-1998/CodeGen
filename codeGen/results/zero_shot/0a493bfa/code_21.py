def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def process_array(array, bad_primes):
    beauty = 0
    for i in range(len(array)):
        subset = array[:i] + array[i+1:]
        gcd_val = array[i]
        for num in subset:
            gcd_val = math.gcd(gcd_val, num)
        if gcd_val not in bad_primes:
            beauty += gcd_val
    return beauty

array = [int(x) for x in input().split()]
bad_primes = set(int(x) for x in input().split())
print(process_array(array, bad_primes))
