import os
from My_queue import Queue, Node


photos_Load = "C:\Users\piraj\proyecto_estructuras\Look 2"


queue_photos = Queue()
for i in os.listdir(photos_Load):
    queue_photos.enqueue(i)
