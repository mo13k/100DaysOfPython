from tkinter import *
import tkinter as tk
from tkinter import messagebox
import html
from Day017Bzquiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizSetupGUI:
    def __init__(self):
        self.window = Tk()
        self.window.title("Mo's Quiz Setup")
        
        # Load and set background image
        try:
            self.bg_image = tk.PhotoImage(file="Day017Bzquizbgpng.png")
            # Get image dimensions
            width = self.bg_image.width()
            height = self.bg_image.height()
            
            # Set window size to match image
            self.window.geometry(f"{width}x{height}")
            self.window.resizable(False, False)  # Prevent resizing
            
            bg_label = tk.Label(self.window, image=self.bg_image)
            bg_label.place(x=0, y=0, relwidth=1, relheight=1)
            bg_label.lower()  # Put background behind other widgets
            print("Background image loaded successfully")
        except Exception as e:
            # Fallback to original color if image not found
            print(f"Could not load background image: {e}")
            self.window.config(bg=THEME_COLOR)
        
        # Frame to hold everything - this is the key improvement!
        self.main_frame = tk.Frame(self.window, bg="white", padx=20, pady=20)
        self.main_frame.place(relx=0.5, rely=0.5, anchor="center")
        
        # Welcome title
        title_label = tk.Label(self.main_frame, text="Welcome to Mo's Quiz!", fg="black", bg="white", font=("Calibri", 24, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Number of questions
        tk.Label(self.main_frame, text="Number of questions:", fg="black", bg="white", font=("Calibri", 12)).grid(row=1, column=0, sticky="e", pady=5, padx=10)
        self.amount_var = tk.StringVar(value="10")
        tk.Entry(self.main_frame, textvariable=self.amount_var, width=10, bg="white", fg="black").grid(row=1, column=1, sticky="w", padx=10)
        
        # Difficulty
        tk.Label(self.main_frame, text="Difficulty:", fg="black", bg="white", font=("Calibri", 12)).grid(row=2, column=0, sticky="e", pady=5, padx=10)
        self.difficulty_var = tk.StringVar(value="easy")
        difficulty_menu = tk.OptionMenu(self.main_frame, self.difficulty_var, "easy", "medium", "hard")
        difficulty_menu.config(bg="white", fg="black", font=("Calibri", 10))
        difficulty_menu.grid(row=2, column=1, sticky="w", padx=10)
        
        # Question type
        tk.Label(self.main_frame, text="Question type:", fg="black", bg="white", font=("Calibri", 12)).grid(row=3, column=0, sticky="e", pady=5, padx=10)
        self.type_var = tk.StringVar(value="multiple")
        type_menu = tk.OptionMenu(self.main_frame, self.type_var, "multiple", "boolean")
        type_menu.config(bg="white", fg="black", font=("Calibri", 10))
        type_menu.grid(row=3, column=1, sticky="w", padx=10)
        
        # Start button
        tk.Button(self.main_frame, text="Start Quiz", command=self.start_quiz, bg="white", fg="black", font=("Calibri", 14, "bold")).grid(row=4, column=0, columnspan=2, pady=20)
        
        self.quiz_data = None
        
    def start_quiz(self):
        try:
            amount = int(self.amount_var.get())
            if amount <= 0 or amount > 50:
                messagebox.showerror("Error", "Number of questions must be between 1 and 50")
                return
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number for questions")
            return
            
        difficulty = self.difficulty_var.get()
        qtype = self.type_var.get()
        
        self.quiz_data = {
            'amount': amount,
            'difficulty': difficulty,
            'type': qtype
        }
        
        self.window.destroy()

class QuizInterface:

    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz

        self.window = Tk()
        self.window.title("Mo's Quiz Game")
        
        # Load and set background image
        try:
            self.bg_image = tk.PhotoImage(file="Day017Bzquizbgpng.png")
            # Get image dimensions
            width = self.bg_image.width()
            height = self.bg_image.height()
            
            # Set window size to match image
            self.window.geometry(f"{width}x{height}")
            self.window.resizable(False, False)  # Prevent resizing
            
            bg_label = tk.Label(self.window, image=self.bg_image)
            bg_label.place(x=0, y=0, relwidth=1, relheight=1)
            bg_label.lower()  # Put background behind other widgets
            print("Background image loaded successfully")
        except Exception as e:
            # Fallback to original color if image not found
            print(f"Could not load background image: {e}")
            self.window.config(bg=THEME_COLOR)

        self.score_label = tk.Label(text="Score: 0", fg="black", bg="white", font=("Calibri", 20, "bold"))
        self.score_label.place(relx=0.5, rely=0.1, anchor="center")

        self.canvas = tk.Canvas(width=400, height=150, bg="white")
        self.question_text = self.canvas.create_text(200, 75, text="", fill=THEME_COLOR, width=380, font=("Arial", 16, "italic"), anchor="center", justify="center")
        self.canvas.place(relx=0.5, rely=0.35, anchor="center")

        self.answer_buttons = []
        self.boolean_buttons = []

        # Create 4 buttons for multiple choice (arranged in 2x2 grid)
        for i in range(4):
            btn = tk.Button(
                text=f"Option {i+1}",
                width=25,
                height=2,
                bg="#ffffff",
                fg="#000000",
                font=("Arial", 12),
                command=lambda i=i: self.check_answer(i)
            )
            # Arrange in 2x2 grid centered
            if i < 2:  # First row
                btn.place(relx=0.3 + (i * 0.4), rely=0.65, anchor="center")
            else:  # Second row
                btn.place(relx=0.3 + ((i-2) * 0.4), rely=0.8, anchor="center")
            self.answer_buttons.append(btn)

        # Create 2 buttons for boolean (initially hidden)
        for i in range(2):
            btn = tk.Button(
                text="True" if i == 0 else "False",
                width=25,
                height=2,
                bg="#ffffff",
                fg="#000000",
                font=("Arial", 12),
                command=lambda i=i: self.check_answer(i)
            )
            btn.place(relx=0.3 + (i * 0.4), rely=0.65, anchor="center")
            self.boolean_buttons.append(btn)
            btn.place_forget()  # Hide initially

        self.current_choices = []  # Store answer options

        self.get_next_question()  # Start the quiz

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")

        if self.quiz.still_has_questions():
            q_text, choices = self.quiz.next_question()
            q_text = html.unescape(q_text)
            self.canvas.itemconfig(self.question_text, text=q_text)

            # Load answer choices
            if choices is None:
                # Boolean question (True/False)
                self.current_choices = ["True", "False"]
                
                # Hide multiple choice buttons
                for btn in self.answer_buttons:
                    btn.place_forget()
                
                # Show boolean buttons
                for i, choice in enumerate(self.current_choices):
                    self.boolean_buttons[i].config(text=choice, state="normal", bg="white")
                    self.boolean_buttons[i].place(relx=0.3 + (i * 0.4), rely=0.65, anchor="center")
            else:
                # Multiple choice question
                self.current_choices = choices
                
                # Hide boolean buttons
                for btn in self.boolean_buttons:
                    btn.place_forget()
                
                # Show multiple choice buttons in 2x2 grid
                for i, choice in enumerate(self.current_choices):
                    self.answer_buttons[i].config(text=html.unescape(choice), state="normal", bg="white")
                    # Arrange in 2x2 grid centered
                    if i < 2:  # First row
                        self.answer_buttons[i].place(relx=0.3 + (i * 0.4), rely=0.65, anchor="center")
                    else:  # Second row
                        self.answer_buttons[i].place(relx=0.3 + ((i-2) * 0.4), rely=0.8, anchor="center")
                
                # Hide unused multiple choice buttons
                for i in range(len(self.current_choices), 4):
                    self.answer_buttons[i].place_forget()

            # Update score
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            final_score_text = f"Quiz Complete!\n\nFinal Score: {self.quiz.score}/{self.quiz.questionnum}"
            self.canvas.itemconfig(self.question_text, text=final_score_text, font=("Arial", 18, "bold"), anchor="center", justify="center")
            
            # Hide score label and all answer buttons
            self.score_label.place_forget()
            for btn in self.answer_buttons:
                btn.place_forget()
            for btn in self.boolean_buttons:
                btn.place_forget()

    def check_answer(self, index):
        selected = self.current_choices[index]
        is_right, correct_answer = self.quiz.check_answer(selected)

        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)
