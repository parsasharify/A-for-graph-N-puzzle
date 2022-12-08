# A*-for-graph-N-puzzle

We have a graph G with n vertices and m edges. Each vertex of G, such as v, is labeled with
There a value of 0 ≤ lv < n. At each step, we can match the label with value 0 to one of the labels on the vertex
Move next to it. The goal is to label each vertex v with its own value. That is, v = lv.
Find the least number of possible moves to reach the goal. It is also guaranteed that there is a way for
Reaching the goal (the condition where the label on every vertex with the same vertex number) exists.



For this problem, we use A* algorithm
