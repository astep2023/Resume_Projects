'''
Amir Stephens, A20439928.
'''
import sys
import csv
import timeit
from Node_A20439928 import Node 
from search_algorithms_A20439928 import greedyBFS, aStar

if __name__ == "__main__":
    distances = dict()
    states = dict()
    '''
    This section is for filling out our search space and where the states are and cost values to travel to n from those states.
    '''
    reader = csv.reader(open("straightline.csv"))
    state_names = next(reader)
    for row in reader:
        for i in range(1, len(row)):
            distances[(row[0], state_names[i])] = int(row[i])

    reader = csv.reader(open("driving.csv"))
    state_names = next(reader)
    for row in reader:
        neighbors = list()
        for i in range(1, len(row)):
            if int(row[i]) > 0:
                neighbors.append((int(row[i]), state_names[i]))
        states[row[0]] = neighbors

    '''
    This is where the built of the work is done. With the algorithms in their own file "search_algorithms_A20439928". 
    '''
    if len(sys.argv) == 3:
        start = timeit.timeit()
        goal_node = greedyBFS(sys.argv[1], sys.argv[2], states, distances)
        timeEnd = timeit.timeit() - start 

        print("Stephens, Amir, A20439928 solution:")
        print("Initial state: %s." % str(sys.argv[1]))
        print("Goal state: %s." % str(sys.argv[2]))
        if goal_node:
            print("Greedy Best First Search:")
            print("Solution path: %s." % goal_node.path)
            print("Number of states on path: %d." % (len(goal_node.path)))
            print("Number of nodes expanded: %d." % (len(goal_node.reached)))
            print("Path cost: %d." % goal_node.path_cost)
            print("Execution time: %f seconds." % timeEnd)
        else:
            print("Greedy Best First Search:")
            print("Solution path: FAILURE: NO PATH FOUND.")
            print("Number of states on a path: 0.")
            print("Number of nodes expanded: 0.")
            print("Path cost: 0.")
            print("Execution time: %f seconds." % timeEnd)
        print("\n")
        
        start = timeit.timeit()
        goal_node = aStar(sys.argv[1], sys.argv[2], states, distances)
        timeEnd = timeit.timeit() - start 

        if goal_node:
            print("A* Search:")
            print("Solution path: %s." % goal_node.path)
            print("Number of states on path: %d." % (len(goal_node.path)))
            print("Number of nodes expanded: %d." % (len(goal_node.reached)))
            print("Path cost: %d." % goal_node.path_cost)
            print("Execution time: %f seconds." % timeEnd)
        else:
            print("A* Search:")
            print("Solution path: FAILURE: NO PATH FOUND.")
            print("Number of states on a path: 0.")
            print("Number of nodes expanded: 0.")
            print("Path cost: 0.")
            print("Execution time: %f seconds." % timeEnd)
    else:
        print("ERROR: Not enough or too many input arguments.")