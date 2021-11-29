from typing import Dict, Union


class Vertex:
    def __init__(
            self,
            label: str,
            cost: Union[int, float],
            previousVertex: Union[object, None],
            neighbours: Dict[str, int]
    ):
        self.label = label
        self.cost = cost
        self.previousVertex = previousVertex
        self.neighbours = neighbours
