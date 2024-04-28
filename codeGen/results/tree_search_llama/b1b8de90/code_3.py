import random

def recursive_sort(n):
    # Generate a random permutation of integers from 1 to n
    permutation = list(range(1, n+1))
    random.shuffle(permutation)

    # Check if the permutation can be sorted by the recursive sorting function
    for i in range(1, n):
        if permutation[i-1] > permutation[i]:
            return False

    return True

def find_permutation(n):
    while True:
        permutation = list(range(1, n+1))
        random.shuffle(permutation)

        # Check if the permutation can be sorted by the recursive sorting function
        if recursive_sort(len(permutation)):
            return ' '.join(map(str, permutation))

if __name__ == "__main__":
    n = int(input())
    print(find_permutation(n))
