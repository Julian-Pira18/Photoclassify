import os
from My_queue import Queue, Node
import random
from My_tree import *
from list_dinamic import *
from models import *
from funcionalidad_1 import *
from My_Stack import *


def add_favorites(list_photos=None, favorites=None):
    if favorites == None:
        favorites = Stack()

    for i in list_photos:
        favorites.push(i)

    return favorites


def show_favorites(favorites):
    while True:
        favorites.show(5)
        print()

        option = int(input("""
    Options: 
        1. PRINT All FAVORITES
        3. EXIT FAVORITES 
"""))
        if option == 1:
            favorites.show()
        elif option == 2:
            break
