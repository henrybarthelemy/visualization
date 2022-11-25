
from manim import *
import random
from scipy.stats import binom

class BinomialFour(Animation):
    def __init__(self, chart: BarChart, **kwargs) -> None:
        super().__init__(chart, **kwargs)
        self.start = 0
        self.end = 1
    
    def interpolate_mobject(self, alpha: float) -> None:
        value = self.start + (alpha * (self.end - self.start))
        self.mobject.change_bar_values(self.flipCoin(4, value))
        print(self.flipCoin(4, value))


    def flipCoin(self, n, p):
        r_values = list(range(n + 1))
        mean, var = binom.stats(n, p)
        dist = [round(binom.pmf(r, n, p), 2) for r in r_values]
        return dist

class Count(Animation):
    def __init__(self, number: DecimalNumber, start: float, end: float, **kwargs) -> None:
        super().__init__(number, **kwargs)
        self.start = start
        self.end = end
    
    def interpolate_mobject(self, alpha: float) -> None:
        value = self.start + (alpha * (self.end - self.start))
        self.mobject.set_value(value)

class AnimateBinomialFourScene(Scene):
    def construct(self):
        chart = BarChart(
            values=[1, 0, 0, 0, 0],
            bar_names = ["zero", "one", "two", "three", "four"],
            y_range = [-0.1, 1, 0.2],
            y_length = 6,
            x_length=  10,
            x_axis_config={"font_size": 36},
        ).scale(0.9)

        
        p = DecimalNumber().set_color(WHITE).scale(0.8)
        p.next_to(chart, UP, buff=0.1)
        text = Tex("p value: ").scale(0.8)
        text.next_to(p, UP, buff=0.2)
        textBin = Tex("X $\sim$ Binomial(4, p)")
        textBin.next_to(chart, DOWN, buff=0.4)
        self.add(text, textBin)
        self.play(Write(p))
        self.play(FadeIn(chart))
        self.wait(0.5)
        self.play(BinomialFour(chart), Count(p, 0, 1), run_time=4, rate_func=linear)
        self.wait()