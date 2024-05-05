def can_reach(jumps):
    dp_dict = {0: True}

    def can_reach_recursive(i):
        if i in dp_dict:
            return dp_dict[i]
        
        if i == 0:
            return True
        
        reachable = False
        for j in range(i - jumps[i] - 1, -1, -1):
            if j >= 0 and can_reach_recursive(j):
                reachable = True
                break
        
        dp_dict[i] = reachable
        return reachable
    
    return can_reach_recursive(len(jumps) - 1)
