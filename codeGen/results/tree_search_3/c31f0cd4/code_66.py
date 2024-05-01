from collections import Trie

def find_distinct_sums(N, elements):
    # Initialize memoization Trie
    trie = Trie()

    # Initialize set to store unique sums
    unique_sums = set()

    def dfs(current_sum, current_binary):
        if current_sum > sum(elements):
            return  # Prune tree for sums exceeding the maximum possible

        # Mark this sum as visited
        trie.insert(current_binary)

        # Update set of unique sums
        unique_sums.add(current_sum)

        for i in range(len(elements)):
            new_binary = current_binary + ("1" if elements[i] else "0")
            dfs(current_sum + (1 if i < N - 1 else 0), new_binary)

    # Start DFS from sum 0 with binary representation ""
    dfs(0, "")

    return sorted(list(unique_sums))
