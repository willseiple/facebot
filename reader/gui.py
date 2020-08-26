import tkinter as tk
from PIL import ImageTk, Image
from tkinter import filedialog
import sys
from os import path, getcwd


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
        # PyInstaller creates a temp folder and stores path in _MEIPASS
    base_path = getattr(sys, '_MEIPASS', getcwd())
    return path.join(base_path, relative_path)

def shorten_path(filename):
    '''
    returns final elem of path
    '''
    return filename.split('/')[-1]

def selected_res(event):
    '''
    sets global variable dims to resolution selected in res_drop dropdown
    '''
    global dims
    select = res_clicked.get()
    if select != 'Custom...':
        dims = dimensions[select]
    else:
        pass

def set_thumbnail(filename):
    '''
    '''
    global preview
    new_im = Image.open(filename)
    new_im.thumbnail((200, 200))
    preview = ImageTk.PhotoImage(new_im)
    preview_label.configure(image=preview)
    preview_label.image=preview


def selected_model(event):
    '''
    sets global variable model to model selected in menu_model dropdown
    '''
    global model_path
    global custom_flag
    global preview_label
    global model_name

    select = model_clicked.get()
    if select != 'Custom...':
        custom_flag = False
        model_name = select
        model_path = models[select]
        model_png = model_path.split('.')[0] + '.png'
        preview_filename = resource_path('reader/data/' + model_png)
        set_thumbnail(preview_filename)

    else:
        new_filename = filedialog.askopenfilename(initialdir=".", title="Browse files", filetypes=(("png files", "*.png"),("all files", "*.*")))
        print(new_filename)

        if new_filename == "":
            if custom_flag == True:
                model_clicked.set(shorten_path(model_path))
            else:
                model_clicked.set(shorten_path(model_name))

        else:
            custom_flag = True
            model_path = new_filename
            short_path = shorten_path(model_path)
            model_clicked.set(short_path)
            set_thumbnail(model_path)

def close():
    '''
    '''
    global clicked_flag
    clicked_flag = True
    root.destroy()

WIDTH = 400
HEIGHT = 200

models = {
        'Male bot' : 'willbot.mp4',
        'Male deepfake' : 'willfake.mp4',
        'Custom...' : None,
        }

models_keys = list(models.keys())

dimensions = {
            "4k" : (3840, 2160),
            "1440p" : (2560, 1440),
            "1080p" : (1920, 1080),
            "720p" : (1280, 720),
            "480p" : (852, 480),
            "Custom..." : None,
            }

dimensions_keys = list(dimensions.keys())

dims = dimensions['4k']
model_name = 'Male bot'
model_path = models[model_name]
clicked_flag = False
custom_flag = False
preview_path = resource_path('reader/data/' + model_path.split('.')[0] + '.png')

# define root
root = tk.Tk()

# format window
root.title('iDmission FaceBot')
root.geometry(str(WIDTH) + "x" + str(HEIGHT))
# icon = tk.Image('photo', file="reader/data/icon.gif")
# root.tk.call('wm','iconphoto', root._w, icon)

# define frames
topframe = tk.Frame(root, height=50)
topframe.pack(side='top', fill='x', pady=5)

bottomframe = tk.Frame(root, height=50)
bottomframe.pack(side='bottom', fill='x', pady=5)

leftframe = tk.Frame(root)
leftframe.pack(side='left', fill='y', pady=5)

rightframe = tk.Frame(root)
rightframe.pack(side='right', fill='y', pady=5)

# header
label = tk.Label(topframe, text='Settings').pack()

# dropdown labels
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
res_label = tk.Label(leftframe, text="Resolution:").grid(row=0, column=0)
model_label = tk.Label(leftframe, text="Model:").grid(row=1, column=0)

# variable to save dropdown results
res_clicked = tk.StringVar()
res_clicked.set(dimensions_keys[0])
model_clicked = tk.StringVar()
model_clicked.set(models_keys[0])
preview = tk.StringVar()

# drop down menus
res_drop = tk.OptionMenu(leftframe, res_clicked, *dimensions_keys, command=selected_res)
res_drop.grid(row=0, column=1, sticky='w')
model_drop = tk.OptionMenu(leftframe, model_clicked, *models_keys, command=selected_model)
model_drop.grid(row=1, column=1, sticky='w')

# preview box
preview_im = Image.open(preview_path)
preview_im.thumbnail((200,200))
preview = ImageTk.PhotoImage(preview_im)
preview_label = tk.Label(rightframe, image=preview)
preview_label.pack(side='right', fill='both')

# submit settings and continue to FaceBot
submit = tk.Button(bottomframe, text="Continue to FaceBot", command=close)
submit.pack()

root.mainloop()

def main():
    return dims, model_path, clicked_flag, custom_flag

if __name__ == '__main__':
    main()
