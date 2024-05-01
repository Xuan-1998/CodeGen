import sys

def solve():
    N = int(input())
    numbers = list(map(int, input().split()))

    # Calculate the total sum of the numbers
    total_sum = sum(numbers)

    # Initialize an empty set to store the subset sums
    subset_sums = set()

    # Iterate over the powerset of the input set
    for i in range(1 << N):
        current_sum = 0
        for j in range(N):
            if (i & (1 << j)):
                current_sum += numbers[j]
        subset_sums.add(current_sum)

    # Sort the subset sums and print them
    print(' '.join(map(str, sorted(subset_sums))))

if __name__ == '__main__':
    solve()
