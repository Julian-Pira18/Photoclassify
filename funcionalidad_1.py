import os
from My_queue import Queue, Node
import random
from My_tree import *
from list_dinamic import *
from linkedlist_tail import *

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


def generate_random(bot: int = 0, top: int = 1000, amount: int = 20000) -> list:
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

# -----Alternartive 1.2---------------------------


def add_list(list_photos, list_create=None):
    if list_create == None:
        list_create = dinamic_arraylist()

    for i in list_photos:
        list_create.pushback(i)

    return list_create


def create_photos(import_photo, list_create=None):
    if list_create == None:
        list_create = dinamic_arraylist()

    while import_photo.contador > 0:
        list_create.pushback(import_photo.popback())

    return list_create


def call_list(list_photo, import_photo=None, load_photo=None):
    if import_photo and load_photo:
        import_photo = add_list(list_photo, import_photo)
        load_photo = create_photos(import_photo, load_photo)

    else:
        import_photo = add_list(list_photo)
        load_photo = create_photos(import_photo)

    return load_photo

# --------------------------------------------------------------

# -----------------Alternative 1.3


def add_linkedlist(list_photo, listcreate=None):
    if listcreate == None:
        listcreate = Double_linked_list()

    for i in list_photo:
        listcreate.pushback(i)
    return listcreate


def create_linked(import_photos, create_photos=None):
    if create_photos == None:
        create_photos = Double_linked_list()

    while import_photos.size > 0:
        create_photos.pushback(import_photos.popback())

    return create_photos


def call_linked(list_photo, import_photo=None, load_photo=None):
    if import_photo and load_photo:
        import_photo = add_linkedlist(list_photo, import_photo)
        load_photo = create_linked(import_photo, load_photo)

    else:
        import_photo = add_linkedlist(list_photo)
        load_photo = create_linked(import_photo)


#  --------------------------------------------------------------


def add_favorites(incial: True, favorites):
    if incial == False:
        favorites = Queue()
    else:
        favorites.enqueue()


# usar la cola para clasificar
def add_scheme(queue_photos, tree):
    while queue_photos.first:
        config = input("configuracion de la camara para esta foto")
