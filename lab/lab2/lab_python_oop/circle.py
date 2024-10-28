import math
from lab_python_oop.color import FigureColor
from lab_python_oop.figure import Figure


class Circle(Figure):
    figure_type="circle"

    def __init__(self,radius,color):
        self.fc=FigureColor()
        self.fc.color=color
        self.radius=radius

    @classmethod
    def get_figure_type(cls): return cls.figure_type

    def square(self): return math.pi*math.pow(self.radius,2)

    def __repr__(self): return 'figure: {}; radius: {}; color: {}; square: {};'.format(Circle.get_figure_type(),self.radius,self.fc.color,self.square())