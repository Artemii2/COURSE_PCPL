from lab_python_oop.rectangle import Rectangle


class Square(Rectangle):
    figure_type="square"

    def __init__(self, side, color):
        self.side=side
        super().__init__(side, side, color)

    @classmethod
    def get_figure_type(cls): return cls.figure_type

    def __repr__(self): return 'figure: {}; side: {}; color: {}; square: {};'.format(Square.get_figure_type(),self.side,self.fc.color,self.square())