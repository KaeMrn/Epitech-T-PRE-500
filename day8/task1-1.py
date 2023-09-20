import tkinter as tk
from PIL import Image, ImageTk  

window = tk.Tk()
window.title("Under the sea")

frame = tk.Frame(window, relief="raised", borderwidth=10)
frame.pack(padx=20, pady=20)

canvas = tk.Canvas(frame, width=400, height=300)
canvas.pack()

image = Image.open("sea.png") 
image = image. resize((400, 300))
photo = ImageTk.PhotoImage(image)

canvas.create_image(0, 0, image=photo, anchor=tk.NW) 

window.mainloop()
