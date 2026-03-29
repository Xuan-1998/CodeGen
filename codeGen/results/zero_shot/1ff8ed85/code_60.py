def can_send_over_network(b):
    n = len(b)
    segments_a = []

    for bi in b:
        # Check if bi can be formed by concatenating segment lengths
        for i in range(1, n+1):  # consider all possible segment lengths
            for j in range(i+1, n+1):  # and their combinations
                total_length = sum(segments_a[:i]) + sum(segments_a[i:j])
                if bi == total_length:
                    segments_a.extend([total_length] * (j-i))
                    break
        else:  # if no combination is found
            return False

    # Check if the total length of segments in a matches original sequence length
    return sum(segments_a) == n

# Example usage:
t = int(input())  # number of test cases
for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    print("YES" if can_send_over_network(b) else "NO")
