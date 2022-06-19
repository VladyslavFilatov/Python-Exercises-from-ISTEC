import tkinter as tk
from tkinter import *



class Root(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title = "a minha app"
        self.configure(bg="red")
        print(self.configure().keys())

        self.left_frame = tk.Frame(self, bg="red")
        self.left_frame.pack(side=tk.LEFT)

        self.txt1 = tk.Label(self.left_frame, text="Texto 1", bg="blue", fg="black")
        self.txt1.grid(row=0, column=0)

        self.right_frame = tk.Frame(self, bg="blue")
        self.right_frame.pack(side=tk.LEFT)


        self.txt2 = tk.Label(self.right_frame, text="Olá ISTEC")
        self.txt2.grid(row=0, column=0)

        self.l1 = tk.Label(self.left_frame, text="User Name")
        self.l1.grid(row=1, column=0)

        self.l2 = Entry(self.right_frame, bd=5)
        self.l2.grid(row=1, column=0)

        def ChangeLabelText():
            self.txt2.config(text=self.l2.get())

        self.button = tk.Button(self.left_frame, text="Hey", bg="white", fg="black", command=ChangeLabelText)
        self.button.grid(row=1, column=1)
