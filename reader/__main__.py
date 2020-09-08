import reader.animator
import reader.gui
from os import path, getcwd
import sys

def main():
    '''
    ''' 
    cache = reader.gui.main()
    WINDOW_SIZE = cache['dims']
    REL_PATH = cache['model_path']
    clicked_flag = cache['clicked_flag']
    custom_flag = cache['custom_flag']
    check = cache['check']
    SCREEN_SIZE = cache['screen_size']

    FILENAME = reader.gui.resource_path('reader/data/' + REL_PATH)
    WINDOW_NAME = 'iDmission FaceBot'

    if custom_flag:
        print('Custom input coming soon, please select one of the premade models.')
        return

    if clicked_flag:
        reader.animator.main(FILENAME, WINDOW_SIZE, WINDOW_NAME, SCREEN_SIZE)

if __name__ == '__main__':
    main()

