from piece import  *
class GameWall():

    def __init__(self, screen):
        self.screen = screen
        self.area = []

        line = [WALL_BLANK_LABEL] *COLUMN_NUM
        for i in range(LINE_NUM):
            self.area.append(line[:])

    def print(self):
        print(len(self.area), 'raw', len(self.area[0]), 'column')
        for line in self.area:
            print(line)

    def set_cell(self, column, row, shape_label):
                self.area[row][column] = shape_label

    def add_to_wall(self, piece):
        shape_turn = PIECES[piece.shape][piece.turn_times]
        for r in range(len(shape_turn)):
            for c in range(len(shape_turn[0])):
                if shape_turn[r][c] == 'O':
                    self.set_cell(piece.x + c, piece.y + r, piece.shape)

    def is_wall(self, column, row):
        return self.area[row][column] != WALL_BLANK_LABEL

    def eliminate_lines(self):
        lines_eliminate = []
        for r in range(LINE_NUM):
            if self.is_full(r):
                lines_eliminate.append(r)

        for r in lines_eliminate:
            self.copy_down(r)
            for c in range(COLUMN_NUM):
                self.area[0][c] = WALL_BLANK_LABEL

        eliminated_num = len(lines_eliminate)
        assert(eliminated_num <= 4 and eliminated_num >= 0)
        if eliminated_num < 3:
            score = eliminated_num * 100
        elif eliminated_num == 3:
            score = 400
        else:
            score = 800
        return score
    def is_full(self, row):
        for c in range(COLUMN_NUM):
            if self.area[row][c] == WALL_BLANK_LABEL:
                return False
        return True

    def copy_down(self, row):
        for r in range(row, 0, -1):
            for c in range(COLUMN_NUM):
                self.area[r][c] = self.area[r - 1][c]
    def clear(self):
        for r in range(LINE_NUM):
            for c in range(COLUMN_NUM):
                self.area[r][c] = WALL_BLANK_LABEL



