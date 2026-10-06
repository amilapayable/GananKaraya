from manim import *
import numpy as np


class CircleAngleQuestion(Scene):

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

    
        # =========================================================
        # 1. Question from paper
        # =========================================================

        question = Text(
            "දී ඇති රුපයේ A, B, C, සහ D යනු O කේන්ද්‍රය වූ වෘත්තය මත\n"
            "පිහිටි ලක්ෂ්‍ය හතරකි. දී ඇති තොරතුරු ඇසුරෙන්\n"
            "ADC කෝණයේ විශාලත්වය සොයන්න",
            font="Iskoola Pota",
            font_size=30,
            color=BLACK,
            line_spacing=0.8
        )

        question.to_edge(UP)

        self.play(Write(question))
        self.wait(3)

        # Keep the question visible throughout the video.
        # Reduce it from font-size 30 appearance to font-size 20
        # and move it to the top-left to leave room for the diagram.
        self.play(
            question.animate
            .scale(20 / 30)
            .to_edge(UP, buff=0.2),
            # .to_edge(LEFT, buff=0.2),
            run_time=1
        )
        self.wait(1)

        # =========================================================
        # 2. Circle
        # =========================================================

        radius = 2.5

        circle = Circle(
            radius=radius,
            color=BLACK,
            stroke_width=3
        )

        self.play(Create(circle))

        # =========================================================
        # 3. Define points
        #
        # A = lower-left
        # C = upper-left
        # D = left side, between A and C
        # B = right side
        #
        # Minor arc AC = 110 degrees
        # =========================================================

        # Angles measured from positive X-axis

        angle_A = np.deg2rad(235)
        angle_C = np.deg2rad(125)

        # D is on the minor arc A-C
        angle_D = np.deg2rad(180)

        # B is on the major arc A-C
        angle_B = np.deg2rad(0)

        A = radius * np.array([
            np.cos(angle_A),
            np.sin(angle_A),
            0
        ])

        B = radius * np.array([
            np.cos(angle_B),
            np.sin(angle_B),
            0
        ])

        C = radius * np.array([
            np.cos(angle_C),
            np.sin(angle_C),
            0
        ])

        D = radius * np.array([
            np.cos(angle_D),
            np.sin(angle_D),
            0
        ])

        O = ORIGIN

        # # =========================================================
        # # 4. Points
        # # =========================================================

        dot_A = Dot(A, color=BLACK)
        dot_B = Dot(B, color=BLACK)
        dot_C = Dot(C, color=BLACK)
        dot_D = Dot(D, color=BLACK)
        dot_O = Dot(O, color=BLACK)

        self.play(
            FadeIn(dot_A),
            FadeIn(dot_B),
            FadeIn(dot_C),
            FadeIn(dot_D),
            FadeIn(dot_O)
        )

        # =========================================================
        # 5. Labels
        # =========================================================

        label_A = Text(
            "A",
            font="Arial",
            font_size=30,
            color=BLACK
        ).next_to(dot_A, DOWN + LEFT, buff=0.1)

        label_B = Text(
            "B",
            font="Arial",
            font_size=30,
            color=BLACK
        ).next_to(dot_B, RIGHT, buff=0.1)

        label_C = Text(
            "C",
            font="Arial",
            font_size=30,
            color=BLACK
        ).next_to(dot_C, UP + LEFT, buff=0.1)

        label_D = Text(
            "D",
            font="Arial",
            font_size=30,
            color=BLACK
        ).next_to(dot_D, LEFT, buff=0.1)

        label_O = Text(
            "O",
            font="Arial",
            font_size=30,
            color=BLACK
        ).next_to(dot_O, DOWN, buff=0.15)

        self.play(
            Write(label_A),
            Write(label_B),
            Write(label_C),
            Write(label_D),
            Write(label_O)
        )

        # =========================================================
        # 6. Draw AD, DC, CB, BA
        # =========================================================

        line_AD = Line(
            A, D,
            color=BLACK,
            stroke_width=3
        )

        line_DC = Line(
            D, C,
            color=BLACK,
            stroke_width=3
        )

        line_CB = Line(
            C, B,
            color=BLACK,
            stroke_width=3
        )

        line_BA = Line(
            B, A,
            color=BLACK,
            stroke_width=3
        )

        self.play(
            Create(line_AD),
            Create(line_DC),
            Create(line_CB),
            Create(line_BA)
        )

        # =========================================================
        # 7. Draw AO and OC
        # =========================================================

        line_AO = Line(
            A, O,
            color=BLACK,
            stroke_width=3
        )

        line_OC = Line(
            O, C,
            color=BLACK,
            stroke_width=3
        )

        self.play(
            Create(line_AO),
            Create(line_OC)
        )

        self.wait(2)

        angle_text = MathTex(
            r"110^\circ",
            font_size=34,
            color=BLACK
        )

        # Put 110° inside the AOC angle
        angle_text.move_to(
            np.array([
                -0.65,
                0,
                0
            ])
        )

        self.play(Write(angle_text))

        self.wait(2)
        self.wait(18)

        # =========================================================
        # Red arrows pointing to AOC and ABC
        # Arrow heads are on the RIGHT side
        # =========================================================

        arrow_AOC_red = Arrow(
            start=np.array([-1.4, 0.2, 0]),
            end=np.array([-0.2, 0.2, 0]),
            color=RED,
            buff=0.1,
            stroke_width=5,
            max_tip_length_to_length_ratio=0.15
        )

        arrow_ABC_red = Arrow(
            start=np.array([1.0, 0.2, 0]),
            end=np.array([2.2, 0.2, 0]),
            color=RED,
            buff=0.1,
            stroke_width=5,
            max_tip_length_to_length_ratio=0.15
        )

        self.play(
            GrowArrow(arrow_AOC_red),
            GrowArrow(arrow_ABC_red)
        )

        # self.wait(1)
        # =========================================================
        # Blue arrows pointing to ADC and major arc AOC
        # Arrow heads are on the LEFT side
        # =========================================================

        arrow_ADC_blue = Arrow(
            start=np.array([-1.0, -0.2, 0]),
            end=np.array([-2.3, 0, 0]),
            color=BLUE,
            buff=0.1,
            stroke_width=5,
            max_tip_length_to_length_ratio=0.15
        )

        arrow_AOC_major_blue = Arrow(
            start=np.array([1.4, -0.2, 0]),
            end=np.array([0.1, 0, 0]),
            color=BLUE,
            buff=0.1,
            stroke_width=5,
            max_tip_length_to_length_ratio=0.15
        )

        self.play(
            GrowArrow(arrow_ADC_blue),
            GrowArrow(arrow_AOC_major_blue)
        )

        # self.wait(1)

        # =========================================================
        # Move the complete diagram to the top-right.
        #
        # The question remains visible at the top-left.
        # The entire diagram (circle, points, labels, lines,
        # and 110-degree label) is reduced to half size.
        # =========================================================

        diagram = VGroup(
            circle,
            dot_A,
            dot_B,
            dot_C,
            dot_D,
            dot_O,
            label_A,
            label_B,
            label_C,
            label_D,
            label_O,
            line_AD,
            line_DC,
            line_CB,
            line_BA,
            line_AO,
            line_OC,
            angle_text,
            arrow_AOC_red,
            arrow_ABC_red,
            arrow_ADC_blue,
            arrow_AOC_major_blue
        )

        self.play(
            diagram.animate
            .scale(0.5)
            .to_corner(UR, buff=0.25),
            # .to_edge(RIGHT, buff=0.5),
            run_time=1.5
        )



        # =========================================================
        # . Move Question to left
        # =========================================================

        self.play(
            question.animate
            .to_edge(LEFT, buff=0.3),
            run_time=1
        )


        explanation = Text(
            "ඕනෑම ලක්ෂයක් වටා ඇති සියලුම කොන වල එකතුව 360°\n"
            "වෘත්තයේ සම්පූර්ණ කෝණය = 360°",
            font="Iskoola Pota",
            font_size=30,
            color=BLACK
        )

        # Initially show in the center
        explanation.move_to(ORIGIN)

        self.play(Write(explanation))
        self.wait(25)
        self.wait(8)
        # Move to the final position and reduce the size
        self.play(
            explanation.animate
            .scale(20 / 30)
            .to_edge(UP)
            .shift(DOWN * 0.8),
            run_time=1
        )

        self.wait(2)


        # =========================================================
        # 10. Explain angle at circumference
        # =========================================================

        theory = Text(
            "වෘත්ත චාපයක් මගින් කේන්ද්‍රයේ ආපාතනය කරන කෝණය \n පරිධියේ ආපාතනය කරන කෝණය මෙන් දෙගුණයක් වේ",
            font="Iskoola Pota",
            font_size=34,
            color=BLACK,
            line_spacing=0.8
        )

        theory.move_to(ORIGIN)

        self.play(Write(theory))
        self.wait(72)
        self.wait(10)
        self.wait(50)
        # Shrink and move underneath the explanation
        self.play(
            theory.animate
            .scale(20 / 34)
            .next_to(explanation, DOWN, buff=0.4),
            run_time=1
        )

        self.wait(2)



        # =========================================================
        # 11. Find the major arc AC
        # =========================================================

        calculation1 = MathTex(
            r"\text{Major}AOC = 360^\circ - 110^\circ = 250^\circ ",
            font_size=38,
            color=BLACK
        )


        # Initial position: about 3/4 of the way down from the top
        calculation1.move_to(
            UP * 0.5
        )

        self.play(Write(calculation1))
        self.wait(2)


        self.wait(7)
        self.wait(15)

        # =========================================================
        # 12. Calculate ADC
        # =========================================================

        step1 = MathTex(
            r"\angle ADC = \frac{250^\circ}{2}",
            font_size=38,
            color=BLACK
        )

        step1.next_to(
            calculation1,
            DOWN,
            buff=0.4
        )

        self.play(Write(step1))
        self.wait(7)


        self.wait(2)

        # =========================================================
        # 13. Final answer
        # =========================================================

        answer = Text(
            "පිළිතුර : ADC කෝණය = 125°",
            font="Iskoola Pota",
            font_size=46,
            color=BLACK
        )

        answer.next_to(
            step1,
            DOWN,
            buff=0.5
        )

        self.play(Write(answer))
        self.wait(24)
