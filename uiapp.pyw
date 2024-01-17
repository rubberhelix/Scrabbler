import tkinter as tk

root = tk.Tk()

# Two checkboxes at the top
for i in range(2):
    tk.Checkbutton(root).grid(row=0, column=i)

# 15 letter inputs in one row with 2 checkboxes below each
for i in range(15):
    tk.Entry(root, width=2).grid(row=1, column=i)
    for j in range(2):
        tk.Checkbutton(root).grid(row=2+j, column=i)

# Submit button
tk.Button(root, text="Submit").grid(row=4, column=0, columnspan=15)

root.mainloop()