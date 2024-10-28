from lab_python_oop.figure import Figure
from lab_python_oop.color import FigureColor

class Rectangle(Figure):
    figure_type="rectangle"

    def __init__(self,width,height,color):
        self.fc=FigureColor()
        self.fc.color=color
        self.width=width
        self.height=height

    @classmethod
    def get_figure_type(cls): return cls.figure_type

    def square(self): return self.width*self.height
        
    def __repr__(self): return 'figure: {}; width: {}; height: {}; color: {}; square: {};'.format(Rectangle.get_figure_type(),self.width,self.height,self.fc.color,self.square())