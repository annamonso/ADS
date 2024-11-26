from yogi import scan
import sys 

class LinkedQueue:
    """Queue implementation using a singly linked list for storage."""

    class _Node:
        """Nonpublic class for storing a singly linked node."""
        __slots__ = '_element', '_next'  # Optimize memory usage

        def __init__(self, element, next=None):
            """Initialize a new node with an element and a pointer to the next node."""
            self._element = element  # The value stored in the node
            self._next = next  # Pointer to the next node in the queue

    def __init__(self):
        """Create an empty queue."""
        self._head = None  # Pointer to the front of the queue
        self._tail = None  # Pointer to the back of the queue
        self._size = 0  # Count of elements in the queue

    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size  # Return the size of the queue

    def is_empty(self):
        """Return True if the queue is empty."""
        return self._size == 0  # Check if size is zero

    def first(self):
        """Return (but do not remove) the element at the front of the queue.
        Raise an exception if the queue is empty.
        """
        if self.is_empty():
            raise Exception("Queue is empty.")  # Raise error if empty
        return self._head._element  # Return the front element

    def dequeue(self):
        """Remove and return the first element of the queue.
        Raise an exception if the queue is empty.
        """
        if self.is_empty():
            raise Exception("Queue is empty.")  # Raise error if empty
        result = self._head._element  # Store the front element
        self._head = self._head._next  # Move the head pointer to the next node
        self._size -= 1  # Decrement the size of the queue
        if self.is_empty():  # If the queue is now empty
            self._tail = None  # Update the tail to None
        return result  # Return the removed element

    def enqueue(self, element):
        """Add an element to the back of the queue."""
        new_node = self._Node(element)  # Create a new node for the element
        if self.is_empty():
            self._head = new_node  # If empty, new node is now the head
        else:
            self._tail._next = new_node  # Link the old tail to the new node
        self._tail = new_node  # Update the tail to the new node
        self._size += 1  # Increment the size of the queue

    def concatenate(self, q2):
        if q2.is_empty():
            return
        if self.is_empty():
            self._head = q2._head
            self._tail = q2._tail
        else:
            self._tail._next = q2._head
            self.tail = q2._tail
        q2._head = None
        q2._tail = None  
        self._size += q2._size
        q2._size = 0 
    
        
    def __str__(self):
        v = [None]*self._size
        n = self._head
        for i in range(self._size):
            v[i] = n._element
            n = n._next
        return ' '.join(str(e) for e in v)



def scan_type(data_type):
    """
    Función para leer una línea de entrada y convertir al tipo especificado.
    """
    
    line = sys.stdin.readline().strip()
    if not line:
        return None
    parts = line.split()
    if len(parts) == 1:
        return data_type(parts[0])
    return [data_type(part) for part in parts]
    
    
if __name__ == '__main__':
    q1 = LinkedQueue()
    q2 = LinkedQueue()
    while True:
        try: 
            line = scan_type(str)
            if not line: 
                break 

            queue = line[0]
            command = line[1] if len(line) > 1 else None
            value = line[2] if len(line) > 2 else None
            

            if command == "enqueue":
                if queue == "1":
                    q1.enqueue(value)
                else: 
                    q2.enqueue(value) 
                print("queue " + queue + ": " + str(value) + " enqueued")
                
            
            if command == "first":
                if queue =="1":
                    first = q1.first()
                else: 
                    first = q2.first()
                
                print("queue " + queue + " first element: " + first)
                
            if command == "print":
                if queue == "1":
                    res = q1.__str__()
                else: 
                    res = q2.__str__()
                print("queue "+  queue + ": " + res )
                
            if command == "dequeue":
                if queue == "1":
                    res = q1.dequeue()
                else: 
                    res = q2.dequeue()
                print("queue "+  queue + ": " + res + " dequeued")
                
            if command == "is_empty":
                if queue == "1":
                    res = q1.is_empty()
                else: 
                    res = q2.is_empty()

                if res: print("queue "+  queue + " is empty ")
                else : print("queue "+  queue + " is not empty ")
                
            if command == "concatenate":
                if queue == "1":
                    q1.concatenate(q2)
                    print("queues 1 and 2 concatenated")
                else: 
                    q2.concatenate(q1)
                    print("queues 2 and 1 concatenated")
                res = q1.__str__() 
                res2 =q2.__str__() 
                print("queue 1: "+ res )
                print("queue 2: " + res2)
        
            if command == "len":
                if queue == "1":
                    print("queue 1 has " + str(q1._size) + " element(s)")
                else:
                    print("queue 2 has " + str(q2._size) + " element(s)")
                    

                
        except EOFError:
            break

