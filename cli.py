import os
from os.path import isfile, abspath
from file_to_dict import file2dict
from dict_to_file import dict2file


folder = os.getcwd()
print("You are at the folder " + folder + "\n")
foldername = input("Enter the path of the folder where we should look for the files: ")

try:
    os.chdir(foldername)
except FileNotFoundError:
    print("This folder does not exist !")

extents = ["csv", "json", "xml", "yaml", "yml"]
files = []
for file in os.listdir("."):
    if isfile(abspath(file)):
        ext = file.split('.')[-1]
        if ext in extents:
            files.append(file)

print()
print("Choose a file: ")
for i in range(len(files)):
    print(i + 1, '-', files[i])

print()
print("Choose a number")
your_choice = int(input("Enter your chosen number: "))

name = files[your_choice - 1].split('.')[0]
extent = files[your_choice - 1].split('.')[-1]
print("You chose: ", files[your_choice - 1])

yaml_list = ["yaml", "yml"]

if extent in yaml_list:
    extents.remove("yaml")
    extents.remove("yml")
else:
    extents.remove(extent)

print()

print("Choose an output format: ")
for format in extents:
    print(format, " ", end="")
print()

output_ext = ''
while output_ext not in extents:
    print("Choose the right output format: ")
    output_ext = input()

data = file2dict(files[your_choice - 1])
dict2file(data, name, output_ext)

