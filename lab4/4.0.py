import pygame as pg
from pygame.draw import *

# Global variable

w = 768
l = 1032


COLORS = {
    'BLACK': (0, 0, 0),
    'WHITE': (255, 255, 255),
    'GREEN': (17, 240,  80),
    'RED':  (255, 0, 0),
    'GREY': (128, 128, 128),
    'YELLOW': (255, 255, 0),
    'BLUE': (17, 225, 240),
    'PINK': (247,  22, 199),
    'WASHY':  (255, 227, 255)
}

pg.init()

FPS = 30
screen = pg.display.set_mode((l, w))

def draw_background(x, h, col1, col2):
    '''
    Функция закрашивает землю и небо
    x: длина рамки
    h: ширина рамки
    col1: цвет неба
    col2: цвет земли
    '''

    rect(screen, COLORS[col1], (0, 0, x, h / 2))
    rect(screen, COLORS[col2], (0, h / 2, x, h / 2))

def draw_bodies(x, h, col1, col2, col3, col4):
    '''
    Функция рисует тела (естественно с руками)
    x: длина рамки
    h:ширина рамки
    col1: цвет женцины
    col2: цвет мужчины
    col3: цвет голов
    col4: цвет рук и ног
    '''

    var = 0
    for i in range(2):
        x *= -1
        polygon(screen, COLORS[col1], [(var - x / 2 * 6 / 10, h / 4 + h / 2 * 3 / 4), (var - x / 2 * 8 / 10, h / 4 + h / 2 * 3 / 4),
        (var - x / 2 * 7 / 10, h / 4 + h / 2 * 1 / 4)])
        ellipse(screen, COLORS[col2], (var - x / 2 * 1 / 5 - x / 2 * 1 / 6, h / 4 + h / 2 * 1 / 4, x / 2 * 1 / 6, h / 2 * 1 / 2))

        circle(screen, COLORS[col3], (var - x / 2 * 7 / 10, h / 4 + h / 2 * 1 / 4), h / 2 * 1 / 12)
        circle(screen, COLORS[col3], (var - x / 2 * 17 / 60, h / 4 + h / 2 * 1 / 4), h / 2 * 1 / 12)

        line(screen, COLORS[col4], (var - x / 2 * 7 / 32, h / 4 + h / 2 * 15 / 40),
             (var - x / 2 * 1 / 7, h / 4 + h / 2 * 11 / 20), 1)
        line(screen, COLORS[col4], (var - x / 2 * 120 / 344, h / 4 + h / 2 * 270 / 768),
             (var - x / 2 * 483 / 1032, h / 4 + h / 2 * 423 / 768), 1)
        line(screen, COLORS[col4], (var - x / 2 * 483 / 1032, h / 4 + h / 2 * 423 / 768),
             (var - x / 2 * 700 / 1032, h / 4 + h / 2 * 276 / 768), 1)
        line(screen, COLORS[col4], (var - x / 2 * 750 / 1032, h / 4 + h / 2 * 275 / 768),
             (var - x / 2 * 930 / 1032, h / 4 + h / 2 * 330 / 768), 1)
        line(screen, COLORS[col4], (var - x / 2 * 930 / 1032, h / 4 + h / 2 * 330 / 768),
             (var - x / 2 * 1032 / 1032, h / 4 + h / 2 * 250 / 768), 1)
        line(screen, COLORS[col4], (var - x / 2 * 250 / 1032, h / 4 + h / 2 * 536 / 768),
             (var - x / 2 * 183 / 1032, h / 4 + h / 2 * 714 / 768), 1)
        line(screen, COLORS[col4], (var - x / 2 * 183 / 1032, h / 4 + h / 2 * 714 / 768),
             (var - x / 2 * 133 / 1032, h / 4 + h / 2 * 714 / 768), 1)
        line(screen, COLORS[col4], (var - x / 2 * 345 / 1032, h / 4 + h / 2 * 528 / 768),
             (var - x / 2 * 360 / 1032, h / 4 + h / 2 * 710 / 768), 1)
        line(screen, COLORS[col4], (var - x / 2 * 360 / 1032, h / 4 + h / 2 * 710 / 768),
             (var - x / 2 * 410 / 1032, h / 4 + h / 2 * 710 / 768), 1)
        line(screen, COLORS[col4], (var - x / 2 * 680 / 1032, h / 4 + h / 2 * 3 / 4),
             (var - x / 2 * 680 / 1032, h / 4 + h / 2 * 696 / 768), 1)
        line(screen, COLORS[col4], (var - x / 2 * 680 / 1032, h / 4 + h / 2 * 696 / 768),
             (var - x / 2 * 630 / 1032, h / 4 + h / 2 * 696 / 768), 1)
        line(screen, COLORS[col4], (var - x / 2 * 760 / 1032, h / 4 + h / 2 * 3 / 4),
             (var - x / 2 * 760 / 1032, h / 4 + h / 2 * 696 / 768), 1)
        line(screen, COLORS[col4], (var - x / 2 * 760 / 1032, h / 4 + h / 2 * 696 / 768),
             (var - x / 2 * 810 / 1032, h / 4 + h / 2 * 696 / 768), 1)
        line(screen, COLORS[col4], (abs(x) / 2, h / 4 + h / 2 * 250 / 768), (abs(x) / 2, h / 4 + h / 2 * 150 / 768), 1)
        var = -x
        
def draw_ice(x, h, col1, col2, col3, col4):
    '''
    Функция рисует "сахарную вату" и мороженое
    x: длина рамки
    h: ширина рамки
    col1: цвет рожка мороженого
    col2: цвет пломбирного мороженого (по дефолту)
    col3: цвет мороженого со вкусом клубники (по дефолту) и также "сахарной ваты"
    col4: цвет мороженого со вкусом киви (по дефолту)
    '''
    var = 0
    for i in range (2):
        x *= -1
        polygon(screen, COLORS[col1], [(var - x / 2 * 162 / 1032, h / 4 + h / 2 * 437 / 768), (var - x / 2 * 155 / 1032, h / 4 + h / 2 * 300 / 768),
        (var - x / 2 * 74 / 1032, h / 4 + h / 2 * 430 / 1032)])

        circle(screen, COLORS[col2], (var - x / 2 * 110 / 1032, h / 4 + h / 2 * 250 / 768), h / 2 * 25 / 768)
        circle(screen, COLORS[col3], (var - x / 2 * 130 / 1032, h / 4 + h / 2 * 285 / 768), h / 2 * 25 / 768)
        circle(screen, COLORS[col4], (var - x / 2 * 95 / 1032, h / 4 + h / 2 * 290 / 768), h / 2 * 25 / 768)

        polygon(screen, COLORS[col3], [(var - x / 2 * 1020 / 1032, h / 4 + h / 2 * 167 / 768), (var - x / 2 * 1060 / 1032, h / 4 + h / 2 * 100 / 768),
        (var - x / 2 * 1010 / 1032, h / 4 + h / 2 * 90 / 768)])

        circle(screen, COLORS[col3], (abs(x) / 2, h / 4 + h / 2 * 85 / 768), h / 2 * 25 / 768)
        circle(screen, COLORS[col3], (abs(x) / 2, h / 4 + h / 2 * 95 / 768), h / 2 * 25 / 768)
        var = -x

draw_background(l, w, 'BLUE', 'GREEN')
draw_bodies(l, w, 'PINK', 'GREY', 'WASHY', 'BLACK')
draw_ice(l, w, 'YELLOW', 'WHITE', 'RED', 'GREEN')

pg.display.update()
clock = pg.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True

pg.quit()



