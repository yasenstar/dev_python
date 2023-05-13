# Imports ----------------
from guizero import App, Text, PushButton
from random import choice


def choose_name():
    # print("Button was pressed")
    first_name = ["Barbara", "Woody", "Yasen", "Tiberius",
                  "Eason", "Smokey", "William", "Jennifer", "Ruby"]
    last_name = ["Spindleshanks", "Zhao", "Mysterioso",
                 "Dungeon", "Catseye", "Darkmeyer", "Flamingobreath"]
    spy_name = choice(first_name) + " " + choice(last_name)
    # print(spy_name)
    name.value = spy_name

# Functions --------------


# App ----------------
app = App('TOP SECRET')

# Widgets ----------------
title = Text(app, "Push the red button to find out your spy name")

button = PushButton(app, choose_name, text="Tell me!")
# button.bg = "#0000AA" ? no effect
button.text_color = "#FF0000"
button.text_size = 30

name = Text(app, text="")

# Display -----------
app.display()
