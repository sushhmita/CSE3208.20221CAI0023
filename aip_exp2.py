# -*- coding: utf-8 -*-
"""AIP_EXP2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Ak3mPktgLitpp3y6nmD47z_6xFPi_F16
"""

RomaniaMap  = dict()

#Let us add the vertices representing the Romanian cities by their first letter
vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U', 'V', 'Z']
print(len(vertices))

#Let us now add the edges and insert it into the dictionary
RomaniaMap['A'] = [('S', None, 1), ('T', None, 1), ('Z', None, 1)]
RomaniaMap['B'] = [('F', None, 1), ('G', None, 1), ('P', None, 1), ('U', None, 1)]
RomaniaMap['C'] = [('D', None, 1), ('R', None, 1), ('P', None, 1)]
RomaniaMap['D'] = [('C', None, 1), ('M', None, 1)]
RomaniaMap['E'] = [('E', None, 1)]
RomaniaMap['F'] = [('B', None, 1), ('S', None, 1)]
RomaniaMap['G'] = [('B', None, 1)]
RomaniaMap['H'] = [('E', None, 1), ('U', None, 1)]
RomaniaMap['I'] = [('N', None, 1), ('V', None, 1)]
RomaniaMap['L'] = [('M', None, 1), ('T', None, 1)]
RomaniaMap['M'] = [('D', None, 1), ('L', None, 1)]
RomaniaMap['N'] = [('I', None, 1)]
RomaniaMap['O'] = [('S', None, 1), ('Z', None, 1)]
RomaniaMap['P'] = [('B', None, 1), ('C', None, 1), ('R', None, 1)]
RomaniaMap['R'] = [('C', None, 1), ('P', None, 1), ('S', None, 1)]
RomaniaMap['S'] = [('A', None, 1), ('F', None, 1), ('O', None, 1), ('R', None, 1)]
RomaniaMap['T'] = [('A', None, 1), ('L', None, 1)]
RomaniaMap['U'] = [('B', None, 1), ('H', None, 1), ('V', None, 1)]
RomaniaMap['V'] = [('I', None, 1), ('U', None, 1)]
RomaniaMap['Z'] = [('A', None, 1), ('O', None, 1)]
print(RomaniaMap)

from queue import Queue

romaniaMap = {
    'Arad': ['Sibiu', 'Zerind', 'Timisoara'],
    'Zerind': ['Arad', 'Oradea'],
    'Oradea': ['Zerind', 'Sibiu'],
    'Sibiu': ['Arad', 'Oradea', 'Fagaras', 'Rimnicu'],
    'Timisoara': ['Arad', 'Lugoj'],
    'Lugoj': ['Timisoara', 'Mehadia'],
    'Mehadia': ['Lugoj', 'Drobeta'],
    'Drobeta': ['Mehadia', 'Craiova'],
    'Craiova': ['Drobeta', 'Rimnicu', 'Pitesti'],
    'Rimnicu': ['Sibiu', 'Craiova', 'Pitesti'],
    'Fagaras': ['Sibiu', 'Bucharest'],
    'Pitesti': ['Rimnicu', 'Craiova', 'Bucharest'],
    'Bucharest': ['Fagaras', 'Pitesti', 'Giurgiu', 'Urziceni'],
    'Giurgiu': ['Bucharest'],
    'Urziceni': ['Bucharest', 'Vaslui', 'Hirsova'],
    'Hirsova': ['Urziceni', 'Eforie'],
    'Eforie': ['Hirsova'],
    'Vaslui': ['Iasi', 'Urziceni'],
    'Iasi': ['Vaslui', 'Neamt'],
    'Neamt': ['Iasi']
}


def bfs(startingNode, destinationNode):
    # For keeping track of what we have visited
    visited = {}
    # keep track of distance
    distance = {}
    # parent node of specific graph
    parent = {}

    bfs_traversal_output = []
    # BFS is queue based so using 'Queue' from python built-in
    queue = Queue()

    # travelling the cities in map
    for city in romaniaMap.keys():
        # since intially no city is visited so there will be nothing in visited list
        visited[city] = False
        parent[city] = None
        distance[city] = -1

    # starting from 'Arad'
    startingCity = startingNode
    visited[startingCity] = True
    distance[startingCity] = 0
    queue.put(startingCity)

    while not queue.empty():
        u = queue.get()     # first element of the queue, here it will be 'arad'
        bfs_traversal_output.append(u)

        # explore the adjust cities adj to 'arad'
        for v in romaniaMap[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                distance[v] = distance[u] + 1
                queue.put(v)

        # reaching our destination city i.e 'bucharest'
    g = destinationNode
    path = []
    while g is not None:
        path.append(g)
        g = parent[g]

    path.reverse()
    # printing the path to our destination city
    print(path)


# Starting City & Destination City
bfs('Arad', 'Bucharest')

def getNeighbours(x):
    # Check if the vertex exists in the graph
    if x in RomaniaMap: # Changed 'graph' to 'RomaniaMap'
        # Return the sorted list of neighbours
        return sorted(RomaniaMap[x]) # Changed 'graph' to 'RomaniaMap'
    else:
        # If the vertex doesn't exist, return an empty list
        return []

# Example usage:
vertex = 'B'
neighbours = getNeighbours(vertex)
print(f"Neighbours of {vertex}: {neighbours}")

vertex = 'G'
neighbours = getNeighbours(vertex)
print(f"Neighbours of {vertex}: {neighbours}")

vertex = 'P'
neighbours = getNeighbours(vertex)
print(f"Neighbours of {vertex}: {neighbours}")

def createGraph():
    # Initialize an empty graph
    graph = {}

    # Prompt the user for the number of vertices
    num_vertices = int(input("Enter the number of vertices: "))

    # Loop to input each vertex and its neighbors
    for _ in range(num_vertices):
        vertex = input("\nEnter vertex: ")
        neighbours = input(f"Enter neighbours of {vertex} separated by spaces: ").split()
        graph[vertex] = neighbours

    return graph

def getNeighbours(graph, x):
    # Check if the vertex exists in the graph
    if x in graph:
        # Return the sorted list of neighbours
        return sorted(graph[x])
    else:
        # If the vertex doesn't exist, return an empty list
        return []

# Example usage:
graph = createGraph()

# Ask the user for the vertex to find its neighbours
vertex = input("\nEnter the vertex to find its neighbours: ")
neighbours = getNeighbours(graph, vertex)
print(f"\nNeighbours of {vertex}: {neighbours}")

file1 = open("/content/sample_data/My File.txt", "r")
text = file1.read()
print(text)

# Your roll number
roll_number = "20221CAI0023"
inputfilename = 'Test1.txt'
outputfilename = f"{roll_number}-Lab-02-output.txt"

# Read the input file
with open("/content/Test1.txt", 'r') as file:
    lines = file.readlines()

#Parse the input to extract vertices and neighbors
graph = {}
for line in lines:
    parts = line.strip().split("\t")  # Split the line by tab character
    vertex = parts[0]
    neighbors = parts[1].split(",")  # Split neighbors by comma
    graph[vertex] = sorted(neighbors)  # Sort neighbors in ascending order

#Sort the vertices in descending order
sorted_vertices = sorted(graph.keys(), reverse=True)

#Format the output according to the specified format
output_lines = []
for vertex in sorted_vertices:
    sorted_neighbors = graph[vertex]
    # Create formatted neighbor tuples with no spaces inside parentheses
    formatted_neighbors = " ".join([f"({neighbor},None,1)" for neighbor in sorted_neighbors])
    output_line = f"{vertex}->{formatted_neighbors}"
    output_lines.append(output_line)

#Write the output to the specified file
with open(outputfilename, 'w') as output_file:
    output_file.write("\n".join(output_lines))

print(f"Output written to {outputfilename}")