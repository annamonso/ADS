from yogi import scan
from heapq import heapify, heappop, heappush
import sys


def orders(v):
  print('DEPARTS')
  print('-------')
  ord = scan(str)
  while ord is not None: 
   if ord == 'LEAVES':
     i = scan(int)  
     if 0 <= i-1 < len(v) and len(v[i-1]) != 0: print(heappop(v[i-1])[1])
   else:
     name = scan(str)
     age = scan(float)  
     c = (-age, name)
     i = scan(int)
     if 0 <= i-1 < len(v): heappush(v[i-1],c)
   ord = scan(str)                 
  print()

  
def escribe(v):
  print('FINAL CONTENTS')
  print('--------------')
  for i in range(len(v)):
    print('queue {}:'.format(i+1), end='')  
    while len(v[i]) != 0:
        print(' {}'.format(heappop(v[i])[1]), end='')
    print()
              

def read_prior_queues(n, v):
   i = 0
   for line in sys.stdin:
      if i == n: return
      else:
         data = line.split()
         v[i] = [None for j in range(len(data)//2)]
         for j in range(len(v[i])):  
            v[i][j] = (-float(data[2*j+1]), data[2*j])
         heapify(v[i])
         i += 1
    
if __name__ == '__main__':
  n = scan(int)
  v = [[]  for _ in range(n)]
  read_prior_queues(n, v)
  orders(v)
  escribe(v)  
