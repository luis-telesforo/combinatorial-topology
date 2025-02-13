from manim import Scene, Create, Uncreate, Text, Title
## These colors are colorblind friendly!
ROSA = "#CC79A7"
NARANJA = "#E69F00"
AZUL = "#56B4E9"
VERDOSO = "#0072B2"


class MyScene(Scene):

    def construct(self):
        Text.set_default(font_size=20)

    def create_title(self, title_text):
        title = Title(title_text, include_underline=False)
        self.play(Create(title))
        self.wait(1.5)
        self.play(Uncreate(title))

    def add_description(self, description_text):
        description = Title(description_text, font_size=30, include_underline=False)
        self.play(Create(description))

    def add_title_and_description(self, title, description):
        self.create_title(title)
        self.add_description(description)