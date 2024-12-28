from yogi import scan
from heapq import heapify, heappush, heappop
from collections import deque


def read_case(nv):
    ne = scan(int)
    adj = [[] for _ in range(nv)]
    for _ in range(ne):
        u = scan(int)
        v = scan(int)
        w = scan(int)
        adj[u].append((v, w))
    s = scan(int)
    t = scan(int)
    return adj, s, t



def path(u, s, pi):
  p = deque([u])
  while u != s:
    p.appendleft(pi[u])
    u = pi[u]
  return p



class Est_Vert:
    __slots__ = '_estimate', '_vert'

    def __init__(self, e, v):
      self._estimate = e
      self._vert = v

    def dist_estimate(self):
        return self._estimate

    def vertex(self):
        return self._vert

    def __lt__(self, other):
        if self._estimate is None:
            return False
        if other._estimate is None:
            return True
        return self._estimate < other._estimate

    

def dijkstra(adj, s, t):
  # initialization
  nv = len(adj)
  r = [False for _ in range(nv)]
         # Subset of vertices whose final shortest-path weight from s
         # has already been determined.
         
  pi = [None for _ in range(nv)] # predecessor subgraph attribute
  
  #INF = 2 ** 31
  d = [None for _ in range(nv)] # distance estimate attribute (None interpreted as infinite)
  d[s] = 0
  
  q = [Est_Vert(d[i], i) for i in range(nv)]
  heapify(q)
         
  while len(q) != 0:
    e = heappop(q) # extract min
    if not r[e.vertex()]: # otherwise du is not the smallest distance estimate for u 
      r[e.vertex()] = True
      if e.vertex() == t:
          if e.dist_estimate() is None: return None
          else: return path(t, s, pi)

      for (v, w) in adj[e.vertex()]:
        if not r[v] and e.dist_estimate() is not None:  
          current = e.dist_estimate() + w
          if d[v] is None or current < d[v]:
            d[v] = current
            pi[v] = e.vertex()
            heappush(q, Est_Vert(current, v)) # Instead of calling to decreaseKey
            # redundant pairs of the form (distance_estimate, node) are
            # added to the priority queue. The pair with smallest estimate 
            # will come out in first place. 

            

if __name__ == '__main__':
  #INF = 2 ** 31    
  nv = scan(int)
  while nv is not None:
    (adj, s, t) = read_case(nv)
    sp = dijkstra(adj, s, t)
    if sp is None: print(f'no path from {s} to {t}')
    else:
        p = ' '.join(str(e) for e in sp)
        print(p)

    nv = scan(int)
