from graphics import Window, Point, Line
import time


class Cell:
    def __init__(self, win: Window = None) -> None:
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

        left_wall_top = Point(self._x1, self._y1)
        left_wall_bottom = Point(self._x1, self._y2)
        left_wall = Line(left_wall_top, left_wall_bottom)
        if self.has_left_wall:
            self._win.draw_line(left_wall, "black")
        else:
            self._win.draw_line(left_wall, "white")

        right_wall_top = Point(self._x2, self._y1)
        right_wall_bottom = Point(self._x2, self._y2)
        right_wall = Line(right_wall_top, right_wall_bottom)
        if self.has_right_wall:
            self._win.draw_line(right_wall, "black")
        else:
            self._win.draw_line(right_wall, "white")

        top_wall_right = Point(self._x2, self._y1)
        top_wall_left = Point(self._x1, self._y1)
        top_wall = Line(top_wall_left, top_wall_right)
        if self.has_top_wall:
            self._win.draw_line(top_wall, "black")
        else:
            self._win.draw_line(top_wall, "white")

        bottom_wall_right = Point(self._x2, self._y2)
        bottom_wall_left = Point(self._x1, self._y2)
        bottom_wall = Line(bottom_wall_left, bottom_wall_right)
        if self.has_bottom_wall:
            self._win.draw_line(bottom_wall, "black")
        else:
            self._win.draw_line(bottom_wall, "white")

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
        win=None,
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
        self._break_entrance_and_exit()

    def _create_cells(self):
        for col in range(0, self._num_cols):
            self._cells.append([])
            for row in range(0, self._num_rows):
                self._cells[col].append(Cell(self._win))
                if self._win:
                    self._draw_cell(col, row)

    def _draw_cell(self, col, row):
        x1 = self._x1 + self._cell_size_x * col
        y1 = self._y1 + self._cell_size_y * row
        x2 = self._x1 + self._cell_size_x * col + self._cell_size_x
        y2 = self._y1 + self._cell_size_y * row + self._cell_size_y
        self._cells[col][row].draw(x1, y1, x2, y2)
        if self._win:
            self._animate()

    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        if self._win:
            self._draw_cell(0, 0)
            self._draw_cell(self._num_cols - 1, self._num_rows - 1)