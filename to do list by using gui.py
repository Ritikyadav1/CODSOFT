import tkinter as tk
from tkinter import messagebox

def add_task():
    task_text = entry.get()  
    if task_text:
        listbox.insert(tk.END, task_text) 
        entry.delete(0, tk.END) 
    else:
        messagebox.showwarning("Warning", "Please enter a task.")


def remove_task():
    try:
        selected_task_index = listbox.curselection()[0]  
        listbox.delete(selected_task_index)  
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to remove.")


def clear_tasks():
    listbox.delete(0, tk.END)  


root = tk.Tk()
root.title("To-Do List")


entry = tk.Entry(root, width=40)
entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task)
remove_button = tk.Button(root, text="Remove Task", command=remove_task)
clear_button = tk.Button(root, text="Clear All Tasks", command=clear_tasks)

add_button.pack()
remove_button.pack()
clear_button.pack()


listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=40, height=10)
listbox.pack()


root.mainloop()
