import tkinter as tk
from theme import Theme

class FileManagerApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Zenth")

        #Initialize the theme from the theme module
        self.theme = Theme()

    def themeMenu(self):
        defaultOption = tk.StringVar(value=self.theme.defaultTheme)
        tk.OptionMenu(self.root, defaultOption, *self.theme.themes.keys()).pack()
        return defaultOption

    def changingTheme(self, theme):
        print(theme)
        #self.root.config(bg=theme["background"], fg=theme["foreground"])