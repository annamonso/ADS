import heapq
import sys

'''
root element = 4 
min heap:
    4
   / \
  10  5
     / \
    6   9
max heap:
    4
   / \
  1   2
  
first chil index = 2*i + 1
second child index = 2*i + 2
parent index = (i-1)//2
.heapify(data) -> crea un arbre ordenat
.headpop(data) -> borra el primer elem i torna a crear el arbre ordenat
.headpush(data,i) -> afegeix un element i torna a crear el arbre ordenat

'''
def process_queue(data):
    data = [int(x) for x in data]
    data2 = data.copy()
    heapq.heapify(data)
    heapq._heapify_max(data2)
    # print all the elements in order and in the same line
    first = True
    while data:
        if not first:
            print(' ', end='')
        print(heapq.heappop(data), end='')
        first = False
    print()
    
    # print all the elements in reverser order and in the same line
    first = True
    while data2:
        if not first:
            print(' ', end='')
        print(heapq._heappop_max(data2), end='')
        first = False
    print()
    
# main
if __name__ == '__main__':
    while True:
        try:
            line = input()
            data = line.split() # vector with the elements
            process_queue(data)
        except EOFError:
            break

