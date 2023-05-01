from funcionalidad_1 import generate_random, add_queue, create_tree_photos, call, call_list, call_linked
from My_queue import *
from My_tree import *
from menu import show_header, show_exit, show_options, show_invalid_input, show_project
import sys
import time
import os


def main():
    # photos_Load = "C:\Users\piraj\proyecto_estructuras\assets"
    list_photos = generate_random()
    import_photo = 0
    load_photos = 0
    show_header()

    while True:
        option = show_options()

        if (option == 1):
            # ------------ Alternative1.1---------
            start_time = time.time()

            if import_photo and load_photos:
                photos = call(list_photos, import_photo, load_photos)
            else:
                photos = call(list_photos)

            end_time = time.time()
            print(end_time - start_time)

            list_photos = []
            list_photos = generate_random()

            # ------------------------------------

            # # ------------ Alternative1.2---------
            # start_time = time.time()
            # if import_photo and load_photos:
            #     photos = call_list(list_photos, import_photo, load_photos)
            # else:
            #     photos = call_list(list_photos)

            # end_time = time.time()
            # print(end_time - start_time)

            # # list_photos = []
            # list_photos = generate_random()

            # ---------------Alternative 1.3-----------

            # start_time = time.time()
            # if import_photo and load_photos:
            #     photos = call_linked(list_photos, import_photo, load_photos)

            # else:
            #     photos = call_linked(list_photos)

            # end_time = time.time()
            # print(end_time - start_time)

            # list_photos = []
            # list_photos = generate_random()

            # ----------------------------------------

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


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        show_exit()
        try:
            sys.exit(0)
        except SystemError:
            os._exit(0)
