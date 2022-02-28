import requests
import random
from tkinter import *


endpoint = "https://the-one-api.dev/v2/quote"
headers = {"Authorization": "Bearer W3uL97UB7YPgJgeI13jR"}

def get_quote():
    num = random.randint(0, 999)
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()

    book = response.json()
    quotes = book["docs"]

    text = quotes[num]['dialog']
    canvas.itemconfig(quote_text, text=text)

window = Tk()
window.title('LOTR quotes!')

canvas = Canvas(width=500, height=500)
background_img = PhotoImage(file="balaob.png")
canvas.create_image(250, 250, image=background_img)
quote_text = canvas.create_text(250, 210, text="Click the button!", width=250, font=("Arial", 15, "bold"), fill="black")

canvas.grid(row=0, column=0)

lotr_img = PhotoImage(file="lotr(1).png")
lotr_button = Button(image=lotr_img, highlightthickness=0, command=get_quote)
lotr_button.grid(row=1, column=0)


window.mainloop()

