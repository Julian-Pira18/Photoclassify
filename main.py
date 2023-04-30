from funcionalidad_1 import generate_random, add_queue, create_tree_photos
from My_queue import *
from My_tree import *
from menu import show_header, show_exit, show_options, show_invalid_input, show_project
import sys
import os


def main():
    # photos_Load = "C:\Users\piraj\proyecto_estructuras\assets"
    list_photos = generate_random()

    show_header()

    while True:
        option = show_options()

        if (option == 1):
            pass

        elif (option == 2):
            show_project()

        elif (option == 3):
            show_exit()
            try:
                sys.exit(0)
            except SystemError:
                os._exit(0)

        else:
            show_invalid_input()

        # queue_photo = add_queue(list_photos)
        # tree_photos = create_tree_photos(queue_photo)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        show_exit()
        try:
            sys.exit(0)
        except SystemError:
            os._exit(0)
