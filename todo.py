"""ToDo List"""
import json
from tkinter import *
from tkinter import messagebox

window = Tk()
window.title('ToDo')
window.geometry('300x230') # window size

start_dict = {}
len_list = []
i = None

with open("data_file.json", "r") as read_file: # read data file
    start_dict = json.load(read_file)

task_listbox = Listbox(font = ('Arial Bold', 10))

def start(start_dict):
    """Check start file"""
    if start_dict == {}:
        task_listbox.insert(END, "No tasks")
    else:
        for tasks in start_dict:
            task_listbox.insert(END, str(tasks) + ") " + start_dict[tasks])

    for task in start_dict:
        len_list.append(task) # start count list

    task_listbox.grid(row = 0, column = 0, padx = 15, columnspan = 3, sticky=W+E)

start(start_dict)
i = len(len_list) + 1 # count number

def add():
    """Add task action"""
    global i
    task = task_entry.get()
    dict = {i: task}
    i += 1
    start_dict.update(dict) # upd start dict
    task_listbox.delete(0, i)
    start(start_dict)

def del_data():
    """Delete all data action"""
    global i
    task_listbox.delete(0, i)
    start_dict.clear()
    i = 1
    with open("data_file.json", "w") as write_file:
        json.dump(start_dict, write_file, indent=4)
    messagebox.showinfo("Ok", "The data was successfully removed")

def save():
    """Save data action"""
    with open("data_file.json", "w") as write_file: # write data file
        json.dump(start_dict, write_file, indent=4)
    messagebox.showinfo("Ok", "The data was successfully saved")

task_label = Label(text = "Enter task:", font = ('Arial Bold', 13))
task_label.grid(row = 1, column = 0) # grid positioning

task_entry = Entry(window, width = 20, font = ('Arial Bold', 10))
task_entry.grid(row = 1,column = 1)

btn_add = Button(text = "Add", command = add, font = ('Arial Bold', 10), width = 5)
btn_add.grid(row = 1, column = 2)

btn_del = Button(text = "Delete data", command = del_data, font = ('Arial Bold', 10))
btn_del.grid(row = 3, column = 0)

btn_save = Button(text = "Save", command = save, font = ('Arial Bold', 10), width = 5)
btn_save.grid(row = 3, column = 2)

window.mainloop() # infinite loop of Windows is always necessary
