#--------IMPORTS--------
import os
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import networkx as nx
import pandas as pd
import seaborn as sns
import webbrowser


#Functions

"""
    GLOBAL FUNCTIONS
"""

clear = lambda:os.system("clear")

"""
This function will colored the print message with the pretended color.
The objetive of it is to define the type of printed message (SUCCESS, ERROR, WARNING, etc.).
"""
def colored(r, g, b, text):

    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

"""
    PART I FUNCTIONS
"""

#printMenu function like the name says just print all the menus that we need cross the program.
def printMenu():

    #Getting all keys from the menu array
    #for cicle to print all menu array options with the respective entries(1,2,-1)
    for key in menuOptions.keys():
        print (key, '-', menuOptions[key] )
    return menuOptions.keys()

#Draw the G graphic(define labels,colors and title)
def drawG():
    fig,ax = plt.subplots()
    labels = nx.get_edge_attributes(G,"weight")

    #Draw the Graph g with Matplotlib
    nx.draw(G, ax=ax, pos=pos,node_color="lightblue", with_labels=True, arrowstyle="-")
    nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)

    #Set title, change color and localization
    ax.set_title("Figure 1 - Graph Theory", color="lightslategray", y=-0.1 )

#Shows useful G graphic information
def showGraphInfo():    
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

#Draw the shorted path from valid nodes
def showShortedPath():

    #Find shortest path    
    shortestPath = nx.shortest_path(G,source,target)
    print(shortestPath)
    path_edges = zip(shortestPath, shortestPath[1:])
    drawG()
    nx.draw_networkx_edges(G,pos,edgelist=list(path_edges),edge_color="r")

#Change weight or add edges to the G Graphic
def changeWeightedEdges():
    G.add_weighted_edges_from(weighted_edges)
    drawG()

    nx.draw_networkx_edges(G,pos,edgelist=weighted_edges,edge_color="springgreen", arrowstyle="-")      

"""
    PART II FUNCTIONS
"""

def buildCpPlot():
    """
    Set plot maker color depending on chest pain value 
        0-green
        1-yellow
        2-orange
        3-red
    """
    for i in chest__pain:
        if i == 0:
            color.append("#06FF00")
        if i == 1:
            color.append("#FFE400")
        if i == 2:
            color.append("#FF8E00")
        if i == 3:
            color.append("#FF1700")

    # Set plot figure window size
    plt.figure(figsize=(16,3))

    # Set the exat number values to x(Patient Ages) and y(Chest Pain type) axis
    plt.xticks(patient_age)
    plt.yticks(chest__pain)

    # scatter(x,y,marker_color)
    plt.scatter(patient_age,chest__pain, c=color)                       

def buildFactPlots():
    fig, axs = plt.subplots(2,2)
    # plot window size
    plt.gcf().set_size_inches(3*plt.gcf().get_size_inches())
    
    # plot 1 (Pie) - Heart Disease
    axs[0,0].set_title("Heart Disease")
    df_target = df.groupby("target").size()
    axs[0,0].pie(df_target.values, autopct = '%1.1f%%', radius=1.1, textprops={"fontsize":12})
    labels=["No heart disease","With heart disease"]
    axs[0,0].legend(labels,loc="lower left")
    labels=["Female Withoud HD", "Female With HD", "Male Without HD", "Male With HD"]

    # plot 2 (Pie) - Heart Disease per Gender
    axs[0,1].set_title("Heart Disease per Gender")
    df_sex = df.groupby(["sex","target"]).size()
    axs[0,1].pie(df_sex.values,  autopct='%1.1f%%', radius=1.1, textprops={"fontsize":12})
    axs[0,1].legend(labels,loc="lower left")

    # plot 3 (Bar) - Heart Disease per Gender
    axs[1,0].set_title("Cholestrol levels per age")
    axs[1,0].set_xlabel("Age")
    axs[1,0].set_ylabel("Chol")
    axs[1,0].bar(df.age, df.chol)
    
    # plot 3 (Heatmap) - Pairwise Correlation of all columns
    axs[1,1].set_title("Pairwise Correlation of all columns")
    sns.heatmap(df.corr(),ax=axs[1,1],annot=True,cmap="magma",fmt='.2f')
   
while True:

    #Creation of the main 'menu' arrays
    menuOptions = {
    1: 'Part I - Graph Theory',
    2: 'Part II - The Heart Disease UCI .csv file',
    -1: 'Exit'
    }

    print("\nMain Menu")
    print("--------------------------------------------------------")

    printMenu()

    #Save user selected option in variable 'chosen'
    
    chosen=input("\nPlease, select the part: ")

    """
    If the user's input is 1 or 2 it will goes to the respective part.
    Otherwise when the input is -1 it will exit from the application.
    An different input of those 3 mentioned above a error message will be displayed
    """

    #Part 1 - Graph Theory
    if chosen == '1':
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
                #Menu inside part 1
                menuOptions = {
                'a': 'Display graphic',
                'b': 'Show graphic information',
                'c': 'Shorted path of introduced nodes',
                'd': 'Update weight and add edges',
                'e': 'Back to the main menu'
                }
                
                while True:
                    print("\nPart I- Graph Theory")
                    print("--------------------------------------------------------")     

                    printMenu()
                    chosen=input("\nSelect an option: ")

                    if(chosen == 'a'):
                        clear()
                        #Call the funcion that draw the graphic G with respective weighted edges and positions, and show the G graphic
                        drawG()
                        plt.show()
                    elif(chosen == 'b'):
                        clear()
                        #Call the function that show the graphic G information
                        showGraphInfo()

                    elif(chosen == 'c'):
                        source = int(input("Source Node: "))
                        target = int(input("Target Node: "))

                        showShortedPath()
                        print(colored(0,255,0,"\nSUCCESS:"),"shortest path generated.")
                        plt.show()

                    elif(chosen == 'd'):
                        nOfTImes = int(input("Number of edges: "))
                        weighted_edges= []

                        for i in range(0,nOfTImes):
                            node1 = int(input("Node 1: "))
                            node2 = int(input("Node 2: "))
                            weight = int(input("Weight: "))
                            weighted_edges.append((node1,node2,weight))

                        changeWeightedEdges()
                        print(colored(0,255,0,"\nSUCCESS:"),"graphic updated.")
                        plt.show()

                    elif(chosen == 'e'):
                        clear()
                        break

                    else:
                        clear()
                        print(colored(255,0,0,"\nERROR:"),"invalid selected option.")
                        print()

                    continue

            except ValueError:
                print(colored(255,0,0,"\nERROR:"),"an error has occured. Invalid value")
            except nx.NetworkXNoPath:
                print(colored(255,0,0,"\nERROR:"),"no path between those nodes")
            except nx.NodeNotFound:
                print(colored(255,0,0,"\nERROR:"),"invalid nodes, please check the graphic")
            except nx.NetworkXError:
                print(colored(255,0,0,"\nERROR:"),"invalid nodes, please check the graphic")
            else:
                break
    #Part 2 - Data and Statistics
    elif chosen == '2':
        while True:    
            try:
                #Menu inside part 1
                menuOptions = {
                'a': 'Count Missing Values',
                'b': 'Chest pain according to the age of the patients',
                'c': 'Descriptive Statistics',
                'd': 'Useful information',
                'e': 'Who used this Dataset?',
                'f': 'Back to the main menu'
                }
                
                while True:
                    print("\nPart II - The Heart Disease UCI .csv file")
                    print("--------------------------------------------------------")
                    printMenu()

                    chosen=input("\nSelect an option: ")

                    #Part II Variables
                    nRowsRead = 1000
                    df = pd.read_csv('heart.csv',delimiter=',',nrows=nRowsRead)
                    df.dataframeName = 'heart.csv'
                    nRow,nCol = df.shape

                    chest__pain = df["cp"]
                    patient_age = df["age"]
                    color = []

                    if(chosen == 'a'):
                        clear()
                        print("Number of missing values on dataset:", df.isnull().sum().sum())
                    elif(chosen == 'b'):
                        clear()
                        buildCpPlot()
                        plt.show()
                    elif(chosen == 'c'):
                        clear()
                        
                        pd.set_option('display.max_columns',None)
                        print("\nDiscriptive Statistics Data:")
                        print("--------------------------------------------------------")
                        print(df.describe())
                        
                    elif(chosen == 'd'):
                        clear()

                        # Plot Description Table Array
                        tableInfo ={
                            1: ['Heart Disease Pie','Ratio of people that was diagnosed with heart disease. More than 50% have this disease.'],
                            2: ['Heart Disease Pie(Gender)','The ratio of male and female with and without heart disease. 30.7% of male with that disease, higher than female'],
                            3: ['Cholestrol/age Plot Bar','All the ages and correspondent cholestrol'],
                            4: ['Column Dataframe Correlation','Pairwaise correlation of all columns in the dataframe. Negative Numbers - one variable increase and the other decrease or vice versa. Positive numbers - the two variables increase or decrease. Perfect correlation (1 or -1) - it is the perfect correlation.']
                        }

                        buildFactPlots()
                        
                        # All Plot Details. Plot Names and its description 
                        print("\nPlot Details","\n---------------------------------------------------")
                        print(f'\nThere are {nRow} rows and {nCol} columns on the csv file\n\n')

                        print ("{:<30} {:<50}".format('Plot Name','Description'))
                        print ("{:<30} {:<50}".format('-----------------------------','----------------------------------------------------------'))

                        # Get all keys and values of tableInfo Array and show the values
                        for k, v in tableInfo.items():
                            plotName, plotDesc = v
                            print("{:<30} {:<50}".format(plotName,plotDesc))
                        plt.show()

                    elif(chosen == 'e'):
                        clear()

                        # show pdf with all information
                        webbrowser.open_new('studieswheartscsv.pdf')
                        break
                    elif(chosen == 'f'):
                        clear()
                        break
                    else:
                        clear()
                        print(colored(255,0,0,"\nERROR:"),"invalid selected option.")
                        print()
                    continue
            except ValueError:
                print(colored(255,0,0,"\nERROR:"),"an error has occured. Invalid value.")
            except FileNotFoundError:
                print(colored(255,0,0,"\nERROR:"),"File not found. Try to change file path.")
            else:
                break
    elif chosen == '-1':
        break
    else:
        print(colored(255,0,0,"\nError:"),"invalid selected option.")
        print()
