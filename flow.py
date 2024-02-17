from collections import deque

def find_edges(edges, capacities, s, t):
    
    # all vertices
    vertices = [i[0] for i in edges] + [i[1] for i in edges]
    vertices = set(vertices)

    # (n1, n2): weight
    capacity_dict = dict()

    adj_list = {} # residual graph
    i = 0
    visited = {} 
    parent = {}
    capacity_dict = {}
    directed = {}

    original_capacities = {}
    og_capacities = {}

    for e in edges:
        if e[0] not in adj_list: 
            adj_list[e[0]] = {}
            original_capacities[e[0]] = {}
            og_capacities[e[0]] = {}
        
        adj_list[e[0]][e[1]] = capacities[i]

        original_capacities[e[0]][e[1]] = capacities[i]
        og_capacities[e[0]][e[1]] = capacities[i]

        
        if e[1] not in adj_list: 
            adj_list[e[1]] = {}
            original_capacities[e[1]] = {}
            og_capacities[e[1]] = {}
        if e[0] not in adj_list[e[1]]: 
            adj_list[e[1]][e[0]] = 0
            original_capacities[e[1]][e[0]] = 0
            og_capacities[e[1]][e[0]] = 0
        visited[e[0]] = False
        visited[e[1]] = False
        parent[e[0]] = -1
        parent[e[1]] = -1
        capacity_dict[(e[0], e[1])] = capacities[i]
        if e[0] not in directed: directed[e[0]] = []
        directed[e[0]].append(e[1])

        i+=1

    max_flow = 0
    
    crossing_edges = set()

    # creating residual graph
    while BFS(s, t, parent, vertices, adj_list):
        path_flow = float("Inf")
        end = t
        while(end != s):
            path_flow = min(path_flow, adj_list[parent[end]][end])
            end = parent[end]

        # Adding the path flows
        max_flow += path_flow

        # Updating the residual values of edges
        v = t
        while(v != s):
            u = parent[v]
            adj_list[u][v] -= path_flow
            adj_list[v][u] += path_flow
            v = parent[v]

    unsaturated_edges = set()
    priority_edges = set()

    paths = all_paths_dfs(original_capacities, s, t)
    #seen_paths = []
    for path in paths:
        pair_path = []
        for index, val in enumerate(path[:-1]):
            pair_path.append((val, path[index+1]))

        path = pair_path

        print(path)

        min_residual = float("inf")
        min_edges = set()
        min_capacity = float("inf")
        for edge in path:
            #print("residual", og_capacities[edge[0]][edge[1]] , adj_list[edge[0]][edge[1]])
            residual_value = og_capacities[edge[0]][edge[1]] - adj_list[edge[0]][edge[1]]
            print(edge, og_capacities[edge[0]][edge[1]], adj_list[edge[0]][edge[1]])
            # if residual_value < min_residual:
            #     u = edge[0]
            #     v = edge[1]
            #     min_edges = {(u, v)}

            if og_capacities[edge[0]][edge[1]] == min_capacity:
                u = edge[0]
                v = edge[1]
                min_edges.add((u, v))
            if og_capacities[edge[0]][edge[1]] < min_capacity:
                min_capacity = og_capacities[edge[0]][edge[1]]
                u = edge[0]
                v = edge[1]
                min_edges = {(u, v)}


            #print(edge, residual_value)

        if len(min_edges) != len(path):
            priority_edges.update(min_edges)

        # for u, v in min_edges:
        #     original_capacities[u][v] = -1

        #path = BFS2(s, t, parent, vertices, original_capacities)
        

        #print(path)
        # original_capacities[u][v] -= path_flow
        # original_capacities[v][u] += path_flow

    return priority_edges        



def DFS(adj_list, s, visited):
    visited[s]=True
    for i in adj_list.keys():
        # if s in adj_list and i in adj_list[s] and adj_list[s][i]>0 and not visited[i]:
        if adj_list[s][i]>0 and not visited[i]:

            DFS(adj_list,i,visited)
    return visited

def BFS2(s, t, parent, vertices, adj_list):

    visited = {}

    print(parent)

    for key in adj_list.keys():        
        visited[key] = False

    # visited =[False]*(len(vertices))
    queue = []

    queue.append(s)
    visited[s] = True

    while queue:

        u = queue.pop(0)

        for ind in adj_list[u]:
            val = adj_list[u][ind]
            if not visited[ind] and val > 0:
                queue.append(ind)
                visited[ind] = True
                parent[ind] = u
                #if ind == t: return (True, visited)
                if ind == t: return get_path(parent, s, t)

    #return (False, visited)
    return False

def BFS(s, t, parent, vertices, adj_list):

    visited = {}

    print(parent)

    for key in adj_list.keys():        
        visited[key] = False

    # visited =[False]*(len(vertices))
    queue = []

    queue.append(s)
    visited[s] = True

    while queue:

        u = queue.pop(0)

        for ind in adj_list[u]:
            val = adj_list[u][ind]
            if not visited[ind] and val > 0:
                queue.append(ind)
                visited[ind] = True
                parent[ind] = u
                #if ind == t: return (True, visited)
                if ind == t: return True


    #return (False, visited)
    return False

def all_paths_dfs(adj_list, source, dest):
    paths = []
    visited = set()

    def dfs_helper(current, path):
        visited.add(current)
        path.append(current)

        if current == dest:
            paths.append(path[:])

        #for neighbor in graph[current]:
        for ind in adj_list[current]:
            val = adj_list[current][ind]
            if ind not in visited and val > 0:
            #if neighbor not in visited:
                dfs_helper(ind, path)

        path.pop()
        visited.remove(current)

    dfs_helper(source, [])
    return paths


def get_path(parent, start, end):
    path = []
    node = end
    while node != start:
        parent_node = parent[node]
        path.append((parent_node, node))
        node = parent_node
    #path.append(start)
    path.reverse()
    return path

# CASES
# edges =  [(0, 1), (1, 2), (2, 3)]
# capacities =  [2, 1, 2]
# source =  0
# target =  3

# edges =  [(0, 1), (1, 2), (2, 3)]
# capacities = [2, 2, 2]
# source = 0
# target = 3
# output: [(1, 2)]



edges =  [(0, 1), (0, 2), (1, 3), (3, 2), (2, 4), (3, 4)]
capacities =   [3, 1, 3, 1, 3, 1]
source =  0
target = 4

#expected output:  [(0, 2), (3, 2), (3, 4)]

print(find_edges(edges, capacities, source, target))





# edges = [(0, 1), (1, 2), (2, 3)]
# capacities =  [2, 2, 2]
# source =  0
# target =  3
# output: []

# print(find_edges(edges, capacities, source, target))