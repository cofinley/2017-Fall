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
    start = "D4"
    target = "G5"
    excluded = []
    verbose = True
    # Straight-line = a, fewest links = b
    heuristic = "a"
    path = search.search(graph, start, target, excluded, verbose, heuristic)
