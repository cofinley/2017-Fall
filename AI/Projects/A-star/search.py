from math import sqrt


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

        if current == target:
            print("Final path:")
            pprint(path)
            if verbose:
                total_distance = measure_total_distance(graph, path)
                print("Distance traveled: {0:.2f}".format(total_distance))
            return path

        if verbose:
            print("Current optimal path: ")
            pprint(path)
            total_distance = measure_total_distance(graph, path)
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
                    g = calc_distance(start["pos"], choice["pos"])
                    h = calc_distance(choice["pos"], target["pos"])
                else:
                    # Fewest moves heuristic
                    g = len(path)
                    h = 0
                f = g + h
                open[choice["name"]] = f

    return None


def search_shortest(graph, start, target, excluded, verbose, path=[]):
    path = path + [start]
    if start == target:
        return path
    if start not in graph:
        return None
    shortest_path = None
    for connection in graph[start]["cons"]:
        if connection not in path:
            new_path = search_shortest(graph, connection, target, excluded, verbose, path)
            if new_path:
                if not shortest_path or len(new_path) < len(shortest_path):
                    shortest_path = new_path
    return shortest_path


def calc_distance(p1, p2):
    x2 = p2[0]
    x1 = p1[0]
    y2 = p2[1]
    y1 = p1[1]
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def pprint(path):
    print(" -> ".join(path))


def measure_total_distance(graph, path):
    total_distance = 0
    for i, step in enumerate(path):
        node = graph[step]
        if i != 0:
            prev = path[i-1]
            prev_node = graph[prev]
            total_distance += calc_distance(prev_node["pos"], node["pos"])

    return total_distance
