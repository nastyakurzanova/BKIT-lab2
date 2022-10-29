
class FigureColor:
    """
    Класс «Цвет фигуры»
    """
    # отдельный класс, ни от кого не наследуется
    def __init__(self):
        self._color = None
    #класс состоит из двух функций - геттера и сеттора
    @property
    def colorproperty(self):
        """
        Get-аксессор
        """
        return self._color

    @colorproperty.setter
    def colorproperty(self, value):
        """
        Set-аксессор
        """
        self._color = value
