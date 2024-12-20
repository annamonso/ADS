from yogi import scan
import sys

class Empty(Exception):
  """Error attempting to access an element from an empty container"""
  pass


class LinkedQueue:
  """FIFO queue implementation using a singly linked list for storage."""


  #-------------------------- nested _Node class -------------
  class _Node:
    """Lightweight, nonpublic class for storing a singly linked node."""
    __slots__ = '_element', '_next'  

    
    def __init__(self, element, next):
      self._element = element
      self._next = next

      
  #------------------------------- queue methods -------------

  
  def __init__(self):
    """Create an empty queue."""
    self._head = None
    self._tail = None
    self._size = 0                   

    
  def __len__(self):
    """Return the number of elements in the queue."""
    return self._size

  
  def is_empty(self):
    """Return True if the queue is empty."""
    return self._size == 0

  
  def first(self):
    """Return (but do not remove) the element at the front of the queue. Raise Empty exception if the queue is empty. """
    if self.is_empty():
      raise Empty('Queue is empty')
    return self._head._element            

  
  def dequeue(self):
    """Remove and return the first element of the queue (i.e., FIFO). Raise Empty exception if the queue is empty."""
    if self.is_empty():
      raise Empty('Queue is empty')
    answer = self._head._element
    self._head = self._head._next
    self._size -= 1
    if self.is_empty():                   
      self._tail = None                   
    return answer

  
  def enqueue(self, e):
    """Add an element to the back of queue."""
    newest = self._Node(e, None)          
    if self.is_empty():
      self._head = newest                 
    else:
      self._tail._next = newest
    self._tail = newest                   
    self._size += 1


  # ----------------------------- Rotate ---------------------

  
  def rotate(self):
    if self._size == 0:
      raise Empty('Queue is empty')
    answer = self._head._element
    if self._size > 1:
      
      node = self._head # Reference to the first node before rotation.

      self._head = self._head._next # The second node in the original  
      # queue becomes the first node of the queue after rotation.
      
      self._tail._next = node # 'node' is added at the back of the linked
      # list by connecting the last node in the original queue to 'node'.
      
      self._tail = node # 'node' becomes the last node after rotation.

      self._tail._next = None # This is necessary to end the linked list.

      # Note that it is not necessary to create a new node (i.e. to call
      # to the _Node constructor). We only move the first node of the
      # original linked list to the back of such list.
                           
    return answer
    
    
  def __str__(self):
    v = [None]*self._size
    n = self._head
    for i in range(self._size):
      v[i] = n._element
      n = n._next
    return ' '.join(str(e) for e in v)



if __name__ == '__main__':
    q = LinkedQueue()
    for line in sys.stdin:  
        values = line.strip().split()  
        for value in values:
            q.enqueue(value)
    
    print(q)
    print(f'rotate returns: {q.rotate()}')
    print(q)
    
