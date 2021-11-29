from typing import Dict, Union

from Vertex import Vertex


def updateVertex(vertex, cost, currentVertex):
    calculated_cost = cost + currentVertex.cost
    if vertex.cost < calculated_cost:
        return

    vertex.cost = calculated_cost
    vertex.previousVertex = currentVertex


class Vertices:
    def __init__(self):
        self.unexplored_v: Dict[str, Vertex] = {}
        self.explored_v: Dict[str, Vertex] = {}

    def addVertex(self, v):
        self.unexplored_v[v.label] = v

    def exploreVertex(self, v):
        self.explored_v[v.label] = v
        self.unexplored_v.pop(v.label)

