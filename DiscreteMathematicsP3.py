#--------IMPORTS--------
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd

#Functions

def displayMenu(menuItems):

    #Getting all keys from the menu array
    options=menuItems.keys()
    print("\nChoose one of the options:")
    print("--------------------------------------------------------")
    #for cicle to print all menu array options with the respective entries(1,2,-1)
    for entry in options:
        print(entry, menuItems[entry])


def colored(r, g, b, text):

    """
    This function will colored the print message with the pretended color.
    The objetive of it is to define the type of printed message (SUCCESS, ERROR, WARNING, etc.).
    """

    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

def createGraphic(G,pos):    
                      
    fig,ax = plt.subplots()
    labels = nx.get_edge_attributes(G,"weight")
    
    plt.figure(1)
    #Draw the Graph g with Matplotlib
    nx.draw(G, ax=ax, pos=pos,node_color="lightblue", with_labels=True, arrowstyle="-")
    nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)

    #Set title, change color and localization
    ax.set_title("Figure 1 - Graph Theory", color="lightslategray", y=-0.1 )

    plt.show(block=False)

def showGraphInfo(G):    
    #Get general information
    print(nx.info(G))

    #Calculate average degree of the graph
    #Creation of degrees array
    degrees = []

    #Appending the sum of all nodes degree of the graph
    for i in G.nodes:
        degrees.append(G.degree(i))

    #Calculating the average degree - division of the sum with the number of nodes
    avg = sum(degrees) / len(G.nodes)
    print("Average degree of the graph: ", round(avg,2))

    #Calculate the density of the graph
    density = nx.density(G)
    print("Density of the graph: ", round(density,2))

    #Compute planarity
    planarity,_ = nx.check_planarity(G)
    print("Planarity: ", planarity)

    #Compute Adjacency Matrix
    adjacencyMatrix = nx.adjacency_matrix(G)
    print("Adjacency matrix below:\n\n",adjacencyMatrix.todense())
       
    plt.show()

def showShortedPath(G,source,target):
    pos = {0:(0,0), 1:(0.1,-0.8), 2:(0.6,-1.3), 3:(1,-1.5), 4:(1.5,-1.4), 5:(2,-1.2),
            6:(2.3,-0.7), 7:(2.3,0.1), 8:(2,0.6), 9:(1.5,1), 10:(1,1.1), 11:(0.6,0.9), 12:(0.2,0.5)}
    plt.figure(1)
    #Find shortest path    
    shortestPath = nx.shortest_path(G,source,target)
    print(shortestPath)
    path_edges = zip(shortestPath, shortestPath[1:])
    nx.draw_networkx_edges(G,pos,edgelist=list(path_edges),edge_color="r")
    plt.show()

#Creation of the 'menu' arrays
"""
menu = {}
menu['1']="Part I - Graph Theory"
menu['2']="Part II - Data and Statistics"
menu['-1']="Exit"
"""

while True:
    menu=np.array(["Part I - Graph Theory", "Part II - Data and Statistics", "Exit"])

    displayMenu(menu)

    #Save user selected option in variable 'chosen'
    chosen=input("\nPlease, select the part: ")

    """
    If the user's input is 1 or 2 it will goes to the respective part.
    Otherwise when the input is -1 it will exit from the application.
    An different input of those 3 mentioned above a error message will be displayed
    """

    #Part 1 - Graph Theory
    if chosen == '1':
        print("\nPart I- Graph Theory")
        print("--------------------------------------------------------")
        while True:
            try:
                G = nx.DiGraph()
                G.add_weighted_edges_from([
                    (0,1,10), (1,4,5), (1,12,5), (2,12,2), (2,7,1), (2,6,4), (2,5,6), (3,10,0), (3,6,0),
                    (4,8,10), (4,7,8), (4,5,2), (5,12,1), (6,10,3), (7,8,7), (8,12,9), (8,10,1),
                    (9,10,5), (10,11,2), (11,12,6)
                ])
                pos={0:(0,0), 1:(0.1,-0.8), 2:(0.6,-1.3), 3:(1,-1.5), 4:(1.5,-1.4), 5:(2,-1.2),
                     6:(2.3,-0.7), 7:(2.3,0.1), 8:(2,0.6), 9:(1.5,1), 10:(1,1.1), 11:(0.6,0.9), 12:(0.2,0.5)}
                #Call the funcion that create the graphic G with respective weighted edges and position
                createGraphic(G,pos)
                showGraphInfo(G)
                """
                source = int(input("Source Node: "))
                target = int(input("Target Node: "))
                showShortedPath(G,source,target)
                """

            except ValueError:
                print("shit")
            else:
                break
    #Part 2 - Data and Statistics
    elif chosen == '-1':
        break
    else:
        print("Invalid selected option.")
        print()
