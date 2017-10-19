from math import sqrt
from random import randint


def search(graph, start, target, excluded, verbose, heuristic):
    if heuristic == "a":
        print("Heuristic: Straight line distance:")
    else:
        print("Heuristic: Fewest Links:")
    print("Starting city:", start)
    print("Target city:", target)

    # Init visited list
    closed = excluded

    # Init final path
    path = []

    # Create open set mapped to f values
    open = {start: 0}

    # Graph lookup for input strings
    start = graph[start]
    target = graph[target]

    current = start

    while open:

        # Pick move which minimizes f value
        current = min(open, key=open.get)
        current = graph[current]

        # Add current to path
        path.append(current["name"])

        # Check if end
        if current == target:
            print("Final path:")
            pprint(path)
            if verbose:
                if heuristic == "a":
                    total_distance = measure_total_distance(graph, path)
                else:
                    total_distance = len(path) - 1
                print("Distance traveled: {0:.2f}".format(total_distance))
            return path

        # Print path and current distance
        if verbose:
            print("Current optimal path: ")
            pprint(path)
            if heuristic == "a":
                total_distance = measure_total_distance(graph, path)
            else:
                # If fewest links heuristic, use edge count for distance
                total_distance = len(path) - 1
            print("Distance traveled: {0:.2f}".format(total_distance))

        # Remove current from possible moves
        open.pop(current["name"])
        closed.append(current["name"])

        # Get neighbors of current node
        neighbors = current["cons"]
        for choice in neighbors:
            if choice not in closed:
                open[choice] = 0
                # Graph lookup for choice
                choice = graph[choice]

                if heuristic == "a":
                    # Straight-line distance heuristic
                    # Calculate distances from start and finish to choice
                    g = find_target_straight_line_distance(start["pos"], choice["pos"])
                    h = find_target_straight_line_distance(choice["pos"], target["pos"])
                else:
                    # Fewest moves heuristic
                    g = len(path)
                    # Use bfs for h value
                    h = len(find_target_edge_distance(graph, choice["name"], target["name"], excluded))
                f = g + h
                open[choice["name"]] = f

    return None


def find_target_edge_distance(graph, start, target, excluded, path=[]):
    # Distance to target using BFS
    path = path + [start]
    if start == target:
        return path
    if start not in graph:
        return None
    shortest_path = None
    for connection in graph[start]["cons"]:
        if connection not in path:
            new_path = find_target_edge_distance(graph, connection, target, excluded, path)
            if new_path:
                if not shortest_path or len(new_path) < len(shortest_path):
                    shortest_path = new_path
    return shortest_path


def find_target_straight_line_distance(p1, p2):
    # Distance to target using euclidian distance
    x2 = p2[0]
    x1 = p1[0]
    y2 = p2[1]
    y1 = p1[1]
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def pprint(path):
    print(" -> ".join(path))


def measure_total_distance(graph, path):
    # Reconstruct path and find total distance
    total_distance = 0
    for i, step in enumerate(path):
        node = graph[step]
        if i != 0:
            prev = path[i-1]
            prev_node = graph[prev]
            total_distance += find_target_straight_line_distance(prev_node["pos"], node["pos"])

    return total_distance
