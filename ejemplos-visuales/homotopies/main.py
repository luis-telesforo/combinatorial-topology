from manim import *

from MyScene import MyScene, VERDOSO


class HomotopyLine(MyScene):
    def construct(self):
        self.create_title("Ejemplo de homotopía")
        scale = 4

        axes = (Axes(x_range=[0, 1, 1],
                     y_range=[0, 1, 1],
                     x_length=scale,
                     y_length=scale,
                     tips=True,
                     axis_config={'tip_width':.2, 'tip_height':.2})
                .add_coordinates()
                .set_z_index(0))
        line = axes.plot(lambda x: x, x_range=[0, 1])
        line.set_z_index(2)
        parabola = axes.plot(lambda x: x ** 2, x_range=[0, 1]).set_color(VERDOSO)
        parabola.set_z_index(1)
        description = r"$H(t,s) = (s, ts^{2}+(1-t)s)$ es una homotopía entre $f(s)=s$ y $g(s)=s^{2}$"
        self.add_description(description)
        self.play(Create(axes))
        self.play(Create(line))
        self.play(Create(parabola))

        def scaled_homotopy(x, y, z, t):
            return x * scale - (scale/2), (t * (y ** 2) + (1 - t) * y) * scale - (scale/2), z

        self.play(Homotopy(scaled_homotopy, line.apply_function(lambda p: (p + (scale/2))/scale), rate_func=linear, run_time=5))

        self.wait()
