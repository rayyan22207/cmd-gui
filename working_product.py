from tkinter import *
import subprocess
import os


def _subprocess(what, SCREEN):
    try:
        output = subprocess.check_output(what, shell=True)
        global OUTPUT
        OUTPUT = output.decode()
        sc = SCREEN
        Label(sc, text=output.decode())
        print(output.decode())

    except Exception as e:
        print(e)

def screen_for_find():
    global screen1
    screen1 = Toplevel(screen)
    screen1.geometry("850x950")
    screen1.title("Find a file")
    global entry2
    entry2 =  Entry(screen1, width=50, borderwidth=10, fg="yellow", bg="black")
    entry2.pack()
    Label(screen1,text="").pack()
    Label(screen1,text="").pack()
    Button(screen1, text= "submit", height="2", width="30", command=Find).pack()

def Find():
    
    Label(screen1,text="this might take a while").pack()
    name = entry2.get()
    start_dir = "the starting dir e.g c:/Users"

    for dirpath, dirnames, filenames in os.walk(start_dir):
        if name in dirnames or name in filenames:
            path = os.path.join(dirpath, name)
            Label(screen1,text="").pack()
            Label(screen1,text="Path: " + path).pack()
            
            if os.path.isfile(path):
                if os.path.exists(path):
                    with open(path, "r") as file:
                        content = file.read()
                        Label(screen1,text="").pack()
                        Label(screen1,text="Content: "+ content).pack()
                        
                else:
                    Label(screen1,text="").pack()
                    Label(screen1,text="File does not exist").pack()
                    
            elif os.path.isdir(path):
                entries = os.listdir(path)
                Label(screen1,text="").pack()
                Label(screen1,text="Contents: ")
                
                for intry in entries:
                    Label(screen1,text="").pack()
                    Label(screen1,text=intry)
                    
    



def screen_for_dir():
    global screen2
    screen2 = Toplevel(screen)
    screen2.geometry("450x600")
    screen2.title("test")
    Label(text=OUTPUT).pack()
    _subprocess("dir", screen2)

def Command():

    function = entry.get()
    if function == "find":
        screen_for_find()

    elif function == "dir" or function == "files" or function == "folders":
        screen_for_dir()





def main_screen():
    global screen
    screen = Tk()
    screen.geometry("550x600")
    screen.title("LeafBerry")
    #screen.configure(background="grey")
    Label(text="Welcome to Leafberry\n this is a tool for people who want to learn cmd\n try entring find").pack()
    Label(text="").pack()
    Label(text = "enter a command or type help for help", width="300", height= "2", font=("Calibre", 14)).pack()
    Label(text="").pack()
    global entry
    entry = Entry(screen, width=50, borderwidth=10, fg="yellow", bg="black")
    entry.pack()

    Label(text="").pack()


    Button(text= "submit", height="2", width="30", command=Command).pack()
    Label(text="").pack()
    
    screen.mainloop()

 
main_screen()

