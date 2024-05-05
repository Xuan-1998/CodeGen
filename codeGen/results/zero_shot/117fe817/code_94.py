import sys

n = int(sys.stdin.readline())

ones_place_count = sum([(n//10**(i+1)) * ((10**i) - (10**(i-1))) + min(n, (10**i)-1) for i in range(9)])

print(ones_place_count)
