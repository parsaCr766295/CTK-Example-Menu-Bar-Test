import os
import tkinter as tk  # Importing the tkinter module for creating the GUI
from tkinter import filedialog , messagebox  # Importing specific functions from tkinter
import customtkinter  # Importing the customtkinter module for custom GUI components

# Pre-defining some defaults
FONT_LARGE = ("Arial", 48)  # Defining a large font for a label
ALLOWED_FILES = (("JPEG files", "*.jpg"), ("PNG files", "*.png"), ("All files", "*.*"))  # Allowed file types for opening and saving files
SavedContent = "This is the final content."  # Default content for saving a file

class MyApp(customtkinter.CTk):  # Defining a custom class inheriting from CTk
    def __init__(self):
        super().__init__()  # Initializing the superclass

        # Initializing variables
        self.default_folder = tk.StringVar(self)  # Creating a StringVar for storing the default folder path
        self.default_folder.set(os.path.expanduser("~"))  # Setting the default folder path to the user's home directory

        self.geometry("400x200")  # Setting the window size
        self.title("CustomTkinter Sample Menu Bar")  # Setting the window title
        self.hello_label = customtkinter.CTkLabel(self, text="Hello World", font=FONT_LARGE)  # Creating a custom label with a large font
        self.hello_label.grid(row=0, column=0, padx=10, pady=10)  # Placing the label in the grid

        self.menu_bar = tk.Menu(self)  # Creating a menu bar
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)  # Creating a file menu
        self.file_menu.add_command(label="Open File", command=self.open_file)  # Adding an "Open File" command to the file menu
        self.file_menu.add_command(label="Save File", command=self.save_final)  # Adding a "Save File" command to the file menu
        self.file_menu.add_command(label="Set default folder", command=self.select_folder)  # Adding a "Set default folder" command to the file menu
        self.file_menu.add_separator()  # Adding a separator to the file menu
        self.file_menu.add_command(label="Exit", command=self.quit)  # Adding an "Exit" command to the file menu
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)  # Adding the file menu to the menu bar

        self.theme_menu = tk.Menu(self.menu_bar, tearoff=0)  # Creating a theme menu
        self.theme_menu.add_command(label="Light", command=lambda: self.theme_selection(1))  # Adding a "Light" theme command to the theme menu
        self.theme_menu.add_command(label="Dark", command=lambda: self.theme_selection(2))  # Adding a "Dark" theme command to the theme menu
        self.theme_menu.add_command(label="Dark-blue", command=self.theme_selection_dark_blue)  # Adding a "Dark-blue" theme command to the theme menu
        self.theme_menu.add_command(label="System", command=lambda: self.theme_selection(0))  # Adding a "System" theme command to the theme menu
        self.menu_bar.add_cascade(label="Theme", menu=self.theme_menu)  # Adding the theme menu to the menu bar

        helpmenu = tk.Menu(self.menu_bar, tearoff=0)  # Creating a help menu
        helpmenu.add_command(label="About", command=self.about)  # Adding an "About" command to the help menu

        self.menu_bar.add_cascade(label="Help", menu=helpmenu)  # Adding the help menu to the menu bar

        self.config(menu=self.menu_bar)  # Configuring the window with the menu bar

    def open_file(self):
        filename = filedialog.askopenfilename(filetypes=ALLOWED_FILES)  # Opening a file dialog for selecting a file
        if filename:  # If a file is selected
            with open(filename, 'r') as file:  # Opening the file in read mode
                content = file.read()  # Reading the file content
            print(content)  # Printing the file content

    def select_folder(self):
        initialdir = self.default_folder.get()  # Getting the default folder path
        self.default_folder = filedialog.askdirectory(initialdir=initialdir, title="Select folder containing student photos")  # Opening a folder dialog for selecting a folder
        print(f"Set default folder: {self.default_folder}")  # Printing the selected folder path

    def save_final(self):
        initialdir = self.default_folder  # Getting the default folder path
        title = "Save File"  # Setting the save file dialog title
        default_ext = "txt"  # Setting the default file extension
        filename = filedialog.asksaveasfilename(initialdir=initialdir, title=title, defaultextension=default_ext,
                                                filetypes=[("Text Files", "*.txt")])  # Opening a save file dialog
        if filename:  # If a file is selected for saving
            filepath = filename if filename.endswith(".txt") else f"{filename}.txt"  # Setting the filepath with the ".txt" extension if not provided
            with open(filepath, 'w') as file:  # Opening the file in write mode
                file.write(SavedContent)  # Writing the default content to the file

    def theme_selection(self, choice):
        if choice == 1:  # If the "Light" theme is selected
            customtkinter.set_appearance_
