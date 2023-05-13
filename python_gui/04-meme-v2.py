from guizero import App, TextBox, Drawing, Combo, Slider


def draw_meme():
    meme.clear()
    meme.image(0, 0, "./python_gui/monkey.jpg")
    meme.text(20, 20, top_text.value, color=color.value, size=size.value,
              font="courier")
    meme.text(20, 320, bottom_text.value, color="green",
              size=28, font="time new roman")


app = App("meme")

top_text = TextBox(app, "top text", command=draw_meme)
bottom_text = TextBox(app, "bottom text", command=draw_meme)
color = Combo(app, options=["black", "white", "red", "green", "blue",
              "orange", "cyan", "yellow"], command=draw_meme, selected="blue")
size = Slider(app, start=20, end=60, command=draw_meme)

meme = Drawing(app, width="fill", height="fill")

draw_meme()

app.display()
