from colorama import Fore, Back, Style
from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square


def main():
    # Создаем три объекта и даем им значения
    r = Rectangle("синего", 3, 2)
    c = Circle("зеленого", 5)
    s = Square("красного", 5)
    # Выводим значения объекта на экран
    print(Back.BLACK + Fore.BLUE + Style.BRIGHT)
    print(r)
    print(Fore.GREEN)
    print(c)
    print(Fore.RED)
    print(s)


if __name__ == "__main__":
    main()
