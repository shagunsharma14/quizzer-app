from tkinter import *
from data import question_data
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzer")
        self.window.config(padx=20,pady=20,background=THEME_COLOR)

        self.score_label = Label(text=f"Score: 0",background=THEME_COLOR,foreground="White")
        self.score_label.grid(row=0,column=1)

        self.canvas = Canvas(width=300,height=250,background="white")
        self.canvas.create_text(150, 125, text="Some Question Here",fill=THEME_COLOR,font=("Arial",20,"italic"))
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)

        true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_img,highlightthickness=0)
        self.true_button.grid(row=2,column=0)

        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_img,highlightthickness=0)
        self.false_button.grid(row=2, column=1)


        self.window.mainloop()