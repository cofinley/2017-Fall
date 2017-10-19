import run
import search

if __name__ == "__main__":
    cons = run.read_cons("c.txt")
    locs = run.read_locs("l.txt")
    graph = run.create_graph(cons, locs)
    start = "A1"
    target = "C3"
    excluded = []
    verbose = False
    # Straight-line = a, fewest links = b
    heuristic = "b"
    search.search(graph, start, target, excluded, verbose, heuristic)
