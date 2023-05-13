from guizero import App, Text, Picture

app = App("Wanted!")
app.bg = "#FBFBD0"

wanted_text = Text(app, "WANTED")
wanted_text.text_size = 50
wanted_text.font = "Arial"
wanted_text.text_color = "#FF0000"

monkey = Picture(app, image="./python_gui/monkey.jpg")

app.display()
