from settings import *
import pygame



class GameDisplay():
    @staticmethod
    def draw_cell(screen, column, row, color):
            cell_position = ((column * CELL_WIDTH + GAME_AREA_LEFT + 1),
                             (row * CELL_WIDTH + GAME_AREA_TOP + 1))
            cell_width_height = (CELL_WIDTH - 2, CELL_WIDTH - 2)
            cell_rect = pygame.Rect(cell_position, cell_width_height)
            pygame.draw.rect(screen, color, cell_rect)

    @staticmethod
    def draw_game_window(screen, game_state, game_resource):

        GameDisplay.draw_border(screen, GAME_AREA_LEFT - EDGE_WIDTH, GAME_AREA_TOP, LINE_NUM, COLUMN_NUM)
        GameDisplay.draw_wall(game_state.wall)
        GameDisplay.draw_score(screen, game_state.game_score)




        if game_state.stopped:
            if game_state.session_count > 0:
                GameDisplay.draw_game_over(screen, game_resource)
            GameDisplay.draw_start_prompt(screen, game_resource)
        if game_state.paused:
            GameDisplay.draw_pause_prompt(screen, game_resource)
        GameDisplay.draw_next_piece(screen, game_state.next_piece)
        GameDisplay.draw_mannual(screen)
        GameDisplay.draw_difficulty_level(screen, game_state.difficulty)
    @staticmethod
    def draw_game_over(screen, game_resource):
        over_position = (GAME_AREA_LEFT + 0.66 * CELL_WIDTH, GAME_AREA_TOP + 7 * CELL_WIDTH)
        screen.blit(game_resource.load_gameover_img(), over_position)
    @staticmethod
    def draw_pause_prompt(screen, game_resource):
        pause_position = (GAME_AREA_LEFT + 0.66 * CELL_WIDTH, GAME_AREA_TOP + 9 * CELL_WIDTH)
        screen.blit(game_resource.load_pausing_img(), pause_position)

        resume_tip_position = (GAME_AREA_LEFT + 0.66 *CELL_WIDTH, GAME_AREA_TOP + 11 *CELL_WIDTH)
        screen.blit(game_resource.load_continue_img(), resume_tip_position)

    @staticmethod
    def draw_start_prompt(screen, game_resource):
        start_tip_position =(GAME_AREA_LEFT + 0.66 * CELL_WIDTH, GAME_AREA_TOP + 10 * CELL_WIDTH)
        screen.blit(game_resource.load_newgame_img(), start_tip_position)


    def draw_wall(game_wall):
        for r in range(LINE_NUM):
            for c in range(COLUMN_NUM):
                if game_wall.area[r][c] != WALL_BLANK_LABEL:
                    GameDisplay.draw_cell(game_wall.screen, c, r, PIECE_COLORS[game_wall.area[r][c]])

    def draw_score(screen, score):
        score_label_font = pygame.font.SysFont('simhei', 28)
        score_label_surface = score_label_font.render(u'得分：', False, SCORE_LABEL_COLOR)
        score_label_position = (GAME_AREA_LEFT + COLUMN_NUM * CELL_WIDTH + 40, GAME_AREA_TOP + 7 * CELL_WIDTH)
        screen.blit(score_label_surface, score_label_position)


        score_font = pygame.font.SysFont('arial', 36)
        score_surface = score_font.render(str(score), False, SCORE_COLOR)
        score_label_width = score_label_surface.get_width()
        score_position = (score_label_position[0] + score_label_width + 20, score_label_position[1] - 5) #-5是为了调整高度
        screen.blit(score_surface, score_position)
    def draw_mannual(screen):
        base_position_x = 30
        base_position_y = GAME_AREA_TOP + 30
        title_font = pygame.font.SysFont('simhei', 28)
        title_surface = title_font.render(u'玩法：', True, TITLE_COLOR)
        title_position = (base_position_x, base_position_y)
        screen.blit(title_surface, title_position)

        base_position_y += 50
        gamectrl_label_font = pygame.font.SysFont('simhei', 24)
        gamectrl_label_surface = gamectrl_label_font.render(u'游戏控制', True, TITLE_COLOR)
        gamectrl_label_position = (base_position_x, base_position_y)
        screen.blit(gamectrl_label_surface, gamectrl_label_position)

        base_position_y += 40
        man_font = pygame.font.SysFont('simhei', 20)
        man_down_surface = man_font.render(u'开始：s   退出：q', False, HANZI_COLOR)
        man_down_position = (base_position_x, base_position_y)
        screen.blit(man_down_surface, man_down_position)

        base_position_y += 30
        man_pause_surface = man_font.render(u'暂停/继续：p', False, HANZI_COLOR)
        man_pause_position = (base_position_x, base_position_y)
        screen.blit(man_pause_surface, man_pause_position)

        base_position_y += 30
        man_restart_surface = man_font.render(u'重玩：r', False, HANZI_COLOR)
        man_restart_position = (base_position_x, base_position_y)
        screen.blit(man_restart_surface, man_restart_position)

        base_position_y += 30
        man_music_surface = man_font.render(u'暂停/继续播放音乐：m', False, HANZI_COLOR)
        man_music_position = (base_position_x, base_position_y)
        screen.blit(man_music_surface, man_music_position)

        base_position_y += 50
        gamectrl_label_surface = gamectrl_label_font.render(u'方块控制', True, TITLE_COLOR)
        gamectrl_label_position = (base_position_x, base_position_y)
        screen.blit(gamectrl_label_surface, gamectrl_label_position)

        base_position_y += 40
        man_down_surface = man_font.render(u'翻转：↑    下移：↓', False, HANZI_COLOR)
        man_down_position = (base_position_x, base_position_y)
        screen.blit(man_down_surface, man_down_position)

        base_position_y += 30
        man_move_surface = man_font.render(u'左移：←    右移：→', False, HANZI_COLOR)
        man_move_position = (base_position_x, base_position_y)
        screen.blit(man_move_surface, man_move_position)

        base_position_y += 30
        man_fall_surface = man_font.render(u'快速到底：f', False, HANZI_COLOR)
        man_fall_position = (base_position_x, base_position_y)
        screen.blit(man_fall_surface, man_fall_position)
    @staticmethod
    def draw_next_piece(screen, next_piece):
        start_x = GAME_AREA_LEFT + COLUMN_NUM * CELL_WIDTH + MARGIN_WIDTH * 2
        start_y = GAME_AREA_TOP
        GameDisplay.draw_border(screen, start_x, start_y, 4, 4)

        if next_piece:
            start_x += EDGE_WIDTH
            start_y += EDGE_WIDTH
            cells = []
            shape_template = PIECES[next_piece.shape]
            shape_turn = shape_template[next_piece.turn_times]
            for r in range(len(shape_turn)):
                for c in range(len(shape_turn[0])):
                    if shape_turn[r][c] == 'O':
                        cells.append((c, r, PIECE_COLORS[next_piece.shape]))

            max_c = max([cell[0] for cell in cells])
            min_c = min([cell[0] for cell in cells])
            start_x += round((4 - (max_c - min_c + 1)) / 2 * CELL_WIDTH)
            max_r = max([cell[1] for cell in cells])
            min_r = min([cell[1] for cell in cells])
            start_y += round((4 - (max_r - min_r + 1)) / 2 * CELL_WIDTH)

            for cell in cells:
                color = cell[2]
                left_top = (start_x + (cell[0] - min_c) * CELL_WIDTH, start_y + (cell[1] - min_r) * CELL_WIDTH)
                GameDisplay.draw_cell_rect(screen, left_top, color)

    @staticmethod
    def draw_border(screen, start_x, start_y, line_num, column_num):
        top_border = pygame.Rect(start_x, start_y, 2 * EDGE_WIDTH + column_num * CELL_WIDTH, EDGE_WIDTH)
        pygame.draw.rect(screen, EDGE_COLOR, top_border)

        left_border = pygame.Rect(start_x, start_y, EDGE_WIDTH, 2 * EDGE_WIDTH + line_num * CELL_WIDTH)
        pygame.draw.rect(screen, EDGE_COLOR, left_border)

        right_border = pygame.Rect(start_x + EDGE_WIDTH + column_num * CELL_WIDTH, start_y, EDGE_WIDTH,
                                   2 * EDGE_WIDTH + line_num * CELL_WIDTH)
        pygame.draw.rect(screen, EDGE_COLOR, right_border)

        bottom_border = pygame.Rect(start_x, start_y + EDGE_WIDTH + line_num * CELL_WIDTH,
                                    2 * EDGE_WIDTH + column_num * CELL_WIDTH, EDGE_WIDTH)
        pygame.draw.rect(screen, EDGE_COLOR, bottom_border)

    @staticmethod
    def draw_cell_rect(screen, left_top_anchor, color):
        left_top_anchor = (left_top_anchor[0] + 1, left_top_anchor[1] + 1)
        cell_width_height = (CELL_WIDTH - 2, CELL_WIDTH - 2)
        cell_rect = pygame.Rect(left_top_anchor, cell_width_height)
        pygame.draw.rect(screen, color, cell_rect)

    @staticmethod
    def draw_difficulty_level(screen, level):
        level_label_font = pygame.font.SysFont('simhei', 28)
        level_label_surface = level_label_font.render(u'难度：', False, SCORE_LABEL_COLOR)
        level_label_position = (GAME_AREA_LEFT + COLUMN_NUM * CELL_WIDTH + MARGIN_WIDTH,
                                GAME_AREA_TOP + 9 * CELL_WIDTH)
        screen.blit(level_label_surface, level_label_position)

        level_difficulty_font = pygame.font.SysFont('arial', 36)
        level_difficulty_surface = level_difficulty_font.render(str(level), False, SCORE_COLOR)
        level_label_width = level_label_surface.get_width()
        level_difficulty_position = (level_label_position[0] + level_label_width + 20, level_label_position[1] - 5) #-5是为了调整高度
        screen.blit(level_difficulty_surface, level_difficulty_position)
'''
    def draw_mannual(screen):
        base_position_x = 30
        base_position_y = GAME_AREA_TOP + 30
        title_font = pygame.font.SysFont('simhei', 28)
        title_surface = title_font.render(u'玩法：', True, TITLE_COLOR)
        title_position = (base_position_x, base_position_y)
        screen.blit(title_surface, title_position)

        base_position_y += 50
        gamectrl_label_font = pygame.font.SysFont('simhei', 24)
        gamectrl_label_surface = gamectrl_label_font.render(u'游戏控制', True, TITLE_COLOR)
        gamectrl_label_position = (base_position_x, base_position_y)
        screen.blit(gamectrl_label_surface, gamectrl_label_position)

        base_position_y += 30
        man_font = pygame.font.SysFont('simhei', 20)
        man_down_surface = man_font.render(u'开始：s字母键；退出：q字母键', False, HANZI_COLOR)
        man_down_position = (base_position_x, base_position_y)
        screen.blit(man_down_surface, man_down_position)

        base_position_y += 30
        man_pause_surface = man_font.render(u'暂停/继续：p字母键', False, HANZI_COLOR)
        man_pause_position = (base_position_x, base_position_y)
        screen.blit(man_pause_surface, man_pause_position)

        base_position_y += 30
        man_restart_surface = man_font.render(u'重玩：r字母键', False, HANZI_COLOR)
        man_restart_position = (base_position_x, base_position_y)
        screen.blit(man_restart_surface, man_restart_position)

        base_position_y += 30
        man_music_surface = man_font.render(u'暂停/继续播放音乐：m字母键', False, HANZI_COLOR)
        man_music_position = (base_position_x, base_position_y)
        screen.blit(man_music_surface, man_music_position)

        base_position_y += 50
        gamectrl_label_surface = gamectrl_label_font.render(u'方块控制', True, TITLE_COLOR)
        gamectrl_label_position = (base_position_x, base_position_y)
        screen.blit(gamectrl_label_surface, gamectrl_label_position)

        base_position_y += 30
        man_down_surface = man_font.render(u'翻转：上方向键；下移：下方向键', False, HANZI_COLOR)
        man_down_position = (base_position_x, base_position_y)
        screen.blit = (man_down_surface, man_down_position)

        base_position_y += 30
        man_move_surface = man_font.render(u'左移：左方向键：右移：右方向键', False, HANZI_COLOR)
        man_move_position = (base_position_x, base_position_y)
        screen.blit(man_move_surface, man_move_position)

        base_position_y += 30
        man_fall_surface = man_font.render(u'快速到底：f字母键', False, HANZI_COLOR)
        man_fall_position = (base_position_x, base_position_y)
        screen.blit(man_fall_surface, man_fall_position)
        '''
''' 
        pygame.draw.line(screen, (0, 0, 0),
                         (GAME_AREA_LEFT, GAME_AREA_TOP), (GAME_AREA_RIGHT, GAME_AREA_TOP))
        pygame.draw.line(screen, (0, 0, 0),
                         (GAME_AREA_RIGHT, GAME_AREA_TOP), (GAME_AREA_RIGHT, GAME_AREA_FLOOR))
        pygame.draw.line(screen, (0, 0, 0),
                         (GAME_AREA_RIGHT, GAME_AREA_FLOOR), (GAME_AREA_LEFT, GAME_AREA_FLOOR))
        pygame.draw.line(screen, (0, 0, 0),
                         (GAME_AREA_LEFT, GAME_AREA_FLOOR), (GAME_AREA_LEFT, GAME_AREA_TOP))

        X = GAME_AREA_LEFT
        Y = GAME_AREA_TOP

        for i in range(10):
            X = X + 30
            pygame.draw.line(screen, (0, 0, 0), (X, GAME_AREA_FLOOR), (X, GAME_AREA_TOP))

        for j in range(20):
            Y = Y + 30
            pygame.draw.line(screen, (0, 0, 0), (GAME_AREA_LEFT, Y), (GAME_AREA_RIGHT, Y))
'''


