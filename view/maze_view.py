from tkinter import Canvas, Frame, BOTH
from model.result_Item import Cell
from settings import settings
from time import sleep

class MazeView(Frame):

    def __init__(self, debug=False):
        self._debug = debug
        super().__init__()
        self.master.title("Maze")
        self.pack(fill=BOTH, expand=1)
        self._canvas = Canvas(self)

    def _create_circle(self, x, y, r): #center coordinates, radius
        x0 = x - r
        y0 = y - r
        x1 = x + r
        y1 = y + r
        return self._canvas.create_oval(x0, y0, x1, y1)


    def refresh(self, algo_type, maze, cell_y, cell_x):
        sleep(0.125)
        self._canvas.delete("all")
        for y, row in enumerate(maze):
            for x, column in enumerate(row):
                if algo_type == 'path_finding':
                    cell = column.cell
                else:
                    cell = column
                color = None
                if cell.path:
                    color = settings['path']
                elif cell.current:
                    color = settings['current']
                elif cell.computed:
                    color = settings['computed']
                elif cell.backtracked:
                    color = settings['backtracked']
                elif cell.visited:
                    color = settings['visited']

                if color is not None:
                    x_start = x*cell_x
                    if x != 0:
                        if maze[y][x-1].right_wall_exists():
                            x_start = x*cell_x + 1

                    y_start = y*cell_y
                    if y != 0:
                        if maze[y-1][x].bottom_wall_exists():
                            y_start = y*cell_y + 1


                    self._canvas.create_rectangle(
                        x_start, 
                        y_start, 
                        x*cell_x + cell_x, 
                        y*cell_y + cell_y, 
                        width=0,
                        fill=color
                    )

                for wall in cell.walls.values():
                    if wall[0]:
                        self._canvas.create_line(wall[1], wall[2], wall[3], wall[4])

                if algo_type == 'path_finding':
                    if self._debug:
                        if cell.computed:
                            self._canvas.create_text(
                                x*cell_x + cell_x/4,
                                y*cell_y + cell_y/4,
                                text = column.g * 10
                            )
                            self._canvas.create_text(
                                (x+1)*cell_x - cell_x/4,
                                y*cell_y + cell_y/4,
                                text = column.h * 10
                            )

                            self._canvas.create_text(
                                (x+1)*cell_x - cell_x/2,
                                (y+1)*cell_y - cell_y/4,
                                text = (column.g + column.h) * 10
                            )
                    if column.start:
                        self._create_circle(
                            x*cell_x + cell_x/2,
                            y*cell_y + cell_y/2,
                            (cell_x + cell_y)/2/4
                        )
                    if column.end:
                        self._canvas.create_line(
                            x*cell_x + cell_x/4,
                            y*cell_y + cell_y/4,
                            (x+1)*cell_x - cell_x/4,
                            (y+1)*cell_y - cell_y/4
                        )
                        self._canvas.create_line(
                            (x+1)*cell_x - cell_x/4,
                            y*cell_y + cell_y/4,
                            x*cell_x + cell_x/4,
                            (y+1)*cell_y - cell_y/4
                        )


        self._canvas.pack(fill=BOTH, expand=1)
