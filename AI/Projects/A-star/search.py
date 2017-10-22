"""
    Connor Finley, Joseph Farmer (Group 5)
    Introduction to A.I.
    Project 1
    A* Search Algorithm
    2017/10/19
"""

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
    print("Target city:", target)
    print("Excluding:", ", ".join(excluded))
    print()

    came_from = {start: None}

    # Create open set mapped to f values
    open = {start: 0}

    g_scores = {start: 0}

    # Graph lookup for input strings
    start_node = graph[start]
    target_node = graph[target]

    while open:

        current = min(open, key=open.get)
        current_node = graph[current]

        open.pop(current)

        # Print out best next move from previous state
        if len(construct_path(came_from, current)) > 0:
            if verbose:
                print("Best move is to", current_node["name"], "\n")
                input("Press ENTER for next step")
                print()

        # Check if end
        is_end = current_node["name"] == target_node["name"]

        # If reached end or verbose flag, print out path and total distance so far
        if verbose or is_end:
            if is_end:
                print("Final path: ", end="")
            else:
                print("Current path: ", end="")
            path = construct_path(came_from, current)
            if heuristic == "a":
                # If straight line distance, use euclidean distance
                total_distance = measure_total_straight_line_distance(graph, path)
            else:
                # If fewest links heuristic, use edge count for distance
                total_distance = len(path) - 1
            print("Distance traveled: {0:.2f}".format(total_distance))
            if is_end:
                return path

        # Loop through the neighbors of the current node
        for choice in current_node["cons"]:
            # Graph lookup for choice
            choice_node = graph[choice]

            if heuristic == "b":
                # Cost is number of moves up to this point plus the next one
                g = g_scores[current] + 1
            else:
                g = find_target_straight_line_distance(start_node["pos"], choice_node["pos"])

            if choice not in g_scores or g < g_scores[choice]:

                g_scores[choice] = g

                if heuristic == "a":
                    h = find_target_straight_line_distance(choice_node["pos"], target_node["pos"])
                else:
                    h = 0

                f = g + h

                # Replace choice's initial f value with real f value
                open[choice] = f
                came_from[choice] = current

    return None


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


def construct_path(came_from, target):
    """
    Construct path from start to target

    Args:
        came_from (dict): linked list of explored connections
        target (str): target node name
    """
    path = [target]
    previous = came_from[target]
    while previous is not None:
        path.append(previous)
        previous = came_from[previous]
    path.reverse()
    return path


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
