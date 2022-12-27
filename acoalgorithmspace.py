import random

# Define the search space
search_space = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Define the cost function
def cost(x):
  return x ** 2

# Define the pheromone update function
def update_pheromone(pheromone, cost, evaporation_rate):
  pheromone *= (1 - evaporation_rate)
  pheromone += cost
  return pheromone

# Define the probability function
def probability(cost, pheromone, alpha, beta):
  return pheromone ** alpha * (1 / cost) ** beta

# Define the main ACO function
def ACO(iterations, num_ants, evaporation_rate, alpha, beta):
  # Initialize the pheromone matrix
  pheromone = [[0.1 for i in range(len(search_space))] for j in range(len(search_space))]

  # Run the ACO algorithm for the specified number of iterations
  for i in range(iterations):
    # Create a list to store the solutions found by each ant
    solutions = []
    for j in range(num_ants):
      # Choose the starting point for the ant
      current_node = random.choice(search_space)
      solution = [current_node]

      # Run the ant's search until it reaches a termination condition
      while True:
        # Calculate the probabilities for each possible next node
        probabilities = []
        for k in search_space:
          if k == current_node:
            continue
          cost = cost(k)
          pheromone_level = pheromone[current_node][k]
          prob = probability(cost, pheromone_level, alpha, beta)
          probabilities.append(prob)

        # Choose the next node based on the probabilities
        next_node = random.choices(
