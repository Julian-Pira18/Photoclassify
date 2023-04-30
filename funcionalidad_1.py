import os
from My_queue import Queue, Node
import random
from My_tree import *
from list_dinamic import *


# ---------------------------------


def add_queue(list_photos, queue_photos=None):
    if queue_photos == None:
        queue_photos = Queue()
    for i in list_photos:
        queue_photos.enqueue(i)

    # FORMA DE CARGAR EN UNA QUEUE TODOS LAS FOTOS DE UNA CARPETA
    # queue_photos = Queue()
    # for i in os.listdir(photos_Load):
    #     queue_photos.enqueue(i)

    return queue_photos


def create_tree_photos(queue, tree_photo=None) -> None:
    if tree_photo == None:
        tree_photo = Tree()

    while queue.size > 0:
        tree_photo.insert(queue.dequeue())

    return tree_photo


def generate_random(bot: int = 0, top: int = 1000, amount: int = 200000) -> list:
    list_photos = []
    for _ in range(amount):
        list_photos.append(random.randint(bot, top))
    return list_photos


def call(list_photos, queue_photo=None, tree_photos=None):

    if queue_photo and tree_photos:
        queue_photo = add_queue(list_photos, queue_photo)
        tree_photos = create_tree_photos(queue_photo, tree_photos)

    else:
        queue_photo = add_queue(list_photos)
        tree_photos = create_tree_photos(queue_photo)
    return tree_photos


def add_favorites(incial: True, favorites):
    if incial == False:
        favorites = Queue()
    else:
        favorites.enqueue()


# usar la cola para clasificar
def add_scheme(queue_photos, tree):
    while queue_photos.first:
        config = input("configuracion de la camara para esta foto")
