from search import search


def prompt_choice(s):
    choice = None
    while choice != "a" or choice != "b":
        choice = input(s)
        if choice == "a" or choice == "b":
            break
    return choice


def read_cons(filename):
    connections = {}
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if "end" not in line.lower():
                line = line.split(" ")
                node = line[0]
                cons = [i.strip() for i in line[2:]]
                connections[node] = cons
    return connections


def read_locs(filename):
    locations = {}
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if "end" not in line.lower():
                line = line.split(" ")
                node = line[0]
                pos_x = int(line[1])
                pos_y = int(line[2])
                pos = (pos_x, pos_y)
                locations[node] = pos
    return locations


def read_city(endpoint, locations):
    valid = False
    while not valid:
        city = input("Enter {} city: ".format(endpoint))
        if city in locations:
            valid = True
        else:
            print("Not a valid city, try again.")
        if valid:
            return city


def create_graph(cons, locs):
    g = {}
    for loc in locs:
        name = loc
        pos = locs[loc]
        connections = cons[loc]
        g[name] = {"name": name, "pos": pos, "cons": connections}
    return g


def pprint(path):
    print(" -> ".join(path))

if __name__ == "__main__":
    c_file = str(input("Input path to connections file: "))
    l_file = str(input("Input path to locations file: "))
    cons = read_cons(c_file)
    locs = read_locs(l_file)
    graph = create_graph(cons, locs)
    start = read_city("start", locs)
    target = read_city("target", locs)
    excluded = input("Enter excluded cities, separated by comma: ")
    if excluded == "":
        excluded = []
    else:
        excluded = [i.strip() for i in excluded.split(",")]
    readout = prompt_choice("Just show end result (a) or go step-by-step (b)? ")
    verbose = readout == "b"
    heuristic = prompt_choice("Heuristic: straight line distance(a) or fewest links(b): ")
    print()
    search(graph, start, target, excluded, verbose, heuristic)
