import tkinter as tk

# Create a tkinter window
root = tk.Tk()
root.title("StickGirl")

# Create a canvas to draw on
canvas = tk.Canvas(root, width=200, height=200)
canvas.pack()

left_arm_coords = [100, 100, 80, 150]
right_arm_coords = [100, 100, 120, 150]

left_arm_direction = -1 
right_arm_direction = -1

def animate_arms():
    global left_arm_coords, right_arm_coords, left_arm_direction, right_arm_direction
    left_arm_coords[3] += 5 * left_arm_direction
    right_arm_coords[3] += 5 * right_arm_direction
    if left_arm_coords[3] >= 150 or left_arm_coords[3] <= 100:
        left_arm_direction *= -1
    if right_arm_coords[3] >= 150 or right_arm_coords[3] <= 100:
        right_arm_direction *= -1
    canvas.delete("arms")
    canvas.create_line(left_arm_coords, fill="black", width=2, tags="arms")
    canvas.create_line(right_arm_coords, fill="black", width=2, tags="arms")
    canvas.after(100, animate_arms)

head = canvas.create_oval(50, 50, 110, 90, outline="black", fill="pink", width=2)
body = canvas.create_line(100, 90, 100, 140, fill="black", width=2)
left_leg = canvas.create_line(100, 140, 80, 180, fill="black", width=2)
left_lower_leg = canvas.create_line(80, 180, 70, 200, fill="black", width=2)
right_leg = canvas.create_line(100, 140, 120, 180, fill="black", width=2)
right_lower_leg = canvas.create_line(120, 180, 130, 200, fill="black", width=2)
left_arm = canvas.create_line(left_arm_coords, fill="black", width=2, tags="arms")
rope = canvas.create_line(100, 10, 100, 100, fill="red", width=6)
pole = canvas.create_line(10, 0, 10, 200, fill="Brown", width=6)
pole1 = canvas.create_line(0, 10, 170, 10, fill="Brown", width=6)

canvas.create_line(right_arm_coords, fill="black", width=2, tags="arms")
text = canvas.create_text(100, 40, text="Stick-Girl", fill="#FF1493")

animate_arms()

root.mainloop()
