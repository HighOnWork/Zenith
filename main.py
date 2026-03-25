import os
from graphics import FileManagerApp

def main():
    #Lists the files in the current directory
    app = FileManagerApp()
    choosenTheme = app.themeMenu()
    names = os.listdir('.')
    print(f"The files in the current directory are: {names}")
    app.root.mainloop()

if __name__ == '__main__':
    main()
    