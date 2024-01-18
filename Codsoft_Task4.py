import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsGame:
    def __init__(self):
        # User score
        self.uscore = 0
        # Computer score
        self.cscore = 0

        # Create main window
        self.window = tk.Tk()
        self.window.title("Rock_Paper_Scissors Game")

        # Create GUI components
        self.label = tk.Label(self.window, text="Choose rock, paper, or scissors:", font=("Helvetica", 15))
        self.label.grid(row=0, column=0, columnspan=3, pady=10)

        # Variable to store user's choice
        self.choice_var = tk.StringVar()
        self.choice_var.set("")

        # Creating the radio buttons for choices
        self.radio_buttons = []
        choices = ["Rock", "Paper", "Scissors"]
        for index, choice in enumerate(choices):
            button = tk.Radiobutton(self.window, text=choice, value=choice.lower(), font=("Helvetica", 15), variable=self.choice_var)
            self.radio_buttons.append(button)
            button.grid(row=1, column=index, padx=10)

        # createing the Play button
        self.play_button = tk.Button(self.window, text="Play", font=("Helvetica", 15), bg="red", fg="white", command=self.play)
        self.play_button.grid(row=2, column=0, columnspan=3, pady=10)

        # displaying  Result label
        self.result_label = tk.Label(self.window, text="", font=("Helvetica", 15))
        self.result_label.grid(row=3, column=0, columnspan=3, pady=10)

        # displaying the Score label
        self.score_label = tk.Label(self.window, text="", font=("Helvetica", 15))
        self.score_label.grid(row=4, column=0, columnspan=3, pady=10)

        # create the Play again button
        self.play_again_button = tk.Button(self.window, text="Replay", font=("Helvetica", 15), bg="blue", fg="white", command=self.play_again)
        self.play_again_button.grid(row=5, column=0, columnspan=3, pady=10)

    def play(self):
        # Asking the  user's choice
        uchoice = self.choice_var.get()
        if not uchoice:
            messagebox.showinfo("Error Occurred", "Please choose rock, paper, or scissors.")
            return

        # Generating the  computer's choice
        cchoice = random.choice(['rock', 'paper', 'scissors'])

        # Identifying  the winner and displaying result
        winner = self.determine_winner(uchoice, cchoice)
        result = f"User choice: {uchoice.capitalize()}\nComputer's choice: {cchoice.capitalize()}\n"

        if winner == 'tie':
            result += "It's a tie!"
        elif winner == 'user':
            result += "Congratulations.... You won....!"
            self.uscore += 1
        else:
            result += "Oh no!!!, you lose.... Better luck next time!...."
            self.cscore += 1

        # Updating the result label and score label
        self.result_label.config(text=result)
        self.score_label.config(text=f"Score - User: {self.uscore} | Computer: {self.cscore}")

    def determine_winner(self, uchoice, cchoice):
        if uchoice == cchoice:
            return 'tie'
        elif (uchoice == 'rock' and cchoice == 'scissors') or \
             (uchoice == 'scissors' and cchoice == 'paper') or \
             (uchoice == 'paper' and cchoice == 'rock'):
            return 'user'
        else:
            return 'computer'

    def play_again(self):
        # Reseting to a  new game
        self.choice_var.set("")
        self.result_label.config(text="")
        self.score_label.config(text="")
        for button in self.radio_buttons:
            button.deselect()

if __name__ == "__main__":
    game = RockPaperScissorsGame()
    game.window.mainloop()
