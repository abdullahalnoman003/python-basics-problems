#shortest path to reach destination
#f(n) = g(n) +h(n)      -> g(n) backword cost  h(n) forword cost
# data structure needed g cost and came from : using priorith queue 
import heapq

GRAPH = {
    'A': {'B': 1, "C":4},
    'B': {'D': 5, 'E': 2},
    'C': {'E':1},
    'D':{'F':3},
    'E': {'D':1, 'F':6},
    'F':{}
}
HURISTICS = {
    'A': 7,
    'B' : 5,
    'C' : 2,
    'D' : 3,
    'E': 4,
    'F': 0
}

def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    return path[:: -1]

def a_star (graph, heuristics, start_node, goal_node):
    open_list = [(heuristics[start_node], start_node)]
    g_cost = {node : float('inf') for node in graph}
    g_cost[start_node] = 0

    came_from = {}

    while open_list:
        f_cost, current_node = heapq.heappop(open_list)
        if current_node == goal_node:
            path = reconstruct_path(came_from, current_node)
            cost = g_cost[current_node]
            return path, cost

        for neibour, travel_cost in graph[current_node].items():
            tentative_g = g_cost[current_node] + travel_cost

            if tentative_g < g_cost[neibour]:
                came_from[neibour] = current_node
                g_cost[neibour] = tentative_g
                h= heuristics.get(neibour, float('inf'))
                new_f = tentative_g+h
                heapq.heappush(open_list, (new_f, neibour))

            else: 
                continue

    return None, float('inf')  

start = 'A'
goal = 'F'

path, cost = a_star(GRAPH, HURISTICS, start, goal)

if path:
    print(f"Shortest path: {' -> '.join(path)}")
    print(f"Total cost: {cost}")
else:
    print("No path found.")

