import tkinter as tk
import time
from tkinter import messagebox
import random

x=tk.Tk()            #first window with a menu
x.geometry("400x500")
x.title("Flipping Memory Game")
x.configure(background="light pink")
l1=tk.Label(x,text="Welcome to Flipping Memory Game",bg="light pink",fg="black",font=('Arial',15,'bold'))
l1.pack(side="top",fill=tk.X)
l2=tk.Label(x,text="Modes",bg="light pink",fg="black",font=('Arial',15,'bold'))
l2.pack(side="top",pady=10,fill=tk.X)
def on_enter(e):
    e.widget['background']='lavenderblush'
def on_leave(e):
    e.widget['background']='light pink'

def easy():
    m=tk.Tk()                                   #main window for easy mode
    m.geometry("700x650")
    m.title("Flipping Cards-Memory Game")
    m.configure(padx=10,pady=20,background="light pink")
    title_frame=tk.Frame(m,width=600,height=500)
    title_frame.pack(side="top", fill="x", pady=10)
    game_title= tk.Label(title_frame,text="Flipping Cards-Memory Game",font=("Arial",35,"bold"),background="light pink")
    game_title.pack(anchor="center",fill="x")
    card_frame=tk.Frame(m,width=650,height=600,padx=10,pady=10)
    card_frame.pack(side="left")
    lives_text="❤❤❤❤❤"
    lives=tk.Label(m,text=lives_text,font=("Arial",20),pady=50,bg="light pink")
    lives.place(x=500,y=100)
    score_label=tk.Label(m,text="Score:",font=("Arial",20,"bold"),bg="light pink")
    score_label.place(x=500, y=300)
    score=0
    game_score=tk.Label(m,text=score,font=("Arial",20,"bold"),bg="light pink")
    game_score.place(x=600,y=300)

    buttons = []  # cards
    lst = []  # input
    clicked = []  # card tracking

    def reset():                #resets the game
        global score, lives_text, lst, clicked
        score = 0
        lives_text = "❤❤❤❤❤❤"
        lst = []
        clicked = []
        game_score.configure(text=score)
        lives.configure(text=lives_text)
        for btn in buttons:
            btn.configure(text='X', bg='white', fg='black', state='normal')
    m.update()
    reset=tk.Button(m,text="Reset",font=("Arial",20,"bold"),relief="flat",bg="light pink",activebackground="white",cursor="hand2",command=reset)
    reset.place(x=500,y=400)
    reset.bind("<Enter>", on_enter)
    reset.bind("<Leave>", on_leave)

    class Cards:            #creates buttons and checks them (main game logic)
        def __init__(self,value,j,i):

            self.value=value
            self.button=tk.Button(card_frame,text="X",font=("Arial",20,"bold"),height=2,width=5,bg="white",activebackground="grey",foreground="black",borderwidth=1.5,relief="sunken",command=self.click,cursor="hand2")
            self.button.grid(row=j,column=i)
            buttons.append(self.button)

        def click(self): #function inputs numbers and checks them for validity
            nonlocal lst, clicked, score, lives_text
            if len(lst)==2:                     #corectly matched cards stay flipped
                return
            self.button.configure(text=self.value,bg="grey",state="disabled")   #flips cards
            lst.append(self.value)                                                 #inputs numbers
            clicked.append(self.button)                                             #tracks cards
            if len(lst)==2:
                m.update()
                time.sleep(0.5)
                if lst[0] == lst[1]:                  #checks if both numbers are same
                    score=score+1
                    game_score.configure(text=score)
                    for button in clicked:             #makes cards unavailable
                            button.configure(state="disabled")
                else:
                    if len(lives_text)>1:                 #checks if lives are available and removes one for wrong selection
                        lives_text = lives_text[:len(lives_text)-1]
                        lives.configure(text=lives_text)                #updating lives
                    else:
                        lives_text = lives_text[:len(lives_text) - 1]
                        lives.configure(text=lives_text)
                        messagebox.showerror("You lose!",lives_text)
                        m.destroy()
                        return                  #ends game
                    for button in clicked:                          #if unmatched makes cards available
                        button.configure(text="X",bg="white",state="normal",foreground="black")
                clicked=[]                  #empties the button tracking list
                lst=[]                      #empties input taking list
    button_value=[3, 2, 4, 3, 6, 6, 5, 2, 5, 4]*2#cards
    random.shuffle(button_value)
    a=0
    for j in range(4):
        for i in range(5):
            x=Cards(button_value[a],j,i)
            a+=1
            m.update()
b1=tk.Button(x,text="Easy",bg="light pink",fg="black",font=('Arial',15,'bold'),width=6,command=easy)
b1.place(x=160,y=100)
b1.bind("<Enter>",on_enter)
b1.bind("<Leave>",on_leave)

def medium():
    m=tk.Tk()                                   #main window for medium mode
    m.geometry("700x650")
    m.title("Flipping Cards-Memory Game")
    m.configure(padx=10,pady=20,background="light pink")
    title_frame=tk.Frame(m,width=600,height=500)
    title_frame.pack(side="top", fill="x", pady=10)
    game_title= tk.Label(title_frame,text="Flipping Cards-Memory Game",font=("Arial",35,"bold"),background="light pink")
    game_title.pack(anchor="center",fill="x")
    card_frame=tk.Frame(m,width=650,height=600,padx=10,pady=10)
    card_frame.pack(side="left")
    lives_text="❤❤❤❤❤"
    lives=tk.Label(m,text=lives_text,font=("Arial",20),pady=50,bg="light pink")
    lives.place(x=500,y=100)
    score_label=tk.Label(m,text="Score:",font=("Arial",20,"bold"),bg="light pink")
    score_label.place(x=500, y=300)
    score=0
    game_score=tk.Label(m,text=score,font=("Arial",20,"bold"),bg="light pink")
    game_score.place(x=600,y=300)

    buttons = []  # cards
    lst = []  # input
    clicked = []  # card tracking

    def reset():
        global score, lives_text, lst, clicked
        score = 0
        lives_text = "❤❤❤❤❤❤"
        lst = []
        clicked = []
        game_score.configure(text=score)
        lives.configure(text=lives_text)
        for btn in buttons:
            btn.configure(text='X', bg='white', fg='black', state='normal')
    m.update()
    reset=tk.Button(m,text="Reset",font=("Arial",20,"bold"),relief="flat",bg="light pink",activebackground="white",cursor="hand2",command=reset)
    reset.place(x=500,y=400)
    reset.bind("<Enter>", on_enter)
    reset.bind("<Leave>", on_leave)

    class Cards:
        def __init__(self,value,j,i):

            self.value=value
            self.button=tk.Button(card_frame,text="X",font=("Arial",20,"bold"),height=2,width=5,bg="white",activebackground="grey",foreground="black",borderwidth=1.5,relief="sunken",command=self.click,cursor="hand2")
            self.button.grid(row=j,column=i)
            buttons.append(self.button)

        def click(self): 
            nonlocal lst, clicked, score, lives_text
            if len(lst)==2:                     #corectly matched cards stay flipped
                return
            self.button.configure(text=self.value,bg="grey",state="disabled")   #flips cards
            lst.append(self.value)                                                 #inputs numbers
            clicked.append(self.button)                                             #tracks cards
            if len(lst)==2:
                m.update()
                time.sleep(0.5)
                if lst[0] == lst[1]:                  #checks if both numbers are same
                    score=score+1
                    game_score.configure(text=score)
                    for button in clicked:             #makes cards unavailable
                            button.configure(state="disabled")
                else:
                    if len(lives_text)>1:                 #checks if lives are available and removes one for wrong selection
                        lives_text = lives_text[:len(lives_text)-1]
                        lives.configure(text=lives_text)                #updating lives
                    else:
                        lives_text = lives_text[:len(lives_text) - 1]
                        lives.configure(text=lives_text)
                        messagebox.showerror("You lose!",lives_text)
                        m.destroy()
                        return                  #ends game
                    for button in clicked:                          #if unmatched makes cards available
                        button.configure(text="X",bg="white",state="normal",foreground="black")
                clicked=[]                  #empties the button tracking list
                lst=[]                      #empties input taking list
    button_value=[3, 2, 4, 3, 6, 6, 5, 2, 5, 4]*3    #cards
    random.shuffle(button_value)
    a=0
    for j in range(6):
        for i in range(5):
            x=Cards(button_value[a],j,i)
            a+=1
            m.update()
    m.mainloop()
b2=tk.Button(x,text="Medium",bg="light pink",fg="black",font=('Arial',15,'bold'),width=6,command=medium)
b2.place(x=160,y=180)
b2.bind("<Enter>",on_enter)
b2.bind("<Leave>",on_leave)

def hard():
    m=tk.Tk()                                   #main window for hard mode
    m.geometry("700x650")
    m.title("Flipping Cards-Memory Game")
    m.configure(padx=10,pady=20,background="light pink")
    title_frame=tk.Frame(m,width=600,height=500)
    title_frame.pack(side="top", fill="x", pady=10)
    game_title= tk.Label(title_frame,text="Flipping Cards-Memory Game",font=("Arial",35,"bold"),background="light pink")
    game_title.pack(anchor="center",fill="x")
    card_frame=tk.Frame(m,width=650,height=600,padx=10,pady=10)
    card_frame.pack(side="left")
    lives_text="❤❤❤❤"                #lesser lives
    lives=tk.Label(m,text=lives_text,font=("Arial",20),pady=50,bg="light pink")
    lives.place(x=500,y=100)
    score_label=tk.Label(m,text="Score:",font=("Arial",20,"bold"),bg="light pink")
    score_label.place(x=500, y=300)
    score=0
    game_score=tk.Label(m,text=score,font=("Arial",20,"bold"),bg="light pink")
    game_score.place(x=600,y=300)

    buttons = []  # cards
    lst = []  # input
    clicked = []  # card tracking

    def reset():
        global score, lives_text, lst, clicked
        score = 0
        lives_text = "❤❤❤❤"
        lst = []
        clicked = []
        game_score.configure(text=score)
        lives.configure(text=lives_text)
        for btn in buttons:
            btn.configure(text='X', bg='white', fg='black', state='normal')
    m.update()
    reset=tk.Button(m,text="Reset",font=("Arial",20,"bold"),relief="flat",bg="light pink",activebackground="white",cursor="hand2",command=reset)
    reset.place(x=500,y=400)
    reset.bind("<Enter>", on_enter)
    reset.bind("<Leave>", on_leave)

    class Cards:
        def __init__(self,value,j,i):

            self.value=value
            self.button=tk.Button(card_frame,text="X",font=("Arial",20,"bold"),height=2,width=5,bg="white",activebackground="grey",foreground="black",borderwidth=1.5,relief="sunken",command=self.click,cursor="hand2")
            self.button.grid(row=j,column=i)
            buttons.append(self.button)

        def click(self): #function inputs numbers and checks them for validit
            nonlocal lst, clicked, score, lives_text
            if len(lst)==2:                     #corectly matched cards stay flipped
                return
            self.button.configure(text=self.value,bg="grey",state="disabled")   #flips cards
            lst.append(self.value)                                                 #inputs numbers
            clicked.append(self.button)                                             #tracks cards
            if len(lst)==2:
                m.update()
                time.sleep(0.5)
                if lst[0] == lst[1]:                  #checks if both numbers are same
                    score=score+1
                    game_score.configure(text=score)
                    for button in clicked:             #makes cards unavailable
                            button.configure(state="disabled")
                else:
                    if len(lives_text)>1:                 #checks if lives are available and removes one for wrong selection
                        lives_text = lives_text[:len(lives_text)-1]
                        lives.configure(text=lives_text)                #updating lives
                    else:
                        lives_text = lives_text[:len(lives_text) - 1]
                        lives.configure(text=lives_text)
                        messagebox.showerror("You lose!",lives_text)
                        m.destroy()
                        return                  #ends game
                    for button in clicked:                          #if unmatched makes cards available
                        button.configure(text="X",bg="white",state="normal",foreground="black")
                clicked=[]                  #empties the button tracking list
                lst=[]                      #empties input taking list
    button_value=[3, 2, 4, 3, 6, 6, 5, 2, 5, 4]*3#cards
    random.shuffle(button_value)
    a=0
    for j in range(7):
        for i in range(5):
            x=Cards(button_value[a],j,i)
            a+=1
            m.update()

b3=tk.Button(x,text="Hard",bg="light pink",fg="black",font=('Arial',15,'bold'),width=6,command=hard)
b3.place(x=160,y=260)
b3.bind("<Enter>",on_enter)
b3.bind("<Leave>",on_leave)

def h_t_play():                         #function explaining the game
    m1=tk.Tk()                          #new window
    m1.geometry("700x250")
    m1.title("Rules")

    rule1=tk.Label(m1,text="1)You have several lives.",font=("Arial",15))
    rule1.place(x=0,y=0)
    rule2=tk.Label(m1,text="2)Select two cards.",font=("Arial",15))
    rule2.place(x=0,y=30)
    rule3=tk.Label(m1,text="3)If both cards have the same number, the game continues.",font=("Arial",15))
    rule3.place(x=0,y=60)
    rule4=tk.Label(m1,text="4)If both cards do not have the same number,\n you lose 1 life.",font=("Arial",15))
    rule4.place(x=0,y=90)
    rule5 = tk.Label(m1,text="5)If all lives are gone, you lose.",font=("Arial", 15))
    rule5.place(x=0,y=120)

h_t_p=tk.Button(x,text="Rules",font=("Arial",20,"bold"),bg="light pink",activebackground="white",cursor="hand2",command=h_t_play,width=6)
h_t_p.place(x=150,y=350)
h_t_p.bind("<Enter>",on_enter)
h_t_p.bind("<Leave>",on_leave)
x.mainloop()

