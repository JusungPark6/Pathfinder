#Name: Jusung Park
#Date: 3/9/22
#Purpose: Create a file that contains the Breath First Search

from vertex import *
from collections import deque


#breadth-first search on a graph
def bfs(start_vertex, goal_vertex):
    q = deque()
    backpointer_dictionary = {} #create a dictionary that holds backpointers
    backpointer_dictionary[start_vertex] = None #initialize backpointers of start_vertex as None
    q.append(start_vertex) #append start vertex in to the deque
    list_of_path = [] #create a list for path
    while len(q) > 0: #while there is still vertex object in the deque
        x = q.popleft() #x is the most recently removed vertex object
        if x == goal_vertex: #if x is the goal vertex
            while x != None: #making the list of path from start to goal vertex
                list_of_path.append(x)
                x = backpointer_dictionary[x]
        else: #if x is not the goal vertex
            for vertex_adjacent in x.get_adjacency_list(): #loop over the adjacency list of x
                if vertex_adjacent not in backpointer_dictionary: #if vertex object in the adjacency list is not in the backpointer dictionary
                    backpointer_dictionary[vertex_adjacent] = x #that vertex object which is adjacent to the x is the key and x is the value
                    q.append(vertex_adjacent) #append the vertex object to the deque
    return list_of_path




