#--------IMPORTS--------
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd

#Functions
def createGraph():
    G = nx.DiGraph()
    G.add_weighted_edges_from([
        (0,1,10), (1,4,5), (1,12,5), (2,12,2), (2,7,1), (2,6,4), (2,5,6), (3,10,0), (3,6,0),
        (4,8,10), (4,7,8), (4,5,2), (5,12,1), (6,10,3), (7,8,7), (8,12,9), (8,10,1),
        (9,10,5), (10,11,2), (11,12,6)
    ])
    fig,ax = plt.subplots()
    pos = {0:(0,0), 1:(0.1,-0.8), 2:(1,-1), 3:(1.5,-1.3), 4:(2,-1.2), 5:(2.5,-0.8),
            6:(3,-0.4), 7:(3,0.2), 8:(2.5,0.8), 9:(2.2,1.2), 10:(1.5,1.3), 11:(1.2,1), 12:(1,0.5)}
    labels = nx.get_edge_attributes(G,"weight")
    nx.draw(G, ax=ax, pos=pos, with_labels=True, arrowstyle="-")
    nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
    ax.set_title("Figure 1 - Graph Theory")
    plt.show()

#Creation of the 'menu' array
menu = {}

menu['1']="Part I - Graph Theory"
menu['2']="Part II - Data and Statistics"
menu['-1']="Exit"

while True:
    #Getting all keys from the menu array
    options=menu.keys()
    print("\nChoose on of the options:")
    print("--------------------------------------------------------")
    #for cicle to print all menu array options with the respective entries(1,2,-1)
    for entry in options:
        print(entry, menu[entry])

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
                createGraph()                
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
