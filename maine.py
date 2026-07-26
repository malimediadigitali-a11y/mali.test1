import tkinter as tk

def update_label():
    name = entry_name.get()
    age = entry_age.get()
    output = f"Hello, {name}! You are {age} years old."
    label_output.config(text=output)
print("wait mali")
root = tk.Tk()
root.title("Adeshborde Interactivy")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

tk.Label(frame, text="Enter your name:").grid(row=0, column=0, sticky="e")
entry_name = tk.Entry(frame)
entry_name.grid(row=0, column=1)

tk.Label(frame, text="Enter your age:").grid(row=1, column=0, sticky="e")
entry_age = tk.Entry(frame)
entry_age.grid(row=1, column=1)

btn = tk.Button(frame, text="Submit", command=update_label)
btn.grid(row=2, columnspan=2, pady=10)

label_output = tk.Label(frame, text="")
label_output.grid(row=3, columnspan=2)

root.mainloop()