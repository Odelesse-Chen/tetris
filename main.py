import sys
import pygame
from settings import *
from gamedisplay import GameDisplay
from gamestate import GameState
from gameresource import GameResource
def main():

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HIGH))
    pygame.display.set_caption("俄罗斯方块")
    pygame.key.set_repeat(50, 100)
    game_state = GameState(screen)
    game_resource = GameResource()
    game_resource.play_bg_music()


    while True:



        if game_state.piece and game_state.piece.is_on_floor:
            game_state.touch_floor()

        check_events(game_state, game_resource)

        screen.blit(game_resource.load_bg_img(), (0, 0))


        if game_state.piece:
            game_state.piece.paint()

        GameDisplay.draw_game_window(screen, game_state, game_resource)

        pygame.display.flip()

def check_events(game_state, game_resource):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            on_key_down(event, game_state, game_resource)
        elif event.type == pygame.USEREVENT:
            game_state.piece.move_down()

def on_key_down(event, game_state, game_resource):#?
    if event.key == pygame.K_DOWN:
        if game_state.piece:
            if not game_state.paused and not game_state.stopped:
                game_state.piece.move_down()
    elif event.key == pygame.K_UP:
        if game_state.piece:
            if not game_state.paused and not game_state.stopped:
                game_state.piece.turn()
    elif event.key == pygame.K_RIGHT:
        if game_state.piece:
            if not game_state.paused and not game_state.stopped:
                game_state.piece.move_right()
    elif event.key == pygame.K_LEFT:
        if game_state.piece:
            if not game_state.paused and not game_state.stopped:
                game_state.piece.move_left()
    elif event.key == pygame.K_f:
        if game_state.piece:
            if not game_state.paused and not game_state.stopped:
                game_state.piece.fall_down()
    elif event.key == pygame.K_s and game_state.stopped:
        game_state.start_game()
    elif event.key == pygame.K_p and not game_state.stopped:
        if game_state.paused:
            game_state.resume_game()
        else:
            game_state.pause_game()
    elif event.key == pygame.K_r:
        game_state.start_game()
    elif event.key == pygame.K_m:
        game_resource.pause_bg_music()
    elif event.key == pygame.K_q:
        sys.exit()




if __name__ == '__main__':
    main()
