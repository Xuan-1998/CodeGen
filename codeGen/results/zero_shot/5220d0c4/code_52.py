if __name__ == '__main__':
    # Read input from stdin
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    bad_primes = list(map(int, input().split()))

    # Calculate the beauty score
    beauty_score = calculate_beauty_score(arr, bad_primes)

    # Print the answer to stdout
    print(beauty_score)
