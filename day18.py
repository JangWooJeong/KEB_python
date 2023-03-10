# BFS
from collections import deque


class Graph:
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for x in range(size)] for x in range(size)]


def BFS(g):
    queue = deque([])
    visited_array = []

    for i in range(g1.SIZE):
        for j in range(g1.SIZE):
            print(g1.graph[i][j], end=' ')
        print()

    start = 0
    queue.append(start)
    visited_array.append(start)

    while queue:
        current = queue.popleft()
        for vertex in range(g.SIZE):
            if g.graph[current][vertex] == 1 and vertex not in visited_array:
                queue.append(vertex)
                visited_array.append(vertex)

    for i in visited_array:
        print(chr(ord('A')+i), end=' -> ')
    print("END")


g = None

A, B, C, D, E, F, G, H, I = 0, 1, 2, 3, 4, 5, 6, 7, 8

g1 = Graph(9)
g1.graph[A][B] = 1; g1.graph[A][C] = 1; g1.graph[A][E] = 1
g1.graph[B][A] = 1; g1.graph[B][C] = 1; g1.graph[B][D] = 1
g1.graph[C][A] = 1; g1.graph[C][B] = 1; g1.graph[C][D] = 1; g1.graph[C][E] = 1; g1.graph[C][F] = 1
g1.graph[D][B] = 1; g1.graph[D][C] = 1
g1.graph[E][A] = 1; g1.graph[E][C] = 1; g1.graph[E][G] = 1; g1.graph[E][H] = 1
g1.graph[F][C] = 1
g1.graph[G][E] = 1; g1.graph[G][I] = 1
g1.graph[H][E] = 1; g1.graph[H][I] = 1
g1.graph[I][G] = 1; g1.graph[I][H] = 1

g2 = Graph(4)
g2.graph[A][C] = 1; g2.graph[A][D] = 1
g2.graph[B][C] = 1
g2.graph[C][A] = 1; g2.graph[C][B] = 1; g2.graph[C][D] = 1
g2.graph[D][A] = 1; g2.graph[C][B] = 1


BFS(g1)
BFS(g2)
