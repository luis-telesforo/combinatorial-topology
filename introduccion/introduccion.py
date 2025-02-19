from manim import Text, FadeOut, BulletedList, Create, Title, Axes, Dot, RIGHT, UR, UL, ScaleInPlace, MoveToTarget, \
    VGroup, UP, LEFT
from pandas import read_csv

from white_slide import WhiteBackgroundSlide, VERDOSO


class Presentation(WhiteBackgroundSlide):
    def construct(self):
        main_question = Text(r"¿Qué es el Análisis topológico de datos?")
        self.add(main_question)
        self.next_slide()

        self.play(FadeOut(main_question))
        temas = BulletedList("Análisis topológico de datos",
                             "Topología Algebraica Combinatoria",
                             "Otras aplicaciones.")
        self.play(Create(temas))
        self.next_slide()

        temas.fade_all_but(1)
        self.next_slide()

        self.play(FadeOut(temas))
        analisis_topologico_datos = Title(r"¿Por qué importa la topoología de los datos?")
        self.play(Create(analisis_topologico_datos))
        dataframe = read_csv('../introduccion/datasets/datasaurus.csv')
        wide_lines = dataframe[dataframe['dataset'] =='wide_lines']
        wide_lines.drop(columns='dataset', inplace=True)
        axe_and_dots = self.create_scatter_and_move_to_left(wide_lines)
        axe_and_dots.target.shift(UP*2 + LEFT*8).scale(.5)
        self.play(MoveToTarget(axe_and_dots))
        self.next_slide()

    def create_scatter_and_move_to_left(self, wide_lines):
        axes = Axes(x_range=[0, 100, 100], y_range=[0, 100, 100])
        axes.scale(.4).move_to(RIGHT * 3)
        self.play(Create(axes))
        axe_and_dots = VGroup(axes)
        for x, y in wide_lines.values:
            dot = Dot(axes.c2p(x, y), color=VERDOSO, radius=.03)
            axe_and_dots.add(dot)
            self.play(Create(dot, run_time=.07))
        axe_and_dots.generate_target()
        return axe_and_dots


