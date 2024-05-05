import sys

def solve(N, M, C):
    # Create a prefix sum array for upper hemispheres
    upper_sum = [0] * (C + 1)
    for i in range(N):
        radius = int(input()) - 1
        upper_sum[radius] += 1

    # Create a prefix sum array for lower hemispheres
    lower_sum = [0] * (C + 1)
    for i in range(M):
        radius = int(input()) - 1
        lower_sum[radius] += 1

    # Initialize the result array with zeros
    result = [0] * C

    # Calculate the number of X-sequences for each possible length
    for i in range(1, C + 1):
        upper_count = upper_sum[i]
        lower_count = lower_sum[i]
        if i % 2 == 0:  # Even length sequence
            result[i] += (upper_count * (upper_count - 1)) // 2
            result[i] += (lower_count * (lower_count - 1)) // 2
        else:  # Odd length sequence
            result[i] += upper_count * lower_count

    return result


def main():
    T = int(input())
    for _ in range(T):
        N, M, C = map(int, input().split())
        print(' '.join(map(str, solve(N, M, C))))


if __name__ == '__main__':
    main()
