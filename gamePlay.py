from paddle import Paddle
from time import sleep
from ball import Ball
from scoreboard import Scoreboard


def start_game(screen):
    game_is_on = True
    r_paddle = Paddle()
    l_paddle = Paddle(right_paddle=False)
    ball = Ball()
    scoreboard = Scoreboard()
    while game_is_on:
        sleep(0.1)
        screen.listen()
        screen.onkey(r_paddle.up, "Up")
        screen.onkey(r_paddle.down, "Down")
        screen.onkey(l_paddle.up, "w")
        screen.onkey(l_paddle.down, "s")
        ball.move()
        if ball.ycor() < -250 or ball.ycor() > 250:
            ball.bounce_y()
        if (ball.xcor() > 320 or ball.xcor() < -320) and (ball.distance(r_paddle) < 50 or ball.distance(l_paddle) < 50):
            ball.bounce_x()
            ball.increase_speed()
        elif ball.xcor() > 340:
            scoreboard.l_point()
            ball.reset()
        elif ball.xcor() < -340:
            scoreboard.r_point()
            ball.reset()

        screen.update()
