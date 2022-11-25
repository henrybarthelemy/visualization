from manim import *
from scipy.stats import norm

class CreateGraph(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-3, 3, 0.5],
            y_range=[0, 1, 0.1], 
            axis_config={"color": BLUE,
            "include_numbers": True},
        )

        #creating the graph
        graph = axes.plot(lambda x: norm.pdf(x), color=WHITE)
        label = Tex("X $\sim$ Normal(0, 1.0)")
        label.to_corner(UL, buff=0.5)

        #displaying
        self.play(Create(axes))
        self.play(Create(graph), Write(label))
        #self.wait(1)
        #self.play(Create(graph))

        #graph from sigma 1 to 1.5
        for s in range(10, 4, -1):
            graph2 = axes.plot(lambda x: norm.pdf(x, scale = (s / 10)), color=WHITE)
            label2 = Tex("X $\sim$ Normal(0, " + str(s/10) + ")")
            label2.to_corner(UL, buff=0.5)
            self.play(ReplacementTransform(graph, graph2), ReplacementTransform(label, label2), run_time = 0.7)
            graph = graph2
            label = label2
            self.wait(0.05)
        #self.play(Transform(graph, graph2), Transform(graph_label, graph_label2))
        self.wait(1)
        #go back to N(0,1)
        graph2 = axes.plot(lambda x: norm.pdf(x), color=WHITE)
        label2 = Tex("X $\sim$ Normal(0, 1.0)")
        label2.to_corner(UL, buff=0.5)
        self.play(ReplacementTransform(graph, graph2), ReplacementTransform(label, label2))
        graph = graph2
        label = label2

        #Graph from sigma 1 to 0.5
        for s in range(10, 16, 1):
            graph2 = axes.plot(lambda x: norm.pdf(x, scale = (s / 10)), color=WHITE)
            label2 = Tex("X $\sim$ Normal(0, " + str(s/10) + ")")
            label2.to_corner(UL, buff=0.5)
            self.play(ReplacementTransform(graph, graph2), ReplacementTransform(label, label2), run_time = 0.7)
            graph = graph2
            label = label2
            self.wait(0.05)
        
        #go back to N(0, 1)
        self.wait(0.5)
        graph2 = axes.plot(lambda x: norm.pdf(x), color=WHITE)
        label2 = Tex("X $\sim$ Normal(0.0, 1)")
        label2.to_corner(UL, buff=0.5)
        self.play(ReplacementTransform(graph, graph2), ReplacementTransform(label, label2))
        graph = graph2
        label = label2
        self.wait(0.5)


        #Now vary the mean = 1
        graph2 = axes.plot(lambda x: norm.pdf(x, loc = 1), color=WHITE)
        label2 = Tex("X $\sim$ Normal(1, 1)")
        label2.to_corner(UL, buff=0.5)
        self.play(ReplacementTransform(graph, graph2), ReplacementTransform(label, label2))
        graph = graph2
        label = label2
        self.wait(1)

        #Now vary the mean = -1
        graph2 = axes.plot(lambda x: norm.pdf(x, loc = -1), color=WHITE)
        label2 = Tex("X $\sim$ Normal(-1, 1)")
        label2.to_corner(UL, buff=0.5)
        self.play(ReplacementTransform(graph, graph2), ReplacementTransform(label, label2))
        graph = graph2
        label = label2
        self.wait(1)

        # #Now vary the mean 0 -> -0.5
        # for s in range(0, -6, -1):
        #     graph2 = axes.plot(lambda x: norm.pdf(x, loc = (s / 10)), color=WHITE)
        #     label2 = Tex("X $\sim$ Normal(" + str(s / 10) + ", 1)")
        #     label2.to_corner(UL, buff=0.5)
        #     self.play(ReplacementTransform(graph, graph2), ReplacementTransform(label, label2), run_time = 0.4)
        #     graph = graph2
        #     label = label2
        
        #go back to N(0, 1)
        graph2 = axes.plot(lambda x: norm.pdf(x), color=WHITE)
        label2 = Tex("X $\sim$ Normal(0, 1.0)")
        label2.to_corner(UL, buff=0.5)
        self.play(ReplacementTransform(graph, graph2), ReplacementTransform(label, label2))
        graph = graph2
        label = label2
        self.wait()

        

class CreateGraphNormal(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-3, 3, 0.5],
            y_range=[0, 1, 0.1], 
            axis_config={"color": BLUE,
            "include_numbers": True},
        )

        #creating the graph
        graph = axes.plot(lambda x: norm.pdf(x), color=WHITE)
        label = Tex("X $\sim$ Normal(0, 1)")
        label.to_corner(UL, buff=0.5)

        #displaying
        self.play(Create(axes))
        self.play(Create(graph), Write(label))
        self.wait(1)    