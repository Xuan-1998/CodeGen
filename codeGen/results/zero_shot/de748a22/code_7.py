import sys

def process_query(arr, l, r):
    # Calculate prefix sum
    prefix_sum = 0
    for i in range(l-1):
        prefix_sum += arr[i]
    
    # Calculate suffix sum
    suffix_sum = 0
    for i in range(r+1, len(arr)):
        suffix_sum += arr[i]
    
    # Find the minimum number of elements that can be removed
    min_removals = max(0, (prefix_sum + suffix_sum) // 2)
    return min_removals

def main():
    t = int(input())
    for _ in range(t):
        n, q = map(int, input().split())
        arr = [int(x) for x in input()]
        
        for _ in range(q):
            l, r = map(int, input().split())
            min_removals = process_query(arr, l, r)
            print(min_removals)

if __name__ == "__main__":
    main()
