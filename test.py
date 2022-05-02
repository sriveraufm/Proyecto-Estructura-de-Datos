# Python program to
# demonstrate implementation of
# queue using queue module


from queue import Queue

# Initializing a queue
q = Queue(maxsize = 3)

# qsize() give the maxsize
# of the Queue
# print(q.qsize())

# Adding of element to queue
q.put('a')
q.put('b')
print(q.queue)
print(q.qsize())
# # q.put('c')
# print('reee')
# print(q.queue[0])
# # Return Boolean for Full
# # Queue
# print("\nFull: ", q.full())
# # if not q.full():
# #     print('yuaya')
# # # Removing element from queue
# # print("\nElements dequeued from the queue")
# # print(q.get())
# # print(q.get())
# # print(q.get())
# q.pop('b')
# print(q)
# Return Boolean for Empty
# Queue
# print("\nEmpty: ", q.empty())

# q.put(1)
# print("\nEmpty: ", q.empty())
# print("Full: ", q.full())

# This would result into Infinite
# Loop as the Queue is empty.
# print(q.get())

