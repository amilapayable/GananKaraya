from manim import *


class TankFilling(Scene):
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

        title = Text(
            "2025-කෙටි ප්‍රශ්නපත්‍රයේ 05 ප්‍රශ්නය",
            font="Iskoola Pota",
            color=BLACK
        ).scale(1)



        # title = VGroup(title1, title2).arrange(DOWN, buff=0.15)

        title.scale(0.7)
        title.to_edge(UP)

        self.play(Write(title))
        self.wait(1)

        self.play(FadeOut(title, run_time=0.3))

        # -------------------------------------------------
        # 1. Question from the paper
        # -------------------------------------------------

        question = Text(
            "හිස් ටැංකියකට සවිකර ඇති නළයකින් ජලය ගලා එන ශිග්‍රතාවය මිනිත්තුවට ලීටර 28කි.\n"
            "ටැංකියෙහි ධාරිතාවය ලීටර 112ක් නම්, ටැංකිය සම්පුර්ණයෙන් ජලයෙන් පිරවීමට මිනිත්තු කියක් ගත වේ ද ?",
            font="Iskoola Pota",
            font_size=20,
            line_spacing=0.8,
            color=BLACK
        )

        question.to_edge(UP)

        self.play(Write(question))
        self.wait(2)

        # -------------------------------------------------
        # 2. Given values
        # -------------------------------------------------

        volume = Text(
            "ටැංකියේ ධාරිතාවය = 112L",
            font="Iskoola Pota",
            font_size=40,
            color=BLACK
        )

        rate = Text(
            "මිනිත්තුවකට ගලා එන ජල ප්‍රමාණය = 28L",
            font="Iskoola Pota",
            font_size=40,
            color=BLACK
        )

        values = VGroup(volume, rate).arrange(
            DOWN,
            buff=0.35
        )

        values.next_to(question, DOWN, buff=0.5)

        self.play(Write(volume))
        self.play(Write(rate))
        self.wait(2)

        # -------------------------------------------------
        # 3. Formula
        # -------------------------------------------------

        formula_title = Text(
            "කාලය සොයමු",
            font="Iskoola Pota",
            font_size=34,
            color=BLACK
        )

        formula_title.next_to(values, DOWN, buff=0.5)

        formula = Text(
            "කාලය = මුළු ජල ප්‍රමාණය ÷ මිනිත්තුවකට ගලා එන ජල ප්‍රමාණය",
            font="Iskoola Pota",
            font_size=36,
            color=BLACK
        )

        formula.next_to(formula_title, DOWN, buff=0.25)

        self.play(Write(formula_title))
        self.play(Write(formula))
        self.wait(2)
        self.play(FadeOut(formula_title, run_time=0.3))
        self.play(FadeOut(formula, run_time=0.3))
        # -------------------------------------------------
        # 4. Substitute values
        # -------------------------------------------------

        formula_text = Text(
            "කාලය =",
            font="Iskoola Pota",
            font_size=40,
            color=BLACK
        )

        fraction = MathTex(
            r"\frac{112}{28}",
            font_size=48,
            color=BLACK
        )

        formula = VGroup(
            formula_text,
            fraction
        ).arrange(RIGHT, buff=0.2)

        self.play(Write(formula))
        self.wait(2)
        # -------------------------------------------------
        # 5. Calculate
        # -------------------------------------------------

        # result = MathTex(
        #     r"\text{කාලය} = 4\text{ මිනිත්තු}",
        #     font_size=52
        # )

        # result.next_to(calculation, DOWN, buff=0.4)

        # self.play(Write(result))
        # self.wait(2)

        # -------------------------------------------------
        # 6. Final answer
        # -------------------------------------------------

        answer = Text(
            "පිළිතුර : මිනිත්තු 4යි",
            font="Iskoola Pota",
            font_size=44,
            color=BLACK
        )

        answer.to_edge(DOWN)
        answer.shift(UP * 1.0)   # quite a bit up

        self.play(
            Write(answer)
        )

        self.wait(3)