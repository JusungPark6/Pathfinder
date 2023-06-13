#Name: Jusung Park
#Date: 3/9/22
#Purpose: Create a file that draws the visualization of the map

from bfs import *
from load_graph import *

#constants
WINDOW_WIDTH = 1012
WINDOW_HEIGHT = 811

#state variable for mouse press
x = 0 # x location of the mouse when pressed
y = 0 # y location of the mouse when pressed

#state variable of mouse being pressed
ever_pressed = False

#initiate start and goal vertex
start_vertex = None
goal_vertex = None

#load image of Darmtouth campus map
img = load_image('dartmouth_map.png')

#create dictionary from the load graph
dictionary_list = load_graph('dartmouth_graph.txt')

def vertice_click(x, y, vertex_object): #function for drawing the rectangle
    (left, top, right, bottom) = vertex_object.get_bounding_box()
    return right >= x and x >= left and bottom >= y and top <= y

def find_start_vertice(x, y): #function for finding the start vertex
    global start_vertex, dictionary_list
    # iterate through the dictionary
    for key in dictionary_list:
        if vertice_click(x, y, dictionary_list[key]):
            # if the mouse is inside the rectangular box, that's the start_vertex
            start_vertex = dictionary_list[key]


# pressing on mouse press for start_vertex
def process_mouse_press(x, y):
    global ever_pressed
    ever_pressed = True
    find_start_vertice(x, y)

def process_mouse_release(x, y): #function for when mouse is released
    global ever_pressed
    ever_pressed = False

def find_goal_vertice(x, y): #function for finding the goal vertex
    global ever_pressed, goal_vertex
    for key in dictionary_list: #for function for going through the dictionary
        if vertice_click(x, y, dictionary_list[key]):
            #if the mouse is inside the rectangular box, that's the start_vertex
            goal_vertex = dictionary_list[key]


# function more mouse move, if mouse is on a vertex, that is the goal vertex
def process_mouse_move(mx, my):
    if start_vertex != None:
        find_goal_vertice(mx, my)


# main function that draws the visualization
def main():
    draw_image(img, 0, 0)
    for key in dictionary_list: #for function to loop over the dictionary
        dictionary_list[key].draw_edge_bt_adj(0, 0, 1)
        dictionary_list[key].draw_vertex(0, 0, 1)
    if start_vertex != None: #if a vertex is clicked on, draw vertex
        start_vertex.draw_vertex(1, 0, 0)
    if goal_vertex != None: #function for if there is a goal vertex
        goal_vertex.draw_vertex(1, 0, 0)
        list_neighbors = bfs(start_vertex, goal_vertex)
        i = 0
        for vertex_list in list_neighbors:
            vertex_list.draw_vertex(1, 0, 0)
            while i < len(list_neighbors)-1:
                vertex_list.draw_edge(1, 0, 0, list_neighbors[i+1])
                vertex_list = list_neighbors[i+1]
                i += 1
start_graphics(main, title="Map of Dartmouth", mouse_move = process_mouse_move, mouse_press = process_mouse_press, mouse_release = process_mouse_release, width=WINDOW_WIDTH , height=WINDOW_HEIGHT, framerate=1)
