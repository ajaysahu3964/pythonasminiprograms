from tkinter import*
from tkinter import ttk

class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550*800+0+0")
        
        if __name__ == "__main__":
            root=Tk()
            app=logic_Window(root)
            root.mainloop()