n, m = map(int, input().split())
arr = list(map(int, input().split()))
bad_primes = list(map(int, input().split()))

def beauty(num):
    # TO DO: implement the logic to calculate the beauty of the number
    pass

max_beauty = 0
for num in arr:
    beauty_value = beauty(num)
    if beauty_value > max_beauty:
        max_beauty = beauty_value

print(max_beauty)
