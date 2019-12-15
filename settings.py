SCREEN_WIDTH = 1200
SCREEN_HIGH = 745
CELL_WIDTH = 30
LINE_NUM = 20
COLUMN_NUM = 10
GAME_AREA_WIDTH = CELL_WIDTH * 10
GAME_AREA_HIGH = CELL_WIDTH * 20
GAME_AREA_LEFT = (SCREEN_WIDTH - GAME_AREA_WIDTH) // 2
GAME_AREA_RIGHT = GAME_AREA_LEFT + GAME_AREA_WIDTH
GAME_AREA_TOP = (SCREEN_HIGH - GAME_AREA_HIGH) // 2
GAME_AREA_FLOOR = GAME_AREA_HIGH + GAME_AREA_TOP
EDGE_COLOR = (0, 0, 0)
CELL_COLOR = (100, 100, 100)
BG_COLOR = (230, 230, 230)
WALL_BLANK_LABEL = '-'
TIMER_INTERVAL = 1000
EDGE_WIDTH = 5
MARGIN_WIDTH = 40
DIFFICULTY_LEVEL_INTERVAL = 5000
TIMER_DECREASE_VALUE = 50

S_SHAPE_TEMPLATE = [['.OO.',
                     'OO..',
                     '....'],
                    ['.O..',
                     '.OO.',
                     '..O.']]

Z_SHAPE_TEMPLATE = [['OO..',
                     '.OO.',
                     '....'],
                    ['..O.',
                     '.OO.',
                     '.O..']]

I_SHAPE_TEMPLATE = [['.O..',
                     '.O..',
                     '.O..',
                     '.O..'],
                    ['....',
                     'OOOO',
                     '....',
                     '....']]

O_SHAPE_TEMPLATE = [['OO',
                     'OO'],
                    ['OO',
                     'OO']]

J_SHAPE_TEMPLATE = [['.O.',
                     '.O.',
                     'OO.'],
                    ['O..',
                     'OOO',
                     '...'],
                    ['OO.',
                     'O..',
                     'O..'],
                    ['OOO',
                     '..O',
                     '...']]

L_SHAPE_TEMPLATE = [['O..',
                     'O..',
                     'OO.'],
                    ['...',
                     'OOO',
                     'O..'],
                    ['OO.',
                     '.O.',
                     '.O.'],
                    ['..O',
                     'OOO',
                     '...']]

T_SHAPE_TEMPLATE = [['.O.',
                     'OOO',
                     '...'],
                    ['.O.',
                     '.OO',
                     '.O.'],
                    ['...',
                     'OOO',
                     '.O.'],
                    ['..O',
                     '.OO',
                     '..O']]

PIECES = {'S': S_SHAPE_TEMPLATE,
          'Z': Z_SHAPE_TEMPLATE,
          'J': J_SHAPE_TEMPLATE,
          'L': L_SHAPE_TEMPLATE,
          'I': I_SHAPE_TEMPLATE,
          'O': O_SHAPE_TEMPLATE,
          'T': T_SHAPE_TEMPLATE
          }

PIECE_TYPES = ['S', 'Z', 'J', 'L', 'I', 'O', 'T']

PIECE_COLORS = {
    'S': (0, 255, 128),
    'Z': (255, 128, 255),
    'J': (128, 0, 255),
    'L': (0, 0, 255),
    'I': (0, 128, 0),
    'O': (255, 0, 0),
    'T': (255, 128, 0)
}

SCORE_LABEL_COLOR = (0, 0, 255)
SCORE_COLOR = (255, 0, 0)
TITLE_COLOR = (0, 0, 255)
HANZI_COLOR = (128, 0, 255)