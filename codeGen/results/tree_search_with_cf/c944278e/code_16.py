def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    s = data[1]
    
    # Initial sequence of elements from 1 to 2^n
    initial_seq = list(range(1, 2**n + 1))
    
    # Function to perform one phase of the reduction
    def reduce_sequence(seq, keep_max):
        reduced_seq = []
        for i in range(0, len(seq), 2):
            if keep_max:
                reduced_seq.append(max(seq[i], seq[i + 1]))
            else:
                reduced_seq.append(min(seq[i], seq[i + 1]))
        return reduced_seq
    
    # Process each phase according to the binary string s
    current_seq = initial_seq
    for i in range(n):
        keep_max = s[i] == '1'
        current_seq = reduce_sequence(current_seq, keep_max)
    
    # The resulting sequence should have only one element, which is the maximum possible value
    result = current_seq[0]
    
    # Output the result
    print(result)


