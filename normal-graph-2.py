from manim import *
from scipy.stats import norm

class NormalGraph2(Scene):
    def construct(self):
        s = ValueTracker(1)
        m = ValueTracker(0)
        axes = Axes(
            x_range=[-3, 3, 0.5],
            y_range=[0, 1, 0.1], 
            axis_config={"color": BLUE,
            "include_numbers": True},
        )

        #creating the graph
        graph = always_redraw(lambda :
            axes.plot(lambda x: norm.pdf(x, loc=m.get_value(), scale=s.get_value()), color=WHITE)
        )

        label = always_redraw(lambda :
            Tex("X $\sim$ Normal(" + str(round(m.get_value(), 1)) + ", " + str(round(s.get_value(), 1)) + ")").to_corner(UL, buff=0.5)
        )

        #displaying
        self.play(Create(axes))
        self.play(Create(graph), Write(label), run_time=2)
        self.wait(1)    
        self.play(s.animate.set_value(0.5), rate_function=linear, run_time=2)
        self.wait(1)
        self.play(s.animate.set_value(1.5), rate_function=linear, run_time=2)
        self.wait(1)
        self.play(s.animate.set_value(1), rate_function=linear, run_time=1)
        self.wait(1.5)
        self.play(m.animate.set_value(1), rate_function=linear, run_time=2)
        self.wait(0.5)
        self.play(m.animate.set_value(-1), rate_function=linear, run_time=3)
        self.wait(1)



