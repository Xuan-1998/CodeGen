from functools import lru_cache

@lru_cache(maxsize=None)
def max_joy(i):
    if i == 1:
        return max(b[0], c[0])
    elif i % 2 == 0:  # both adjacent hares are full
        return a[i//2 - 1] + max_joy((i-2)//2)
    else:  # exactly one adjacent hare is full
        return b[(i-1)//2] + max_joy((i-3)//2)

n = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
c = [int(x) for x in input().split()]

print(max_joy(n))
