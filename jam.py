import tkinter as tk
import time

def update_time():
    current_time = time.strftime('%H:%M:%S')
    label.config(text=current_time)
    root.after(1000, update_time)

root = tk.Tk()
root.title("Jam Digital Rafa")
root.geometry("300x150")
root.configure(bg="black")

label = tk.Label(root, font=('Arial', 40), bg="black", fg="lime")
label.pack(expand=True)

update_time()
root.mainloop()