from random import random
import pygame, sys, string, math, time
from pygame.locals import *
import numpy as np
import hill_climbing_tba1 as hill_climbing

# DATOS GENERALES

white = (255, 255, 255)
gray = (217, 217, 217)
blue = (40, 75, 99)
green = (60, 110, 113)
black = (0, 0, 0)
red = (249, 65, 68)

mainClock = pygame.time.Clock()

pygame.init()
scr = pygame.display.set_mode((1280, 720), 0, 32)
pygame.display.set_caption("Aerolineas Peru")
font_text = pygame.font.SysFont(None, 25)
font_name_city = pygame.font.SysFont(None, 45)

def random_color():
    return list(np.random.choice(range(255),size=3))

    
class Map:
    @staticmethod
    def calc_distance(x1, y1, x2, y2):
        difX = math.pow(x2 - x1, 2)
        difY = math.pow(y2 - y1, 2)
        d = math.sqrt(difX + difY)
        return math.trunc(d)

    @staticmethod
    def generate_name(pos):
        letters_ascii = string.ascii_letters
        return letters_ascii[pos]

    @staticmethod
    def create_matrix(points):
        i = 0
        matrix = []
        for _ in points:
            matrix.append([])

        for city in points:
            for neighbour in points:
                distance = 0
                if city.name != neighbour.name:
                    distance = Map.calc_distance(city.x, city.y, neighbour.x, neighbour.y)
                matrix[i].append(distance)
            i = i + 1
        return matrix

    @staticmethod
    def draw_text(text, font, color, surface, x, y):
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)


class City:
    def __init__(self, x, y, index, name,color, distance: float = 0):
        self.index = index
        self.name = name
        self.x = x
        self.y = y
        self.city_rect = pygame.Rect(5, 5, 10, 10)
        self.city_rect.centerx = x
        self.city_rect.centery = y
        self.distance = distance
        self.color = color

    def __lt__(self, other):
        return self.distance < other.distance

    def draw_city(self):
        pygame.draw.circle(scr, green, (self.x, self.y), 10, 3)
        Map.draw_text(str(self.name), font_name_city, self.color, scr, self.x, self.y)

    def draw_road(self, city, color):
        pygame.draw.line(scr, color, (self.x, self.y), (city.x, city.y), 3)




class Algorithms:

    @staticmethod
    def hill_climbing(matrix_distances):
        hill_climbing.matrix = matrix_distances
        return hill_climbing.draw_solution()

    @staticmethod
    def show_path(path, points):
        if len(path) > 2:
            for i in range(len(points) - 1):
                for j in range(i + 1, len(points)):
                    points[i].draw_road(points[j], gray)

            path_points = []
            for i in path:
                path_points.append(points[i])

            for i in range(len(path_points) - 1):
                city_actual = path_points[i]
                city_to_go = path_points[i + 1]
                city_actual.draw_road(city_to_go, red)
            path_points[len(path_points) - 1].draw_road(path_points[0], red)


def gui():
    points = []
    add_city_action = False
    is_click = False
    distance_matrix = []
    show_result = False
    path_result = []
    possible_result = []
    best_distance = 0
    index_result = 0
    while True:

        # TITULO
        scr.fill((0, 0, 0))
        Map.draw_text('POSICIÓN DEL MOUSE', font_text, (255, 255, 255), scr, 20, 20)

        # MOSTRAR POSICIÓN
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # DISEÑO DE LA GUI Y BOTONES
        Map.draw_text('X ' + str(mouse_x) + ' Y ' + str(mouse_y), font_text, (255, 255, 255), scr, 20, 40)

        background_map = pygame.Rect(75, 100, 800, 550)
        add_city_button = pygame.Rect(975, 300, 250, 100)
        solve_map_button = pygame.Rect(975, 425, 250, 100)
        clean_map_button = pygame.Rect(975, 550, 250, 100)

        pygame.draw.rect(scr, white, background_map)
        pygame.draw.rect(scr, gray, add_city_button)
        pygame.draw.rect(scr, red, clean_map_button)

        Map.draw_text('MAPA', font_text, black, scr, 95, 110)
        Map.draw_text('Añadir Coordenada', font_text, black, scr, 1030, 345)
        Map.draw_text('Limpiar Mapa', font_text, black, scr, 1040, 585)

        # PINTA LAS RUTAS DE TODOS LOS PUNTOS
        for i in range(len(points) - 1):
            for j in range(i + 1, len(points)):
                points[i].draw_road(points[j], gray)

        if show_result:
            # SE VAN MOSTRANDO TODOS LOS RESULTADOS QUE NOS DIO EL ALGORITOM
            Algorithms.show_path(possible_result[index_result], points)
            if index_result < len(possible_result) - 1:
                index_result = index_result + 1
            time.sleep(1)

        # PINTA LAS CIUDADES
        for city in points:
            city.draw_city()

        if len(points) > 2:
            pygame.draw.rect(scr, green, solve_map_button)
            Map.draw_text('Obtener Ruta Optima', font_text, black, scr, 1005, 465)

        if len(points) > 0:
            Map.draw_text('Ultima coordenada añadida: ' + str(points[len(points) - 1].name)+ "["+str(points[len(points)-1].distance)+"]", font_text, white, scr,
                          900, 40)

        if show_result:
            Map.draw_text('Total distancia de la mejor ruta: : ' + str(best_distance), font_text, white,
                          scr,
                          900, 67)
            

        # ESCUCHA SI SE SELECCION EL BOTON DE AÑADIR CIUDAD
        if add_city_button.collidepoint((mouse_x, mouse_y)):
            if is_click and not add_city_action:
                add_city_action = True
                is_click = False
                show_result = False

        # ESCUCHA SI SE SELECCION EL MAPA PARA AÑADIR UNA CIUDAD
        if background_map.collidepoint((mouse_x, mouse_y)):
            if is_click and add_city_action:
                city_x = mouse_x
                city_y = mouse_y
                name = Map.generate_name(len(points))
                new_city = City(city_x, city_y, len(points), name, random_color())
                points.append(new_city)
                add_city_action = False
                is_click = False
                show_result = False
                distance_matrix = Map.create_matrix(points)
                print(distance_matrix)

        # ESCUCHA SI SE SELECCION EL BOTON DE RESOLVER PARA MOSTRAR LAS RUTAS
        if solve_map_button.collidepoint((mouse_x, mouse_y)):
            if is_click:
                best_distance, path_result, possible_result = Algorithms.hill_climbing(distance_matrix)
                show_result = True
                add_city_action = False
                is_click = False

        # ESCUCHA SI SE SELECCION EL BOTON PARA LIMPIAR LA LISTA
        if clean_map_button.collidepoint((mouse_x, mouse_y)):
            if is_click:
                show_result = False
                points = []
                is_click = False

        # ESCUCHA LOS CLICKS O PARA SALIR DEL PROYECTO (ESC)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    is_click = True

        pygame.display.update()
        mainClock.tick(60)


gui()
