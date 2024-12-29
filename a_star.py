graph = [
    ['A', 'B', 1, 3],
    ['A', 'C', 2, 4],
    ['A', 'H', 7, 8],
    ['B', 'D', 4, 2],
    ['B', 'E', 6, 6],
    ['C', 'F', 3, 3],
    ['C', 'G', 2, 1],
    ['D', 'E', 7, 6],
    ['D', 'H', 5, 0],
    ['F', 'H', 1, 0],
    ['G', 'H', 2, 0]
]


def find_path(graph, cost, open, closed, cur_node):
    if cur_node in open:
        open.remove(cur_node)
        closed.add(cur_node)
    
    for i in graph:
        if i[0] == cur_node and cost[i[0]] + i[2] + i[3] < cost[i[1]]:
            open.add(i[1])
            cost[i[1]] = cost[i[0]] + i[2] + i[3]
            path[i[1]] = path[i[0]] + '->' + i[1]
    
    cost[cur_node] = 99999
    
    small = min(cost, key=cost.get)
    
    if small not in closed:
        find_path(graph, cost, open, closed, small)



temp = []
temp1 = []

for i in graph:
    temp.append(i[0])
    temp1.append(i[1])

nodes = set(temp).union(set(temp1))

    
cost = dict()
temp_cost = dict()
path = dict()

for i in nodes:
    cost[i] = 99999
    path[i] = ''

open = set()
closed = set()

start_node = input("Enter the start node : ")

open.add(start_node)
path[start_node] = start_node
cost[start_node] = 0

find_path(graph, cost, open, closed, start_node)

goal_node = input("Enter goal node : ")
print("Path with least cost is : ", path[goal_node])