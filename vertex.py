#Name: Jusung Park
#Date: 3/9/22
#Purpose: Create a file that hold vertex class

from cs1lib import *

# Constants
RADIUS_VERTEX = 8
WIDTH_EDGE = 3


class Vertex:
    def __init__(self, name, x, y):
        self.name = str(name) # holds the name
        self.x = int(x)  # holds the x location on the map
        self.y = int(y)  # holds the y location on the map
        self.adjacency_list = []  # a list of references to Vertex objects for its adjacent vertices.

    # getter method for the name
    def get_name(self):
        return self.name

    # method which append adjacency list
    def append_adj_list(self, obj_ref):
        self.adjacency_list.append(obj_ref)

    # getter method for adjacency list
    def get_adjacency_list(self):
        return self.adjacency_list

    def get_x(self):
        return int(self.x)

    def get_y(self):
        return int(self.y)

    def __str__(self):
        neighbor = ""
        for j in self.adjacency_list:
            neighbor = neighbor + " " + j.get_name() + ","
        # return all but last character which is the extra comma
        return (self.name + ";" + " Location: " + str(self.x) + ", " + str(self.y) + "; " + "Adjacent vertices:" + neighbor)[:-1]

    # Return a 4-tuple of the Ball's left, top, right, and bottom
    def get_bounding_box(self):
        return (self.x - RADIUS_VERTEX, self.y - RADIUS_VERTEX, self.x + RADIUS_VERTEX, self.y + RADIUS_VERTEX)

    # draw vertex in a color given by parameters for r, g, and b
    def draw_vertex(self, r, g, b):
        disable_stroke()
        set_fill_color(r, g, b)
        draw_circle(self.x, self.y, RADIUS_VERTEX)

    # draws an edge between the Vertex
    # that the method is called on (i.e., self) and the other vertex
    def draw_edge(self, r, g, b, vertex_another_obj):
        # disable_stroke()
        enable_stroke()
        set_stroke_width(WIDTH_EDGE)
        set_stroke_color(r, g, b)
        draw_line(self.x, self.y, vertex_another_obj.get_x(), vertex_another_obj.get_y())

    # draws all the edges between the vertex and all the vertices in
    # its adjacency list in the color given by r, g, b
    def draw_edge_bt_adj(self, r, g, b):
        disable_stroke()
        for adjacent_vertex in self.adjacency_list:
            self.draw_edge(r, g, b, adjacent_vertex)



