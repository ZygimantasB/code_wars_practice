from heapq import heappush, heappop, nlargest, nsmallest, heapify

heap_list = []

heappush(heap_list, 1)
heappush(heap_list, 2)
heappush(heap_list, 4)
heappush(heap_list, 6)
heappush(heap_list, 8)
heappush(heap_list, -8)
heappush(heap_list, 11)
heappush(heap_list, -5)

print(heap_list)

smallest = heappop(heap_list)
print(smallest)
print(heap_list)

largest = nlargest(3, heap_list)
print(largest)
three_smallest = nsmallest(2, heap_list)
print(three_smallest)

tasks = []

heappush(tasks, (2, 'write code'))
heappush(tasks, (1, 'specify requirements'))
heappush(tasks, (3, 'test the software'))

while tasks:
    priority, task = heappop(tasks)
    print(f"Process task: {task} with priority: {priority}")

print(heapify(heap_list))
print(heap_list)