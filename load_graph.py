#Name: Jusung Park
#Date: 3/9/22
#Purpose: Create a file that contains load_graph which create one Vertex object per line in the data file and add to a dictionary a reference to each Vertex object it creates.

from vertex import *


def load_graph(file_name):
    in_file = open(file_name, 'r')
    dictionary = {} #create a dictionary
    #first pass, create all vertex objects, storing the coordinate in the objects, and  creates the dictionary. mapping vertex names to references to Vertex objects
    for line in in_file:
        line = line.strip() #strip line of blank spaces and split them by ';"
        line = line.split(';')
        location = line[2] #line[2] has information of the x and y location
        location = location.strip() #strip line[2] of blank spaces and split them by commas
        location = location.split(',')
        vertex = Vertex(line[0], location[0].strip(), location[1].strip()) #create a vertex object which passes in the name, the x and y location
        dictionary[vertex.get_name()] = vertex #creating the dictionary, key to the dictionary is name of the vertices and the value is Vertex references
    in_file.close()
    #second pass, creates the adjacency list in the vertex objects
    in_file = open(file_name, 'r')
    for line in in_file:
        line = line.strip() #strip line of blank spaces and split them by ';"
        line = line.split(';')
        adjacent = line[1] #adjacent holds string for the adjacency vertices
        adjacent = adjacent.strip() #strip adjacent and split the string by ","
        adjacent = adjacent.split(",")
        for i in adjacent: #go through the adjacent which holds the information about adjacency vertices and append the adjacency list
            i = i.strip()
            dictionary[line[0]].append_adj_list(dictionary[i]) #adjacency list is being appended to the value of the dictionary at the key
    in_file.close()
    return dictionary #return the reference to the dictionary, which will have information about all vertices