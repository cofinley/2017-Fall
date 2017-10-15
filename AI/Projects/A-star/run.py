from connections import Connection
from locations import Location
from graph import Graph


def prompt_choice(s):
    choice = None
    while choice != "a" or choice != "b":
        choice = input(s)
        if choice == "a" or choice == "b":
            break
    return choice


def read_cons():
    c_file = str(input("Input path to connections file: "))
    connections = {}
    print(c_file)
    with open(c_file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if "end" not in line.lower():
                line = line.split(" ")
                connections[line[0]] = [i.strip() for i in line[2:]]
    return connections


def read_locs():
    l_file = str(input("Input path to locations file: "))
    locations = {} 
    with open(l_file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if "end" not in line.lower():
                line = line.split(" ")
                locations[line[0]] = tuple((int(line[1]), int(line[2].strip())))
    return locations


def map_locations(cons, locs):
    g = Graph()
    for loc in locs:
        node = loc
        pos = locs[loc]
        connections = [cons[c] for c in cons if c == loc][0]
        l = Location(node, pos, connections)
        g.locs.append(l)
    return g


if __name__ == "__main__":
    cons = read_cons()
    locs = read_locs()
    graph = map_locations(cons, locs)
    for loc in graph.locs:
        print(loc.node, loc.pos, loc.cons)
    start = input("Enter start city: ")
    target = input("Enter target city: ")
    excluded = input("Enter excluded cities, separated by comma: ")
    excluded = [i.strip for i in ex.split(",")]
    heuristic = prompt_choice("Heuristic: straight line distance(a) or fewest links(b): ")
    readout = prompt_choice("Just show end result (a) or go step-by-step (b)? ")
