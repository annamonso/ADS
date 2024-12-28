import heapq
import sys
from collections import defaultdict

def process_queue(data):
    min_heap = []
    max_heap = []
    count_map = defaultdict(int)
    total_sum = 0
    count = 0
    
    for line in data:
        data2 = line.split()
        if line == 'delete':
            # if there are elements in the heap otherwise don't remove and print 'no elements'
            if min_heap: 
                min_value = heapq.heappop(min_heap) # remove the root of the min heap (highest priority)
                count_map[min_value] -= 1 # decrease the number of times that the element is in the heap
                total_sum -= min_value
                count -= 1
                # the second condition checks if the max element element should be in the heap or not. if not then remove it
                # this starts when it gets to the last element in the heap and then remove all elements in the maxheap
                # (clean the max heap)
                while max_heap and count_map[-max_heap[0]] == 0: 
                    heapq.heappop(max_heap)
                    
                    
            if count == 0:
                print('no elements')
            else:
                max_value = -max_heap[0]
                min_value = min_heap[0]
                mean_value = total_sum / count
                print("minimum: {:d}, maximum: {:d}, average: {:.4f}".format(min_value, max_value, mean_value))
        else:
            number = int(data2[1])
            heapq.heappush(min_heap, number)
            heapq.heappush(max_heap, -number) # to have a max heap using a min heap
            count_map[number] += 1 # to count the number of times that the element is in the heap
            total_sum += number # to calculate the mean
            count += 1 # to calculate the mean
            max_value = -max_heap[0] # to get the root of the max heap (inverted)
            min_value = min_heap[0] # to get the root of the min heap
            mean_value = total_sum / count
            print("minimum: {:d}, maximum: {:d}, average: {:.4f}".format(min_value, max_value, mean_value))

if __name__ == '__main__':
    input_data = []
    for line in sys.stdin:
        line = line.strip()
        input_data.append(line)
    
    process_queue(input_data)