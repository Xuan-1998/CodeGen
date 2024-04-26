from collections import deque

def find_subsequences(initial, final):
    subsequences = []
    i = 0
    for weight in final:
        subseq_sum = 0
        subseq = deque()
        while i < len(initial) and subseq_sum < weight:
            subseq_sum += initial[i]
            subseq.append(i+1)
            i += 1
        if subseq_sum != weight:
            return "NO", []
        subsequences.append(subseq)
    return "YES", subsequences

def determine_eating_order(subsequences):
    eating_order = []
    for subseq in subsequences:
        while len(subseq) > 1:
            if subseq[0] < subseq[-1]:
                eating_order.append(f"{len(subseq)} L")
                subseq.popleft()
            else:
                eating_order.append(f"1 R")
                subseq.pop()
    return eating_order

def main():
    n = int(input())
    initial = list(map(int, input().split()))
    k = int(input())
    final = list(map(int, input().split()))
    
    if sum(initial) != sum(final):
        print("NO")
        return
    
    possible, subsequences = find_subsequences(initial, final)
    if possible == "NO":
        print(possible)
        return
    else:
        eating_order = determine_eating_order(subsequences)
        print(possible)
        for order in eating_order:
            print(order)

if __name__ == "__main__":
    main()
