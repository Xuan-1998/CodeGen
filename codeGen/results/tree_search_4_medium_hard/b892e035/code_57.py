def get_probability():
    T = int(input())
    
    dp = {}
    
    for _ in range(T):
        n = int(input())
        
        probabilities = []
        seen = set()
        
        for _ in range(n):
            p1, num1, num2 = map(int, input().split())
            
            if num1 not in seen:
                seen.add(num1)
            else:
                num1 = None
                
            if num2 not in seen:
                seen.add(num2)
            else:
                num2 = None
                
            probabilities.append((p1, num1, num2))
        
        probability = 0
        
        for p1, num1, num2 in probabilities:
            if num1 is None and num2 is None:
                if (n-1, seen) not in dp:
                    dp[(n-1, seen)] = get_probability_core(n-1, seen)
                probability += p1 * dp[(n-1, seen)]
            elif num1 is None:
                if (n-1, set.union(seen, {num2})) not in dp:
                    dp[(n-1, set.union(seen, {num2}))] = get_probability_core(n-1, set.union(seen, {num2}))
                probability += p1 * dp[(n-1, set.union(seen, {num2}))]
            elif num2 is None:
                if (n-1, set.union(seen, {num1})) not in dp:
                    dp[(n-1, set.union(seen, {num1}))] = get_probability_core(n-1, set.union(seen, {num1}))
                probability += p1 * dp[(n-1, set.union(seen, {num1}))]
            else:
                if (n-2, set.union(seen, {num1, num2})) not in dp:
                    dp[(n-2, set.union(seen, {num1, num2}))] = get_probability_core(n-2, set.union(seen, {num1, num2}))
                probability += p1 * dp[(n-2, set.union(seen, {num1, num2}))]
        
        print(round(probability, 6))

def get_probability_core(i, seen):
    if i == 0:
        return 1.0
    elif (i, seen) in dp:
        return dp[(i, seen)]
    
    probability = 0.0
    
    for p, num1, num2 in probabilities[i-1]:
        if num1 is None and num2 is None:
            probability += p * get_probability_core(i-1, set())
        elif num1 is None:
            probability += p * get_probability_core(i-1, set.union(seen, {num2}))
        elif num2 is None:
            probability += p * get_probability_core(i-1, set.union(seen, {num1}))
        else:
            probability += p * get_probability_core(i-1, set.union(seen, {num1, num2}))
    
    dp[(i, seen)] = round(probability, 6)
    
    return dp[(i, seen)]
