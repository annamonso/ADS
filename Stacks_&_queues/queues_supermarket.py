from collections import deque
import sys

def process_queues(data):
    num_queues = data[0]
    queue_list = []

    for i in range(1, num_queues + 1):
        queue_data = data[i].split()
        queue_list.append(deque(queue_data))

    num_events = len(data) - num_queues - 2
    departures = []


    for event_index in range(num_events):
        event_data = data[event_index + num_queues + 2].split()
        queue_num = int(event_data[-1])

        if 1 <= queue_num <= num_queues:
            if event_data[0] == 'ENTERS':
                queue_list[queue_num - 1].append(event_data[1])
            elif event_data[0] == 'LEAVES' and queue_list[queue_num - 1]:
                departures.append(queue_list[queue_num - 1].popleft())

   
    final_queue_status = [list(queue) for queue in queue_list]
    final_content = []

    for i in range(num_queues):
        final_content.append(f'queue {i + 1}:' + (f" {' '.join(final_queue_status[i])}" if final_queue_status[i] else ""))

    result = ['DEPARTS', '-------'] + departures + ['', 'FINAL CONTENTS', '--------------'] + final_content

    return result

if __name__ == '__main__':
    input_data = []
    for line in sys.stdin:
        line = line.strip()
        try:
            line = int(line)
        except:
            pass
        input_data.append(line)

 
    result = process_queues(input_data)

    sys.stdout.write("\n".join(str(item) for item in result) + "\n")

