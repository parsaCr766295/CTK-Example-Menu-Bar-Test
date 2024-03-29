import os
import tkinter as tk
from tkinter import filedialog, messagebox
import customtkinter

FONT_LARGE = ("Arial", 48)
ALLOWED_FILES = (("JPEG files", "*.jpg"), ("PNG files", "*.png"), ("All files", "*.*"))
SavedContent = "This is the final content."

class MyApp(customtkinter.CTk):
    """
    Custom application class with menu bar.
    """

    def __init__(self):
        super().__init__()

        self.default_folder = tk.StringVar(self)
        self.default_folder.set(os.path.expanduser("~"))

        self.geometry("400x200")
        self.title("CustomTkinter Sample Menu Bar")
        self.hello_label = customtkinter.CTkLabel(self, text="Hello World", font=FONT_LARGE)
        self.hello_label.grid(row=0, column=0, padx=10, pady=10)

        self.menu_bar = tk.Menu(self)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Open File", command=self.open_file)
        self.file_menu.add_command(label="Save File", command=self.save_final)
        self.file_menu.add_command(label="Set default folder", command=self.select_folder)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.quit)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

        self.theme_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.theme_menu.add_command(label="Light", command=lambda: self.theme_selection(1))
        self.theme_menu.add_command(label="Dark", command=lambda: self.theme_selection(2))
        self.theme_menu.add_command(label="Dark-blue", command=self.theme_selection_dark_blue)
        self.theme_menu.add_command(label="System", command=lambda: self.theme_selection(0))
        self.menu_bar.add_cascade(label="Theme", menu=self.theme_menu)

        helpmenu = tk.Menu(self.menu_bar, tearoff=0)
        helpmenu.add_command(label="About", command=self.about)
        self.menu_bar.add_cascade(label="Help", menu=helpmenu)

        self.config(menu=self.menu_bar)

    def open_file(self):
        """Open a file dialog and print the content."""
        filename = filedialog.askopenfilename(filetypes=ALLOWED_FILES)
        if filename:
            with open(filename, 'r') as file:
                content = file.read()
            print(content)

    def select_folder(self):
        """Select a folder and print the path."""
        initialdir = self.default_folder.get()
        folder = filedialog.askdirectory(initialdir=initialdir, title="Select folder containing student photos")
        if folder:
            print(f"Set default folder: {folder}")

    def save_final(self):
        """Save a file with default content."""
        initialdir = self.default_folder.get()
        title = "Save File"
        default_ext = "txt"
        filename = filedialog.asksaveasfilename(initialdir=initialdir, title=title, defaultextension=default_ext,
                                                filetypes=[("Text Files", "*.txt")])
        if filename:
            filepath = filename if filename.endswith(".txt") else f"{filename}.txt"
            try:
                with open(filepath, 'w') as file:
                    file.write(SavedContent)
            except Exception as e:
                messagebox.showerror("Error", f"Error saving file: {e}")

    def theme_selection(self, choice):
        """Change the theme."""
        if choice == 1:
            customtkinter.set_appearance_mode("Light")
        elif choice == 2:
            customtkinter.set_appearance_mode("Dark")
        elif choice == 0:
            customtkinter.set_appearance_mode("System")
        else:
            self.theme_selection_dark_blue()

    def theme_selection_dark_blue(self):
        """Change the theme to dark blue."""
        pass  # Add your custom theme implementation here

    def about(self):
        """Display about information."""
        messagebox.showinfo("About", "CustomTkinter Sample Menu Bar")

if __name__ == "__main__":
    app = MyApp()
    app.mainloop()
