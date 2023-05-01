import os
from My_queue import Queue, Node
import random
from My_tree import *
from list_dinamic import *
from models import *
from funcionalidad_1 import *
from My_Stack import *


def add_favorites(data, favorites=None, incial=True,):
    if incial == False:
        favorites = Stack()

    favorites.enqueue(data)
    return favorites
