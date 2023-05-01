import os
from My_queue import Queue, Node
import random
from My_tree import *
from list_dinamic import *
from models import *

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
        scheme_photo = Photo(queue.dequeue())
        tree_photo.insert(scheme_photo)
    return tree_photo


def call(list_photos, queue_photo=None, tree_photos=None):

    if queue_photo and tree_photos:
        queue_photo = add_queue(list_photos, queue_photo)
        tree_photos = create_tree_photos(queue_photo, tree_photos)

    else:
        queue_photo = add_queue(list_photos)
        tree_photos = create_tree_photos(queue_photo)
    return tree_photos


def generate_random(bot: int = 0, top: int = 1000, amount: int = 200000) -> list:
    list_photos = []
    for _ in range(amount):
        list_photos.append(random.randint(bot, top))
    return list_photos

# Agrega scheme a mano, pero no lo agregamos por el momento para medir bien los tiempos


def add_scheme():
    scheme = input("Scheme: ")
    config = input("Configuración:")
    type = input("Type: ")
    configuracion = [scheme, config, type]
