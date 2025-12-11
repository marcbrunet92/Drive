import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

filename=''

# create the root window
# root = tk.Tk()
# root.title('Cliquez sur le bouton')
# root.resizable(False, False)
# root.geometry('300x150')


def select_files():
    global filename
    tk.Tk().withdraw()
    filetypes = (
        ('spectres IR','*.jdx'),
        ('fichiers texte', '*.txt'),
        ('tout type', '*.*')
    )

    filename = fd.askopenfilename(
        title='Sélection du fichier',
        initialdir='.',
        filetypes=filetypes)

    # showinfo(
    #     title='Selected Files',
    #     message=filename
    # )


# # open button
# open_button = ttk.Button(
#     root,
#     text='Sélection du fichier',
#     command=select_files
# )
#
# open_button.pack(expand=True)
#
# root.mainloop()
# tk.Tk().withdraw()
select_files()
print(filename)