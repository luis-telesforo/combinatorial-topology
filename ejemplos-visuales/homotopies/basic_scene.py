from manim import Scene, Create, Uncreate, Text, Title, CairoRenderer, Camera
from manim.renderer.opengl_renderer import OpenGLRenderer

## These colors are colorblind friendly!
ROSA = "#CC79A7"
NARANJA = "#E69F00"
AZUL = "#56B4E9"
VERDOSO = "#0072B2"
VERDOSO_CLARO = "#03FBD0"


class MyScene(Scene):

    def __init__(
            self,
            renderer: CairoRenderer | OpenGLRenderer | None = None,
            camera_class: type[Camera] = Camera,
            always_update_mobjects: bool = False,
            random_seed: int | None = None,
            skip_animations: bool = False,
    ):
        super().__init__(renderer, camera_class, always_update_mobjects, random_seed, skip_animations)
        self.title = None

    def construct(self):
        Text.set_default(font_size=20)

    def create_title(self, title_text):
        self.title = Title(title_text, include_underline=False)
        self.play(Create(self.title))
        self.wait(1.5)
        self.play(Uncreate(self.title))

    def add_description(self, description_text):
        self.play(Uncreate(self.title))
        self.title = Title(description_text, font_size=30, include_underline=False)
        self.play(Create(self.title))

    def add_title_and_description(self, title, description):
        self.create_title(title)
        self.add_description(description)