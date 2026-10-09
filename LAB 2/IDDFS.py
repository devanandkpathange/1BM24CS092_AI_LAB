from collections import deque
import time

# Input array and target
arr = list(map(int, input("Enter array: ").split()))
target = int(input("Enter target: "))

if not arr:
    print("Array cannot be empty.")
    raise SystemExit

# Build binary tree
graph = {x: [] for x in arr}

for i in range(len(arr)):
    left = 2 * i + 1
    right = 2 * i + 2

    if left < len(arr):
        graph[arr[i]].append(arr[left])

    if right < len(arr):
        graph[arr[i]].append(arr[right])

root = arr[0]


# Breadth-First Search
def bfs():
    queue = deque([root])
    visited = {root}

    while queue:
        node = queue.popleft()

        if node == target:
            return True

        for child in graph[node]:
            if child not in visited:
                visited.add(child)
                queue.append(child)

    return False


# Depth-First Search
def dfs():
    visited = set()

    def search(node):
        if node == target:
            return True

        visited.add(node)

        for child in graph[node]:
            if child not in visited and search(child):
                return True

        return False

    return search(root)


# Iterative Deepening DFS
def iddfs():
    def dls(node, depth):
        if node == target:
            return True

        if depth == 0:
            return False

        for child in graph[node]:
            if dls(child, depth - 1):
                return True

        return False

    for depth in range(len(arr)):
        if dls(root, depth):
            return True

    return False


# Run all algorithms and measure time
print("\n--- SEARCH RESULTS ---")

for name, func in [
    ("BFS", bfs),
    ("DFS", dfs),
    ("IDDFS", iddfs)
]:
    start = time.perf_counter()
    result = func()
    elapsed = time.perf_counter() - start

    print(f"{name}: {'FOUND' if result else 'NOT FOUND'}")
    print(f"Time taken: {elapsed:.8f} seconds\n")
