from manim import Line, LEFT, RIGHT, Create, Axes, NumberLine, ArrowTip, ArrowCircleTip, Dot, MathTex, DOWN, \
    Intersection
from numpy import array

from basic_scene import MyScene, ROSA, AZUL, NARANJA


class NerveOfALine(MyScene):
    def construct(self):
        self.add_title_and_description(
            "Ejemplo del nervio de un intervalo",
            r"Consideremos una cubierta formada por $\left[0,.6\right)$ y $\left(.4,1\right]$ ")
        left_point = array([-3., 0, 0])
        zero = MathTex(r"0").next_to(left_point, direction=DOWN)
        right_point = array([3., 0, 0])
        one = MathTex(r"1").next_to(right_point, direction=DOWN)
        interval = Line(start=left_point, end=right_point)
        self.play(Create(interval), Create(zero), Create(one))

        cover_left_endpoint = left_point * .4 + right_point * .6
        cover_left = Line(start=left_point, end=cover_left_endpoint, color=ROSA)
        cover_left_endpoint_label = MathTex(r".6").next_to(cover_left_endpoint, direction=DOWN)
        self.play(Create(cover_left), Create(cover_left_endpoint_label))

        cover_right_startpoint = left_point * .6 + right_point * .4
        cover_right_startpoint_label = MathTex(r".4").next_to(cover_right_startpoint, direction=DOWN)
        cover_right = Line(start=cover_right_startpoint, end=right_point, color=AZUL)
        intersection = Line(start=cover_right_startpoint, end=cover_left_endpoint, color=NARANJA)
        self.play(Create(cover_right), Create(cover_right_startpoint_label), Create(intersection))

        self.wait()