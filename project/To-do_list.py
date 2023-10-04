import tkinter as tk
from tkinter import messagebox


def add_task():
    task = task_entry.get()
    if task:
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")


def update_task():
    selected_task = task_list.curselection()
    if selected_task:
        new_task = task_entry.get()
        if new_task:
            task_list.delete(selected_task)
            task_list.insert(selected_task[0], new_task)
            task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task!")


def remove_task():
    selected_task = task_list.curselection()
    if selected_task:
        task_list.delete(selected_task)


root = tk.Tk()
root.title("To-Do List")


task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)


task_list = tk.Listbox(root, width=40)
task_list.pack()


add_button = tk.Button(root, text="Add Task", command=add_task)
update_button = tk.Button(root, text="Update Task", command=update_task)
remove_button = tk.Button(root, text="Remove Task", command=remove_task)

add_button.pack(pady=5)
update_button.pack(pady=5)
remove_button.pack(pady=5)


root.mainloop()
