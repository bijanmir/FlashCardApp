import random
from word_bank import Word_Bank
from tkinter import *

wb = Word_Bank()
wb.addWord("Hola", "Hello")
wb.addWord("Como", "How")
wb.addWord("Adios", "Bye")
wb.addWord("Amigo", "Friend")
wb.addWord("Comida", "Food")
wb.addWord("La Playa", "Beach")
wb.addWord("El Bosque LLuvioso", "The Rainforest")


def deal_card(wordbank):
    word = random.choice(wordbank)




def next_card():
    current_card = random.choice(wb.words)
    key_list = list(wb.words.keys())
    # word_key = random.choice(wb.words)
    print(key_list)

    canvas.itemconfig(card_english, text="English Test")
    canvas.itemconfig(card_spanish, text="Spanish Test")



shown_words =[]
current_card = None

BACKGROUND_COLOR = "#a7d0cd"

window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg="Gray")

MAX_WIDTH = 800
MAX_HEIGHT = 526
MIDDLE_X_CANVAS = MAX_WIDTH / 2
MIDDLE_Y_CANVAS = MAX_HEIGHT / 2

canvas = Canvas(width=MAX_WIDTH, height=MAX_HEIGHT)

card_front_img = PhotoImage(file="./images/card_front.png")
canvas.create_image(MIDDLE_X_CANVAS, MIDDLE_Y_CANVAS, image=card_front_img)
card_english = canvas.create_text(MIDDLE_X_CANVAS, MIDDLE_Y_CANVAS - 113, text="English", font=("Arial", 40, "italic"))
card_spanish = canvas.create_text(MIDDLE_X_CANVAS, MIDDLE_Y_CANVAS, text="Spanish", font=("Arial", 60, "italic"))
canvas.grid(row=0, column=0, columnspan=2)

wrong_img = PhotoImage(file="./images/wrong.png")
wrong_btn = Button(image=wrong_img, bg=BACKGROUND_COLOR, command=next_card)
wrong_btn.grid(row=1, column=0)

right_img = PhotoImage(file="./images/right.png")
right_btn = Button(image=right_img, bg=BACKGROUND_COLOR, command=next_card)
right_btn.grid(row=1, column=1)




window.mainloop()
