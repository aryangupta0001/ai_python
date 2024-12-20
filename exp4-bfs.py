graph = {'A' : [('B', 12), ('C', 4)], 
         'B' : [('D', 7), ('E', 3)],
         'C' : [('F', 8), ('G', 2)],
         'D' : [],
         'E' : [('H', 0)],
         'F' : [('H', 0)],
         'G':[('H',0)]}

visited = []
queue = []

def bfs(start, target, graph, queue, visited):
    if start not in visited:
        print(start, end = '\t')
    
        visited.append(start)
        queue = queue + [x  for x in graph[start] if x [0][0] not in visited]

        queue.sort(key = lambda x:x[1])
        
        if queue[0][0] == target:
            print(queue[0][0])
        
        else:
            process = queue[0]
            queue.remove(process)
            bfs(process[0], target, graph, queue, visited)

print("Best First Search Traversal :-")
bfs('A', 'H', graph, queue, visited)