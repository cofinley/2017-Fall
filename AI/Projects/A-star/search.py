from math import sqrt


def search(graph, start, target, excluded):
    print("Heuristic: Straigh line distance:")
    print("Starting city:", start)
    print("Target city:", target)
    # Init visited list
    closed = excluded
    # Init final path
    path = []
    total_distance = 0
    found = False

    # Graph lookup for input strings
    start = graph[start]
    target = graph[target]

    current = start
    open = []

    while not open or not found:
        # open.append(current["name"])

        # Add current to path
        path.append(current["name"])
        print("Current optimal path: ")
        pprint(path)
        print("Distance traveled: {0:.2f}".format(total_distance))

        # Get neighbors of current node, add to open list
        neighbors = current["cons"]
        open += neighbors

        # Remove current from possible moves
        closed.append(current["name"])

        # If target in closed list, means path has been found
        if target["name"] in closed:
            found = True
            break

        # Remove current from open list
        open = [i for i in open if i != current["name"]]

        # Get ready to pick a neighbor
        picked_node = None
        picked_f = 10000
        for choice in open:
            if choice not in closed:
                # Graph lookup for choice
                choice = graph[choice]

                # Calculate distances from start and finish to choice
                g = calc_distance(start["pos"], choice["pos"])
                h = calc_distance(choice["pos"], target["pos"])
                f = g + h

                # Find choice with lowest f value
                if picked_node:
                    if f < picked_f:
                        picked_node = choice
                        picked_f = f
                else:
                    picked_node = choice
                    picked_f = f

        # Pick choice with lowest f value
        current = picked_node

        # Find distance traveled from last node
        last_node_name = path[-1]
        last_node = graph[last_node_name]
        total_distance += calc_distance(last_node["pos"], current["pos"])

    return path


def calc_distance(p1, p2):
    x2 = p2[0]
    x1 = p1[0]
    y2 = p2[1]
    y1 = p1[1]
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def pprint(path):
    print(" -> ".join(path))