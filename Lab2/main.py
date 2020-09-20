from lab_python_oop.Rectangle import Rectangle
from lab_python_oop.Circle import Circle
from lab_python_oop.Square import Square
import arrow


def main():
    print("ИУ5-51Б Алехин Сергей Лаб2")
    print(arrow.now(), "\n")

    rectangle = Rectangle("синего", 2, 2)
    circle = Circle("зеленого", 2)
    square = Square("красного", 2)

    print(rectangle)
    print(circle)
    print(square)


if __name__ == "__main__":
    main()
