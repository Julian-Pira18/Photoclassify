from funcionalidad_1 import generate_random, add_queue, create_tree_photos, call, add_favorites
from My_queue import *
from My_tree import *
from menu import show_header, show_exit, show_options, show_invalid_input, show_project
import sys
import time
import os


def main():
    # photos_Load = "C:\Users\piraj\proyecto_estructuras\assets"
    list_photos = generate_random()
    queue_photo = 0
    tree_photos = 0
    favorite = 0
    show_header()

    while True:
        option = show_options()
        list_photos = generate_random()
        if (option == 1):
            start_time = time.time()

            if queue_photo and tree_photos:
                photos = call(list_photos, queue_photo, tree_photos)
            else:
                photos = call(list_photos)

            end_time = time.time()
            print(end_time - start_time)
            print(photos.root.data.show())

        elif (option == 2):
            show_project()

        elif (option == 3):
            show_exit()
            try:
                sys.exit(0)
            except SystemError:
                os._exit(0)

        # Agregacion de fotos favoritas
        elif (option == 4):
            data = input("")
            if favorite == None:
                favorite = add_favorites(data, tree_photos, False)
        else:
            show_invalid_input()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        show_exit()
        try:
            sys.exit(0)
        except SystemError:
            os._exit(0)
