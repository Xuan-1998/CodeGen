code
Step 1: Understand the Problem Statement
The Infinite Zoo is an infinite graph where edges satisfy u & v = v condition. Given q queries, for each query find if a path exists between u and v.

Step 2: Define the Queries
Read integer q from stdin.
Read q pairs of integers (u_i, v_i) from stdin. Each pair represents a query to check if a path exists between vertex u_i and vertex v_i.

Step 3: Design an Algorithm
For each query:
    Check if there's a directed edge from u to v (i.e., u & v = v). If yes, return "YES". Otherwise, return "NO".

Step 4: Implement the Solution in 
