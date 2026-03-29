import sys

def max_remaining_element(n, array):
    total_sum = sum(array)
    return abs(total_sum)

if __name__ == "__main__":
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    array = list(map(int, data[1:]))
    print(max_remaining_element(n, array))

