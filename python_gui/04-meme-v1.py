from guizero import App, TextBox, Drawing


def draw_meme():
    meme.clear()
    meme.image(0, 0, "./python_gui/monkey.jpg")
    meme.text(20, 20, top_text.value, color="blue", size=40, font="courier")
    meme.text(20, 320, bottom_text.value, color="green",
              size=28, font="time new roman")


app = App("meme")

top_text = TextBox(app, "top text", command=draw_meme)
bottom_text = TextBox(app, "bottom text", command=draw_meme)

meme = Drawing(app, width="fill", height="fill")

draw_meme()

app.display()
