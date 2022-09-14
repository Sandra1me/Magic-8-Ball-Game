import random
from tkinter import *
from PIL import ImageTk,Image

def asking():
    answers=("It is certain","It is decidedly so","Without a doubt","Yes definitely","Yes definitely",
    "As I see it, yes","Most likely","Outlook good","Yes","Signs point to yes","Reply hazy, try again",
    "Ask again later","Better not tell you now","Cannot predict now","Concentrate and \nask again",
    "Don’t count on it","My reply is no","My sources say no","Outlook not so good","Very doubtful")
    
    answer.config(text="", bg="#FFFFFF")
    chose=random.choice(answers)
    answer.config(text=chose,font=("Arial",26))
    answer.grid(row=1,column=1)

root=Tk()
root.title("Magic 8 Ball")
root.resizable(0,0)
root.config(bg="#6B9FBF")

ball=ImageTk.PhotoImage(Image.open("MagicBall.png"))

magic=Label(image=ball, bg="#6B9FBF")
magic.grid(row=0, column=0, padx=10, pady=10, rowspan=3, columnspan=3)

ask=Button(root,text="Ask the question!", padx=10, pady=10, command=asking, fg="#0D0D0D", bg="#D9D5A0")
ask.grid(row=3, column=1, pady=20)

answer=Label(root,text="8", font=("Arial",60),bg="#FFFFFF")
answer.grid(row=1,column=1)

root.mainloop()