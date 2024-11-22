from Node_A20439928 import Node 
import heapq

def aStar(initial:str, goal:str, states:dict, distances:dict):
    if goal not in states or initial not in states:
        return None
    current = Node(initial, [initial], 0, 0)
    frontier = list()
    heapq.heappush(frontier, current)
    reached = dict()
    reached[initial] = current
    while frontier != None:
        current = heapq.heappop(frontier)
        if current.state == goal:
            return current
        for cost, state in states[current.state]:
            path_cost = current.path_cost + cost
            if state not in reached or path_cost < reached[state].path_cost:
                heuristic = path_cost + distances[state, goal]
                path = current.path[::] + [state]
                neighbor = Node(state, path, path_cost, heuristic, reached)
                reached[state] = neighbor
                heapq.heappush(frontier, neighbor)
    return None

def greedyBFS(initial:str, goal:str, states:dict, distances:dict):
    if goal not in states or initial not in states:
        return None
    current = Node(initial, [initial], 0, 0)
    frontier = list()
    heapq.heappush(frontier, current)
    reached = dict()
    reached[initial] = current
    while frontier != None:
        current = heapq.heappop(frontier)
        if current.state == goal:
            return current
        for cost, state in states[current.state]:
            path_cost = current.path_cost + cost
            if state not in reached or path_cost < reached[state].path_cost:
                straight_line = distances[state, goal]
                path = current.path[::] + [state]
                neighbor = Node(state, path, path_cost, straight_line, reached)
                reached[state] = neighbor
                heapq.heappush(frontier, neighbor)
    return None