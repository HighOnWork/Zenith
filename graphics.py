import tkinter as tk
from theme import Theme

class FileManagerApp:
    def __init__(self):
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=800, height=600)
        self.canvas.pack()
        self.root.title("Zenth")
        self.root.geometry("800x600")

        #Initialize the theme from the theme module
        self.theme = Theme()

    def themeMenu(self):
        defaultOption = tk.StringVar(value=self.theme.defaultTheme)
        tk.OptionMenu(self.canvas, defaultOption, *self.theme.themes.keys()).pack()
        return defaultOption

    def changingTheme(self, theme):
        selectedTheme = theme.get().capitalize()
        self.root.configure(bg=self.theme.themes[selectedTheme]["background"])
        self.root.after(1000, lambda: self.changingTheme(theme=theme))
