import sys

def main():
    n = int(sys.stdin.readline().strip())  # Number of towns and roads
    roads = []
    total_length = 0
    max_length = 0

    for _ in range(n):
        u, v, l = map(int, sys.stdin.readline().strip().split())
        roads.append((u, v, l))
        total_length += l
        max_length = max(max_length, l)

    # The minimum inconvenience is the total length minus the length of the longest road
    min_inconvenience = total_length - max_length
    print(min_inconvenience)

if __name__ == "__main__":
    main()
