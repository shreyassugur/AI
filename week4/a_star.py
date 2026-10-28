 
import heapq

GOAL = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

START = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)


def manhattan(state):
    distance = 0

    for i, tile in enumerate(state):
        if tile != 0:
            goal_index = GOAL.index(tile)

            current_row, current_col = divmod(i, 3)
            goal_row, goal_col = divmod(goal_index, 3)

            distance += abs(current_row - goal_row)
            distance += abs(current_col - goal_col)

    return distance


def get_neighbors(state):
    neighbors = []
    zero = state.index(0)
    row, col = divmod(zero, 3)

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in moves:
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_index = new_row * 3 + new_col

            new_state = list(state)
            new_state[zero], new_state[new_index] = (
                new_state[new_index], new_state[zero]
            )

            neighbors.append(tuple(new_state))

    return neighbors


def is_solvable(state):
    tiles = [tile for tile in state if tile != 0]
    inversions = 0

    for i in range(len(tiles)):
        for j in range(i + 1, len(tiles)):
            if tiles[i] > tiles[j]:
                inversions += 1

    return inversions % 2 == 0


def astar(start):
    if not is_solvable(start):
        print("This puzzle is not solvable.")
        return None

    pq = [(manhattan(start), 0, start)]
    parent = {start: None}
    cost = {start: 0}

    while pq:
        f, g, current = heapq.heappop(pq)

        if g != cost[current]:
            continue

        # Display the current state's G, H, and F values
        h = manhattan(current)

        print("Current State:")
        print_board(current)
        print("G(n) =", g)
        print("H(n) =", h)
        print("F(n) = G(n) + H(n) =", g + h)
        print("-" * 30)

        if current == GOAL:
            path = []

            while current is not None:
                path.append(current)
                current = parent[current]

            return path[::-1]

        for neighbor in get_neighbors(current):
            new_g = g + 1

            if neighbor not in cost or new_g < cost[neighbor]:
                cost[neighbor] = new_g
                parent[neighbor] = current

                h = manhattan(neighbor)
                new_f = new_g + h

                heapq.heappush(
                    pq, (new_f, new_g, neighbor)
                )

    return None


def print_board(state):
    for i in range(0, 9, 3):
        row = state[i:i + 3]
        print(" ".join("_" if x == 0 else str(x) for x in row))
    print()


if __name__ == "__main__":
    print("INITIAL STATE:")
    print_board(START)

    solution = astar(START)

    if solution:
        print("\nSOLUTION FOUND!")
        print("Number of moves:", len(solution) - 1)
        print("\nFINAL SOLUTION PATH:\n")

        for step, state in enumerate(solution):
            g = step
            h = manhattan(state)
            f = g + h

            print("Step:", step)
            print_board(state)
            print("G(n) =", g)
            print("H(n) =", h)
            print("F(n) =", f)
            print("-" * 30)
    else:
        print("No solution found.")
