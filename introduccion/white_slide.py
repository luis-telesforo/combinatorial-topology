from manim import config, WHITE, Mobject
from manim_slides.slide import Slide

ROSA = "#CC79A7"
NARANJA = "#E69F00"
AZUL = "#56B4E9"
VERDOSO = "#0072B2"
VERDOSO_CLARO = "#03FBD0"

class WhiteBackgroundSlide(Slide):
    config.background_color = WHITE
    Mobject.set_default(color='BLACK')