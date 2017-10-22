"""
    Connor Finley, Joseph Farmer (Group 5)
    Introduction to A.I.
    Project 1
    A* Search Algorithm
    2017/10/19
"""

import search


def prompt_choice(s):
    """
    Prompt user for binary choice

    Args:
        s (str): prompt string

    Returns:
        string of choice ('a' or 'b')
    """
    choice = input(s).lower()
    while choice != "a" and choice != "b":
        choice = input(s).lower()
    return choice


def read_cons(filename):
    """
    Read file containing graph connections, map to dict

    Args:
        filename (str): filename to parse

    Returns:
        dict of {node_name: [connections]}
    """
    connections = {}
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if "end" not in line.lower():
                line = line.split(" ")
                node_name = line[0].upper()
                cons = [i.strip().upper() for i in line[2:]]
                connections[node_name] = cons
    return connections


def read_locs(filename):
    """
    Read file containing graph locations, map to dict

    Args:
        filename (str): filename to parse

    Returns:
        dict of {node_name: (location)}
    """
    locations = {}
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if "end" not in line.lower():
                line = line.split(" ")
                node_name = line[0].upper()
                pos_x = int(line[1])
                pos_y = int(line[2])
                pos = (pos_x, pos_y)
                locations[node_name] = pos
    return locations


def read_city(endpoint, locations):
    """
    Prompt city until valid city entered

    Args:
        endpoint (str): name of node to match
        locations (dict): {node_name: (location)}

    Returns:
        string of valid city entered by user
    """
    valid = False
    while not valid:
        city = input("Enter {} city: ".format(endpoint)).upper()
        if city in locations:
            valid = True
        else:
            print("Not a valid city, try again.")
        if valid:
            return city


def create_graph(cons, locs):
    """
    Merge connections and locations dict into one

    Args:
        cons (dict): {node_name: [connections]}
        locs (dict): {node_name: (location)}

    Returns:
        dict of {node_name: "name": node_name, "cons": cons, "pos": pos}
    """
    g = {}
    for loc in locs:
        name = loc
        pos = locs[loc]
        connections = cons[loc]
        g[name] = {"name": name, "pos": pos, "cons": connections}
    return g


if __name__ == "__main__":

    # Get and parse connections and locations file
    c_file = str(input("Input path to connections file: "))
    l_file = str(input("Input path to locations file: "))
    cons = read_cons(c_file)
    locs = read_locs(l_file)

    # Merge connections and locations into on graph data structure
    graph = create_graph(cons, locs)

    # Get start and target node names
    start = read_city("start", locs)
    target = read_city("target", locs)

    # Get excluded node names
    excluded = input("Enter excluded cities, separated by comma: ")
    if excluded == "":
        excluded = []
    else:
        excluded = [i.strip() for i in excluded.split(",")]

    # Get verbosity and heuristic info before finally searching
    readout = prompt_choice("Just show end result (a) or go step-by-step (b)? ")
    verbose = readout == "b"
    heuristic = prompt_choice("Heuristic: straight line distance(a) or fewest links(b): ")

    print()
    path = search.search(graph, start, target, excluded, verbose, heuristic)
    print(" -> ".join(path))
    input("\nPress ENTER to exit")
