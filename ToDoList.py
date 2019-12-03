#!/usr/bin/env python3
"""
Date Created: 10-07-2019
Developed By: Mevada Dhruvik
E-mail: dhruvikhm98@gmail.com

"""

import tkinter

root = tkinter.Tk()
root.configure(bg='white')
root.title("My To-do list")
root.geometry("300x250")

tasks = []
# empty list to store task


# Functions


def update_list():
    clear_list()
    for i in tasks:
        lbl_display.insert("end", i)


def clear_list():
    lbl_display.delete(0, "end")


def add_new():
    i = txt_input.get()
    tasks.append(i)
    update_list()


def del_single():
    task_del = lbl_display.get("active")
    if task_del in tasks:
        tasks.remove(task_del)
    update_list()


def del_all():
    global tasks
    tasks = []
    update_list()


# GUI Starts
lbl_title = tkinter.Label(root, text="To-Do List", bg='white')
lbl_title.grid(row=0, column=0, padx=10)
txt_input = tkinter.Entry(root, width=25)
txt_input.grid(row=2, column=1, padx=10)
btn_add = tkinter.Button(root, text="Add", fg="green", command=add_new)
btn_add.grid(row=2, column=0, padx=10)
btn_add.config(width=10, height=1)
btn_del = tkinter.Button(root, text="Delete", fg="red", command=del_single)
btn_del.grid(row=3, column=0, padx=10)
btn_del.config(width=10, height=1)
btn_dellall= tkinter.Button(root, text="Delete All", fg="red", command=del_all)
btn_dellall.grid(row=4, column=0, padx=10)
btn_dellall.config(width=10, height=1)
btn_exit = tkinter.Button(root, text="Exit", command=exit)
btn_exit.grid(row=5, column=0, padx=10)
btn_exit.config(width=10, height=1)
lbl_display = tkinter.Listbox(root, width=25, height=5)
lbl_display.grid(row=3, column=1, rowspan=10, padx=10)
# GUI ends


root.mainloop()
