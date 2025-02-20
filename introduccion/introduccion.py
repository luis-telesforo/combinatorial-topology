from manim import Text, Create, Title, Axes, Dot, RIGHT, MoveToTarget, \
    VGroup, UP, LEFT, DOWN, Uncreate, Write, TransformMatchingShapes, Annulus, Line, BLACK, Triangle, Polygon, \
    Transform, WHITE, Unwrite
from pandas import read_csv

from white_slide import WhiteBackgroundSlide, VERDOSO, NARANJA


class Presentation(WhiteBackgroundSlide):
    def construct(self):
        main_question = Text(r"¿Qué es el Análisis topológico de datos?")
        self.play(Write(main_question))
        self.next_slide()

        self.play(Unwrite(main_question))
        self.next_slide()
        analisis_topologico_datos = Title(r"¿Por qué importa la topoología de los datos?")
        self.play(Create(analisis_topologico_datos))
        self.next_slide()

        dataframe = read_csv('../introduccion/datasets/datasaurus.csv')
        dataset_to_plot = ['wide_lines', 'high_lines', 'away', 'dots', 'circle']
        positions = [UP * 2 + LEFT * 8, UP * 2 + LEFT * 4,
                     LEFT * 6,
                     DOWN * 2 + LEFT * 8, DOWN * 2 + LEFT * 4]
        dataset_and_position = zip(dataset_to_plot, positions)
        for dataset, position in dataset_and_position:
            particular_dataset = dataframe[dataframe['dataset'] == dataset]
            particular_dataset.drop(columns='dataset', inplace=True)
            axes_and_dots = self.create_scatter(particular_dataset)
            axes_and_dots.generate_target()
            axes_and_dots.target.shift(position).scale(.5)
            self.play(MoveToTarget(axes_and_dots))
            self.next_slide()

        dino = dataframe[dataframe['dataset'] == 'dino']
        dino.drop(columns='dataset', inplace=True)
        self.create_scatter(dino)
        self.next_slide()

        self.play(Uncreate(analisis_topologico_datos))
        mismos_estadisticos = Title(r"¡Mismos estadísticos diferente forma!")
        self.play(Write(mismos_estadisticos))
        self.next_slide()

        self.wipe(self.mobjects_without_canvas)
        malas_noticias = Text(r"¡No podemos ver la forma de los datos!")
        self.play(Create(malas_noticias))
        buenas_noticias = Text(r"¡Podemos calcular invariantes de su forma!")
        self.next_slide()

        self.play(TransformMatchingShapes(malas_noticias, buenas_noticias))
        self.next_slide()

        self.wipe(self.mobjects_without_canvas)
        problema = Title(r"Si nuestros datos son tomados del siguiente espacio")
        self.next_slide()

        anillo = Annulus(1, 2, color=VERDOSO).set_z_index(1)
        self.play(Create(problema), Create(anillo))
        self.next_slide()

        self.play(Uncreate(problema))
        corolario_teorema = Title(r"Teorema: este espacio es conexo y tiene un hoyo")
        self.play(Create(corolario_teorema))
        self.next_slide()

        self.wipe(self.mobjects_without_canvas)
        malas_noticias_de_nuevo = Title(r"¿Cómo verificamos computacionalmente las hipótesis?")
        self.play(Create(malas_noticias_de_nuevo))
        self.next_slide()

        self.wipe(self.mobjects_without_canvas)
        buenas_noticias_de_nuevo = VGroup(Text(r"Podemos convertir"),
                                          Text(r"muchos de esos"),
                                          Text(r"teoremas").set_color(NARANJA),
                                          Text(r"en algoritmos").set_color(NARANJA)).arrange(DOWN)
        self.play(Write(buenas_noticias_de_nuevo))
        axes = Axes(x_range=[-2,2,1], y_range=[-2,2,1])
        afuera_ai = Dot(axes.c2p(-2,2), color=BLACK).set_z_index(1)
        afuera_ad = Dot(axes.c2p(2,2), color=BLACK).set_z_index(1)
        afuera_bi = Dot(axes.c2p(-2, -2), color=BLACK).set_z_index(1)
        afuera_bd = Dot(axes.c2p(2, -2), color=BLACK).set_z_index(1)

        dentro_ai = Dot(axes.c2p(-1, 1), color=BLACK).set_z_index(1)
        dentro_ad = Dot(axes.c2p(1, 1), color=BLACK).set_z_index(1)
        dentro_bi = Dot(axes.c2p(-1, -1), color=BLACK).set_z_index(1)
        dentro_bd = Dot(axes.c2p(1, -1), color=BLACK).set_z_index(1)

        triangulo_1 = Polygon(afuera_ai.get_center(), dentro_ai.get_center(), dentro_ad.get_center(), fill_opacity=.6).set_z_index(0)
        triangulo_2 = Polygon(afuera_ai.get_center(), dentro_ad.get_center(), afuera_ad.get_center(), fill_opacity=.6).set_z_index(0)
        triangulo_3 = Polygon(afuera_bi.get_center(), dentro_ai.get_center(), dentro_bi.get_center(), fill_opacity=.6).set_z_index(0)
        triangulo_4 = Polygon(afuera_bi.get_center(), dentro_bi.get_center(), afuera_bd.get_center(), fill_opacity=.6).set_z_index(0)
        triangulo_5 = Polygon(afuera_ai.get_center(), dentro_ai.get_center(), afuera_bi.get_center(), fill_opacity=.6).set_z_index(0)
        triangulo_6 = Polygon(afuera_bd.get_center(), dentro_bi.get_center(), dentro_bd.get_center(), fill_opacity=.6).set_z_index(0)
        triangulo_7 = Polygon(afuera_ad.get_center(), dentro_bd.get_center(), afuera_bd.get_center(), fill_opacity=.6).set_z_index(0)
        triangulo_8 = Polygon(afuera_ad.get_center(), dentro_ad.get_center(), dentro_bd.get_center(), fill_opacity=.6).set_z_index(0)

        triangles = VGroup(triangulo_1, triangulo_2, triangulo_3, triangulo_4, triangulo_5, triangulo_6, triangulo_7,
                         triangulo_8)
        complejo = VGroup(afuera_ai,
                          afuera_ad,
                          afuera_bi,
                          afuera_bd,
                          dentro_ai,
                          dentro_ad,
                          dentro_bi,
                          dentro_bd,
                          triangles)
        self.play((Create(complejo)))
        self.wait(3)
        self.next_slide()

        for triangle in triangles:
            triangle.generate_target()
            triangle.target.set_fill(color=WHITE)
            self.play(MoveToTarget(triangle))




    def create_scatter(self, series):
        axes = Axes(x_range=[0, 100, 100], y_range=[0, 100, 100])
        axes.scale(.4).move_to(RIGHT * 3)
        self.play(Create(axes))
        axes_and_dots = VGroup(axes)
        for x, y in series.values:
            dot = Dot(axes.c2p(x, y), color=VERDOSO, radius=.03)
            axes_and_dots.add(dot)
            self.play(Create(dot, run_time=.07))
        return axes_and_dots


