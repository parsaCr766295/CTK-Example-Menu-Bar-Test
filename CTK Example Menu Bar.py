import os
import tkinter as tk  # Preferably import only the required modules
from tkinter import filedialog , messagebox
import customtkinter

customtkinter.set_default_color_theme("dark-blue")
customtkinter.set_appearance_mode("blue")
# Pre-define some defaults
FONT_LARGE = ("Arial", 48)
ALLOWED_FILES = (("JPEG files", "*.jpg"), ("PNG files", "*.png"), ("All files", "*.*"))
SavedContent = "This is the final content."

class MyApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Initializing variables
        self.default_folder = tk.StringVar(self)
        self.default_folder.set(os.path.expanduser("~"))

        # Set window size and title
        self.geometry("400x200")
        self.title("CustomTkinter Sample Menu Bar")

        # Create a label for Hello World
        self.hello_label = customtkinter.CTkLabel(self, text="Hello World", font=FONT_LARGE)
        self.hello_label.grid(row=0, column=0, padx=10, pady=10)

        # Create a menu bar
        self.menu_bar = tk.Menu(self)

        # Create a File menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Open File", command=self.open_file)
        self.file_menu.add_command(label="Save File", command=self.save_final)
        self.file_menu.add_command(label="Set default folder", command=self.select_folder)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.quit)

        # Add the File menu to the menu bar
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

        # Create a Theme menu
        self.theme_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.theme_menu.add_command(label="Light", command=lambda: self.theme_selection(1))
        self.theme_menu.add_command(label="Dark", command=lambda: self.theme_selection(2))
        self.theme_menu.add_command(label="Dark-blue", command=self.theme_selection_dark_blue)
        self.theme_menu.add_command(label="System", command=lambda: self.theme_selection(0))

        # Add the Theme menu to the menu bar
        self.menu_bar.add_cascade(label="Theme", menu=self.theme_menu)

        # Create a Help menu
        helpmenu = tk.Menu(self.menu_bar, tearoff=0)
        helpmenu.add_command(label="About", command=self.about)

        # Add the Help menu to the menu bar
        self.menu_bar.add_cascade(label="Help", menu=helpmenu)

        # Set the menu bar for the window
        self.config(menu=self.menu_bar)

    def open_file(self):
        # Open a file dialog to select a file
        filename = filedialog.askopenfilename(filetypes=ALLOWED_FILES)
        if filename:
            # Read the content of the file
            with open(filename, 'r') as file:
                content = file.read()
            # Print the content of the file
            print(content)

    def select_folder(self):
        # Set the initial directory to the default folder
        initialdir = self.default_folder.get()
        # Open a directory dialog to select a folder
        self.default_folder = filedialog.askdirectory(initialdir=initialdir, title="Select folder containing student photos")
        # Print the selected folder
        print(f"Set default folder: {self.default_folder}")

    def save_final(self):
        # Set the initial directory to the default folder
        initialdir = self.default_folder
        # Set the title and default extension for the save file dialog
        title = "Save File"
        default_ext = "txt"
        # Open a file dialog to save a file
        filename = filedialog.asksaveasfilename(initialdir=initialdir, title=title, defaultextension=default_ext,
                                                filetypes=[("Text Files", "*.txt")])
        if filename:
            # Get the filepath with the .txt extension
            filepath = filename if filename.endswith(".txt") else f"{filename}.txt"
            # Write the SavedContent to the file
            with open(filepath, 'w') as file:
                file.write(SavedContent)

    def theme_selection(self, choice):
        if choice == 1:
            customtkinter.set_appearance_mode("Light")
        elif choice == 2:
            customtkinter.set_appearance_mode("Dark")
        else:
            customtkinter.set_appearance_mode("System")

    def theme_selection_dark_blue(self):
        customtkinter.set_appearance_mode("dark-blue")

    def about(self):
        # Show an info message box with the about text
        messagebox.showinfo("About", "Copyright 2024 All rights reserved.\nWebsite:https://github.com/parsaCr766295")

if __name__ == "__main__":
    app = MyApp()
    app.mainloop()
    app.destroy()
    # No need to explicitly destroy the window, it will be handled automatically
