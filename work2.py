# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 15:14:22 2024

@author: ASUS
"""
import tkinter as tk
from tkinter import messagebox


def validate_login ():
    username = username_entry.get()
    password = password_entry.get()
    
    if username == "admin" and password == "1981":
       messagebox.showinfo("Login successfull" , "Information")
       open_second_window()
    else :
        messagebox.showerror("Login failed", "Try again")

def open_second_window():
    second_window = tk.Toplevel(root)
    second_window.title("second page")
    second_window.geometry("300x400")
    label = tk.Label(second_window, text="Welcome to the second page!")
    label.pack(pady=5)

root = tk.Tk()
root.title("Login form")
root.geometry("300x400")


username_label = tk.Label(root, text="Username:")
username_label.pack(pady=5)
username_entry = tk.Entry(root)
username_entry.pack(pady=5)

password_label = tk.Label(root, text="Username:")
password_label.pack(pady=5)
password_entry = tk.Entry(root)
password_entry.pack(pady=5)

btn = tk.Button(root, text="Login", command=validate_login).pack(pady=20)

print("I want to change something in here, just for test")
print("this test is for another course")

root.mainloop ()