import heapq

# Display puzzle
def display(state):
    for i in range(0, 9, 3):
        print("+---+---+---+")
        print("|", end="")
        for j in range(i, i + 3):
            print(f" {state[j] if state[j] != 0 else ' '} |", end="")
        print()
    print("+---+---+---+")


# Misplaced tile heuristic
def heuristic(state, goal):
    return sum(
        state[i] != 0 and state[i] != goal[i]
        for i in range(9)
    )


# Generate next states
def neighbors(state):
    zero = state.index(0)
    row, col = divmod(zero, 3)
    result = []

    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        r, c = row + dr, col + dc

        if 0 <= r < 3 and 0 <= c < 3:
            pos = r * 3 + c
            new = list(state)
            new[zero], new[pos] = new[pos], new[zero]
            result.append(tuple(new))

    return result


# Check whether goal is reachable
def solvable(start, goal):
    order = {v: i for i, v in enumerate(goal) if v != 0}
    nums = [order[v] for v in start if v != 0]
    inversions = sum(
        nums[i] > nums[j]
        for i in range(8) for j in range(i + 1, 8)
    )
    return inversions % 2 == 0


# Search using selected method
def solve(start, goal, method):
    pq = [(heuristic(start, goal), 0, start)]
    parent = {start: None}
    cost = {start: 0}
    visited = set()
    counter = 0

    while pq:
        _, _, current = heapq.heappop(pq)

        if current in visited:
            continue
        visited.add(current)

        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            return path[::-1]

        for nxt in neighbors(current):
            new_cost = cost[current] + 1

            if nxt not in cost or new_cost < cost[nxt]:
                cost[nxt] = new_cost
                parent[nxt] = current
                counter += 1

                h = heuristic(nxt, goal)

                # Method 1: Misplaced tile heuristic
                # Method 2: A* search
                priority = h if method == 1 else new_cost + h

                heapq.heappush(pq, (priority, counter, nxt))

    return None


# Get initial and goal states
def get_state(name):
    print(f"\nEnter {name} state (0 = blank):")
    values = []

    for i in range(3):
        row = list(map(int, input(f"Row {i + 1}: ").split()))
        if len(row) != 3:
            raise ValueError("Each row must contain 3 numbers.")
        values.extend(row)

    if len(values) != 9 or set(values) != set(range(9)):
        raise ValueError("Use numbers 0 to 8 exactly once.")

    return tuple(values)


try:
    start = get_state("INITIAL")
    goal = get_state("GOAL")

    print("\nChoose method:")
    print("1. Misplaced Tile Heuristic")
    print("2. A* Search")
    method = int(input("Enter choice: "))

    if method not in (1, 2):
        raise ValueError("Choose 1 or 2.")

    if not solvable(start, goal):
        print("Goal is unreachable from the initial state.")
    else:
        path = solve(start, goal, method)

        if path:
            print("\nSolution found!")
            print("Total moves:", len(path) - 1)

            for step, state in enumerate(path):
                print(f"\nStep {step}:")
                display(state)
                print("Misplaced tiles:", heuristic(state, goal))
        else:
            print("No solution found.")

except ValueError as e:
    print("Invalid input:", e)
