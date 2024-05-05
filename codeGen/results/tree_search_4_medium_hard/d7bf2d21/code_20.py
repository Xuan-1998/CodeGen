from collections import defaultdict

def count_longest_increasing_subsequences(arr):
    memo = defaultdict(int)
    max_length = 1

    for i in range(len(arr)):
        if arr[i] > all(arr[:i]):  # Check if current element is greater than all previous elements
            memo[i] = 1
        else:
            prev_max_length = 0
            for j in range(i):
                if arr[i] > arr[j]:
                    prev_max_length = max(prev_max_length, memo[j])
            memo[i] = prev_max_length + 1
        max_length = max(max_length, memo[i])

    count_longest_increasing_subsequences_count = sum(1 for x in memo.values() if x == max_length)
    return count_longest_increasing_subsequences_count

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    print(count_longest_increasing_subsequences(arr))

if __name__ == "__main__":
    main()
