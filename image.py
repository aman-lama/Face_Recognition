from tkinter import *
import os

def AddDataset():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry('300x250')
    global username
    global TextField
    global Reader
    global username_entry
    global TextField_entry
    global Reader_entry
    username = StringVar()
    TextField = StringVar()
    Reader = StringVar()
    Label(screen1, text = "please enter detail below").pack()
    Label(screen1, text = "").pack()
    Label(screen1, text=" username ").pack()
    username_entry = Entry(screen1, textvariable=username)
    username_entry.pack()

    TextField_entry= Entry(screen1, textvariable = TextField)
    Button(screen1, text="Reader", height="2", width="30", command=upload_reader).pack()
    Label(screen1, text="").pack()

def upload_reader():
    os.system('python3 reader.py')
def upload_recog():
    os.system('python3 recog.py')

def TextField():
    global screen4
    screen4 = Toplevel(screen)
    screen4.title("TextField")
    screen4.geometry('300x250')
    Label(screen4, text="please enter detail below").pack()
    Label(screen4, text="").pack()


def Reader():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Reader")
    screen2.geometry('300x250')
    global welcome
    global welcome_entry
    welcome = StringVar()
    Label(screen2, text="please enter detail below").pack()
    Label(screen2, text="").pack()
    Button(screen2, text="welcome", width=10, height=1, command=welcome).pack()
    Label(screen2, text="").pack()





def login():
        global screen3
        screen3 = Toplevel(screen)
        screen3.title("Login")
        screen3.geometry('300x250')
        Label(screen3,text="please enter detail below").pack()
        Label(screen3, text="").pack()


def main_screen():
    global screen
    screen =Tk()
    screen.geometry("320x250")
    screen.title("recog")
    Label(text = "").pack()
    Button(text = "Login", height = "2", width = "30", command = upload_recog).pack()
    Label(text = "").pack()
    Button(text = "AddDataset",height = "2", width = "30", command = AddDataset).pack()
    screen.mainloop()

main_screen()

