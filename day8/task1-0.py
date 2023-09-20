import tkinter as tk


def uppercase():
    text = entry.get()
    upper_text = text.upper()
    print(upper_text)

root = tk.Tk()
root.title("Tkinter Example")

label_frame = tk.LabelFrame(root, text="Label Frame")
label_frame.pack(padx=10, pady=10)

entry = tk.Entry(label_frame)
entry.pack(padx=10, pady=10)

button = tk.Button(label_frame, text="Submit", command=uppercase)
button.pack(padx=10, pady=10)

root.mainloop()
