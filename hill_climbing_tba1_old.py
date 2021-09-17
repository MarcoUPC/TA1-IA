import random
import numpy as np
import networkx as nx

matrix = []


# encuentra un solucion random
def solution(matrix):
    points = list(range(0, len(matrix)))
    print(points)
    solution = []
    for i in range(0, len(matrix)):
        random_point = points[random.randint(0, len(points) - 1)]
        print(random_point)
        solution.append(random_point)
        points.remove(random_point)

    return solution


# calcula la ruta basándose en la solución aleatoria
def path_length(matrix, solution):
    cycle_length = 0
    for i in range(0, len(solution)):
        cycle_length += matrix[solution[i - 1]][solution[i]]
    print(cycle_length)
    return cycle_length


# generar vecinos de la solución aleatoria intercambiando ciudades y devuelve el mejor vecino
def neighbors(matrix, solution):
    neighbors = []
    for i in range(len(solution)):
        for j in range(i + 1, len(solution)):
            neighbor = solution.copy()
            neighbor[i] = solution[j]
            neighbor[j] = solution[i]
            neighbors.append(neighbor)

    # asumimos que el primer vecino de la lista es el mejor
    best_neighbor = neighbors[0]
    best_path = path_length(matrix, best_neighbor)

    # comprobamos si existe algun vecino mejor
    for neighbor in neighbors:
        current_path = path_length(matrix, neighbor)
        if current_path < best_path:
            best_path = current_path
            best_neighbor = neighbor
    return best_neighbor, best_path


def hill_climbing(coordinate):
    # matrix = generate_matrix(coordinate)

    current_solution = solution(matrix)
    current_path_lenght = path_length(matrix, current_solution)
    neighbor = neighbors(matrix, current_solution)[0]
    best_neighbor, best_neighbor_path = neighbors(matrix, neighbor)

    while best_neighbor_path < current_path_lenght:
        current_solution = best_neighbor
        current_path_lenght = best_neighbor_path
        neighbor = neighbors(matrix, current_solution)[0]
        best_neighbor, best_neighbor_path = neighbors(matrix, neighbor)

    return current_path_lenght, current_solution


def draw_solution():
    final_solution = hill_climbing(matrix)
    print(final_solution[0], final_solution[1])
    return final_solution[0], final_solution[1]

# draw_solution(matrix)
