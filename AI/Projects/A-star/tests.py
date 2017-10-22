"""
    Connor Finley, Joseph Farmer (Group 5)
    Introduction to A.I.
    Project 1
    A* Search Algorithm
    2017/10/19
"""

import run
import search


if __name__ == "__main__":
    cons = run.read_cons("c.txt")
    locs = run.read_locs("l.txt")
    graph = run.create_graph(cons, locs)
    start = "G1"
    target = "C2"
    excluded = []
    verbose = False
    # Straight-line = a, fewest links = b
    heuristic = "b"
    path = search.search(graph, start, target, excluded, verbose, heuristic)
