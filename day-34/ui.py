from cgitb import text
from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class UI:
    # making sure the the value for quiz_brain is an object of QuizBrain
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        # The window
        self.window = Tk()
        self.window.title("Quizzler")  # title of the window
        # the width of the window
        self.window.config(padx=20, pady=20, background=THEME_COLOR)
        ###

        # images
        false_img = PhotoImage(file="./images/false.png")
        true_img = PhotoImage(file="./images/true.png")
        ###
        # canvas
        self.canvas = Canvas(width=300, height=250)  # the canvas
        self.question_text = self.canvas.create_text(
            (150, 125), text="Question goes here", width=270, fill="blue", font=("Arial", 18, "italic"))
        # Label
        self.score = Label(text="Score: 0", fg="white", bg=THEME_COLOR)

        # Buttons
        self.false_btn = Button(
            image=false_img, highlightthickness=0, command=self.false)
        self.true_btn = Button(
            image=true_img, highlightthickness=0, command=self.true)

        # Layout
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.score.grid(row=0, column=2)
        self.false_btn.grid(row=2, column=0)
        self.true_btn.grid(row=2, column=1)

        self.get_next_question()
        self.window.mainloop()  # updating the window
    ###

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)

        else:
            self.canvas.itemconfig(
                self.question_text, text="Youv'e reached the end of the quiz")
            # deactivating the buttons
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def false(self):
        self.give_feedback(self.quiz.check_answer("false"))

    def true(self):
        self.give_feedback(self.quiz.check_answer("true"))

    def give_feedback(self, right):
        if right == True:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)
