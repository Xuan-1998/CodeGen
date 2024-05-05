def solve():
    n, q = map(int, input().split())
    signs = list(map(int, input()))
    answers = []
    
    for _ in range(q):
        l, r = map(int, input().split())
        total_signs = sum(signs[l-1:r])
        cumulative_signs = 0
        removed_elements = 0
        
        for i in range(l-1, r):
            cumulative_signs += signs[i]
            if cumulative_signs == 0:
                removed_elements += 1
            elif cumulative_signs < 0:
                while cumulative_signs < 0 and i < r:
                    cumulative_signs += signs[i]
                    i += 1
        
        answers.append(removed_elements)
    
    for answer in answers:
        print(answer)

if __name__ == "__main__":
    solve()
