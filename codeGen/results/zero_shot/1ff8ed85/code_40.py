import sys

def can_send_over_network():
    t = int(input())
    for _ in range(t):
        n = int(input())
        b = list(map(int, input().split()))
        
        # check if we can send over network
        a = []
        left_segment_sum = 0
        right_segment_sum = 0
        
        for i in range(n-1):
            segment_length = b[i+1] - b[i]
            
            # write length of current segment to the left
            if (a and sum(a) + segment_length == n) or (left_segment_sum + segment_length == n):
                break
            
            # write length of current segment to the right
            elif left_segment_sum < segment_length:
                left_segment_sum += segment_length
            else:
                right_segment_sum += segment_length
        
        if len(a) == n-1 and a[-1] != b[-1]:
            print("YES")
        elif (left_segment_sum + right_segment_sum) == n:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    can_send_over_network()
