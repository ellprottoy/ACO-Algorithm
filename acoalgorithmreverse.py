import random

class Ant:
  def __init__(self, graph):
    self.graph = graph
    self.current_node = random.choice(list(graph.keys()))
    self.path = [self.current_node]
    self.unvisited_nodes = set(graph.keys()) - set(self.path)
    self.total_cost = 0

  def move(self):
    # Calculate the probabilities of moving to each unvisited node
    probabilities = []
    for node in self.unvisited_nodes:
      cost = self.graph[self.current_node][node]
      pheromone = self.current_node.pheromones[node]
      probability = pheromone ** alpha * (1 / cost) ** beta
      probabilities.append(probability)

    # Normalize the probabilities
    s = sum(probabilities)
    probabilities = [p/s for p in probabilities]

    # Choose the next node based on the probabilities
    r = random.random()
    i = 0
    p = probabilities[i]
    while r > p:
      i += 1
      p += probabilities[i]
    next_node = list(self.unvisited_nodes)[i]

    # Update the ant's current node and path
    self.current_node = next_node
    self.path.append(next_node)
    self.unvisited_nodes = set(self.graph.keys()) - set(self.path)
    self.total_cost += self.graph[self.current_node][node]

def aco(graph, num_ants, num_iterations, alpha=1, beta=1):
  # Initialize the pheromones on each edge to a small value
  for u in graph:
    for v in graph[u]:
      u.pheromones[v] = 0.1

  # Run the ACO algorithm for the specified number of
