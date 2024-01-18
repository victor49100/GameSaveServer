import os
import shutil
import time
import tkinter as tk
from tkinter import ttk, filedialog
from tkinter import *
from functools import partial
import Main

root = Tk()
SelectedGameName = ''
selected_folder_path = StringVar()


def addGame():
    input = AddGame.get("1.0", END)
    Main.queryAdd(input)
    time.sleep(0.5)
    loadCombobox()


def create_zip_archive():
    global selected_folder_path
    global SelectedGameName
    folder_path = selected_folder_path.get()
    SelectedGameName = combobox.get()

    zip_file_name = f"{SelectedGameName}.zip"
    zip_file_path = f"{os.getcwd()}/{zip_file_name}"
    shutil.make_archive(SelectedGameName, 'zip', folder_path)
    print(f"Archive {SelectedGameName}.zip created successfully.")
    Main.pushZip(zip_file_path, SelectedGameName)


def loadCombobox():
    Jeux = Main.querySelectAllGames()
    game_names = [game['NomDuJeu'] for game in Jeux]
    combobox['values'] = game_names


def browse_button():
    folder_path = filedialog.askdirectory()
    Label2.config(text=folder_path)
    selected_folder_path.set(folder_path)


def update_label(event):
    global SelectedGameName  # Déclarer comme une variable globale
    SelectedGameName = combobox.get()


root.geometry('800x400')
root.configure(background='#F0F8FF')
root.title('Game Saver')

Label1 = Label(root, text='Game Saver')
Label1.place(x=340, y=20)

Label2 = Label(root, text='')
Label2.place(x=450, y=220)

Load = Button(root, text='Load', command=Main.querySelectAllGames)
Load.place(x=250, y=100)

Save = Button(root, text='Save', command=create_zip_archive)
Save.place(x=450, y=100)

Browse = Button(text="Browse", command=browse_button)
Browse.place(x=450, y=170)

AddGameButton = Button(text="Add Game", command=partial(addGame))
AddGameButton.place(x=650, y=130)

AddGame = Text(root, width=10, height=1)
AddGame.place(x=650, y=170)

combobox = ttk.Combobox(root, textvariable=Main.querySelectAllGames())
combobox.place(x=250, y=150, width=100, height=25)
try:
    loadCombobox()
    combobox.current(0)
except:
    print("pas de valeurs dans le combo box")

# Associez la fonction update_label à l'événement <<ComboboxSelected>>
combobox.bind("<<ComboboxSelected>>", update_label)

root.mainloop()
