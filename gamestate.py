import random
import pygame
import time
from settings import *
from piece import Piece
from gamewall import GameWall

class GameState():
    def __init__(self, screen):
        self.screen = screen
        self.wall = GameWall(screen)
        self.piece = None
        self.next_piece = None
        self.timer_interval = TIMER_INTERVAL
        self.game_score = 0
        self.session_count = 0
        self.stopped = True
        self.paused = False
        self.difficulty = 1


    def pause_game(self):
        pygame.time.set_timer(pygame.USEREVENT, 0)
        self.paused = True
    def resume_game(self):
        self.set_timer(self.timer_interval)
        self.paused = False

    def start_game(self):
        self.stopped = False
        self.set_timer(TIMER_INTERVAL)
        self.timer_interval = TIMER_INTERVAL
        #self.piece = Piece(random.choice(PIECE_TYPES), self.screen, self.wall)
        self.piece = self.new_piece()
        self.piece = self.new_piece()
        self.session_count += 1
        self.wall.clear()
        self.game_score = 0
        self.paused = False
        random.seed(int(time.time()))
    def new_piece(self):
        self.piece = self.next_piece
        self.next_piece = Piece(random.choice(PIECE_TYPES), self.screen, self.wall)
        return self.piece


    def set_timer(self, timer_interval):
        self.game_timer = pygame.time.set_timer(pygame.USEREVENT, timer_interval)
    def stop_timer(self):
        pygame.time.set_timer(pygame.USEREVENT, 0)

    def add_score(self, score):
        self.game_score += score
        difficulty = self.game_score // DIFFICULTY_LEVEL_INTERVAL + 1
        if difficulty > self.difficulty:
            self.difficulty += 1
            self.timer_interval -= TIMER_DECREASE_VALUE
            pygame.time.set_timer(pygame.USEREVENT, self.timer_interval)

    def touch_floor(self):
        self.wall.add_to_wall(self.piece)
        self.add_score(self.wall.eliminate_lines())
        #self.piece = Piece(random.choice(PIECE_TYPES), self.screen, self.wall)
        for c in range(COLUMN_NUM):
            if self.wall.is_wall(c, 0):
                self.stopped = True
                break
        if not self.stopped:
            self.piece = self.new_piece()
            #self.piece = Piece(random.choice(PIECE_TYPES), self.screen, self.wall)
            if self.piece.hit_wall():
                self.stopped = True

        if self.stopped:
            self.stop_timer()



