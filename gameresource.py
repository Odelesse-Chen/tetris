import pygame

class GameResource():
    def __init__(self):
        self.img_path ='images/'
        self.music_path = 'music/'
        self.newgame_img = None
        self.pausing_img = None
        self.continue_img = None
        self.gameover_img = None
        self.music_paused = False
        self.bg_img = None

    def load_gameover_img(self):
        if not self.gameover_img:
            self.gameover_img = pygame.image.load(self.img_path + "game-over.png").convert_alpha()

        return self.gameover_img

    def load_newgame_img(self):
        if not self.newgame_img:
            self.newgame_img = pygame.image.load(self.img_path + "press-s-newgame.png").convert_alpha()
        return self.newgame_img
    def load_pausing_img(self):
        if not self.pausing_img:
            self.pausing_img = pygame.image.load(self.img_path + "game-pausing.png").convert_alpha()
        return self.pausing_img
    def load_continue_img(self):
        if not self.continue_img:
            self.continue_img = pygame.image.load(self.img_path + 'press-p-continue.png').convert_alpha()
        return self.continue_img

    def load_bg_img(self):
        if not self.bg_img:
            self.bg_img = pygame.image.load(self.img_path + 'bg-1.jpg')
        return self.bg_img

    def play_bg_music(self):
        pygame.mixer.init()
        bg_music_file = self.music_path + 'bg_music.mp3'
        pygame.mixer.music.load(bg_music_file)

        pygame.mixer.music.play(-1)

    def pause_bg_music(self):
        if not self.music_paused:
            pygame.mixer.music.pause()
            self.music_paused = True
        else:
            pygame.mixer.music.unpause()
            self.music_paused = False

