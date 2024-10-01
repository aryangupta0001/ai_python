graph = {1 : [4, 2], 4 : [1, 3], 2 : [1, 3, 8, 5, 7], 3 : [4, 10, 9, 2], 8 : [2, 5, 7], 5 : [2, 8, 7, 6], 7 : [2, 5, 8], 10 : [3], 9 : [3], 6 : [5]}
visited = []
queue = []

def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while(queue):
        m = queue.pop(0)
        print(m, end = ' ')

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

root = 1
bfs(visited, graph, 1)