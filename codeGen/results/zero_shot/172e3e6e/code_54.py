import sys
input = sys.stdin.readline

def main():
    n = int(input())
    a = list(map(int, input().split()))

    # Create a dictionary to store the count of each number in array 'a'
    freq = {}
    for num in a:
        if num not in freq:
            freq[num] = 0
        freq[num] += 1

    # Initialize variables to keep track of good subsequences
    mod = int(1e9) + 7
    good = 1
    for i, count in sorted(freq.items()):
        if i > 0 and i % i != 0:
            break
        good *= (count + 1)
        good %= mod

    print(good)

if __name__ == "__main__":
    main()
