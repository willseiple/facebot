import reader.animator
import reader.gui
from os import path, getcwd
import sys

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
        # PyInstaller creates a temp folder and stores path in _MEIPASS
    base_path = getattr(sys, '_MEIPASS', getcwd())
    return path.join(base_path, relative_path)

def main():
    '''
    ''' 
    WINDOW_SIZE, REL_PATH, clicked_flag, custom_flag = reader.gui.main()
    FILENAME = resource_path('reader/data/' + REL_PATH)
    WINDOW_NAME = 'iDmission FaceBot'

    if clicked_flag:
        reader.animator.main(FILENAME, WINDOW_SIZE, WINDOW_NAME)

if __name__ == '__main__':
    main()

