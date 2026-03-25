class Theme:
    

    def __init__(self):

        self.defaultTheme = "Dark"

        self.themes = {
            "Dark": {
                "foreground": "#FFFFFF",
                "background": "#000000"
            },
            "Light": {
                "foreground": "#000000",
                "background": "#FFFFFF"
            },
            "Gruvbox": {
                "foreground": "#EBDBB2",
                "background": "#282828"
            },
            "Plum": {
                "foreground": "#E5C1FF",
                "background": "#2D1B4E"
            }
        }
