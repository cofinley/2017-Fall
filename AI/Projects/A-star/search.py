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
        final path (a linked list of node names) if one found, else None
    """

    if heuristic == "a":
        print("Heuristic: Straight line distance:")
    else:
        print("Heuristic: Fewest Links:")
    print("Starting city:", start)
    print("Target city:", target)
    print("Excluding:", ", ".join(excluded))
    print()

    # Create reversed linked list/map for each graph edge chosen
    path_links = {start: None}

    # Create open set mapped to f values
    open = {start: 0}

    # Create closed set in form of g_scores, add excluded
    g_scores = {i: 0 for i in excluded}
    g_scores[start] = 0

    start_node = graph[start]
    target_node = graph[target]

    while open:

        # Select node with lowest f value as current
        current = min(open, key=open.get)
        current_node = graph[current]

        open.pop(current)

        # Print out best next move from previous state
        if verbose and len(construct_path(path_links, current)) > 0:
            previous = path_links[current_node["name"]]
            print("Best move is from {} to {}".format(previous, current))
            input("Press ENTER for next step")
            print()

        is_end = current_node["name"] == target_node["name"]

        # If reached end or verbose flag, print out path and total distance so far
        if verbose or is_end:

            if is_end:
                print("Final path: ", end="")
            else:
                print("Current path: ", end="")
            path = construct_path(path_links, current)
            print(" -> ".join(path))

            if heuristic == "a":
                # If straight line distance, use euclidean distance
                total_distance = measure_total_straight_line_distance(graph, path)
            else:
                # If fewest links heuristic, use edge count for distance
                total_distance = len(path) - 1
            print("Distance traveled: {0:.2f}".format(total_distance))

            if is_end:
                return path

        for choice in current_node["cons"]:

            choice_node = graph[choice]

            if heuristic == "a":
                # G cost is straight-line distance from start to choice
                g = find_target_straight_line_distance(start_node["pos"], choice_node["pos"])
            else:
                # G cost is number of moves up to this point plus the next one
                g = g_scores[current] + 1

            if choice not in g_scores or g < g_scores[choice]:

                # Only consider choices not visited before or with better costs than before

                g_scores[choice] = g

                if heuristic == "a":
                    h = find_target_straight_line_distance(choice_node["pos"], target_node["pos"])
                else:
                    # For fewest links, only consider g cost
                    h = 0

                f = g + h

                # Update f values and path links for choices
                open[choice] = f
                path_links[choice] = current

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


def construct_path(path_links, target):
    """
    Construct path from start to target

    Args:
        path_links (dict): linked list of explored connections
        target (str): target node name
    """
    path = [target]
    previous = path_links[target]
    while previous is not None:
        path.append(previous)
        previous = path_links[previous]
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
