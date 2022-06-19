import tkinter as tk

window=tk.Tk()
# add widgets here

window.title('Hello Python')
label = tk.Label(text='Hello World')

label.pack()

window.geometry("300x200+10+20")
window.mainloop()