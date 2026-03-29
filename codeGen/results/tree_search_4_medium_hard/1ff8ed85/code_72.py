from collections import defaultdict

def send_sequence(t):
    dp = [[False] * (t + 1) for _ in range(t + 1)]
    segments = []

    for _ in range(t):
        n, *b = map(int, input().split())
        b = list(map(str, map(str.format, *[["{}" if i % 2 == 0 else "{}"] for i in range(n)])))

        for a in range(1, n + 1):
            segment = ''.join([str(b[i-1]) if (i+1) % 2 == 1 else str(a) for i in range(a, n+1)])
            segments.append(segment)

    for i, b_segment in enumerate(segments):
        a_index = 0
        for j, c in enumerate(b_segment):
            while a_index < len(segments[i]) and (c[0] == 'l' and int(c) <= len(segments[i][a_index:]) or c[0] == 'r' and int(c) >= len(segments[i][a_index:])):
                if j + 1 != len(b_segment):
                    a_index += 1
                else:
                    print("YES" if any(dp[b_index][int(segment)] for b_index, segment in enumerate(segments)) else "NO")
                    return

    for i, (b_index, b) in enumerate(enumerate(segments)):
        a_index = 0
        for c in b:
            while a_index < len(segments[i]) and (c[0] == 'l' and int(c) <= len(segments[i][a_index:]) or c[0] == 'r' and int(c) >= len(segments[i][a_index:])):
                if i + 1 != len(segments):
                    a_index += 1
                else:
                    print("YES" if dp[b_index][int(segment)] for segment in segments[i+1:]) else "NO")
                    return

    print("YES" if all(dp) else "NO")

if __name__ == "__main__":
    t = int(input())
    send_sequence(t)
