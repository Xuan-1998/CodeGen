for each test case:
    n = number of chapters
    graph = create a directed graph with n nodes
    indegree = array to store the indegree of each node
    for each chapter i:
        read k_i and the list of prerequisites
        for each prerequisite p of chapter i:
            add a directed edge from p to i in the graph
            increment indegree[i]
    
    if graph has a cycle:
        print -1
        continue
    
    sorted_chapters = perform topological sort on the graph
    read_count = count the number of reads needed using sorted_chapters
    
    print read_count
