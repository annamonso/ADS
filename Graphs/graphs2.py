from yogi import scan
from collections import deque

# only graph, soruce, target and color (better boolean) are needed
def dfs(graph, source, target, time, color, pred, time_d, time_f,cities):
    inverse_cities = {v: k for k, v in cities.items()}
    print(f"Soure: {inverse_cities[source]} Target: {inverse_cities[target]}")
    time += 1
    time_d[source] = time
    color[source] = 'g' # first time we see the node
    if source == target: # if current node is the target return True
        return True, time
    for v in graph[source]: # check all neighbors of the source node 
      if color[v] == 'w':
        pred[v] = source # set the predecessor
        r = dfs(graph, v, target, time, color, pred, time_d, time_f,cities)
        if r[0]:
          return r
    color[source] = 'b' # all neighbors visited
    time += 1
    time_f[source] = time
    return False, time

def bfs(graph, source, target, color, pred, cities):
    inverse_cities = {v: k for k, v in cities.items()}
    print(f"Soure: {inverse_cities[source]} Target: {inverse_cities[target]}")
    queue = deque()
    queue.append(source)
    color[source] = 'g'
    while queue:
        u = queue.popleft()
        if u == target:
            return True
        for v in graph[u]:
            if color[v] == 'w':
                color[v] = 'g'
                pred[v] = u
                queue.append(v)
        color[u] = 'b'
    return False

            
if __name__ == '__main__':
    n = scan(int)
    graph = [[] for _ in range(n)] # Adjacency list
    
    # create a dictionary to relate the string to the index
    cities = {}
    
    for i in range(n):
        s = scan(str)
        if s not in cities:
            cities[s] = i
        
    print(cities)
    
    # create the graph
    m = scan(int)
    for i in range(m):
        node_city = scan(str)
        next_city = scan(str)
        # get number of the city
        node = cities[node_city]
        graph[node].append(cities[next_city])
    print(graph)
    # 'w' means white, 'g' gray, and 'b' black 
    color = ['w' for _ in range(n)] # set all to not visited
    pred = [None for _ in range(n)] # None means predecessor unknown
    time_d = [None for _ in range(n)] # None means discovery time unknown
    time_f = [None for _ in range(n)] # None means finishing time unknown    
    
    source = scan(str)
    print(f"Source: {source}")
    source_index = cities[source]
    target = scan(str)
    print(f"Target: {target}")
    target_index = cities[target]
    time = 0

    #r = dfs(graph, source_index, target_index, time, color, pred, time_d, time_f, cities)
    r = bfs(graph, source_index, target_index, color, pred, cities)
    if r: print('yes')
    else: print('no')
    print(f"pred: {pred}")
    