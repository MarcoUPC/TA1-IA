import random
import numpy as np
import networkx as nx

matrix = []

paths = []

def neighbors(matrix, sol):
    neighbors = []
    for i in range(len(sol)):
        for j in range(i + 1, len(sol)):
            neighbor = sol.copy()
            neighbor[i] = sol[j]
            neighbor[j] = sol[i]
            neighbors.append(neighbor)

    b_neighbor = neighbors[0]
    b_path = path_lng(matrix, b_neighbor)

    for neighbor in neighbors:
        c_pth = path_lng(matrix, neighbor)
        if c_pth < b_path:
            b_path = c_pth
            b_neighbor = neighbor
    return b_neighbor, b_path


def hill_climbing(coordinate):

    c_sol = sol(matrix)
    c_path_lng = path_lng(matrix, c_sol)
    neighbor = neighbors(matrix, c_sol)[0]
    b_neighbor, b_neighbor_pth = neighbors(matrix, neighbor)

    while b_neighbor_pth < c_path_lng:
        c_sol = b_neighbor
        c_path_lng = b_neighbor_pth
        neighbor = neighbors(matrix, c_sol)[0]
        b_neighbor, b_neighbor_pth = neighbors(matrix, neighbor)
        paths.append(b_neighbor)
    paths.append(c_sol)
    return c_path_lng, c_sol


def sol(matrix):
    coord = list(range(0, len(matrix)))
    sol = []
    for i in range(0, len(matrix)):
        random_point = coord[random.randint(0, len(coord) - 1)]
        sol.append(random_point)
        coord.remove(random_point)

    return sol


def path_lng(matrix, sol):
    c_lengh = 0
    for i in range(0, len(sol)):
        c_lengh += matrix[sol[i - 1]][sol[i]]
    return c_lengh


def draw_solution():
    final_solution = hill_climbing(matrix)
    print('RESULTADO RUTAS')
    print(paths[len(paths)-1])
    return final_solution[0], final_solution[1], paths
