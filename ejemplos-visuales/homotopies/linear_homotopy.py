import math

from numpy import array, linalg
from manim import *

from basic_scene import MyScene, VERDOSO

SCALE = 4


class LinearHomotopy(MyScene):
    def construct(self):
        self.create_title("Ejemplo de homotopía")

        axes = (Axes(x_range=[0, 1, 1],
                     y_range=[0, 1, 1],
                     x_length=SCALE,
                     y_length=SCALE,
                     tips=True,
                     axis_config={'tip_width':.2, 'tip_height':.2})
                .add_coordinates()
                .set_z_index(0))
        description = r"$H(t,s) = (s, ts^{2}+(1-t)s)$ es una homotopía entre $f(s)=s$ y $g(s)=s^{2}$"

        self.play_linear_homotopy(axes, lambda x : x, lambda x : pow(x, 2), description)

        self.wait()

    def play_linear_homotopy(self, axes, initial_function, final_function, description):
        function_at_0 = axes.plot(lambda x: initial_function(x), x_range=[0, 1])
        function_at_0.set_z_index(2)
        function_at_1 = axes.plot(lambda x: final_function(x), x_range=[0, 1]).set_color(VERDOSO)
        function_at_1.set_z_index(1)

        self.add_description(description)
        self.play(Create(axes))
        self.play(Create(function_at_0))
        self.play(Create(function_at_1))

        def scaled_homotopy(x, y, z, t):
            return x * SCALE - (SCALE/2), (t * (final_function(y)) + (1 - t) * initial_function(y)) * SCALE - (SCALE/2), z

        self.play(Homotopy(scaled_homotopy, function_at_0.apply_function(lambda p: (p + (SCALE / 2)) / SCALE), run_time=5))

class NullHomotopy(MyScene):
    def construct(self):
        self.create_title("Ejemplo de homotopía")

        description = r"$H(t,s) = (s, (1-t)s)$ es una homotopía entre $1_{S}$ y $g(s,t)=0$, donde $S$ es un convexo en $\mathbb{R}^{2}$."

        self.add_description(description)

        def null_homotopy(x, y, z, t):
            return (1 - t) * x, (1 - t) * y, z

        self.play(Homotopy(null_homotopy, Square(fill_opacity=1), run_time=5))

        self.wait()

class NoNullHomotopic(MyScene):
    def construct(self):
        self.create_title("Ejemplo de espacio no contráctil")

        description = r"Un anillo es homotópicamente equivalente a un círculo. Y el círculo no es contráctil."

        self.add_description(description)

        ring = Annulus(1, 2, color=VERDOSO).set_z_index(1)

        def null_homotopy(x, y, z, t):
            first_coordinate = (1-t) * x + t*( x/ linalg.norm(array([x, y]), 2))
            second_coordinate = (1-t) * y + t*( y/ linalg.norm(array([x, y]), 2))
            return first_coordinate, second_coordinate, z
        final_circle = Circle(radius=1, color= VERDOSO, stroke_width=2).set_z_index(2)
        self.play(Homotopy(null_homotopy, ring, run_time=5), Add(final_circle, run_time=1))

        self.wait()



