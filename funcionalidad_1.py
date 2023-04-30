import os
from My_queue import Queue, Node
import random
from My_tree import *


def add_favorites(incial: True, favorites):
    if incial == False:
        favorites = Queue()
    else:
        favorites.enqueue()


def create_tree_photos(queue):
    tree_photo = Tree()
    while queue.size > 0:
        tree_photo.insert(queue.dequeue())

    return tree_photo


def generate_random(bot: int = 0, top: int = 1000, amount: int = 200) -> list:
    list_photos = []
    for _ in range(amount):
        list_photos.append(random.randint(bot, top))

    return list_photos


def add_queue(list_photos):
    queue_photos = Queue()

    for i in list_photos:
        queue_photos.enqueue(i)

    # FORMA DE CARGAR EN UNA QUEUE TODOS LAS FOTOS DE UNA CARPETA
    # queue_photos = Queue()
    # for i in os.listdir(photos_Load):
    #     queue_photos.enqueue(i)

    return queue_photos


# usar la cola para clasificar
def add_scheme(queue_photos, tree):
    while queue_photos.first:
        config = input("configuracion de la camara para esta foto")
