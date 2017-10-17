import run
import search

if __name__ == "__main__":
    cons = run.read_cons("c.txt")
    locs = run.read_locs("l.txt")
    graph = run.create_graph(cons, locs)
    start = "D4"
    target = "G5"
    excluded = []
    verbose = False
    heuristic = "b"
    print()
    search.search(graph, start, target, excluded, verbose, heuristic)
