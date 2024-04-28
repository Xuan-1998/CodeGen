from functools import lru_cache

@lru_cache(None)
def f(i):
    if i == 1:
        return 0
    total_sum = sum(array[:i+1])
    left_sum = 0
    partitions = 0
    for j in range(i, -1, -1):
        left_sum += array[j]
        if left_sum == (total_sum - left_sum) // 2:
            partitions += f(j-1) + 1
            break
    return max(0, partitions)

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        array = [int(x) for x in input().split()]
        print(f(n-1))

if __name__ == "__main__":
    main()
