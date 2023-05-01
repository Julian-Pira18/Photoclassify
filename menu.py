from colorama import Fore


def show_line():
    print(Fore.MAGENTA + "-----------------------------------------------")


def show_header():
    show_line()
    text = """  

                  ____    
                 /___/\_                     
                _\   \/_/\__                
              __\       \/_/\                 
              \   __    __ \ \                    
             __\  \_\   \_\ \ \   __        
            /_/\\\   __   __  \ \_/_/\         
            \_\/_\__\/\__\/\__\/_\_\/          
               \_\/_/\       /_\_\/           
                  \_\/       \_\/       
    
                   PhotoClassif

"""
    print(Fore.BLUE + text)
    show_line()


def show_photo():
    pass


def show_options() -> int:
    text = """
    
    Options: 
        1. PRINT All IDs OF THE PHOTOS
        2. PRINT PROJECT INFO
        3. EXIT OF PROGRAM
    
"""
    print(Fore.BLUE + text)
    opt = input("\n")

    try:
        opt = int(opt.strip())
    except ValueError:
        opt = -1

    show_line()
    return opt


def show_project():
    text = """
    Name: PhotoClassif

    Participants:
                Julian Pira 
                Daniel Garcia
                Anderson Barrera 
                Camilo Rodriguez
    
    Ing. Systems and Computing
    National university of Colombia
    """

    print(Fore.BLUE + text)


def show_invalid_input():
    text = """
    
        Set a valid option man -_- 

"""

    print(Fore.BLUE + text)


def show_exit():
    text = """

        Came back 🥵.

"""
    print(Fore.BLUE + text)
    show_line()
