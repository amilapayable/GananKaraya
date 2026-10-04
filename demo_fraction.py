from manim import *



config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

class DemoFraction(Scene):

    def construct(self):

        # -------------------------------------------------
        # Background
        # -------------------------------------------------

        background = ImageMobject(
            r"G:\GananKarayaa\Background.jpeg"
        )

        background.set_width(config.frame_width)
        background.set_height(config.frame_height)

        self.add(background)

        # -------------------------------------------------
        # Title
        # -------------------------------------------------

        title1 = Text(
            "2025-කෙටි ප්‍රශ්නපත්‍රයේ 03 ප්‍රශ්නය",
            font="Iskoola Pota",
            color=BLACK
        ).scale(1)

        title2 = Text(
            "භාග සහිත සමීකරණයක් විසඳමු",
            font="Iskoola Pota",
            color=BLACK
        ).scale(0.9)

        title = VGroup(title1, title2).arrange(DOWN, buff=0.15)

        title.scale(0.7)
        title.to_edge(UP)

        self.play(Write(title))
        self.wait(1)

        # -------------------------------------------------
        # Step 1
        # -------------------------------------------------

        equation1 = MathTex(
            r"\frac{4}{x} - \frac{5}{2x} = \frac{1}{8}"
        )

        equation1.set_color(BLACK)
        equation1.scale(1.2)

        self.play(Write(equation1))
        self.wait(2)

        # -------------------------------------------------
        # Step 2
        # -------------------------------------------------

        equation2 = MathTex(
            r"\frac{4}{x} - \frac{5}{2x} = \frac{1}{8}",
            r"\\",
            r"\frac{8}{2x} - \frac{5}{2x} = \frac{1}{8}"
        )

        equation2.set_color(BLACK)
        equation2.scale(1.2)

        self.play(
            Transform(equation1, equation2)
        )

        self.wait(2)


        
        # -------------------------------------------------
        # Step 2b
        # -------------------------------------------------

        equation2b = MathTex(
            r"\frac{4}{x} - \frac{5}{2x} = \frac{1}{8}",
            r"\\",
            r"\frac{8}{2x} - \frac{5}{2x} = \frac{1}{8}",
            r"\\",
            r"\frac{8-5}{2x}  = \frac{1}{8}"
        )

        equation2b.set_color(BLACK)
        equation2b.scale(1.2)

        self.play(
            Transform(equation1, equation2b)
        )

        self.wait(2)


        # -------------------------------------------------
        # Step 3
        # -------------------------------------------------

        equation3 = MathTex(
            r"\frac{4}{x} - \frac{5}{2x} = \frac{1}{8}",
            r"\\",
            r"\frac{8}{2x} - \frac{5}{2x} = \frac{1}{8}",
            r"\\",
            r"\frac{8-5}{2x}  = \frac{1}{8}",
            r"\\",
            r"\frac{3}{2x} = \frac{1}{8}"
        )

        equation3.set_color(BLACK)
        equation3.scale(1.2)

        self.play(
            Transform(equation1, equation3)
        )

        self.wait(2)

        # -------------------------------------------------
        # Step 4
        # -------------------------------------------------

        equation4 = MathTex(
            r"\frac{4}{x} - \frac{5}{2x} = \frac{1}{8}",
            r"\\",
            r"\frac{8}{2x} - \frac{5}{2x} = \frac{1}{8}",
            r"\\",
            r"\frac{8-5}{2x}  = \frac{1}{8}",
            r"\\",
            r"\frac{3}{2x} = \frac{1}{8}",
            r"\\",
            r"8 \times 3 = 2x"
        )

        equation4.set_color(BLACK)
        equation4.scale(1.2)

        self.play(
            Transform(equation1, equation4)
        )

        self.wait(2)

        # -------------------------------------------------
        # Step 5
        # -------------------------------------------------

        equation5 = MathTex(
            r"\frac{4}{x} - \frac{5}{2x} = \frac{1}{8}",
            r"\\",
            r"\frac{8}{2x} - \frac{5}{2x} = \frac{1}{8}",
            r"\\",
            r"\frac{8-5}{2x}  = \frac{1}{8}",
            r"\\",
            r"\frac{3}{2x} = \frac{1}{8}",
            r"\\",
            r"8 \times 3 = 2x",
            r"\\",
            r"2x = 24"
        )

        equation5.set_color(BLACK)
        equation5.scale(1.2)

        self.play(
            Transform(equation1, equation5)
        )

        self.wait(2)

        # -------------------------------------------------
        # Answer
        # -------------------------------------------------

        answer = MathTex(
            r"\frac{4}{x} - \frac{5}{2x} = \frac{1}{8}",
            r"\\",
            r"\frac{8}{2x} - \frac{5}{2x} = \frac{1}{8}",
            r"\\",
            r"\frac{8-5}{2x}  = \frac{1}{8}",
            r"\\",
            r"\frac{3}{2x} = \frac{1}{8}",
            r"\\",
            r"8 \times 3 = 2x",
            r"\\",
            r"2x = 24",
            r"\\",
            r"x = 12"
        )

        # answer = MathTex(
        #     r"""
        #     \begin{aligned}
        #     \frac{4}{x} - \frac{5}{2x} &= \frac{1}{8} \\
        #     \frac{8}{2x} - \frac{5}{2x} &= \frac{1}{8} \\
        #     \frac{8-5}{2x} &= \frac{1}{8} \\
        #     \frac{3}{2x} &= \frac{1}{8} \\
        #     8 \times 3 &= 2x \\
        #     2x &= 24 \\
        #     x &= 12
        #     \end{aligned}
        #     """
        # )
        # highlight1 = SurroundingRectangle(
        #     answer[2],
        #     color=RED,
        #     buff=0.15
        # )

        # highlight2 = SurroundingRectangle(
        #     answer[6],
        #     color=GREEN,
        #     buff=0.15
        # )
        answer.set_color(BLACK)
        answer[2].set_color(BLUE)
        answer[12].set_color(GREEN)

       
        answer.scale(1.5)

        self.play(
            Transform(equation1, answer)
        )
        # self.play(
        #     Create(highlight1),
        #     Create(highlight2)
        # )

        self.wait(3)