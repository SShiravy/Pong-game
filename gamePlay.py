from paddle import Paddle
from time import sleep

def start_game(screen):
    game_is_on = True
    r_paddle = Paddle()
    l_paddle = Paddle(right_paddle=False)
    while game_is_on:
        sleep(0.2)
        screen.listen()
        screen.onkey(r_paddle.up,"Up")
        screen.onkey(r_paddle.down,"Down")
        screen.onkey(l_paddle.up,"w")
        screen.onkey(l_paddle.down,"s")
        screen.update()

