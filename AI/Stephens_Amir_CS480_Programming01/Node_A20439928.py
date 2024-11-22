class Node:
    def __init__(self, state:str, path:list, path_cost:int, heuristic_cost:int, reached = None):
        self.state = state
        self.path = path
        self.path_cost = path_cost
        self.heuristic_cost = heuristic_cost
        self.reached = reached
    
    def __lt__(self, other_node):
        return self.heuristic_cost - other_node.heuristic_cost < 0