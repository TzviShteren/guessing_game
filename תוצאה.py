import tkinter as tk
import random

global number_of_tries
global random_number

guessing_game = tk.Tk()
guessing_game.geometry("400x400")
guessing_game.title("Number Guessing Game")

random_number = random.randint(1, 100)
number_of_tries = 0


def guess():
    global number_of_tries
    guess = int(enter_for_test.get())
    if guess < random_number:
        number_of_tries += 1
        Explanatory_Label.config(text=f"Enter a higher number than {guess}", fg="red")
        enter_for_test.delete(0, tk.END)
    elif guess > random_number:
        number_of_tries += 1
        Explanatory_Label.config(text=f"Enter a smaller number than {guess}", fg="red")
        enter_for_test.delete(0, tk.END)
    else:
        number_of_tries += 1
        Explanatory_Label.config(text=f"Correct! You guessed it in {number_of_tries} tries.", fg="green")
        start_confetti_animation()


def start_confetti_animation():
    confetti_colors = ["red", "green", "blue", "orange", "purple", "yellow", "pink"]
    for _ in range(100):
        x = random.randint(50, 350)
        y = random.randint(50, 250)
        confetti_size = random.randint(5, 15)
        confetti_color = random.choice(confetti_colors)
        confetti = canvas.create_oval(x, y, x + confetti_size, y + confetti_size, fill=confetti_color)
        confetti_fall(confetti)


def confetti_fall(confetti):
    y_speed = random.uniform(0.1, 1.5)
    canvas.move(confetti, 0, y_speed)
    if canvas.coords(confetti)[1] < 400:
        guessing_game.after(50, confetti_fall, confetti)
    else:
        canvas.delete(confetti)


def Reset_function():
    global number_of_tries
    global random_number
    number_of_tries = 0
    random_number = random.randint(1, 100)
    Explanatory_Label.config(text="Enter a number from 1 to 100", fg="black")
    enter_for_test.delete(0, tk.END)


def on_enter_press(event):
    guess()


Explanatory = "Welcome to the Number Guessing Game\nEnter a number from 1 to 100"

Explanatory_Label = tk.Label(guessing_game, text=Explanatory, font=("Helvetica", 12), fg="black")
Explanatory_Label.pack(pady=20)

enter_for_test = tk.Entry(guessing_game, font=("Helvetica", 14))
enter_for_test.pack(pady=10)
enter_for_test.bind("<Return>", on_enter_press)


Test_button = tk.Button(guessing_game, text="Test", command=guess, bg="blue", fg="white", font=("Helvetica", 12))
Test_button.pack(pady=10)

Reset_button = tk.Button(guessing_game, text="Reset", command=Reset_function, bg="red", fg="white",
                         font=("Helvetica", 12))
Reset_button.pack(pady=5)

canvas = tk.Canvas(guessing_game, width=400, height=200)
canvas.pack(pady=20)

guessing_game.mainloop()
