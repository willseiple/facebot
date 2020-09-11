import reader.animator
import reader.gui

def main():
    '''
    ''' 
    cache = reader.gui.main()
    
    REL_PATH = cache['model_path']
    clicked_flag = cache['clicked_flag']
    custom_flag = cache['custom_flag']

    FILENAME = 'reader/data/' + REL_PATH
    WINDOW_SIZE = cache['dims']
    WINDOW_NAME = 'iDmission FaceBot'
    SCREEN_SIZE = cache['screen_size']

    # if custom_flag:
    #     print('Custom input coming soon, please select one of the premade models.')
    #     return

    if clicked_flag:
        reader.animator.main(FILENAME, WINDOW_SIZE, WINDOW_NAME, SCREEN_SIZE)

if __name__ == '__main__':
    main()

