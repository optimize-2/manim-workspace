from manim import *


class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen

class Text(Scene):
    def construct(self):
        text1 = Tex('遗憾的，$2 \\times 3 = 6$, yi han de.', tex_template = TexTemplateLibrary.ctex)
        self.play(Write(text1))
        # text2 = Tex('不幸的，$1 + 1 = 2$', tex_template = TexTemplateLibrary.ctex)
        # self.play(Write(text2))

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set color and transparency

        square = Square()  # create a square
        square.rotate(PI / 4)  # rotate a certain amount

        self.play(Create(square))  # animate the creation of the square
        self.play(Transform(square, circle))  # interpolate the square into the circle
        self.play(FadeOut(square))  # fade out animation