import sys

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    middle = [x for x in arr[1:] if x == pivot]
    right = [x for x in arr[1:] if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def count_ways(M):
    n = len(M)
    ways = 0
    for i in range(n):
        m_i = M[i]
        # Create all possible arrays V that can be merged into a sorted array with the value m_i
        V_i = []
        for j in range(m_i):
            V_i.append(j + 1)
        V_i.extend([k + 1 for k in range(m_i, n)] + [m_i])
        ways += 1 << len(V_i)  # Count the number of different ways to create V_i
    return ways % (10**9 + 7)

n = int(sys.stdin.readline())
M = list(map(int, sys.stdin.readline().split()))
print(count_ways(M))
