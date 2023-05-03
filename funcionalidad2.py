import time
import os
from My_queue import Queue, Node
import random
from My_tree import *
from list_dinamic import *
from models import *
from funcionalidad_1 import *
from My_Stack import *
from My_tree import *

# ----------Favorites Alternative 1.1    ----------------------------------------


# def add_favorites(list_photos=None, favorites=None):
#     if favorites == None:
#         favorites = Stack()

#     for i in list_photos:
#         favorites.push(i)

#     return favorites


# def show_favorites(favorites):
#     while True:
#         favorites.show(5)
#         print()
#         option = int(input("""
#         Options:
#             1. PRINT All FAVORITES
#             2. UPDATE
#             3. EXIT FAVORITES
#         """))
#         if option == 1:
#             favorites.show()
#         elif option == 2:
#             number = int(input("Photo: "))
#             update = int(input("TO: "))
#             start_time = time.time()
#             favorites.search(number, update)
#             end_time = time.time()
#             print(end_time - start_time)
#         elif option == 3:
#             break

# ----------------------------------------------------


# ----------Favorites Alternative 1.2---------------------------------------
def add_favorites(list_photos=None, favorites=None):
    if favorites == None:
        favorites = Tree()

    for i in list_photos:
        scheme_photo = Photo(i)
        favorites.insert(scheme_photo)

    return favorites


def show_favorites(favorites):
    while True:
        favorites.show(5)
        print()
        option = int(input("""
        Options:
            1. PRINT All FAVORITES
            2. SEARCH
            3. EXIT FAVORITES
        """))

        if option == 1:
            favorites.show()

        elif option == 2:
            number = int(input("photo: "))
            update = int(input("To: "))
            start_time = time.time()
            favorites.search(number, update)
            end_time = time.time()
            print(end_time - start_time)

            break

        elif option == 3:
            break
# -------------------------------------------------------------------------
