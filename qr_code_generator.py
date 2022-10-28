from tkinter import *

root = Tk()

canvas = Canvas(root, width=400, height=600)
canvas.pack()
app_label = Label(root, text="QR Code Generator", fg="green", font=("Arial", 30))
canvas.create_window(200, 50, window=app_label)
name_label = Label(root, text="Link Name:", fg="red", bg="cyan")
link_label = Label(root, text="Link", fg="red", bg="cyan")
name_entry = Entry(root)
link_entry = Entry(root)
generate_button = Button(root, text="Generate", bg="black", fg="white")
canvas.create_window(200, 100, window=name_label)
canvas.create_window(200, 130, window=name_entry)
canvas.create_window(200, 160, window=link_label)
canvas.create_window(200, 190, window=link_entry)
canvas.create_window(200, 220, window=generate_button)
root.mainloop()
