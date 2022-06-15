#!/usr/bin/env python
 
import sys
import threading
import time
from queue import Queue

def add_input(input_queue):
    while True:
        input_queue.put(sys.stdin.read(1))

def foobar():
    input_queue = Queue()

    input_thread = threading.Thread(target=add_input, args=(input_queue,))
    input_thread.daemon = True
    input_thread.start()

    last_update = time.time()
    while True:

        if time.time()-last_update>0.5:
            sys.stdout.write(".")
            sys.stdout.flush()
            last_update = time.time()

        if not input_queue.empty():
            print("\ninput:", input_queue.get())

foobar()