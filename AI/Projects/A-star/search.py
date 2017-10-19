from math import sqrt


def search(graph, start, target, excluded, verbose, heuristic):
    """
    Find path through graph from start to target, avoiding nodes in excluded.
    Pick best path based on given heuristic.

    Args:
        graph (dict): {node_name: "name": node_name, "cons": cons, "pos": pos}
        start (str): start node name
        target (str): target node name
        excluded (list): names of nodes to avoid
        verbose (bool): whether to print out steps or not
        heuristic (str): Straight-line distance = a, fewest links = b

    Returns:
        final path (as list of node names) if one found, else None
    """

    if heuristic == "a":
        print("Heuristic: Straight line distance:")
    else:
        print("Heuristic: Fewest Links:")
    print("Starting city:", start)
    print("Target city:", target, "\n")

    # Init visited list, include excluded
    closed = [] + excluded

    # Init final path
    path = []

    # Create open set mapped to f values
    open = {start: 0}

    # Graph lookup for input strings
    start_node = graph[start]
    target_node = graph[target]

    while open:

        # Pick choice in open list which minimizes f value
        lowest_f = min(open, key=open.get)
        current_node = graph[lowest_f]

        # Print out best next move from previous state
        if len(path) > 0:
            if verbose:
                print("Best move is to", current_node["name"], "\n")
                input("Press ENTER for next step")
                print()

        # Add current_node to path
        path.append(current_node["name"])

        # Check if end
        is_end = current_node["name"] == target_node["name"]

        # If reached end or verbose flag, print out path and total distance so far
        if verbose or is_end:
            if is_end:
                print("Final path:")
            else:
                print("Current path: ", end="")
            pprint(path)
            if heuristic == "a":
                # If straight line distance, use euclidean distance
                total_distance = measure_total_straight_line_distance(graph, path)
            else:
                # If fewest links heuristic, use edge count for distance
                total_distance = len(path) - 1
            print("Distance traveled: {0:.2f}".format(total_distance))
            if is_end:
                return path

        # Remove current_node from possible moves
        open.pop(current_node["name"])
        closed.append(current_node["name"])

        # Loop through the neighbors of the current node
        neighbors = current_node["cons"]
        for choice in neighbors:
            if choice not in closed:

                # Init choice's f value
                open[choice] = 0

                # Graph lookup for choice
                choice_node = graph[choice]

                if heuristic == "a":
                    # Straight-line distance heuristic
                    # Calculate distances from start and finish to choice
                    g = find_target_straight_line_distance(start_node["pos"], choice_node["pos"])
                    h = find_target_straight_line_distance(choice_node["pos"], target_node["pos"])
                else:
                    # Fewest links heuristic
                    g = len(path)
                    # Use BFS for h value
                    h = len(find_target_edge_distance(graph, choice_node["name"], target_node["name"], excluded))
                f = g + h

                # Replace choice's initial f value with real f value
                open[choice] = f

    return None


def find_target_edge_distance(graph, start, target, excluded, path=[]):
    """
    Distance to target using BFS

    Args:
        graph (dict): {node_name: "name": node_name, "cons": cons, "pos": pos}
        start (str): start node name
        target (str): target node name
        excluded (list): names of nodes to avoid
        path (list): node names visited

    Returns:
        the shortest possible amount of edges (links) from the starting node to the target node, avoiding those excluded

    """
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
    """
    Distance to target using euclidean distance

    Args:
        p1 (tuple): point 1
        p2 (tuple): point 2

    Returns:
        the euclidean distance between both points
    """
    x2 = p2[0]
    x1 = p1[0]
    y2 = p2[1]
    y1 = p1[1]
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def pprint(path):
    """
    Pretty print path (a -> b -> c -> etc.)

    Args:
        path (list): node names visited
    """
    print(" -> ".join(path))


def measure_total_straight_line_distance(graph, path):
    """
    Reconstruct path and find total distance

    Args:
        graph (dict): {node_name: "name": node_name, "cons": cons, "pos": pos}
        path (list): node names visited

    Returns:
        the euclidean distance from start to end of path
    """

    total_distance = 0
    for i, step in enumerate(path):
        node = graph[step]
        if i != 0:
            prev = path[i-1]
            prev_node = graph[prev]
            total_distance += find_target_straight_line_distance(prev_node["pos"], node["pos"])

    return total_distance
