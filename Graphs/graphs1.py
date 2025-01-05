from yogi import scan

# only graph, soruce, target and color (better boolean) are needed
def dfs(graph, source, target, time, color, pred, time_d, time_f):
    print(f"Soure: {source} Target: {target}")
    time += 1
    time_d[source] = time
    color[source] = 'g'
    if source == target: # if current node is the target return True
        return True, time
    for v in graph[source]: # check all neighbors of the source node 
      if color[v] == 'w':
        pred[v] = source
        r = dfs(graph, v, target, time, color, pred, time_d, time_f)
        if r[0]:
          return r
    color[source] = 'b'
    time += 1
    time_f[source] = time
    return False, time

            
if __name__ == '__main__':
    n = scan(int)
    graph = [[] for _ in range(n)] # Adjacency list
    m = scan(int)
    for _ in range(m):
        s = scan(int)
        t = scan(int)
        graph[s].append(t)
    print(graph)
    # color = ['w' for _ in range(n)] # 'w' means white, 'g' gray, and 'b' black
    # pred = [None for _ in range(n)] # None means predecessor unknown
    # time_d = [None for _ in range(n)] # None means discovery time unknown
    # time_f = [None for _ in range(n)] # None means finishing time unknown    
    

    # source = scan(int)
    # target = scan(int)
    # time = 0

    # r = dfs(graph, source, target, time, color, pred, time_d, time_f)
    # if r[0]: print('yes')
    # else: print('no')
    