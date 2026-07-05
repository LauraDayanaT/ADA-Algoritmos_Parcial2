import heapq

q = int(input())

heap = []
deleted = set()

for _ in range(q):

    query = list(map(int, input().split()))

    if query[0] == 1:

        heapq.heappush(heap, query[1])

    elif query[0] == 2:

        deleted.add(query[1])

    else:

        while heap and heap[0] in deleted:
            deleted.remove(heap[0])
            heapq.heappop(heap)

        print(heap[0])
