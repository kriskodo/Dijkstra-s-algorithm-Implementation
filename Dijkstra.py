# Finds the shortest path between two vertices
import math

import Vertices


def init(vertices, startV, goalV):
    currentVertexLabel = startV.label
    startV.cost = 0

    if startV == goalV:
        return vertices.unexplored_v[currentVertexLabel]

    while len(vertices.unexplored_v) > 0:
        currentVertex = vertices.unexplored_v[currentVertexLabel]

        for key in currentVertex.neighbours:
            if key in vertices.explored_v:
                currentVertex.neighbours[key] = math.inf
                continue

            Vertices.updateVertex(vertices.unexplored_v[key], currentVertex.neighbours[key], currentVertex)

        vertices.exploreVertex(currentVertex)

        if len(vertices.unexplored_v) == 0:
            return vertices.explored_v[goalV.label]

        currentVertexLabel = sorted(vertices.unexplored_v.items(), key=lambda x: x[1].cost)[0][1].label

