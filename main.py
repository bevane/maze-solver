from tkinter import Tk, BOTH, Canvas

def main():
    win = Window(800, 600)
    p1 = Point(0, 0)
    p2 = Point(800, 600)
    p3 = Point(100, 100)
    p4 = Point(300, 100)
    new_line = Line(p1, p2)
    new_line2 = Line(p2, p3)
    new_line3 = Line(p3, p4)
    win.draw_line(new_line, "black")
    win.draw_line(new_line2, "red")
    win.draw_line(new_line3, "green")
    win.wait_for_close()


class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


class Line:
    def __init__(self, start: Point, end: Point) -> None:
        self.start = start
        self.end = end


    def draw(self, canvas: Canvas, fill_color: str):
        canvas.create_line(
            self.start.x, self.start.y, self.end.x, self.end.y, fill=fill_color, width=2
        )

class Window:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas()
        self.__canvas.pack()
        self.__running = False


    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()


    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()


    def close(self):
        self.__running = False


    def draw_line(self, line: Line, fill_color: str):
        line.draw(self.__canvas, fill_color)


main()
