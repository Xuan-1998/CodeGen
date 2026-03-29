code
def count_ones(n):
    ans = 0
    for i in range(30):  # Since we're working with integers less than or equal to n
        if ((n >> i) & 1):
            ans += (i + 1)
        else:
            ans += (n - (1 << i)) * ((1 << (i + 1)) - 1)
    return ans

n = int(input())
print(count_ones(n))
