from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
try:
    data = pandas.read_csv(".\\data\\words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv(".\\data\\french_words.csv")
finally:
    to_learn = data.to_dict(orient="records")

# ----------------------------  App functions  ----------------------------
def next_card():
    global english_word, flip_timer, current_card
    window.after_cancel(flip_timer)

    canvas.create_image(400, 263, image=card_front_image)
    current_card = random.choice(to_learn)
    french_word = current_card["French"]
    english_word = current_card["English"]

    card_title = canvas.create_text(400, 150, text="French", font=("Aerial", 40, "italic"))
    card_word = canvas.create_text(400, 263, text=french_word, font=("Aerial", 40, "bold"))

    flip_timer = window.after(3000, flip_card)

def flip_card():
    canvas.create_image(400, 263, image=card_back_image)
    card_title = canvas.create_text(400, 150, text="English", font=("Aerial", 40, "italic"), fill="white")
    card_word = canvas.create_text(400, 263, text=english_word, font=("Aerial", 40, "bold"), fill="white")

def is_known():
    to_learn.remove(current_card)

    data = pandas.DataFrame(to_learn)
    data.to_csv(".\\data\\words_to_learn.csv", index=False)

    next_card()


# ----------------------------  UI Setup  ----------------------------
window = Tk()
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
window.title("FLASHY - The Flash Card App")
flip_timer = window.after(3000, flip_card)

canvas = Canvas(height= 526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file=".\\images\\card_front.png")
card_back_image = PhotoImage(file=".\\images\\card_back.png")
canvas.create_image(400, 263, image=card_front_image)
canvas.grid(row=0, column=0, columnspan=2)


cross_image = PhotoImage(file=".\\images\\wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file=".\\images\\right.png")
known_button = Button(image=check_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=is_known)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()