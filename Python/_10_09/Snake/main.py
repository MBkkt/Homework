from _10_01.snake.game import Game
from _10_01.snake.object.snake import Snake
from _10_01.snake.object.apple import Apple


if __name__ == '__main__':
    game = Game()
    snake = Snake(game.yellow)
    apple = Apple(game.brown, game.width, game.height)
    game.set_surface()

    while True:
        snake.change_to = game.eventing(snake.change_to)
        snake.change_direction()
        snake.change_head()
        game.score, apple.apple_pos = snake.body_mechanism(game.score, apple.apple_pos, game.width, game.height)
        snake.draw_snake(game.surface, game.green)
        apple.draw_apple(game.surface)
        if snake.check(game.width, game.height):
            game.game_over()
        game.show_score()
        game.refresh_screen()
