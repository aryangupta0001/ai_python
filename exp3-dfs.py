graph = {1 : [4, 2], 4 : [1, 3], 2 : [1, 3, 8, 5, 7], 3 : [4, 10, 9, 2], 8 : [2, 5, 7], 5 : [2, 8, 7, 6], 7 : [2, 5, 8], 10 : [3], 9 : [3], 6 : [5]}

visited = []
stack = []

def dfs(graph, visited, root):

    if(root not in visited):
        stack.append(root)
        visited.append(root)
        print(root, end='\t')

        for i in graph[root]:
            dfs(graph, visited, i)
        
        stack.pop()
        
root = 1
print("DFS Traversal of graph :-")
dfs(graph, visited, root)