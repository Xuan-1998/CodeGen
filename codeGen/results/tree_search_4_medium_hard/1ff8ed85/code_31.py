code
def network_quality(t):
    for _ in range(t):
        n = int(input())
        b = list(map(int, input().split()))
        freq_a = {}
        prev_segment_length = 0
        segment_count = 1
        for val in b:
            if val not in freq_a:
                freq_a[val] = 0
            freq_a[val] += 1
            if val == segment_count * (prev_segment_length + 1) - (freq_a[val] % (prev_segment_length + 1)):
                prev_segment_length += 1
            else:
                prev_segment_length = 0
                segment_count += 1
        print('YES' if segment_count > 1 or prev_segment_length > 0 else 'NO')

network_quality(int(input()))
