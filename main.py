import Vertices
import Vertex
import Dijkstra
import math

positive_infinity = math.inf


def main():
    # Initialising values
    vertices = Vertices.Vertices()

    vertexA = Vertex.Vertex("A", positive_infinity, None, {
        "D": 1,
        "B": 6,
    })
    vertexB = Vertex.Vertex("B", positive_infinity, None, {
        "A": 6,
        "D": 2,
        "E": 2,
        "C": 5
    })
    vertexD = Vertex.Vertex("D", positive_infinity, None, {
        "A": 1,
        "E": 1,
        "B": 2
    })
    vertexE = Vertex.Vertex("E", positive_infinity, None, {
        "D": 1,
        "C": 5,
        "B": 2
    })
    vertexC = Vertex.Vertex("C", positive_infinity, None, {
        "B": 5,
        "E": 5
    })

    vertex0 = Vertex.Vertex("0", positive_infinity, None, {
        "1": 4,
        "7": 8
    })

    vertex1 = Vertex.Vertex("1", positive_infinity, None, {
        "0": 4,
        "7": 11,
        "2": 8,
    })

    vertex7 = Vertex.Vertex("7", positive_infinity, None, {
        "0": 4,
        "1": 11,
        "6": 1,
        "8": 7
    })

    vertex2 = Vertex.Vertex("2", positive_infinity, None, {
        "1": 8,
        "3": 7,
        "8": 2,
        "5": 4
    })

    vertex8 = Vertex.Vertex("8", positive_infinity, None, {
        "7": 1,
        "8": 6,
        "5": 2,
    })

    vertex3 = Vertex.Vertex("3", positive_infinity, None, {
        "2": 7,
        "4": 9,
        "5": 14,
    })

    vertex5 = Vertex.Vertex("5", positive_infinity, None, {
        "2": 4,
        "6": 2,
        "3": 14,
        "4": 10,
    })

    vertex4 = Vertex.Vertex("4", positive_infinity, None, {
        "3": 9,
        "5": 10,
    })

    vertex6 = Vertex.Vertex("6", positive_infinity, None, {
        "1": 8,
        "3": 7,
        "8": 2,
        "5": 4
    })

    vertices.addVertex(vertexA)
    vertices.addVertex(vertexB)
    vertices.addVertex(vertexD)
    vertices.addVertex(vertexE)
    vertices.addVertex(vertexC)

    # vertices.addVertex(vertex0)
    # vertices.addVertex(vertex1)
    # vertices.addVertex(vertex2)
    # vertices.addVertex(vertex3)
    # vertices.addVertex(vertex4)
    # vertices.addVertex(vertex5)
    # vertices.addVertex(vertex6)
    # vertices.addVertex(vertex7)
    # vertices.addVertex(vertex8)

    result = Dijkstra.init(vertices, startV=vertexA, goalV=vertexC)
    resultArr = [result.label]
    while result.previousVertex is not None:
        resultArr.append(result.previousVertex.label)
        result = result.previousVertex

    resultArr.reverse()
    print(resultArr)


main()
