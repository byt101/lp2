import heapq

# Selection Sort
a = [int(input(f"Enter value {i+1}: ")) for i in range(int(input("Total number of elements: ")))]
print("Unsorted Array:", a)

for i in range(len(a)):
    min_idx = i
    for j in range(i+1, len(a)):
        if a[j] < a[min_idx]:
            min_idx = j
    a[i], a[min_idx] = a[min_idx], a[i]

print("Sorted Array:", a)

# Prim's Algorithm
def prim(graph, start):
    mst, visited = [], set([start])
    edges = [(cost, start, to) for to, cost in graph[start].items()]
    heapq.heapify(edges)

    while edges:
        cost, frm, to = heapq.heappop(edges)
        if to not in visited:
            visited.add(to)
            mst.append((frm, to, cost))
            for nxt, cost2 in graph[to].items():
                if nxt not in visited:
                    heapq.heappush(edges, (cost2, to, nxt))
    return mst

graph = {
    'A': {'B': 2, 'C': 3},
    'B': {'A': 2, 'C': 1, 'D': 1},
    'C': {'A': 3, 'B': 1, 'D': 4},
    'D': {'B': 1, 'C': 4}
}

print("Prim's MST:", prim(graph, 'A'))
