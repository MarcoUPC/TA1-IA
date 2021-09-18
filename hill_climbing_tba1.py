import random
import numpy as np
import networkx as nx

mtx = []

paths = []


def solution(mtx):
    coordenadas = list(range(0, len(mtx)))
    solution = []
    for i in range(0, len(mtx)):
        random_point = coordenadas[random.randint(0, len(coordenadas) - 1)]
        solution.append(random_point)
        coordenadas.remove(random_point)
    return solution


def path_length(mtx, sol):
    cycle_length = 0
    for i in range(0, len(sol)):
        cycle_length += mtx[sol[i - 1]][sol[i]]
    # print(cycle_length)
    return cycle_length


def neighbors(mtx, sol):
    neighbors = []
    for i in range(len(sol)):
        for j in range(i + 1, len(sol)):
            neighbour = sol.copy()
            neighbour[i] = sol[j]
            neighbour[j] = sol[i]
            neighbors.append(neighbour)

    b_neighbour = neighbors[0]
    b_path = path_length(mtx, b_neighbour)

    for neighbour in neighbors:
        current_path = path_length(mtx, neighbour)
        if current_path < b_path:
            b_path = current_path
            b_neighbour = neighbour
    return b_neighbour, b_path


def hill_climbing(mtx):
    c_sol = solution(mtx)
    c_path_d = path_length(mtx, c_sol)
    neighbour = neighbors(mtx, c_sol)[0]
    b_neighbour, best_neighbor_path = neighbors(mtx, neighbour)

    while best_neighbor_path < c_path_d:
        c_sol = b_neighbour
        c_path_d = best_neighbor_path
        neighbour = neighbors(mtx, c_sol)[0]
        b_neighbour, best_neighbor_path = neighbors(mtx, neighbour)
        paths.append(b_neighbour)
    paths.append(c_sol)
    return c_path_d, c_sol


def draw_solution():
    final_solution = hill_climbing(mtx)
    print('RESULTADO RUTAS')
    for i in range(0, len(paths)):
        print(paths[i])
    return final_solution[0], final_solution[1], paths

