import tkinter as tk
from tkinter import filedialog

class TabEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Guitar Tab Editor")

        self.text = tk.Text(root)
        self.text.pack(expand=True, fill='both')

        menu = tk.Menu(root)
        file_menu = tk.Menu(menu, tearoff=0)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        menu.add_cascade(label="File", menu=file_menu)
        root.config(menu=menu)

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, 'r') as file:
                content = file.read()
                self.text.delete(1.0, tk.END)
                self.text.insert(tk.END, content)

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, 'w') as file:
                content = self.text.get(1.0, tk.END)
                file.write(content)
