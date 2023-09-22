import tkinter as tk

root = tk.Tk()
root.title("StickGirl")

canvas = tk.Canvas(root, width=200, height=200)
canvas.pack()

body_parts = []

def draw_stickgirl():
    global body_parts
    if not body_parts:
        body_parts.pop(0)
    if len(body_parts) == 6:
        canvas.create_text(100, 170, text="StickGirl is complete!", fill="#FF1493", font=("Arial", 12))

def mouse_click_handler(event):
    if len(body_parts) < 6:
        if len(body_parts) == 0:
            head = canvas.create_oval(80, 50, 120, 90, outline="black", fill="pink", width=2)
            body_parts.append(head)
        elif len(body_parts) == 1:
            body = canvas.create_line(100, 90, 100, 140, fill="black", width=2)
            body_parts.append(body)
        elif len(body_parts) == 2:
            left_leg = canvas.create_line(100, 140, 80, 180, fill="black", width=2)
            body_parts.append(left_leg)
        elif len(body_parts) == 3:
            right_leg = canvas.create_line(100, 140, 120, 180, fill="black", width=2)
            body_parts.append(right_leg)
        elif len(body_parts) == 4:
            left_arm = canvas.create_line(100, 100, 80, 150, fill="black", width=2, tags="arms")
            body_parts.append(left_arm)
        elif len(body_parts) == 5:
            right_arm = canvas.create_line(100, 100, 120, 150, fill="black", width=2, tags="arms")
            body_parts.append(right_arm)
        
        draw_stickgirl()

canvas.bind("<Button-1>", mouse_click_handler)

root.mainloop()
