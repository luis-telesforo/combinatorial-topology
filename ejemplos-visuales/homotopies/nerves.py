from manim import Line, LEFT, RIGHT, Create, Axes, NumberLine, ArrowTip, ArrowCircleTip, Dot, MathTex, DOWN, \
    Intersection, Transform, AnimationGroup, Rectangle, Uncreate, TransformMatchingShapes, Circle, Arc, PI, WHITE, TAU, \
    VGroup, UP, UL, UR, DL, DR
from networkx.algorithms.distance_measures import radius
from numpy import array

from basic_scene import MyScene, ROSA, AZUL, NARANJA, VERDOSO, VERDOSO_CLARO


def edge_as_nerve_cover(scene, cover_left, cover_right, intersection):
    cover_left_copy = cover_left.copy().set_z_index(0)
    scene.play(Create(cover_left_copy))
    scene.wait(.7)
    scene.play(Uncreate(cover_left_copy))
    cover_right_copy = cover_right.copy().set_z_index(0)
    scene.play(Create(cover_right_copy))
    scene.wait(.7)
    scene.play(Uncreate(cover_right_copy))
    scene.add_description("Esta cubierta nos deja con la siguiente intersección.")
    scene.play(Create(cover_right), Create(cover_left), Create(intersection))
    scene.add_description(r"Los índices, identificados con los elementos de la cubierta,"
                          + r" forman los vértices, y la intersección,"
                          + r" una arista.")
    scene.wait()
    left_vertex_coordinates = array([-3., -2, 0])
    left_vertex = Dot(left_vertex_coordinates, color=AZUL, radius=.25)
    right_vertex_coordinates = array([3., -2, 0])
    right_vertex = Dot(right_vertex_coordinates, color=AZUL, radius=.25)
    edge = Line(left_vertex, right_vertex, color=NARANJA)
    scene.play(AnimationGroup(Transform(cover_left, left_vertex),
                              Transform(intersection, edge),
                              Transform(cover_right, right_vertex), run_time=2))
    scene.wait()


class NerveOfALine(MyScene):
    def construct(self):
        self.add_title_and_description(
            "Ejemplo del nervio de la cubierta de un intervalo",
            r"Consideremos la cubierta formada por $\left[0,.6\right)$ y $\left(.4,1\right]$ ")
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

        self.add_description(r"Los índices, identificados con los elementos de la cubierta,"
                                      + r" forman los vértices, y la intersección,"
                                      +  r" una arista.")
        self.wait()

        left_vertex_coordinates = array([-3., -2, 0])
        left_vertex = Dot(left_vertex_coordinates, color=ROSA, radius=.25)
        right_vertex_coordinates = array([3., -2, 0])
        right_vertex = Dot(right_vertex_coordinates, color=AZUL, radius=.25)
        edge = Line(left_vertex, right_vertex, color=NARANJA)

        self.play(AnimationGroup(Transform(cover_left, left_vertex),
                  Transform(intersection, edge),
                  Transform(cover_right, right_vertex), run_time=2))

        self.wait()

class NerveOfARectangle(MyScene):
    def construct(self):
        self.add_title_and_description(
            "Ejemplo del nervio de la cubierta de un rectángulo",
            r"Consideremos la cubierta formada por los siguientes subconjuntos")
        rectangle = Rectangle(width=6, height=2, fill_opacity=1)
        self.play(Create(rectangle))

        cover_left = Rectangle(width=4, height=2, color=AZUL, fill_opacity=1).move_to(LEFT)
        cover_right = Rectangle(width=4, height=2, color=AZUL, fill_opacity=1).move_to(RIGHT)
        intersection = Intersection(cover_right, cover_left, color=NARANJA, fill_opacity=1) \
            .set_z_index(1)

        edge_as_nerve_cover(self, cover_left, cover_right, intersection)

class NerveOfACircle(MyScene):
    def construct(self):
        radius_of_circle =1.5
        self.add_title_and_description(
            "Ejemplo del nervio de la cubierta de un círculo",
            r"Consideremos la cubierta formada por los siguientes subconjuntos")
        circle = Circle(radius=radius_of_circle, color=WHITE).move_to(UP)
        self.play(Create(circle))

        cover_left = Arc(radius=radius_of_circle, start_angle=-PI * (9 / 16), angle=PI + PI * (2 / 16), color=AZUL, arc_center=circle.get_center())
        cover_right = Arc(radius=radius_of_circle, start_angle=PI * (7 / 16), angle=PI + PI * (2 / 16), color=AZUL, arc_center=circle.get_center())
        intersection = VGroup(
            Arc(radius=radius_of_circle, start_angle=-PI * (9 / 16), angle=PI * (2 / 16), color=NARANJA, arc_center=circle.get_center()).set_z_index(1),
            Arc(radius=radius_of_circle, start_angle=PI * (7 / 16), angle=PI * (2 / 16), color=NARANJA, arc_center=circle.get_center()).set_z_index(1))
        edge_as_nerve_cover(self, cover_left, cover_right, intersection)

        self.add_description("Este nervio no parece recuperar el espacio original.")
        self.wait(.8)
        self.add_description("Consideremos una nueva cubierta.")
        self.wait(.8)
        self.play(Uncreate(cover_left), Uncreate(cover_right), Uncreate(intersection))

        circle_copy = circle.copy()

        self.play(Create(circle_copy))

        cover_one = Arc(radius=radius_of_circle, start_angle=-PI * (9 / 16), angle=PI/2 + PI * (2 / 16), color=AZUL,
                         arc_center=circle.get_center())
        cover_one_copy = cover_one.copy()

        cover_two = Arc(radius=radius_of_circle, start_angle=-PI * (1 / 16), angle=PI / 2 + PI * (2 / 16), color=AZUL,
                        arc_center=circle.get_center())
        cover_two_copy = cover_two.copy()

        cover_three = Arc(radius=radius_of_circle, start_angle=PI * (7 / 16), angle=PI/2 + PI * (2 / 16), color=AZUL,
                          arc_center=circle.get_center())
        cover_three_copy = cover_three.copy()

        cover_four = Arc(radius=radius_of_circle, start_angle=PI * (15 / 16), angle=PI / 2 + PI * (2 / 16), color=AZUL,
                          arc_center=circle.get_center())
        cover_four_copy = cover_four.copy()
        intersection = VGroup(
            Arc(radius=radius_of_circle, start_angle=-PI * (9 / 16), angle=PI * (2 / 16), color=VERDOSO,
                arc_center=circle.get_center()).set_z_index(1),
            Arc(radius=radius_of_circle, start_angle=PI * (7 / 16), angle=PI * (2 / 16), color=ROSA,
                arc_center=circle.get_center()).set_z_index(1),
            Arc(radius=radius_of_circle, start_angle=PI * (15 / 16), angle=PI * (2 / 16), color=NARANJA,
                arc_center=circle.get_center()).set_z_index(1),
            Arc(radius=radius_of_circle, start_angle=-PI * (1 / 16), angle=PI * (2 / 16), color=VERDOSO_CLARO,
                arc_center=circle.get_center()).set_z_index(1))

        self.play(Create(cover_one))
        self.play(Uncreate(cover_one))

        self.play(Create(cover_two))
        self.play(Uncreate(cover_two))

        self.play(Create(cover_three))
        self.play(Uncreate(cover_three))

        self.play(Create(cover_four))
        self.play(Uncreate(cover_four))

        self.play(Create(cover_one_copy),
                  Create(cover_two_copy),
                  Create(cover_three_copy),
                  Create(cover_four_copy),
                  Create(intersection))

        self.add_description(r"Esta vez tenemos cuatro elemenmtos de la cubierta y cuatro intersecciones:")

        upper_right = Dot(color=AZUL, radius=.25).next_to(circle_copy.point_at_angle(angle=PI/4), UR)
        upper_left = Dot(color=AZUL, radius=.25).next_to(circle_copy.point_at_angle(angle=PI * (3/ 4)), UL)
        lower_left = Dot(color=AZUL, radius=.25).next_to(circle_copy.point_at_angle(angle=PI * (5 / 4)), DL)
        lower_right = Dot(color=AZUL, radius=.25).next_to(circle_copy.point_at_angle(angle=PI * (7 / 4)), DR)

        upper_edge = Line(upper_right, upper_left, color=ROSA)
        left_edge = Line(upper_left, lower_left, color=NARANJA)
        lower_edge = Line(lower_right, lower_left, color=VERDOSO)
        right_edge = Line(upper_right, lower_right, color=VERDOSO_CLARO)

        self.play(Transform(cover_two_copy, upper_right),
                  Transform(cover_three_copy, upper_left),
                  Transform(cover_four_copy, lower_left),
                  Transform(cover_one_copy, lower_right),
                  Transform(intersection[0], lower_edge),
                  Transform(intersection[1], upper_edge),
                  Transform(intersection[2], left_edge),
                  Transform(intersection[3], right_edge))
        self.wait()
