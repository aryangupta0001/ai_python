graph = {'1' : ['2', '3'], '2' : ['4', '5'],  '3' : ['9', '8'], '4' : ['6', '7'], '5' : [], '9' : ['11'], '8' : [], '6' : [], '7' : [], '11' : []}
visited = []
queue = []

def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while(queue):
        m = queue.pop(0)
        print(m, end = ' ')

        for neighbour in graph:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)



bfs(visited, graph, '1')