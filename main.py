from tkinter import Tk, BOTH, Canvas


def main():
    win = Window(800, 600)
    top_left = Point(10, 10)
    bottom_right = Point(50, 50)
    cell = Cell(top_left, bottom_right, win)
    cell.draw()
    win.wait_for_close()


class Point:
    def __init__(self, x: int, y: int) -> None:
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
    def __init__(self, width: int, height: int) -> None:
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


class Cell:
    def __init__(self, top_left: Point, bottom_right: Point, win: Window) -> None:
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = top_left.x
        self._y1 = top_left.y
        self._x2 = bottom_right.x
        self._y2 = bottom_right.y
        self._win = win

    def draw(self):
        if self.has_left_wall:
            left_wall_top = Point(self._x1, self._y1)
            left_wall_bottom = Point(self._x1, self._y2)
            left_wall = Line(left_wall_top, left_wall_bottom)
            self._win.draw_line(left_wall, "black")

        if self.has_right_wall:
            right_wall_top = Point(self._x2, self._y1)
            right_wall_bottom = Point(self._x2, self._y2)
            right_wall = Line(right_wall_top, right_wall_bottom)
            self._win.draw_line(right_wall, "black")

        if self.has_top_wall:
            top_wall_left = Point(self._x1, self._y1)
            top_wall_right = Point(self._x2, self._y1)
            top_wall = Line(top_wall_left, top_wall_right)
            self._win.draw_line(top_wall, "black")

        if self.has_bottom_wall:
            bottom_wall_left = Point(self._x1, self._y2)
            bottom_wall_right = Point(self._x2, self._y2)
            bottom_wall = Line(bottom_wall_left, bottom_wall_right)
            self._win.draw_line(bottom_wall, "black")


main()
