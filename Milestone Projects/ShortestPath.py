# Author: Joe Do
# March 26, 2018
# Bellevue College Discrete Math - MATH&301
# Dijskstra's algorithm which runs on a graph (potentially directed) with edge weights
# Dijskstra's algorithm will give you the shortest path from a source node to every other nodes

# Find shortest path between two nodes using Dijskstra's algorithm
def dijkstra(graph, source, dest, visited=[], distances={}, predecessors={}):
    # Base case
    if source == dest:
        path = []
        pred = dest
        while pred != None:
            path.append(pred)
            pred = predecessors.get(pred, None)
        print('Shortest path: ' + str(path) + " Cost to travel: $" + str(distances[dest]))

    # Recursive case
    else :
        # Initializes the cost to zero on first run
        if not visited:
            distances[source] = 0

        # Visit all of the adjacent nodes
        for neighbor in graph[source] :
            if neighbor not in visited:
                new_distance = distances[source] + graph[source][neighbor]

                # by default, setting distance to infinity using float('inf')
                if new_distance < distances.get(neighbor, float('inf')):
                    distances[neighbor] = new_distance
                    predecessors[neighbor] = source

        # Add visited node to a list
        visited.append(source)

        # run Dijskstra with source = 'x'
        unvisited = {}
        for k in graph:
            if k not in visited:
                unvisited[k] = distances.get(k, float('inf'))
        x = min(unvisited, key = unvisited.get) # select non visited node with lowest distance to x
        dijkstra(graph, x, dest, visited, distances, predecessors)

# Ask for first city
def firstCity():
    cityOne = input('First City: ')
    while cityOne not in 'annarbormanhattancorvallisiowacharlottesville':
        cityOne = input('Please enter first city again\
        \nChoose between "annarbor, manhattan, corvallis, iowa, charlottesville": ')

    return cityOne

# Ask for second city
def secondCity():
    cityTwo = input('Second City: ')
    while cityTwo not in 'annarbormanhattancorvallisiowacharlottesville':
        cityTwo = input('Please enter second city again\
        \nChoose between "annarbor, manhattan, corvallis, iowa, charlottesville": ')

    return cityTwo
# Wrapper function
def main():
    print('5 best places to live in America in 2018:')
    print('(1)  annarbor, MI')
    print('(2)  manhattan, KS')
    print('(3)  corvallis, OR')
    print('(4)  iowa, IA')
    print('(5)  charlottesville, VA')

    print('----------')
    print('FIND THE SHORTEST PATH BETWEEN TWO CITIES')
    # Create a dictionary inside a dictionary to represent a directed-weighted graph
    cityMap = {
                'annarbor': {'corvallis': 100, 'charlottesville': 200},
                'manhattan': {'corvallis': 600, 'iowa': 700},
                'corvallis': {'manhattan': 400},
                'iowa': {'annarbor': 1000, 'charlottesville': 500},
                'charlottesville': {'annarbor': 300, 'corvallis': 900, 'manhattan': 200}
              }

    city1 = firstCity()
    city2 = secondCity()
    dijkstra(cityMap, city1, city2)

if __name__ == "__main__":
    main()
