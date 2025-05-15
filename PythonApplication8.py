import random
import tkinter as tk
from tkinter import ttk, messagebox

def guess_the_number_game():
    secret_number = random.randint(1, 10)
    attempts = 0

    print("I've picked a number between 1 and 10.")
    while True:
        attempts += 1
        user_input = input(f"Attempt {attempts}: Enter your guess: ")
        if not user_input.isdigit():
            print("Please enter an integer.")
            continue
        user_guess = int(user_input)

        if user_guess < secret_number:
            print("Higher.")
        elif user_guess > secret_number:
            print("Lower.")
        else:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts!")
            break

def guess_the_number_with_hints_game():
    secret_number = random.randint(1, 50)
    attempts = 0

    print("I've picked a number between 1 and 50.")
    while True:
        attempts += 1
        user_input = input(f"Attempt {attempts}: Enter your guess: ")
        if not user_input.isdigit():
            print("Please enter an integer.")
            continue
        user_guess = int(user_input)

        difference = abs(user_guess - secret_number)
        if difference <= 3:
            print("Very close!")
        elif difference <= 10:
            print("Close.")
        else:
            print("Far.")

        if user_guess == secret_number:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts!")
            break

def guess_the_code_game():
    secret_code = random.randint(1, 20)
    attempts_left = 3

    print("I've generated a secret code between 1 and 20. You have 3 attempts to guess it.")
    while attempts_left > 0:
        user_input = input(f"Attempt {4 - attempts_left}: Enter your code: ")
        if not user_input.isdigit():
            print("Please enter an integer.")
            continue
        user_guess = int(user_input)

        if user_guess == secret_code:
            print(f"Congratulations! You guessed the code {secret_code}!")
            return

        attempts_left -= 1
        if attempts_left > 0:
            print(f"Incorrect. Attempts left: {attempts_left}")
        else:
            print(f"You lost. The correct code was {secret_code}.")

def guess_the_pin_code_game():
    secret_pin = str(random.randint(1000, 9999))
    attempts_left = 5

    print("I've generated a 4-digit PIN code. You have 5 attempts to guess it.")
    while attempts_left > 0:
        user_input = input(f"Attempt {6 - attempts_left}: Enter your PIN code: ")
        if not user_input.isdigit() or len(user_input) != 4:
            print("Please enter a 4-digit number.")
            continue
        user_guess = user_input

        correct_positions = 0
        for i in range(4):
            if user_guess[i] == secret_pin[i]:
                correct_positions += 1

        if correct_positions == 4:
            print(f"Congratulations! You guessed the PIN code {secret_pin}!")
            return

        attempts_left -= 1
        if attempts_left > 0:
            print(f"Incorrect. Correct digits in correct positions: {correct_positions}. Attempts left: {attempts_left}")
        else:
            print(f"You lost. The correct PIN code was {secret_pin}.")

def guess_the_color_game_text():
    colors = ["red", "blue", "green", "yellow", "purple"]
    secret_color = random.choice(colors)
    warm_colors = ["red", "yellow"]
    attempts_left = 3

    print("I've chosen a secret color. Try to guess it.")
    while attempts_left > 0:
        user_input = input(f"Attempt {4 - attempts_left}: Enter your color: ").lower()
        if user_input not in colors:
            print("Please enter one of the following colors: red, blue, green, yellow, purple.")
            continue

        if user_input == secret_color:
            print(f"Congratulations! You guessed the color {secret_color}!")
            return

        attempts_left -= 1
        if attempts_left > 0:
            if user_input in warm_colors:
                print("Incorrect. The secret color is warm.")
            else:
                print("Incorrect. The secret color is cold.")
        else:
            print(f"You lost. The correct color was {secret_color}.")

class GuessTheColorGameTkinter:
    def __init__(self, root):
        self.root = root
        self.root.title("Guess the Color")
        self.colors = ["red", "blue", "green", "yellow", "purple"]
        self.secret_color = random.choice(self.colors)
        self.warm_colors = ["red", "yellow"]
        self.attempts_left = 3
        self.already_guessed = False

        self.task_label = ttk.Label(root, text="I've chosen a secret color. Try to guess it.")
        self.attempts_label = ttk.Label(root, text=f"Attempts left: {self.attempts_left}")
        self.color_combobox = ttk.Combobox(root, values=self.colors)
        self.color_combobox.set("")  # Initial value
        self.check_button = ttk.Button(root, text="Check", command=self.check_color)
        self.result_text = tk.StringVar()
        self.result_label = ttk.Label(root, textvariable=self.result_text)

        self.task_label.pack(pady=10)
        self.attempts_label.pack(pady=10)
        self.color_combobox.pack(pady=10)
        self.check_button.pack(pady=10)
        self.result_label.pack(pady=10)

    def check_color(self):
        if self.already_guessed:
            return

        guessed_color = self.color_combobox.get().lower()
        if not guessed_color:
            self.result_text.set("Please select a color.")
            return

        if guessed_color not in self.colors:
            self.result_text.set("Please select one of the provided colors.")
            return

        if guessed_color == self.secret_color:
            self.result_text.set(f"Congratulations! You guessed the color {self.secret_color}!")
            self.already_guessed = True
            self.check_button["state"] = "disabled"  # Disable the button
            return

        self.attempts_left -= 1
        self.attempts_label.config(text=f"Attempts left: {self.attempts_left}")
        if self.attempts_left > 0:
            if guessed_color in self.warm_colors:
                self.result_text.set("Incorrect. The secret color is warm.")
            else:
                self.result_text.set("Incorrect. The secret color is cold.")
            self.color_combobox.set("")
        else:
            self.result_text.set(f"You lost. The correct color was {self.secret_color}.")
            self.check_button["state"] = "disabled"  # Disable the button

if __name__ == '__main__':
    guess_the_number_game()
    guess_the_number_with_hints_game()
    guess_the_code_game()
    guess_the_pin_code_game()
    guess_the_color_game_text() # Run the version without GUI

    root = tk.Tk()
    guess_the_color_game = GuessTheColorGameTkinter(root)
    root.mainloop()
