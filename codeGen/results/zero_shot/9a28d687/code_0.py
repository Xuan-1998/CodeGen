from heapq import heappop, heappush

n = int(input())  # number of strings
costs = [0] * n  # cost of reversing each string
strings = []  # list of strings

for _ in range(n):
    c = int(input())  # cost of the current string
    s = input()  # the string itself
    costs.append(c)
    strings.append(s)

# sort the strings based on their length and then lexicographically
heap = [(len(s), s) for s in strings]
heapq.heapify(heap)

ans = 0
prev_len = float('inf')
prev_s = ''

while heap:
    len_s, s = heappop(heap)
    
    if len_s > prev_len or (len_s == prev_len and s < prev_s):
        ans += costs[-1]
        prev_len = len_s
        prev_s = s
    
    # pop the reversed string from the heap
    costs.pop()
    strings.pop()

print(ans)
