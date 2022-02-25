from tkinter import *
from tkinter.filedialog import askopenfilename, askdirectory
from pathlib import Path
from os.path import abspath
from os.path import basename
from os import chdir
from file_to_dict import file2dict
from dict_to_file import dict2file


root = Tk()
root.title('Xml-Json-Csv-Yaml converter')
root.geometry('700x700')
root.resizable(True, True)

data = ''

def output_extent(data, choice_name, self):
    """ Output the extent of the file

    Args:
        data (dict): a dictionary
        choice_name (str): the name of the file chosen by the user.
    """
    print(self)
    output_folder = askdirectory()
    chdir(abspath(output_folder))
    dict2file(data, choice_name, self)


def construct_button(data, choice_name, extent):
    """construction of file output choices

    Args:
        data (dict): a dictionary
        choice_name (str): the name of the file chosen by the user.
        extent (str): the file extension
    """
    button_1 = Button(root, text = extent[0], command = lambda: output_extent(data, choice_name, extent[0]))
    button_2 = Button(root, text = extent[1], command = lambda: output_extent(data, choice_name, extent[1]))
    button_3 = Button(root, text = extent[2], command = lambda: output_extent(data, choice_name, extent[2]))

    button_1.grid(row=4, column=2)
    button_2.grid(row=4, column=3)
    button_3.grid(row=4, column=4)


def recup_file():
    """Recovered File
    """
    file = askopenfilename(title='Open file',
                       filetypes=[("files",".xml .json .yml .yaml .csv")],
                       initialdir=str(Path.home()))

    extents = ['csv', 'json', 'xml', 'yaml', 'yml']
    chemin_file = abspath(file)
    file = basename(file).split('.')
    choice_name = file[0]
    choice_extent = file[-1]
    if choice_extent in ['yaml', 'yml']:
        extents.remove('yaml')
        extents.remove('yml')
    else:
        extents.remove(choice_extent)
    data = file2dict(chemin_file)
    construct_button(data, choice_name, extents)






filing = Label(root, text='Please add a file', font=('Helvetica', 18), 
               bg='red', fg='white', bd=1, relief="sunken")
filing.pack(pady=20)
filing_btn = Button(root, text='Load file', command=recup_file)

output_line = Label(root, text='', anchor='w', justify='center')

filing.grid(row=1, column=1)
filing_btn.grid(row=2, column=1)

root.mainloop()
