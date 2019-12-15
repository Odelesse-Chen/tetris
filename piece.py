from gamedisplay import *

class Piece():

    def __init__(self, shape, screen, gamewall):
        self.x = 4
        self.y = 0
        self.shape = shape
        self.turn_times = 0
        self.screen = screen
        self.is_on_floor = False
        self.game_wall = gamewall

    def turn(self):
        if self.can_turn():
            shape_list_len = len(PIECES[self.shape])
            self.turn_times = (self.turn_times + 1) % shape_list_len
    def can_turn(self):
        shape_list_len = len(PIECES[self.shape])
        turn_times = (self.turn_times + 1) % shape_list_len
        shape_mtx = PIECES[self.shape][turn_times]
        for r in range(len(shape_mtx)):
            for c in range(len(shape_mtx[0])):
                if shape_mtx[r][c] == 'O':
                    if (self.x + c) * CELL_WIDTH + GAME_AREA_LEFT + 1 >= GAME_AREA_RIGHT \
                            or (self.x + c - 1) * CELL_WIDTH + GAME_AREA_LEFT + 1 <= GAME_AREA_LEFT \
                            or (self.y + r + 2) * CELL_WIDTH + GAME_AREA_TOP + 1 >= GAME_AREA_FLOOR \
                            or self.game_wall.is_wall(self.x + c - 1, self.y + r):
                        return False
        return True



    def move_right(self):
        if self.can_move_right():
            self.x += 1
    def move_left(self):
        if self.can_move_left():
            self.x -= 1
    def move_down(self):
        if self.can_move_down():
            self.y += 1
        else:
            self.is_on_floor = True
    def fall_down(self):
        while not self.is_on_floor:
            self.move_down()
    def can_move_right(self):
        shape_mtx0 = PIECES[self.shape]
        shape_mtx1 = shape_mtx0[self.turn_times]

        for r in range(len(shape_mtx1)):
            for c in range(len(shape_mtx1[0])):
                if shape_mtx1[r][c]  == 'O':
                    if ((self.x + c + 1) * CELL_WIDTH + GAME_AREA_LEFT + 1) >= GAME_AREA_RIGHT \
                            or self.game_wall.is_wall(self.x + c + 1, self.y + r):
                        return False
        return True

    def can_move_left(self):
        shape_mtx0 = PIECES[self.shape]
        shape_mtx1 = shape_mtx0[self.turn_times]

        for r in range(len(shape_mtx1)):
            for c in range(len(shape_mtx1[0])):
                if shape_mtx1[r][c]  == 'O':
                    if ((self.x + c - 1) * CELL_WIDTH + GAME_AREA_LEFT + 1) <= GAME_AREA_LEFT \
                            or self.game_wall.is_wall(self.x + c - 1, self.y + r):
                        return False
        return True

    def can_move_down(self):
        shape_mtx0 = PIECES[self.shape]
        shape_mtx1 = shape_mtx0[self.turn_times]

        for r in range(len(shape_mtx1)):
            for c in range(len(shape_mtx1[0])):
                if shape_mtx1[r][c]  == 'O':
                    if ((self.y + r + 1) * CELL_WIDTH + GAME_AREA_TOP + 1) >= GAME_AREA_FLOOR \
                            or self.game_wall.is_wall(self.x + c, self.y + r + 1):
                        return False
        return True


    def paint(self):
        shape_template = PIECES[self.shape]
        shape_tem = shape_template[self.turn_times]
        for r in range(len(shape_tem)):
            for c in range(len(shape_tem[0])):
                if shape_tem[r][c] == 'O':
                    self.draw_cell(self.x + c, self.y + r)

    def draw_cell(self, column, row):
        GameDisplay.draw_cell(self.screen, column, row, PIECE_COLORS[self.shape])

    def hit_wall(self):
        shape_mtx = PIECES[self.shape][self.turn_times]
        for r in range(len(shape_mtx)):
            for c in range(len(shape_mtx[0])):
                if shape_mtx[r][c] == 'O':
                    if self.game_wall.is_wall(self.x + c, self.y + r + 1):
                        return True
        return False
