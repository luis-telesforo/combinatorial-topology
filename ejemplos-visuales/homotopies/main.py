from manim import *

from MyScene import MyScene, VERDOSO


class HomotopyLine(MyScene):
    def construct(self):
        self.create_title("Ejemplo de homotopía")

        axes = Axes(x_range=[-1, 1, 1], y_range=[-1, 1, 1], x_length=2, y_length=2)
        line = axes.plot(lambda x: x, x_range=[0, 1])
        line.set_z_index(2)
        parabola = axes.plot(lambda x: x ** 2, x_range=[0, 1]).set_color(VERDOSO)
        parabola.set_z_index(1)
        description = r"$H(t,s) = (s, ts^{2}+(1-t)s)$ es una homotopía entre $f(s)=s$ y $g(s)=s^{2}$"
        self.add_description(description)
        self.play(Create(line.apply_function(lambda p: p * 3 - 1.5)))
        self.play(Create(parabola.apply_function(lambda p: p * 3 - 1.5)))

        def scaled_homotopy(x, y, z, t):
            return x * 3 - 1.5, (t * (y ** 2) + (1 - t) * y) * 3 - 1.5, z

        self.play(Homotopy(scaled_homotopy, line.apply_function(lambda p: (p + 1.5)/3), rate_func=linear, run_time=5))

        self.wait()
