import sys
import os
libs_path = os.path.join(os.path.dirname(__file__), 'libs')
sys.path.insert(0, libs_path)
import helper as h



def render():
    print(h.greeting('John', 'Wolf'))

render()