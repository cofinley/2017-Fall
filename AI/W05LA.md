# AI

> 2017/09/19
>
> Week 05, Lecture A

## Search in Game Playing

- MINIMAX
    - P1 selects move to maximize utility value of terminal state
        - Utility value determined by game state evaluation function 
        - If you have the time/resources, you can evaluate utility value multiple levels of state/actions ahead in time 
            - E.g. calculate all possible moves and outcomes
    - P2 selects move that minimizes utility value of terminal state for P1
- Insert tree view with each level labeled for P1/P2
- Pruning
    - Not all tree leaves/terminal states need to be eval'd
        - If all util values of the leaves of a node (node 1) can be beaten by another node's (node 2) leaves, then node 1 can be discarded or *pruned*

---

- Study and do the cannibal/missionary problem
    - Understand alternatives, selection, decision tree
    - Will be on quiz
- Quiz could be sep 26.
    - 3 or 4 questions in-class
    - Some online    