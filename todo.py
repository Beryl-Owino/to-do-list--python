from tkinter import *
from tkinter import ttk

class Todo:
    def __init__(self, root):
        self.root = root
        self.root.title('To_do_list')
        self.root.geometry('650x410+300+150')

        # Use a tuple to define the font
        font_tuple = ('ariel', 25, 'bold')
        font_tuple2 = ('ariel', 18, 'bold')
        
        self.label = Label(self.root, text='To-Do-List-App', 
                           font=font_tuple, width=10, bd=5, bg='orange', fg='black')
        self.label.pack(side='top', fill=BOTH)

        self.label2 = Label(self.root, text='Add Task', 
                           font=font_tuple2, width=10, bd=5, bg='orange', fg='black')
        self.label2.place(x=40, y=54)

        self.label3 = Label(self.root, text='Tasks', 
                           font=font_tuple2, width=10, bd=5, bg='orange', fg='black')
        self.label3.place(x=320, y=54)

        self.main_text = Listbox(self.root, height=9, bd=6, width=23, font="ariel, 20 italic bold")
        self.main_text.place(x=280, y=100)

        self.text = Text(self.root, bd=5, height=2, width=30, font='ariel, 10 bold')
        self.text.place(x=20, y=120)

        self.button_add = Button(self.root, text='Add', font='arial 20 bold italic',
                         width=10, bd=5, bg='orange', fg='black', command=self.add)
        self.button_add.place(x=30, y=180)

        self.button_delete = Button(self.root, text='Delete', font='ariel 20 bold italic',
                                    width=10, bd=5, bg='orange', fg='black', command=self.delete)
        self.button_delete.place(x=30, y=300)

        try:
            with open('data.txt', 'r') as file:
                lines = file.readlines()
                for line in lines:
                    self.main_text.insert(END, line.strip())
        except FileNotFoundError:
    # If the file doesn't exist, create an empty one
                open('data.txt', 'w').close()


    def add(self):
        content = self.text.get(1.0, END)
        self.main_text.insert(END, content)
        with open('data.txt', 'a') as file:
            file.write(content)
        self.text.delete(1.0, END)

    def delete(self):
        delete_ = self.main_text.curselection()
        for index in reversed(delete_):
            self.main_text.delete(index)

        # Update the data file after deletion
        with open('data.txt', 'w') as file:
            items = self.main_text.get(0, END)
            file.writelines(items)

def main():
    root = Tk()
    ui = Todo(root)
    root.mainloop()

if __name__ == "__main__":
    main()
