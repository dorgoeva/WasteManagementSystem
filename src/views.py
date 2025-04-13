import tkinter as tk

class WasteView:
    def __init__(self, root):
        self.root = root
        self.root.title("Waste Management System")
        tk.Label(root, text="Name").pack()
        self.name_entry = tk.Entry(root)
        self.name_entry.pack()
        tk.Button(root, text="Schedule Pickup").pack()
