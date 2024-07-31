from tkinter import Tk, BOTH, Canvas
import time


def main():
    win = Window(800, 600)
    maze = Maze(10, 10, 5, 5, 50, 50, win)
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
    def __init__(self, win: Window) -> None:
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = win

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
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

    def draw_move(self, to_cell, undo=False):
        from_cell_center_x = int((self._x2 + self._x1) / 2)
        from_cell_center_y = int((self._y2 + self._y1) / 2)
        to_cell_center_x = (to_cell._x2 + to_cell._x1) / 2
        to_cell_center_y = (to_cell._y2 + to_cell._y1) / 2
        from_point = Point(from_cell_center_x, from_cell_center_y)
        to_point = Point(to_cell_center_x, to_cell_center_y)
        move_line = Line(from_point, to_point)
        line_color = "red" if undo else "gray"
        self._win.draw_line(move_line, line_color)


class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win,
    ) -> None:
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self._create_cells()

    def _create_cells(self):
        for col in range(0, self._num_cols):
            self._cells.append([])
            for row in range(0, self._num_rows):
                self._cells[col].append(Cell(self._win))
                self._draw_cell(col, row)

    def _draw_cell(self, col, row):
        x1 = self._x1 + self._cell_size_x * col
        y1 = self._y1 + self._cell_size_y * row
        x2 = self._x1 + self._cell_size_x * col + self._cell_size_x
        y2 = self._y1 + self._cell_size_y * row + self._cell_size_y
        self._cells[col][row].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)


main()
